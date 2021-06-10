__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021, Vanessa Sochat"
__license__ = "MPL 2.0"


from shpc.logger import logger
import shpc.main.templates
import shpc.utils

from jinja2 import Template
import os
import re


class ContainerName:
    """
    Parse a container name into named parts
    """

    def __init__(self, raw):
        self.raw = raw
        self.registry = None
        self.repository = None
        self.tool = None
        self.version = None
        self.digest = None
        self.parse(raw)

    def parse(self, raw):
        """
        Parse a name into known pieces
        """
        match = re.search(shpc.main.templates.docker_regex, raw)
        if not match:
            logger.exit("%s does not match a known identifier pattern." % raw)
        for key, value in match.groupdict().items():
            value = value.strip("/") if value else None
            setattr(self, key, value)


class ContainerTechnology:
    """
    A base class for a container technology
    """

    # The module technology adds extensions here
    modulefile = "module"

    # By default, no extra features
    features = {}

    def __init__(self):

        # If we weren't created with settings, add empty
        if not hasattr(self, "settings"):
            from shpc.main.settings import SettingsBase

            self.settings = SettingsBase()

    def add(self, sif, module_name, modulefile, template, **kwargs):
        """
        Manually add a registry container.
        """
        logger.warning("Add is not supported for %s" % self)

    def add_environment(self, module_dir, envars, environment_file):
        """
        Given one or more environment variables in a dictionary, write to file.
        """
        # Podman envars are written directly to the module file
        out = Template(shpc.main.templates.environment_file).render(envars=envars)
        env_file = os.path.join(module_dir, environment_file)
        shpc.utils.write_file(env_file, out)

    def delete(self, image):
        """
        If a container doesn't reside in the module directory, allow custom delete
        """
        pass

    def container_dir(self, name):
        """
        Use a custom container directory, otherwise default to module dir.
        """
        # If the user provided a tag, tags are converted to folders
        if ":" in name:
            name = name.replace(":", os.sep)

        if not self.settings.container_base:
            return os.path.join(self.settings.module_base, name)
        return os.path.join(self.settings.container_base, name)

    def iter_registry(self):
        """
        Iterate over known registries defined in settings.
        """
        for registry in self.settings.registry:
            for filename in shpc.utils.recursive_find(registry):
                yield registry, filename

    def guess_tag(self, module_name, allow_fail=False):
        """
        If a user asks for a name without a tag, try to figure it out.
        """
        if ":" in module_name:
            return module_name
        tags = self.installed_tags(module_name)
        if not tags and allow_fail:
            logger.exit("%s does not have any tags installed." % module_name)
        elif tags and len(tags) == 1:
            return "%s:%s" % (module_name, tags[0])
        elif tags and len(tags) > 1 and allow_fail:
            return

        # Length of tags is > 1
        logger.exit("Multiple tags found for %s: %s." % (module_name, ", ".join(tags)))

    def installed_tags(self, module_name):
        """
        Get a list of installed tags.
        """
        return os.listdir(os.path.join(self.settings.module_base, module_name))

    def get_environment_file(self, module_name):
        """
        Get an environment file for a container.
        """
        module_name = self.guess_tag(module_name)

        # This can be the module or container directory
        container_dir = self.container_dir(module_name)

        # Does the user want to see a module file?
        result = os.path.join(container_dir, self.settings.environment_file)
        if not os.path.exists(result):
            logger.exit("Environment file %s does not exist." % result)
        return result

    def get_features(self, config_features, settings_features, extra=None):
        """
        Get feature values based onsettings and features defined for the container.
        """
        config_features = config_features or {}
        extra = extra or []

        # If extra features are added at runtime, they are set to true
        for extra_feature in extra:
            if extra_feature not in config_features:
                config_features[extra_feature.lower()] = True

        features = {}

        # The config features (defined by the container) determine what we add
        for key, value in config_features.items():

            # If the container technology has the feature and is defined in settings
            if key in self.features and key in settings_features:

                # And if the settings feature is known to the container technology
                if settings_features[key] in self.features[key]:

                    # Add the feature to be given to the container!
                    features[key] = self.features[key][settings_features[key]]

        return features

    def __str__(self):
        return str(self.__class__.__name__)
