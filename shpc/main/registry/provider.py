__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021-2022, Vanessa Sochat"
__license__ = "MPL 2.0"


import os


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

    def __init__(self, source, *args, **kwargs):
        self.assert_match(source)
        self.source = source

    def exists(self, name):
        """
        Determine if a module exists in the registry.
        """
        return os.path.exists(os.path.join(self.source, name))

    @property
    def is_filesystem_registry(self):
        return not self.source.startswith("http") and os.path.exists(self.source)

    @property
    def name(self):
        return self.__class__.__name__.lower()

    @classmethod
    def assert_match(cls, source_url: str):
        pass

    @classmethod
    def matches(cls, source_url: str):
        try:
            cls.assert_match(source_url)
            return True
        except ValueError:
            return False

    def find(self, name):
        pass

    def cleanup(self):
        pass

    def iter_registry(self):
        pass

    def iter_modules(self):
        """
        yield module names
        """
        for filename in shpc.utils.recursive_find(self.source, "container.yaml"):
            module = os.path.dirname(filename).replace(self.source, "").strip(os.sep)
            if not module:
                continue
            yield self.source, module
