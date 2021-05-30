__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021, Vanessa Sochat"
__license__ = "MPL 2.0"


from shpc.logger import logger
import shpc.defaults as defaults
import shpc.main.schemas
import shpc.utils

try:
    from ruamel_yaml import YAML
except:
    from ruamel.yaml import YAML

from datetime import datetime
import jsonschema
import os


class SettingsBase:
    def __init__(self):
        """
        Create a new settings object not requiring a settings file.
        """
        # Set an updated time, in case it's written back to file
        self._settings = {"updated_at": datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")}
        self.settings_file = None

    def __str__(self):
        return "[shpc-settings]"

    def __repr__(self):
        return self.__str__()

    def validate(self):
        """
        Validate the loaded settings with jsonschema
        """
        jsonschema.validate(instance=self._settings, schema=shpc.main.schemas.settings)

    def edit(self):
        """
        Interactively edit a config file.
        """
        if not self.settings_file or not os.path.exists(self.settings_file):
            logger.exit("Settings file not found.")
        shpc.utils.run_command([self.config_editor, self.settings_file], stream=True)

    def load(self, settings_file=None):
        """
        Load the settings file into the settings object
        """
        self.settings_file = settings_file or defaults.default_settings_file

        # Exit quickly if the settings file does not exist
        if not os.path.exists(self.settings_file):
            logger.exit("%s does not exist." % self.settings_file)

        # Default to round trip so we can save comments
        yaml = YAML()

        # Store the original settings for update as we go
        with open(self.settings_file, "r") as fd:
            self._settings = yaml.load(fd.read())

    def get(self, key, default=None):
        value = self._settings.get(key, default)
        return self._substitutions(value)

    def __getattr__(self, key):
        """
        A direct get of an attribute, but default to None if doesn't exist
        """
        return self.get(key)

    def set(self, key, value):
        """
        Set a setting based on key and value. If the key has :, it's nested
        """
        value = True if value == "true" else value
        value = False if value == "false" else value

        # This is a reference to a dictionary (object) setting
        if ":" in key:
            key, subkey = key.split(":")
            self._settings[key][subkey] = value
        else:
            self._settings[key] = value

    def _substitutions(self, value):
        """
        Given a value, make substitutions
        """
        if isinstance(value, bool) or not value:
            return value

        # Currently dicts only support boolean or null so we return as is
        elif isinstance(value, dict):
            return value

        for rep, repvalue in defaults.reps.items():
            if isinstance(value, list):
                value = [x.replace(rep, repvalue) for x in value]
            else:
                value = value.replace(rep, repvalue)

        return value

    def delete(self, key):
        if key in self._settings:
            del self._settings[key]

    def save(self, filename=None):
        filename = filename or self.settings_file
        if not filename:
            logger.exit("A filename is required to save to.")
        yaml = YAML()
        with open(filename, "w") as fd:
            yaml.dump(self._settings, fd)

    def __iter__(self):
        for key, value in self.__dict__.items():
            yield key, value


class Settings(SettingsBase):
    """
    The settings class is a wrapper for easily parsing a settings.yml file.

    We parse into a query-able class. It also gives us control to update settings,
    meaning we change the values and then write them to file. It's basically
    a dictionary-like class with extra functions.
    """

    def __init__(self, settings_file):
        """
        Create a new settings object, which requires a settings file to load
        """
        self.load(settings_file)
        self.validate()

        # Set an updated time, in case it's written back to file
        self._settings["updated_at"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
