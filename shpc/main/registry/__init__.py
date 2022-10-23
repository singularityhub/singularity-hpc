__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021-2022, Vanessa Sochat"
__license__ = "MPL 2.0"


import os
import shutil

import jsonschema

import shpc.main.schemas
import shpc.utils
from shpc.logger import logger
from shpc.main.settings import SettingsBase

from .filesystem import Filesystem, FilesystemResult
from .remote import GitHub, GitLab


def update_container_module(module, from_path, existing_path):
    """
    Update a container module, meaning copying over all files
    """
    if not os.path.exists(existing_path):
        shpc.utils.mkdir_p(existing_path)
    for filename in shpc.utils.recursive_find(from_path):
        relative_path = filename.replace(from_path, "").strip("/")
        to_path = os.path.join(existing_path, relative_path)
        if os.path.exists(to_path):
            shutil.rmtree(to_path)
        shpc.utils.mkdir_p(os.path.dirname(to_path))
        shutil.copy2(filename, to_path)


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

    def iter_registry(self, filter_string=None):
        """
        Iterate over all known registries defined in settings.
        """
        for reg in self.registries:
            for entry in reg.iter_registry(filter_string=filter_string):
                yield entry

    def find(self, name, path=None):
        """
        Find the first occurrence of a module.
        """
        # Custom one-off path provided to load from
        if path:
            path = os.path.abspath(path)
            reg = self.get_registry(path)
            return reg.find(name)

        # Otherwise search through default registries
        for reg in self.registries:
            result = reg.find(name)
            if result:
                return result

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

    def sync(
        self,
        name=None,
        dryrun=False,
        tag="main",
        upgrade_all=False,
        add_new=True,
        local=None,
        config_file=None,
        sync_registry=None,
    ):
        """
        Given a module name (or None for all modules) update container.yaml files.
        """
        if not config_file:
            return self._sync(
                name, dryrun, tag, upgrade_all, add_new, local, sync_registry
            )
        cfg = shpc.utils.read_yaml(config_file)
        jsonschema.validate(cfg, shpc.main.schemas.extraConfig)
        for local, sync_registry in cfg["sync_registry"].items():
            self._sync(name, dryrun, tag, upgrade_all, add_new, local, sync_registry)

    def _sync(
        self,
        name=None,
        dryrun=False,
        tag="main",
        upgrade_all=False,
        add_new=True,
        local=None,
        sync_registry=None,
    ):
        # Registry to sync from
        sync_registry = sync_registry or self.settings.sync_registry

        # Create a remote registry with settings preference
        Remote = GitHub if "github.com" in sync_registry else GitLab
        remote = Remote(sync_registry, tag=tag)
        local = self.get_registry(local or self.settings.filesystem_registry)

        # We sync to our first registry - if not filesystem, no go
        if not local.is_filesystem_registry:
            logger.exit(
                "sync is only supported for a remote to a filesystem registry: %s"
                % sync_registry.source
            )

        # Upgrade the current registry from the remote
        self.sync_from_remote(
            remote,
            name,
            overwrite=upgrade_all,
            dryrun=dryrun,
            add_new=add_new,
            local=local,
        )
        remote.cleanup()

    def sync_from_remote(
        self, remote, name=None, overwrite=False, dryrun=False, add_new=True, local=None
    ):
        """
        Update our local filesystem registry with a new module.

        If the registry module is not installed, we install to the first
        filesystem registry found in the list.
        """
        updates = False

        # A local (string) path provided
        if local and isinstance(local, str) and os.path.exists(local):
            local = Filesystem(local)

        # No local registry provided, use default
        if not local:
            local = Filesystem(self.settings.filesystem_registry)

        tmpdir = remote.source
        if tmpdir.startswith("http") or not os.path.exists(tmpdir):
            tmpdir = remote.clone()

        # These are modules to update
        for regpath, module in remote.iter_modules():
            if name and module != name:
                continue

            from_path = os.path.join(regpath, module)
            existing_path = local.exists(module)

            # If we have an existing module and we want to replace all files
            if existing_path and overwrite:
                updates = True
                logger.info("%s will be upgraded with all new files." % module)
                if not dryrun:
                    update_container_module(module, from_path, existing_path)

            # If the path doesn't exist, we add / update it only if we want to add new
            elif not existing_path and add_new:
                updates = True
                logger.info("%s will be added newly." % module)
                if not dryrun:
                    update_container_module(
                        module, from_path, os.path.join(local.source, module)
                    )

        if not updates:
            logger.info("There were no upgrades.")


# We only currently allow Filesystem registries to be used in settings
PROVIDERS = [GitHub, Filesystem, GitLab]
