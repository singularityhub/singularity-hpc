__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021-2023, Vanessa Sochat"
__license__ = "MPL 2.0"


import os
import shutil

import shpc.utils
from shpc.logger import logger

from .provider import Provider, Result


class FilesystemResult(Result):
    """
    A filesystem result provides courtesy functions for interacting with
    a container yaml recipe on the filesytem.
    """

    def __init__(self, module, container_yaml):
        self.module = module
        self.load(container_yaml)

    def load(self, package_file):
        """
        Load the settings file into the settings object
        """
        # Exit quickly if the package does not exist
        if not os.path.exists(package_file):
            logger.exit("%s does not exist." % package_file)

        # Default to round trip so we can save comments
        self.package_file = os.path.abspath(package_file)
        self._config = shpc.utils.read_yaml(package_file)

    def get_overrides(self, tag):
        """
        Load a filesystem based override file
        """
        overrides = self._config.get("overrides", {})
        override_file = os.path.join(self.dirname, overrides[tag])
        if not os.path.exists(override_file):
            logger.exit(f"Override file {override_file} does not exist.")
        return shpc.utils.read_yaml(override_file)

    def save(self, package_file):
        """
        Save the new package file to container.yaml
        """
        package_file = package_file or self.package_file
        shpc.utils.write_yaml(self._config, package_file)

    def load_wrapper_script(self, container_tech, script):
        """
        Get the content of a wrapper script, if it exists.
        """
        wrapper_script = self.find_wrapper_script(container_tech, script)
        if wrapper_script:
            return shpc.utils.read_file(os.path.join(self.dirname, wrapper_script))

    def override_exists(self, tag):
        """
        Check if an override exists.
        """
        overrides = self._config.get("overrides", {})
        override_file = os.path.join(self.dirname, overrides[tag])
        if not os.path.exists(override_file):
            logger.warning(
                f"Override file {override_file} does not exist in {self.dirname}"
            )
            return False
        return True


class Filesystem(Provider):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.source = os.path.abspath(self.source)

    @classmethod
    def matches(cls, source):
        return os.path.exists(source) or source == "."

    def iter_modules(self):
        for filename in shpc.utils.recursive_find(self.source, "container.yaml"):
            module = os.path.dirname(filename).replace(self.source, "").strip(os.sep)
            if not module:
                continue
            yield self.source, module

    def find(self, name):
        """
        Find and load a container.yaml from the filesystem.
        """
        # STOPPED HERE - test is failing when remote=True and don't know why
        container_yaml = os.path.join(self.source, name, "container.yaml")
        if os.path.exists(container_yaml):
            return FilesystemResult(name, container_yaml)

    def cleanup(self):
        """
        Cleanup the temporary registry (this must be intentionally called)
        """
        if os.path.exists(self.source):
            shutil.rmtree(self.source)

    def iter_registry(self, filter_string=None):
        """
        Iterate over content in filesystem registry.
        """
        for filename in shpc.utils.recursive_find(self.source, filter_string):
            if not filename.endswith("container.yaml"):
                continue
            module_name = (
                os.path.dirname(filename).replace(self.source, "").strip(os.sep)
            )
            yield FilesystemResult(module_name, filename)
