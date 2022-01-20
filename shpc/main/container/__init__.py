__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021-2022, Vanessa Sochat"
__license__ = "MPL 2.0"


from .singularity import SingularityContainer
from .podman import PodmanContainer
from .docker import DockerContainer

from shpc.logger import logger
import shpc.main.schemas as schemas
import shlex

try:
    from ruamel_yaml import YAML
except:
    from ruamel.yaml import YAML

import os
import jsonschema
import sys


class Tags:
    """Make it easy to interact with tags (name and version)"""

    def __init__(self, tagdict, latest):
        tagdict.update(latest)
        self._tags = tagdict
        self._latest = latest

    @property
    def latest(self):
        key = list(self._latest.keys())[0]
        return Tag(key, self._latest[key])

    def __contains__(self, key):
        return key in self._tags

    def keys(self):
        return list(self._tags.keys())

    def get(self, key, default=None):
        digest = self._tags.get(key, default)
        if digest:
            return Tag(key, digest)


class Tag:
    """
    Convert a tag dictionary to a proper class for easy lookup
    """

    def __init__(self, name, digest):
        self.name = name
        self.digest = digest

    def __str__(self):
        return "%s:%s" % (self.name, self.digest)

    def __repr__(self):
        return str(self)


class ContainerConfig:
    """A ContainerConfig wraps a container.yaml file, intended for install."""

    def __init__(self, package_file):
        """Load a package file for a container."""
        self.load(package_file)
        self.validate()

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
        tags = self._config.get("tags", {})
        return Tags(tags, latest)

    @property
    def flatname(self):
        """
        Flatten the docker uri into a filesystem appropriate name
        """
        if self.docker:
            return self.docker.replace("/", "-")
        elif self.gh:
            return self.gh.replace("/", "-")

    @property
    def name(self):
        """
        Return the name, whether it's docker or GitHub
        """
        from .base import ContainerName

        if self.docker:
            return ContainerName(self.docker)
        elif self.gh:
            return ContainerName(self.gh)

    @property
    def latest(self):
        """
        Return the latest tag
        """
        return self.tags.latest

    def set_tag(self, tag):
        """
        Set a tag to be the config default (defaults to latest otherwise)
        """
        # If a tag isn't provided, default to latest
        if not tag:
            self.tag = self.tags.latest

        # This way, if the user explicitly asks for a tag that does not exist
        # this value will be none (and we can raise an error)
        else:
            self.tag = self.tags.get(tag)

    def dump(self, out=None):
        out = out or sys.stdout
        yaml = YAML()
        yaml.dump(self._config, out)

    def get_url(self):
        """
        Given a loaded container recipe, get the registry url.
        """
        # Not in json schema, but currently required
        if "docker" not in self._config and "gh" not in self._config:
            logger.exit("A docker or gh field is currently required in the config.")
        return self._config.get("docker") or self._config.get("gh")

    def get(self, key, default=None):
        return self._config.get(key, default)

    def __getattr__(self, key):
        """
        A direct get of an attribute, but default to None if doesn't exist
        """
        return self.get(key)

    def validate(self):
        """
        Validate a loaded config with jsonschema
        """
        jsonschema.validate(instance=self._config, schema=schemas.containerConfig)

    def get_envars(self):
        """
        Return loaded environment variables.
        """
        return dict(self.env) if self.env else {}

    def get_aliases(self):
        """
        Return a consistently formatted list of aliases
        """
        # Aliases are not required
        if not self.aliases:
            return []

        # Format 1: allows for a list
        if isinstance(self.aliases, list):
            return [dict(x) for x in self.aliases]

        # Format 2: allows for a key:value pair
        aliases = []
        seen = set()
        for key, value in self.aliases.items():
            if key in seen:
                logger.warning("Warning, alias %s is defined more than once." % key)
            command_list = shlex.split(value)
            aliases.append(
                {
                    "name": key,
                    "command": value,
                    "args": " ".join(command_list[1:]),
                    "entrypoint": command_list[0],
                }
            )
            seen.add(key)
        return aliases

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
