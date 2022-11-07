__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021-2022, Vanessa Sochat"
__license__ = "MPL 2.0"


import os
import re
import shutil
import subprocess as sp
import urllib

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
    def __init__(self, source, tag=None, subdir=None):
        if not self.matches(source):
            raise ValueError(
                type(self).__name__ + "registry must be a remote path, got %s." % source
            )
        self.url = source
        # We don't want ".git" hanging around
        if source.endswith(".git"):
            source = source[:-4]
        self.parsed_url = urllib.parse.urlparse(source)
        self._clone = None

        self.tag = tag

        # Cache of remote container metadata
        self._cache = {}

        # E.g., subdirectory with registry files
        self.subdir = subdir

    @property
    def library_url(self):
        """
        Retrieve the URL of this registry's library (in JSON).
        """
        raise NotImplementedError

    def exists(self, name):
        """
        Determine if a module exists in the registry.
        """
        name = name.split(":")[0]
        self._update_cache()
        return name in self._cache

    def has_clone(self):
        return self._clone and os.path.exists(self._clone.source):

    def clone(self, tmpdir=None):
        """
        Clone the known source URL to a temporary directory
        and return an equivalent local registry (Filesystem)
        """
        if self.has_clone():
            return self._clone
        tmpdir = tmpdir or shpc.utils.get_tmpdir()

        cmd = ["git", "clone", "--depth", "1"]
        if self.tag:
            cmd += ["-b", self.tag]
        cmd += [self.url, tmpdir]
        if self.subdir:
            tmpdir = os.path.join(tmpdir, self.subdir)
        try:
            sp.run(cmd, check=True)
        except sp.CalledProcessError as e:
            raise ValueError("Failed to clone repository {}:\n{}", self.url, e)
        assert os.path.exists(tmpdir)
        self._clone = Filesystem(tmpdir)
        return self._clone

    def cleanup(self):
        """
        Cleanup the registry
        """
        if self.has_clone():
            self._clone.cleanup()
        self._clone = None

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

        library_url = self.library_url
        if not library_url:
            return self._update_clone_cache()
        # Check for exposed library API on GitHub or GitLab pages
        response = requests.get(library_url)
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
        tmplocal = self.clone()
        for module in tmplocal.iter_modules():
            # Minimum amount of metadata to function here
            config_url = self.get_raw_container_url(module)
            self._cache[module] = {
                "config": shpc.utils.read_yaml(
                    os.path.join(tmplocal.source, module, "container.yaml")
                ),
                "config_url": config_url,
            }
        tmplocal.cleanup()

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

    def get_container_url(self, module_name):
        raise NotImplementedError

    def get_raw_container_url(self, module_name):
        raise NotImplementedError


class GitHub(VersionControl):
    @classmethod
    def matches(cls, source):
        return urllib.parse.urlparse(source).hostname == "github.com"

    @property
    def library_url(self):
        owner, repo = self.parsed_url.path.lstrip("/").split("/", 1)
        return f"https://{owner}.github.io/{repo}/library.json"

    def get_container_url(self, module_name):
        return f"https://github.com/{self.parsed_url.path}/blob/{self.tag}/{module_name}/container.yaml"

    def get_raw_container_url(self, module_name):
        return f"https://raw.githubusercontent.com/{self.parsed_url.path}/{self.tag}/{module_name}/container.yaml"


class GitLab(VersionControl):
    @classmethod
    def matches(cls, source):
        return urllib.parse.urlparse(source).hostname == "gitlab.com"

    @property
    def library_url(self):
        owner, repo = self.parsed_url.path.lstrip("/").split("/", 1)
        return f"https://{owner}.gitlab.io/{repo}/library.json"

    def get_container_url(self, module_name):
        return f"https://gitlab.com/{self.parsed_url.path}/-/blob/{self.tag}/{module_name}/container.yaml"

    def get_raw_container_url(self, module_name):
        return f"https://gitlab.com/{self.parsed_url.path}/-/raw/{self.tag}/{module_name}/container.yaml"
