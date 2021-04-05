__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021, Vanessa Sochat"
__license__ = "MPL 2.0"


from shpc.logger import logger
import shpc.main.container as container
import shpc.defaults
import shpc.utils as utils
from .settings import Settings

from datetime import datetime
import os
from glob import glob
import requests
import shutil
import json
import sys


class Client(object):
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

    def check(self, module_name):
        """
        Given a module name, check if the latest is installed.

        If the user provides a top level folder, assume we want to look
        at updates for entire tags. If a specific folder is provided with
        a container, check the digest.
        """
        # We derive the current version installed from the container
        # We assume the user has provided the correct prefix
        module_dir = os.path.join(self.settings.lmod_base, module_name)
        if not os.path.exists(module_dir):
            logger.exit("%s does not exist." % module_dir)

        # Case 1: a specific tag is selected
        sif = self.get(module_name)
        if sif:
            return self._check_digest(module_name, sif)

        return self._check_tags(module_name)

    def _check_tags(self, module_name):
        """
        Check if the installed tag is the latest.
        """
        # Derive the registry entry from the module_name
        config = self._load_container(module_name)
        dirname = os.path.join(self.settings.lmod_base, module_name)

        # Does the user have the modules installed?
        if not os.path.exists(dirname):
            logger.exit("%s is not installed." % module_name)

        # Compare the latest name to the version folders
        versions = os.listdir(dirname)
        if config.latest.name not in versions:
            logger.info(
                "The latest tag is %s, but you have: %s."
                % (config.latest.name, ", ".join(versions))
            )
        else:
            logger.info("⭐️ latest tag %s is up to date. ⭐️" % config.latest.name)

    def _check_digest(self, module_name, sif):
        """
        Check if there is an updated digest for a tag.

        At this point we assume only one container per install, as older containers
        are cleaned up to save filesystem space. If this is changed, we would
        need another way to deduce what version of the container is installed.
        """
        if len(sif) > 1:
            logger.exit("Module folder %s has more than one container." % module_name)

        sif = os.path.basename(sif[0])

        # The prefix of the image is the module_name (which includes version here)
        prefix = module_name.replace(os.sep, "-") + "-"
        digest = sif.replace(prefix, "").replace(".sif", "")

        # Get the latest version digest, remove the tag first
        docker = os.sep.join(module_name.split(os.sep)[:-1])
        tag = module_name.split(os.sep)[-1]
        config = self._load_container(docker)

        # Get the tag
        tag = config.tags.get(tag)
        if not tag:
            logger.exit("Tag %s is not present in the registry entry." % tag)

        if tag.digest == digest:
            logger.info("⭐️ tag %s is up to date. ⭐️" % tag.name)
        else:
            logger.info("👉️ tag %s requires an update! 👈️" % tag.name)

    def list(self, pattern=None, out=None):
        """
        List installed modules.
        """
        out = out or sys.stdout
        for module_name in os.listdir(self.settings.lmod_base):
            if pattern and not re.search(pattern, module_name):
                continue
            module_dir = os.path.join(self.settings.lmod_base, module_name)
            versions = os.listdir(module_dir)
            out.write("%s: %s\n" % (module_name, ", ".join(versions)))

    def show(self, name, out=None):
        """
        Show metadata for a package
        """
        if name:
            config = self._load_container(name)
            config.dump(out)
        else:
            out = out or sys.stdout

            # Get the known registry files
            for package in os.listdir(self.settings.registry):
                out.write(package + "\n")

    def get(self, module_name):
        """
        Get the path to a container for a module
        """
        module_dir = os.path.join(self.settings.lmod_base, module_name)

        # A container must be present
        sif = glob("%s%s*.sif" % (module_dir, os.sep))
        if not sif:
            logger.exit(
                "%s is not a module tag folder, or does not have a sif binary."
                % module_name
            )

        return sif[0]

    def inspect(self, module_name):
        """
        Return complete metadata for the user from a container.
        """
        module_dir = os.path.join(self.settings.lmod_base, module_name)
        if not os.path.exists(module_dir):
            logger.exit("%s does not exist." % module_dir)

        sif = self.get(module_name)
        return self._container.inspect(sif[0])
