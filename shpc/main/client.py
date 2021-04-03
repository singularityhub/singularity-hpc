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
        Given a unique resource identifier, install a recipe.
        """
        config = self._load_container(name, tag)

        # If a tag is not defined, use latest
        tag = tag or config.latest

        # The tag must be defined in the config
        if tag not in config.tags:
            logger.exit("%s is not a known tag." % tag)

        print("TODO: this is where we pull and install the container as a module!")
        import IPython

        IPython.embed()

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
        return container.ContainerConfig(package_file)

    def list(self, pattern=None, out=None):
        """
        List known recipes, along with whether something is installed.
        """
        out = out or sys.stdout

        # Get the known registry files
        for package in os.listdir(self.settings.registry):
            out.write(package + "\n")

    def show(self, name, out=None):
        """
        Show metadata for a package
        """
        config = self._load_container(name)
        config.dump(out)

    # Metadata

    def get_metadata(self, image_file, names=None):
        """
        Extract metadata using Singularity inspect.

        This can only happen if the executable is found.
        If not, return a reasonable default (the parsed image name)

        Parameters
        ==========
        image_file: the full path to a Singularity image
        names: optional, an extracted or otherwise created dictionary of
               variables for the image, likely from utils.parse_image_name

        """
        print("TODO get metadata")
        import IPython

        IPython.embed()
        if names is None:
            names = {}

        metadata = {}

        # We can't return anything without image_file or names
        if image_file:
            if not os.path.exists(image_file):
                bot.error("Cannot find %s." % image_file)
                return names or metadata

        # The user provided a file, but no names
        if not names:
            names = parse_image_name(remove_uri(image_file))

        # Look for the Singularity Executable
        singularity = which("singularity")["message"]

        # Inspect the image, or return names only
        if os.path.exists(singularity) and image_file:
            from spython.main import Client as Singularity

            # Store the original quiet setting
            is_quiet = Singularity.quiet

            # We try and inspect, but not required (wont work within Docker)
            try:
                Singularity.quiet = True
                updates = Singularity.inspect(image=image_file)
            except:
                bot.warning("Inspect command not supported, metadata not included.")
                updates = None

            # Restore the original quiet setting
            Singularity.quiet = is_quiet

            # Try loading the metadata
            if updates is not None:
                try:
                    updates = json.loads(updates)

                    # Singularity 3.x bug with missing top level
                    if "data" in updates:
                        updates = updates["data"]
                    metadata.update(updates)

                    # Flatten labels
                    if "attributes" in metadata:
                        if "labels" in metadata["attributes"]:
                            metadata.update(metadata["attributes"]["labels"])
                        del metadata["attributes"]

                except:
                    pass

        metadata.update(names)

        # Add the type to the container
        metadata["type"] = "container"

        return metadata
