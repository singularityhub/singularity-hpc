__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021-2022, Vanessa Sochat"
__license__ = "MPL 2.0"


import shpc.utils
from shpc.main.settings import SettingsBase
import subprocess as sp
import shutil
import os


def update_container_module(module, from_path, existing_path):
    """
    Update a container module, meaning copying over all files
    """
    if not os.path.exists(existing_path):
        shpc.utils.mkdir_p(existing_path)
    relative_dir = existing_path.split(module)[-1]
    for filename in shpc.utils.recursive_find(from_path):
        basename = os.path.join(relative_dir, os.path.basename(filename))
        to_path = os.path.join(existing_path, basename)
        parent = os.path.dirname(to_path)
        shpc.utils.mkdir_p(parent)
        if os.path.isdir(filename):
            shpc.utils.mkdirp(to_path)
        else:
            shutil.copyfile(filename, to_path)


class Registry:
    """
    An shpc registry contains higher level functions to control registries.
    """

    def __init__(self, settings=None):
        self.settings = settings or SettingsBase()

        # On init, the registries are currently all filesystem based
        # and they must exist.
        self.registries = [self.get_registry(r) for r in self.settings.registry]

    def exists(self, name):
        """
        Determine if a module name *exists* in any local registry, return path
        """
        for reg in self.registries:
            if reg.exists(name):
                return os.path.join(reg.source, name)

    def iter_registry(self):
        """
        Iterate over all known registries defined in settings.
        """
        for reg in self.registries:
            for registry, filepath in reg.iter_registry():
                yield registry, filepath

    def iter_modules(self):
        """
        Iterate over modules found across the registry
        """
        for reg in self.registries:
            for registry, module in reg.iter_modules():
                yield registry, module

    def get_registry(self, source):
        """
        A registry is a local or remote registry.

        We can upgrade from, or otherwise list
        """
        for Registry in PROVIDERS:
            if Registry.matches(source):
                return Registry(source)
        raise ValueError("No matching registry provider for %s" % source)


class Provider:
    def __init__(self, source, *args, **kwargs):
        if not (source.startswith("https://") or os.path.exists(source)):
            raise ValueError(
                "Registry source must exist on the filesystem or be given as https://."
            )
        self.source = source

    def exists(self, name):
        return os.path.exists(os.path.join(self.source, name))

    @property
    def name(self):
        return self.__class__.__name__.lower()

    @classmethod
    def matches(cls, source_url: str):
        pass

    def cleanup(self):
        pass

    def iter_registry(self):
        pass

    def iter_modules(self):
        pass


class Filesystem(Provider):
    @classmethod
    def matches(cls, source):
        return os.path.exists(source)

    def iter_modules(self):
        for filename in shpc.utils.recursive_find(self.source):
            yield self.source, os.path.dirname(filename).replace(self.source, "").strip(
                os.sep
            )

    def cleanup(self):
        """
        Cleanup the temporary registry
        """
        if os.path.exists(self.source):
            shutil.rmtree(self.source)

    def iter_registry(self):
        """
        Iterate over known registries defined in settings.
        """
        for filename in shpc.utils.recursive_find(self.source):
            yield self.source, filename


class GitHub(Provider):
    """
    Currently a GitHub provider is only needed for on-demand upgrade.
    """

    def __init__(self, *args, **kwargs):
        self.tag = kwargs.get("tag")

        # E.g., subdirectory with registry files
        self.subdir = kwargs.get("subdir")
        super().__init__(*args, **kwargs)
        self._url = self.source
        self._setup()

    def _setup(self):
        tmpdir = shpc.utils.get_tmpdir()
        self.clone(tmpdir)
        self.source = tmpdir

    def cleanup(self):
        """
        Cleanup the temporary registry
        """
        if os.path.exists(self.source):
            shutil.rmtree(self.source)

    def exists(self, name):
        """
        Determine if a module exists in the registry.
        """
        dirname = self.source
        if self.subdir:
            dirname = os.path.join(dirname, self.subdir)
        return os.path.exists(os.path.join(dirname, name))

    @classmethod
    def matches(cls, source):
        return cls.__name__.lower() in source

    def clone(self, tmpdir):
        """
        Clone the known source URL to a temporary directory
        """
        cmd = ["git", "clone", "--depth", "1"]
        if self.tag:
            cmd += ["-b", self.tag]
        cmd += [self._url, "."]
        try:
            sp.run(cmd, cwd=tmpdir, check=True)
        except sp.CalledProcessError as e:
            raise ValueError("Failed to clone repository {}:\n{}", self.source, e)

    def __exit__(self):
        """
        Clean up temporary clone on exit.
        """
        if os.path.exists(self.source):
            shutil.rmtree(self.source)

    def iter_modules(self):
        """
        yield module names
        """
        dirname = self.source
        if self.subdir:
            dirname = os.path.join(dirname, self.subdir)
        for filename in shpc.utils.recursive_find(dirname):
            module = os.path.dirname(filename).replace(dirname, "").strip(os.sep)
            if not module:
                continue
            yield dirname, module

    def iter_registry(self):
        """
        Iterate over registry paths
        """
        dirname = self.source
        if self.subdir:
            dirname = os.path.join(dirname, self.subdir)
        for filename in shpc.utils.recursive_find(dirname):
            yield dirname, filename


# We only currently allow Filesystem registries to be used in settings
PROVIDERS = [Filesystem]
