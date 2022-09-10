__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021-2022, Vanessa Sochat"
__license__ = "MPL 2.0"


import os
import re
import shutil
import subprocess as sp

import requests

import shpc.utils
from shpc.logger import logger

from .provider import Provider, Result
from .filesystem import Filesystem


class RemoteResult(Result):
    """
    A remote result provides courtesy functions for interacting with
    a container yaml recipe on GitHub.
    """

    def __init__(self, module, spec, load=True, config=None):
        self.module = module
        self._spec = spec
        self._config = config
        if load:
            self.load(spec)

    def load(self, spec):
        """
        Load the settings file into the settings object
        """
        if "config" not in spec:
            logger.exit("Cannot find required 'config' key in remote metadata.")
        self.package_file = spec["config_url"]
        self._config = spec["config"]

    def get_overrides(self, tag):
        """
        Load a filesystem based override file
        """
        logger.exit(
            "We don't have support for remote overrides yet! Please open an issue!"
        )

    def save(self, package_file):
        raise ValueError("Remote save to a GitHub registry is not supported.")

    def load_wrapper_script(self, container_tech, script):
        """
        Get the content of a wrapper script, if it exists.
        """
        wrapper_script = self.find_wrapper_script(container_tech, script)

        if wrapper_script:
            url = os.path.join(self.dirname, wrapper_script)
            response = requests.get(url)
            if response.status_code != 200:
                logger.warning(
                    "Could not find wrapper script %s in remote registry." % script
                )
            return response.text

    def override_exists(self, tag):
        """
        Check if an override exists.
        """
        logger.exit(
            "We don't have support for remote overrides yet! Please open an issue!"
        )


class VersionControl(Provider):

    # The URL is substituted with owner, repo
    library_url_schemes = {
        "github.com": "https://%s.github.io/%s/library.json",
        "gitlab.com": "https://%s.gitlab.io/%s/library.json",
    }

    # The URL is substituted with repo, branch, module_name
    web_container_url_schemes = {
        "github.com": "https://github.com/%s/blob/%s/%s/container.yaml",
        "gitlab.com": "https://gitlab.com/%s/-/blob/%s/%s/container.yaml",
    }

    # The URL is substituted with repo, branch, module_name
    raw_container_url_schemes = {
        "github.com": "https://raw.githubusercontent.com/%s/%s/%s/container.yaml",
        "gitlab.com": "https://gitlab.com/%s/-/raw/%s/%s/container.yaml",
    }

    def __init__(self, source, tag=None, subdir=None):
        assert self.matches(source)
        if "://" not in source:
            raise ValueError(
                "VersionControl registry must be a remote path, got %s." % source
            )
        self.url = source
        self._library_url = None
        self._clone_dir = None

        self.tag = tag

        # Cache of remote container metadata
        self._cache = {}

        # E.g., subdirectory with registry files
        self.subdir = subdir

    @classmethod
    def matches(cls, source):
        return "://" in source

    @property
    def library_url(self):
        """
        Retrieve the web url, either pages or (eventually) custom.
        """
        if self._library_url is not None:
            return self._library_url
        url = self.url
        if url.endswith(".git"):
            url = url[:-4]
        (_, _, domain, owner, repo) = url.split("/", 4)
        if domain in self.library_url_schemes:
            self._library_url = self.library_url_schemes[domain] % (
                owner,
                repo,
            )
        else:
            self._library_url = ""
        return self._library_url

    def exists(self, name):
        """
        Determine if a module exists in the registry.
        """
        name = name.split(":")[0]
        self._update_cache()
        return name in self._cache

    def clone(self, tmpdir=None):
        """
        Clone the known source URL to a temporary directory
        """
        if self._clone_dir:
            return
        tmpdir = tmpdir or shpc.utils.get_tmpdir()

        cmd = ["git", "clone", "--depth", "1"]
        if self.tag:
            cmd += ["-b", self.tag]
        cmd += [self.url, tmpdir]
        self._clone_dir = tmpdir
        if self.subdir:
            self._clone_dir = os.path.join(tmpdir, self.subdir)
        try:
            sp.run(cmd, check=True)
        except sp.CalledProcessError as e:
            raise ValueError("Failed to clone repository {}:\n{}", self.url, e)
        assert os.path.exists(self._clone_dir)
        return tmpdir

    def cleanup(self):
        """
        Cleanup the temporary clone (this must be intentionally called)
        """
        if not self._clone_dir:
            return
        shutil.rmtree(self._clone_dir)
        self._clone_dir = None

    def iter_modules(self):
        """
        yield module names
        """
        self._update_cache()
        yield from self._cache.keys()

    def find(self, name):
        """
        Find a particular entry in a registry
        """
        self._update_cache()
        if name in self._cache:
            return RemoteResult(name, self._cache[name])

    def _update_cache(self, force=False):
        """
        Update local cache from a registry.
        """
        if self._cache and not force:
            return

        if not self.library_url:
            return self._update_clone_cache()
        # Check for exposed library API on GitHub or GitLab pages
        response = requests.get(self.library_url)
        if response.status_code != 200:
            return self._update_clone_cache()
        self._cache = response.json()

    def _update_clone_cache(self):
        """
        Given a remote that does not expose a library.json, handle via clone.
        """
        logger.warning(
            "Remote %s is not deploying a Registry API, falling back to clone."
            % self.url
        )
        tmpdir = self.clone()
        for module in Filesystem(tmpdir).iter_modules():
            # Minimum amount of metadata to function here
            config_url = self.get_module_config_url(module)[0]
            self._cache[module] = {
                "config": shpc.utils.read_yaml(
                    os.path.join(tmpdir, module, "container.yaml")
                ),
                "config_url": config_url,
            }
        self.cleanup()

    def get_module_config_url(self, module_name):
        """
        Get the raw address of the config (container.yaml)
        """
        (_, _, domain, repo_path) = self.url.split("/", 3)
        if domain in self.raw_container_url_schemes:
            t = (repo_path, self.tag, module_name)
            return (
                self.raw_container_url_schemes[domain] % t,
                self.web_container_url_schemes[domain] % t,
            )
        return (None, None)

    def iter_registry(self, filter_string=None):
        """
        Yield metadata about containers in a remote registry.
        """
        self._update_cache()

        # This assumes blob/main branch
        for uri, entry in self._cache.items():

            # If the user has provided a filter, honor it
            if filter_string and not re.search(filter_string, uri):
                continue
            # Assemble a faux config with tags so we don't hit remote
            yield RemoteResult(uri, entry, load=False, config=entry["config"])
