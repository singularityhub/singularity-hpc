__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021, Vanessa Sochat"
__license__ = "MPL 2.0"


from shpc.logger import logger
import shpc.main.container as container
import shpc.utils as utils
from .settings import Settings

import os
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
        if not hasattr(self, "_container"):
            self._container = None

        # If we don't have default settings, load
        if not hasattr(self, "settings"):
            self.settings = Settings(settings_file)

        # If client initialized with _init_db, do it
        if hasattr(self, "_init_db"):
            self._init_db(self.settings.database_file)

    def speak(self):
        """
        A function for the client to announce him or herself.

        Subclasses can define _speak() to add other meaningful information.
        """
        if self.quiet is False:
            logger.info("%s [database|%s]" % (self, self.database))

            if hasattr(self, "_speak"):
                self._speak()

    def _speak(self):
        pass

    def announce(self, command=None):
        """
        A wrapper to speak to control what commands are shown.

        the client will announce itself given that a command is not in a
        particular predefined list.
        """
        if command and command not in ["get"] and self.quiet is False:
            self.speak()

    def __repr__(self):
        return str(self)

    def __str__(self):
        return "[shpc-client]"

    def install(self, name, tag=None):
        """
        Install must be implemented by the subclass (e.g., lmod)
        """
        raise NotImplementedError

    def uninstall(self, name, tag=None):
        """
        Uninstall must also implemented by the subclass (e.g., lmod)
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

    def get(self, module_name):
        """
        Get the path to a container for a module
        """
        raise NotImplementedError

    def _load_container(self, name, tag=None):
        """
        Given a name and an optional tag to default to, load a package
        """
        # Split name and tag
        if ":" in name:
            name, tag = name.split(":", 1)

        # The recipe folder must exist in the registry
        package_dir = os.path.join(self.settings.registry, name)
        package_file = os.path.join(package_dir, "container.yaml")
        config = container.ContainerConfig(package_file)

        # If the user provides a tag, set it
        config.set_tag(tag)
        return config

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

        # Generate a test template
        test_file = os.path.join(tmpdir, "test.sh")

        # Test all tags (this could be subsetted)
        for tag in config.tags.keys():

            # Install the recipe
            sif = self.install(module_name, tag)

            # Assert that the container exists
            assert os.path.exists(sif)

            # Do we want to test loading?
            if not skip_module and hasattr(self, "_test"):
                result = self._test(module_name, tmpdir, tag, template)
                if result != 0:
                    cleanup(tmpdir)
                    logger.exit("Test of %s was not successful." % module_name)

            # Do we want to test the test commands?
            if test_commands and config.test:
                utils.write_file(test_file, config.test)
                command = ["singularity", "exec", sif, "/bin/bash", test_file]
                result = utils.run_command(command)
                # result = subprocess.call(command)

                # We can't run on incompatible hosts
                if (
                    "the image's architecture" in result["message"]
                    and result["return_code"] != 0
                ):
                    logger.warning(
                        "Cannot run test for container with incompatible architecture: %s"
                        % result["message"]
                    )
                elif result["return_code"] != 0:
                    cleanup(tmpdir)
                    logger.exit("Test of %s was not successful." % module_name)

            # Test the commands
            if not test_exec:
                continue
            for alias in config.get_aliases():
                result = self._container.client.execute(sif, alias["command"])

        # Cleanup the test install
        if stage:
            logger.info(tmpdir)
        else:
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

    def show(self, name, names_only=False, out=None):
        """
        Show available packages
        """
        if name:
            config = self._load_container(name)
            config.dump(out)
        else:
            out = out or sys.stdout

            # List the known registry modules
            for fullpath in utils.recursive_find(self.settings.registry):
                if fullpath.endswith("container.yaml"):
                    module_name = (
                        os.path.dirname(fullpath)
                        .replace(self.settings.registry, "")
                        .strip(os.sep)
                    )
                    if names_only:
                        out.write("%s\n" % module_name)
                    else:
                        config = self._load_container(module_name)
                        for version in config.tags.keys():
                            out.write("%s:%s\n" % (module_name, version))
