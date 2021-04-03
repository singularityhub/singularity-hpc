__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021, Vanessa Sochat"
__license__ = "MPL 2.0"


from shpc.logger import logger
import shpc.utils as utils
import shpc.defaults as defaults
from ruamel_yaml import YAML

from datetime import datetime
import os
import requests
import shutil
import json
import sys


class ContainerConfig:
    """A ContainerConfig wraps a container.yaml file, intended for install."""

    def __init__(self, package_file):
        """Load a package file for a container."""
        self.load(package_file)
        self.name = package_file.split(os.sep)[-2]

    def __str__(self):
        return "[container:%s]" % self.name

    def __repr__(self):
        return self.__str__()

    @property
    def tags(self):
        """
        Return a set of tags (including latest)
        """
        latest = self._config.get("latest")
        tags = self._config.get("tags", [])
        if latest:
            tags.append(latest)
        return set(tags)

    @property
    def latest(self):
        """
        Return the latest tag
        """
        return self._config.get("latest")

    def dump(self, out=None):
        out = out or sys.stdout
        yaml = YAML()
        yaml.dump(self._config, out)

    def get_url(self):
        """
        Given a loaded container recipe, get the registry url.
        """
        if "docker" not in self._config:
            logger.exit("A docker field is currently required in the config.")
        return self._config.get("docker")

    def load(self, package_file):
        """Load the settings file into the settings object"""

        # Exit quickly if the package does not exist
        if not os.path.exists(package_file):
            logger.exit("%s does not exist." % package_file)

        # Default to round trip so we can save comments
        yaml = YAML()

        # Store the original settings for update as we go
        with open(package_file, "r") as fd:
            self._config = yaml.load(fd.read())
        self.package_file = package_file
