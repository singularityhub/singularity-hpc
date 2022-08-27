__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021-2022, Vanessa Sochat"
__license__ = "MPL 2.0"


import shlex

import shpc.main.container.update as update
import shpc.main.schemas as schemas
from shpc.logger import add_prefix, logger, underline

try:
    from ruamel_yaml import YAML
except:
    from ruamel.yaml import YAML

import os
import sys

import jsonschema

here = os.path.abspath(os.path.dirname(__file__))


class Tags:
    """
    Make it easy to interact with tags (name and version)
    """

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

    def set(self, key, value):
        self._tags[key] = value


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
    """
    A ContainerConfig is a light wrapper around a registry Entry.
    """

    def __init__(self, entry, validate=True):
        """
        Interact with a registry container config.
        """
        self.entry = entry
        if validate:
            self.validate()

    def __str__(self):
        return "[container:%s]" % self.name

    def __repr__(self):
        return self.__str__()

    @classmethod
    def get_config_template(cls, template_name="container.yaml"):
        """
        Get a container config template
        """
        template_file = os.path.join(here, "templates", template_name)
        if not os.path.exists(template_file):
            template_file = os.path.abspath(template_name)
            if not os.path.exists(template_file):
                logger.exit(f"{template_file} does not exist.")
        return template_file

    @property
    def tags(self):
        """
        Return a set of tags (including latest)
        """
        latest = self.get("latest")
        tags = self.get("tags", {})
        return Tags(tags, latest)

    @property
    def flatname(self):
        """
        Flatten the docker uri into a filesystem appropriate name
        """
        name = self.docker or self.oras or self.gh or self.path or self.entry.module
        return name.replace("/", "-")

    @property
    def name(self):
        """
        Return the name, whether it's docker or GitHub
        """
        from .base import ContainerName

        if hasattr(self, "path") and self.path is not None:
            return ContainerName("/".join(self.entry.dirname.split("/")[-2:]))

        # A path is not set yet
        if not self.docker and not self.oras and not self.gh and not self.entry.module:
            return "undefined"
        name = self.docker or self.oras or self.gh or self.entry.module
        return ContainerName(name)

    def load_wrapper_script(self, container_tech, script):
        """
        Load a wrapper script from the registry.
        """
        return self.entry.load_wrapper_script(container_tech, script)

    def load_override_file(self, tag):
        """
        By the time we get here, the file needs to exist.
        """
        # Do we have an alias file for the tag?
        if not self.overrides or tag not in self.overrides:
            return
        overrides = self.entry.get_overrides(tag) or {}

        # Only allow over-ride of these fields
        allowed_overrides = [
            "aliases",
            "docker_script",
            "singularity_script",
            "env",
            "features",
            "description",
        ]
        for k, v in overrides.items():
            if k in allowed_overrides:
                self.entry._config[k] = v
            else:
                logger.warning("%s is not an allowed override field." % k)

        # Always validate
        self.validate()

    def check_overrides(self):
        """
        Given a loaded config, ensure that all override files exist.
        """
        if not self.overrides:
            return True
        for tag in self.overrides:
            if not self.entry.override_exists(tag):
                return False
        return True

    def update(self, dryrun=False, filters=None):
        """
        Update a container.yaml, meaning the tags and latest.
        """
        updated = None
        if self.docker or self.oras:
            previous_tags = self.get("tags", {})
            previous_latest = self.get("latest", {})
            updated = update.update_config_tags(self, filters=filters)

            # print the container name and latest tag:
            print(add_prefix(underline(self.docker or self.oras)))
            print(add_prefix("Latest"))
            update.print_diff(previous_latest, updated.get("latest"), True)
            print(add_prefix("Tags"))
            update.print_diff(previous_tags, updated.get("tags"))

            # Take a "diff" of tags
            if not dryrun:
                updated.save(updated.package_file)

    @property
    def latest(self):
        """
        Return the latest tag
        """
        return self.tags.latest

    def set(self, key, value):
        """
        Update loaded config with keys and values
        """
        self.entry._config[key] = value

    def add_tag(self, key, value):
        self.entry._config["tags"][key] = value

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
        """
        Dump (display) the config to an output.
        """
        out = out or sys.stdout
        yaml = YAML()
        yaml.dump(self.entry._config, out)

    def get_url(self):
        """
        Given a loaded container recipe, get the registry url.
        """
        # Not in json schema, but currently required
        if (
            "docker" not in self.entry._config
            and "gh" not in self.entry._config
            and "path" not in self.entry._config
        ):
            logger.exit(
                "A docker, gh, or path field is currently required in the config."
            )
        return self.get("docker") or self.get("gh") or self.get("path")

    def get(self, key, default=None):
        return self.entry._config.get(key, default)

    def get_pull_type(self):
        if self.oras:
            return "oras"
        if self.gh:
            return "gh"
        if self.docker:
            return "docker"
        if self.path:
            return self.path
        logger.exit(
            "Cannot identify pull type: one of oras, docker, gh, or path is required."
        )

    def get_uri(self):
        """
        Return the unique resource identifier
        """
        return (
            getattr(self, "docker")
            or getattr(self, "oras")
            or getattr(self, "gh")
            or getattr(self, "path")
        )

    def __getattr__(self, key):
        """
        A direct get of an attribute, but default to None if doesn't exist
        """
        return self.get(key)

    def validate(self):
        """
        Validate a loaded config with jsonschema
        """
        jsonschema.validate(instance=self.entry._config, schema=schemas.containerConfig)

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

    def save(self, package_file):
        """
        Save the container.yaml to file. This is usually for shpc add.
        """
        self.entry.save(package_file)
