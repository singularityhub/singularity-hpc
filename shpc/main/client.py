__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021-2022, Vanessa Sochat"
__license__ = "MPL 2.0"


from shpc.logger import logger
import shpc.main.container as container
import shpc.utils as utils
import shpc.main.registry as registry
from .settings import Settings

import os
import re
import shutil
import sys


class Client:
    """
    Interact with a local filesystem Singularity HPC registry.

    This client has handles to the registry files, lmod (and other) files,
    and settings to make it easy to otherwise updating your config or
    running commands. This client should be retrieved with:

    from shpc.main import get_client
    client = get_client()

    As this will ensure that the proper database functions are added. The
    database will not be accessible otherwise. This is also a really hairy
    name to type out and import.
    """

    # Setup

    def __init__(self, settings_file=None):

        # We don't necessarily need a container technology handle
        if not hasattr(self, "container"):
            self.container = None

        # If we don't have default settings, load
        if not hasattr(self, "settings"):
            self.settings = Settings(settings_file)

        # Load registries from settings (into a single registry)
        self.registry = registry.Registry(self.settings)

    def __repr__(self):
        return str(self)

    def __str__(self):
        return "[shpc-client]"

    def install(self, name, tag=None, **kwargs):
        """
        Install must be implemented by the subclass (e.g., lmod)
        """
        raise NotImplementedError

    def uninstall(self, name, tag=None):
        """
        Uninstall must also implemented by the subclass (e.g., lmod)
        """
        raise NotImplementedError

    def get(self, module_name):
        """
        Get a container path or uri.
        """
        raise NotImplementedError

    def add(self, sif, module_name):
        """
        Add a container directly as a module
        """
        raise NotImplementedError

    def inspect(self, module_name):
        """
        Return complete metadata for the user from a container.
        """
        raise NotImplementedError

    def add_namespace(self, name):
        """
        If a namespace is defined in settings, use it
        """
        if self.settings.namespace:
            name = "%s/%s" % (self.settings.namespace.strip("/"), name)
        return name

    def load_registry_config(self, name):
        """
        Given an identifier, find the first match in the registry.
        """
        for reg, fullpath in self.registry.iter_registry():
            package_dir = os.path.join(reg, name)
            package_file = os.path.join(package_dir, "container.yaml")
            if package_file == fullpath:
                return container.ContainerConfig(package_file)

        logger.exit("%s is not a known recipe in any registry." % name)

    def _load_container(self, name, tag=None):
        """
        Given a name and an optional tag to default to, load a package
        """
        # Split name and tag
        if ":" in name:
            name, tag = name.split(":", 1)

        # If the user provides a tag, set it
        config = self.load_registry_config(name)
        config.set_tag(tag)
        return config

    def update(self, name, dryrun=False, filters=None):
        """
        Given a module name (or None for all modules) upgrade the registry.
        """
        # No name provided == "update all"
        if name:
            modules = [name]
        else:
            modules = [x[1] for x in list(self.registry.iter_modules())]

        for module_name in modules:
            config = self._load_container(module_name)
            config.update(dryrun=dryrun, filters=filters)

    def upgrade(self, name, dryrun=False, tag="main", upgrade_all=False):
        """
        Given a module name (or None for all modules) update container.yaml files.
        """
        # Create a remote registry (currently only support upgrade from shpc)
        url = "https://github.com/singularityhub/singularity-hpc"
        remote = registry.GitHub(url, tag=tag, subdir="registry")

        # Be able to tell user if no updates
        updates = False

        # These are modules to update
        for regpath, module in remote.iter_modules():
            if name and module != name:
                continue

            from_path = os.path.join(regpath, module)
            existing_path = self.registry.exists(module)

            # If we have an existing module and we want to replace all files
            if existing_path and upgrade_all:
                updates = True
                logger.info("%s will be upgraded with all new files." % module)
                if not dryrun:
                    self.registry.update_container_module(
                        module, from_path, existing_path
                    )

            # If the path doesn't exist, we add / update it either way
            elif not existing_path:
                updates = True
                logger.info("%s will be added newly." % module)
                if not dryrun:
                    self.registry.update_container_module(
                        module, from_path, os.path.join(regpath, module)
                    )

        if not updates:
            logger.info("There were no upgrades.")
        del remote

    def test(
        self,
        module_name,
        stage=False,
        test_exec=False,
        skip_module=False,
        test_commands=False,
        template=None,
    ):
        """
        Test install of a module
        """

        def cleanup(tmpdir):
            if not stage:
                shutil.rmtree(tmpdir)

        # Create temporary directory to work in
        tmpdir = utils.get_tmpdir(prefix="shpc-test")
        if hasattr(self, "_test_setup"):
            self._test_setup(tmpdir)

        # Derive the registry entry from the module_name
        config = self._load_container(module_name)

        # Ensure any alias files exist
        if config and not config.check_overrides():
            cleanup(tmpdir)
            logger.exit("Test of %s was not successful." % module_name)

        # Generate a test template
        test_file = os.path.join(tmpdir, "test.sh")

        # If the module name has a tag, only test it
        if ":" in module_name:
            module_name = module_name.split(":", 1)[0]
            tags = [config.tag.name]
        else:
            tags = list(config.tags.keys())

        # Test all tags (this could be subsetted)
        for tag in tags:

            image = self.install(module_name, tag)

            # Do we want to test loading?
            if not skip_module and hasattr(self, "_test"):
                result = self._test(module_name, tmpdir, tag, template)
                if result != 0:
                    cleanup(tmpdir)
                    logger.exit("Test of %s was not successful." % module_name)

            # Do we want to test the test commands?
            if test_commands and config.test:
                utils.write_file(test_file, config.test)
                return_code = self.container.test_script(image, test_file)
                if return_code != 0:
                    cleanup(tmpdir)
                    logger.exit("Test of %s was not successful." % module_name)

            # Test the commands
            if not test_exec:
                continue

            for alias in config.get_aliases():
                result = self.client.execute(image, alias["command"])

        # Cleanup the test install
        if stage:
            logger.info(tmpdir)
        else:
            self.uninstall(module_name, force=True)
            cleanup(tmpdir)

    def check(self, module_name):
        """
        Given a module name, check if the latest is installed.

        If the user provides a top level folder, assume we want to look
        at updates for entire tags. If a specific folder is provided with
        a container, check the digest.
        """
        raise NotImplementedError

    def list(self, pattern=None, names_only=False, out=None):
        """
        List installed modules.
        """
        raise NotImplementedError

    def docgen(self, module_name):
        """
        Render documentation for a module.
        """
        raise NotImplementedError

    def show(self, name, names_only=False, out=None, filter_string=None):
        """
        Show available packages
        """
        if name:
            name = self.add_namespace(name)
            config = self._load_container(name)
            config.dump(out)
        else:
            out = out or sys.stdout

            # List the known registry modules
            for reg, fullpath in self.registry.iter_registry():
                if fullpath.endswith("container.yaml"):
                    module_name = (
                        os.path.dirname(fullpath).replace(reg, "").strip(os.sep)
                    )

                    # If the user has provided a filter, honor it
                    if filter_string and not re.search(filter_string, module_name):
                        continue

                    if names_only:
                        out.write("%s\n" % module_name)
                    else:
                        config = self._load_container(module_name)
                        for version in config.tags.keys():
                            out.write("%s:%s\n" % (module_name, version))
