__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021-2022, Vanessa Sochat"
__license__ = "MPL 2.0"


import os

import shpc.utils


class Result:
    @property
    def dirname(self):
        return os.path.dirname(self.package_file)

    def find_wrapper_script(self, container_tech, script):
        """
        Locate a wrapper script by container tech and name in config
        """
        # Docker and podman share wrappers under same key
        if container_tech == "podman":
            container_tech = "docker"
        wrapper_key = "%s_scripts" % container_tech
        if wrapper_key not in self._config:
            return

        for _, wrapper_script in self._config[wrapper_key].items():
            if script == wrapper_script:
                return script


class Provider:
    """
    A general provider should retrieve and provide registry files.
    """

    @classmethod
    def matches(cls, source):
        """
        Returns true if this class understands the source
        """
        raise NotImplementedError

    def find(self, name):
        """
        Returns a Result object if the module can be found in the registry
        """
        raise NotImplementedError

    def exists(self, name):
        """
        Returns true if the module can be found in the registry
        """
        raise NotImplementedError

    def iter_registry(self, filter_string=None):
        """
        Iterates over the modules of this registry (that match the filte, if
        provided) as Result instances
        """
        raise NotImplementedError

    def iter_modules(self):
        """
        Iterates over the module names of this registry
        """
        raise NotImplementedError
