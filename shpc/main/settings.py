__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021-2022, Vanessa Sochat"
__license__ = "MPL 2.0"


from shpc.logger import logger
import shpc.defaults as defaults
import shpc.main.schemas
import shpc.utils
import shutil

try:
    from ruamel_yaml import YAML
    from ruamel_yaml.comments import CommentedSeq
except:
    from ruamel.yaml import YAML
    from ruamel.yaml.comments import CommentedSeq

from datetime import datetime
import jsonschema
import os


def OrderedList(*l):
    ret = CommentedSeq(l)
    ret.fa.set_flow_style()
    return ret


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

    def inituser(self):
        """
        Create a user specific config in user's home.
        """
        user_home = os.path.dirname(defaults.user_settings_file)
        if not os.path.exists(user_home):
            os.makedirs(user_home)
        if os.path.exists(defaults.user_settings_file):
            logger.exit(
                "%s already exists! Remove first before re-creating."
                % defaults.user_settings_file
            )
        shutil.copyfile(self.settings_file, defaults.user_settings_file)
        logger.info("Created user settings file %s" % defaults.user_settings_file)

    def edit(self):
        """
        Interactively edit a config file.
        """
        if not self.settings_file or not os.path.exists(self.settings_file):
            logger.exit("Settings file not found.")

        # Make sure editor exists first!
        editor = shpc.utils.which(self.config_editor)
        if editor["return_code"] != 0:
            logger.exit(
                "Editor '%s' not found! Update with shpc config set config_editor:<name>"
                % self.config_editor
            )
        shpc.utils.run_command([self.config_editor, self.settings_file], stream=True)

    def get_settings_file(self, settings_file=None):
        """
        Get the preferred used settings file.
        """
        # Only consider user settings if the file exists!
        user_settings = None
        if os.path.exists(defaults.user_settings_file):
            user_settings = defaults.user_settings_file

        # First preference to command line, then user settings, then default
        return settings_file or user_settings or defaults.default_settings_file

    def load(self, settings_file=None):
        """
        Load the settings file into the settings object
        """
        # Get the preferred settings flie
        self.settings_file = self.get_settings_file(settings_file)

        # Exit quickly if the settings file does not exist
        if not os.path.exists(self.settings_file):
            logger.exit("%s does not exist." % self.settings_file)

        # Default to round trip so we can save comments
        yaml = YAML()
        yaml.preserve_quotes = True

        # Store the original settings for update as we go
        with open(self.settings_file, "r") as fd:
            self._settings = yaml.load(fd.read())

    def get(self, key, default=None):
        """
        Get a settings value, doing appropriate substitution and expansion.
        """
        # This is a reference to a dictionary (object) setting
        if ":" in key:
            key, subkey = key.split(":")
            value = self._settings[key][subkey]
        else:
            value = self._settings.get(key, default)
        value = self._substitutions(value)
        # If we allow environment substitution, do it
        if key in defaults.allowed_envars and value:
            if isinstance(value, list):
                value = [os.path.expandvars(v) for v in value]
            else:
                value = os.path.expandvars(value)
        return value

    def __getattr__(self, key):
        """
        A direct get of an attribute, but default to None if doesn't exist
        """
        return self.get(key)

    def add(self, key, value):
        """
        Add a value to a list parameter
        """
        # We can only add to lists
        current = self._settings.get(key)
        if current and not isinstance(current, list):
            logger.exit("You cannot only add to a list variable.")

        if value not in current:
            # Add to the beginning of the list
            current = [value] + current
            self._settings[key] = OrderedList()
            [self._settings[key].append(x) for x in current]
            self.change_validate(key, value)
            logger.warning(
                "Warning: Check with shpc config edit - ordering of list can change."
            )

    def remove(self, key, value):
        """
        Remove a value from a list parameter
        """
        current = self._settings.get(key)
        if current and not isinstance(current, list):
            logger.exit("You cannot only remove from a list variable.")
        if not current or value not in current:
            logger.exit("%s is not in %s" % (value, key))
        current.pop(current.index(value))
        self._settings[key] = current
        self.change_validate(key, current)
        logger.warning(
            "Warning: Check with shpc config edit - ordering of list can change."
        )

    def set(self, key, value):
        """
        Set a setting based on key and value. If the key has :, it's nested
        """
        value = True if value == "true" else value
        value = False if value == "false" else value

        # List values not allowed for set
        current = self._settings.get(key)
        if current and isinstance(current, list):
            logger.exit("You cannot use 'set' for a list. Use add/remove instead.")

        # This is a reference to a dictionary (object) setting
        if isinstance(value, str) and ":" in value:
            subkey, value = value.split(":")
            self._settings[key][subkey] = value
        else:
            self._settings[key] = value

        # Validate and catch error message cleanly
        self.change_validate(key, value)

    def change_validate(self, key, value):
        """
        A courtesy function to validate a new config addition.
        """
        # Don't allow the user to add a setting not known
        try:
            self.validate()
        except jsonschema.exceptions.ValidationError as error:
            logger.exit(
                "%s:%s cannot be added to config: %s" % (key, value, error.message)
            )

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
        """
        Save settings, but do not change order of anything.
        """
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

    def __init__(self, settings_file, validate=True):
        """
        Create a new settings object, which requires a settings file to load
        """
        self.load(settings_file)
        if validate:
            self.validate()

        # Set an updated time, in case it's written back to file
        self._settings["updated_at"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
