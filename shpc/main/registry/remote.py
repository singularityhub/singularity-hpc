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


def get_module_config_url(registry, module_name, branch="main"):
    """
    Get the raw address of the config (container.yaml)
    """
    registry_bare = registry.split(".com")[-1]
    raw = (
        "https://gitlab.com/%s/-/raw/%s/%s/container.yaml"
        if "gitlab" in registry
        else "https://raw.githubusercontent.com/%s/%s/%s/container.yaml"
    )
    return raw % (
        registry_bare,
        branch,
        module_name,
    )


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
    def __init__(self, *args, **kwargs):
        self.tag = kwargs.get("tag")

        # Cache of remote container metadata
        self._cache = {}

        # E.g., subdirectory with registry files
        self.subdir = kwargs.get("subdir")
        super().__init__(*args, **kwargs)
        self._url = self.source

    @classmethod
    def matches(cls, source):
        return cls.provider_name in source and (
            source.startswith("http") or source.startswith("ssh")
        )

    @property
    def source_url(self):
        """
        Retrieve a parsed / formatted url, ensuring https and without git.
        """
        url = self.source
        if not url.startswith("http"):
            url = "https://%s" % url
        if url.endswith(".git"):
            url = url[:-4]
        return url

    @property
    def web_url(self):
        """
        Retrieve the web url, either pages or (eventually) custom.
        """
        parts = self.source_url.split("/")[3:]
        return "https://%s.%s.io/%s/library.json" % (
            parts[0],
            self.provider_name,
            "/".join(parts[1:]),
        )

    def exists(self, name):
        """
        Determine if a module exists in the registry.
        """
        name = name.split(":")[0]
        if self._cache and name in self._cache:
            return True
        dirname = self.source
        if self.subdir:
            dirname = os.path.join(dirname, self.subdir)
        return os.path.exists(os.path.join(dirname, name))

    def clone(self, tmpdir=None):
        """
        Clone the known source URL to a temporary directory
        """
        tmpdir = tmpdir or shpc.utils.get_tmpdir()

        cmd = ["git", "clone", "--depth", "1"]
        if self.tag:
            cmd += ["-b", self.tag]
        cmd += [self._url, tmpdir]
        self.source = tmpdir
        try:
            sp.run(cmd, check=True)
        except sp.CalledProcessError as e:
            raise ValueError("Failed to clone repository {}:\n{}", self.source, e)
        return tmpdir

    def iter_modules(self):
        """
        yield module names
        """
        dirname = self.source
        if self.subdir:
            dirname = os.path.join(dirname, self.subdir)

        # Find modules based on container.yaml
        for filename in shpc.utils.recursive_find(dirname, "container.yaml"):
            module = os.path.dirname(filename).replace(dirname, "").strip(os.sep)
            if not module:
                continue
            yield dirname, module

    def find(self, name):
        """
        Find a particular entry in a registry
        """
        if not self._cache:
            self._update_cache()
        if name in self._cache:
            return RemoteResult(name, self._cache[name])

    def _update_cache(self, force=False):
        """
        Update local cache from a registry.
        """
        if self._cache and not force:
            return

        if self.source.startswith("ssh"):
            return self._update_clone_cache()
        # Check for exposed library API on GitHub or GitLab pages
        response = requests.get(self.web_url)
        if response.status_code != 200:
            return self._update_clone_cache()
        self._cache = response.json()

    def _update_clone_cache(self):
        """
        Given a remote that does not expose a library.json, handle via clone.
        """
        logger.warning(
            "Remote %s is not deploying a Registry API, falling back to clone."
            % self.source
        )
        tmpdir = self.clone()
        for dirname, module in self.iter_modules():
            # Minimum amount of metadata to function here
            config_url = get_module_config_url(self.source, module)
            self._cache[module] = {
                "config": shpc.utils.read_yaml(
                    os.path.join(dirname, module, "container.yaml")
                ),
                "config_url": config_url,
            }
        shutil.rmtree(tmpdir)

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


class GitHub(VersionControl):
    provider_name = "github"


class GitLab(VersionControl):
    provider_name = "gitlab"
