__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021, Vanessa Sochat"
__license__ = "MPL 2.0"


from shpc.logger import logger
import shpc.main.schemas as schemas

try:
    from ruamel_yaml import YAML
except:
    from ruamel.yaml import YAML

import re
import os
import jsonschema
import sys


class SingularityContainer:
    """
    A Singularity container controller.

    All container controllers should have the same general interface.
    """

    def __init__(self):
        try:
            from spython.main import Client

            self.client = Client
        except:
            logger.exit("singularity python (spython) is required to use singularity.")

    def pull(self, uri, dest):
        """
        Pull a container to a destination
        """
        if re.search("^(docker|shub|https)", uri):
            return self._pull(uri, dest)
        elif uri.startswith("gh://"):
            return self._pull_github(uri, dest)

    def _pull(self, uri, dest):
        """
        Pull a URI that Singularity recognizes
        """
        pull_folder = os.path.dirname(dest)
        name = os.path.basename(dest)
        return self.client.pull(uri, name=name, pull_folder=pull_folder)

    def inspect(self, image):
        """
        Inspect an image and return metadata.
        """
        return self.client.inspect(image)

    def _pull_github(self, uri, dest=None):
        """
        Pull a singularity-deploy container to a destination
        """
        # Assemble the url based on the container uri
        uri = uri.replace("gh://", "", 1)

        # repository name and image prefix
        repo = "/".join(uri.split("/")[0:2])
        prefix = repo.replace("/", "-")

        # The tag includes release and contianer tag (e.g., 0.0.1:latest)
        tag = uri.replace(repo, "", 1).strip("/")
        github_tag, container_tag = tag.split(":", 1)

        # Assemble the artifact url
        url = "https://github.com/%s/releases/download/%s/%s.%s.sif" % (
            repo,
            github_tag,
            prefix,
            container_tag,
        )

        # If no destination, default to present working directory
        if not dest:
            dest = os.path.basename(url)
        name = os.path.basename(dest)
        return self.client.pull(url, name=name, pull_folder=os.path.dirname(dest))


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
    def name(self):
        """
        Flatten the docker uri into a filesystem appropriate name
        """
        if self.docker:
            return self.docker.replace("/", "-")
        elif self.gh:
            return self.gh.replace("/", "-")

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

    def get_aliases(self):
        """
        Return a consistently formatted list of aliases
        """
        # Format 1: allows for a list
        if isinstance(self.aliases, list):
            return [dict(x) for x in self.aliases]

        # Format 2: allows for a key:value pair
        aliases = []
        seen = set()
        for key, value in self.aliases.items():
            if key in seen:
                logger.warning("Warning, alias %s is defined more than once." % key)
            aliases.append({"name": key, "command": value})
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
