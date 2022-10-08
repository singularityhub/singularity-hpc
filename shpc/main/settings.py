__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021-2022, Vanessa Sochat"
__license__ = "MPL 2.0"


import shutil

import shpc.defaults as defaults
import shpc.main.schemas
import shpc.utils as utils
from shpc.logger import logger

try:
    from ruamel_yaml.comments import CommentedSeq
except:
    from ruamel.yaml.comments import CommentedSeq

import os
import re
from datetime import datetime

import jsonschema


def OrderedList(*l):
    """
    Preserve ordering when saved to yaml
    """
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
        self.user_settings = None

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

    def edit(self, settings_file=None):
        """
        Interactively edit a config (or other) file.
        """
        settings_file = settings_file or self.settings_file
        if not settings_file or not os.path.exists(settings_file):
            logger.exit("%s does not exist." % settings_file)

        # Discover editor user has preferences for
        editor = None

        # First try EDITOR and VISUAL envars
        for envar_name in ["EDITOR", "VISUAL"]:
            envar = os.environ.get(envar_name)
            editor = self._find_editor(envar)
            if editor is not None:
                break

        # If we get here and no editor, try system default
        if not editor:
            editor = self._find_editor(self.config_editor)
        if not editor:
            logger.exit(
                "No editors found! Update with shpc config set config_editor:<name>"
            )

        utils.run_command([editor, settings_file], stream=True)

    def _find_editor(self, path):
        """
        Check to see that an editor exists.
        """
        if not path:
            return

        editor = utils.which(path)

        # Only return the editor name if we find it!
        if editor["return_code"] == 0:
            return path

    def get_settings_file(self, settings_file=None):
        """
        Get the preferred user settings file, set user settings if exists.
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

        # Always load default settings first
        self._settings = utils.read_yaml(defaults.default_settings_file)

        # Update with user or custom settings if not equal to default
        if self.settings_file != defaults.default_settings_file:
            self._settings.update(utils.read_yaml(self.settings_file))

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
        value = self.parse_boolean(value)

        # We can only add to lists
        current = self._settings.get(key)
        if current and not isinstance(current, list):
            logger.exit("You cannot only add to a list variable.")
        value = self.parse_null(value)

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

    def parse_boolean(self, value):
        """
        If the value is True/False, ensure we return a boolean
        """
        if isinstance(value, str) and value.lower() == "true":
            value = True
        elif isinstance(value, str) and value.lower() == "false":
            value = False
        return value

    def parse_null(self, value):
        """
        Given a null or none from the command line, ensure parsed as None type
        """
        if isinstance(value, str) and value.lower() in ["none", "null"]:
            return None

        # Ensure we strip strings
        if isinstance(value, str):
            value = value.strip()
        return value

    def set(self, key, value):
        """
        Set a setting based on key and value. If the key has :, it's nested
        """
        while ":" in key:
            value = str(value)
            key, extra = key.split(":", 1)
            value = f"{extra}:{value}"

        # List values not allowed for set
        current = self._settings.get(key)
        if current and isinstance(current, list):
            logger.exit("You cannot use 'set' for a list. Use add/remove instead.")

        # This is a reference to a dictionary (object) setting
        # We assume only one level of nesting allowed
        if isinstance(value, str) and ":" in value:
            subkey, value = value.split(":")
            value = self.parse_boolean(value)
            value = self.parse_null(value)
            self._settings[key][subkey] = value
        else:
            value = self.parse_boolean(value)
            value = self.parse_null(value)
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

    @property
    def filesystem_registry(self):
        """
        Return the first found filesystem registry
        """
        for path in self.registry:
            if path.startswith("http") or not os.path.exists(path):
                continue
            return path

    def ensure_filesystem_registry(self):
        """
        Ensure that the settings has a filesystem registry.
        """
        found = False
        for path in self.registry:
            if path.startswith("http") or not os.path.exists(path):
                continue
            found = True

        # Cut out early if registry isn't on the filesystem
        if not found:
            logger.exit(
                "This command is only supported for a filesystem registry! Add one or use --registry."
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
        utils.write_yaml(self._settings, filename)

    def __iter__(self):
        for key, value in self.__dict__.items():
            yield key, value

    def update_params(self, params):
        """
        Update a configuration on the fly (no save) only for set/add/remove.
        Unlike the traditional set/get/add functions, this function expects
        each entry in the params list to start with the action, e.g.:

        set:name:value
        add:name:value
        rm:name:value
        """
        # Cut out early if params not provided
        if not params:
            return

        for param in params:
            if not re.search("^(add|set|rm)", param, re.IGNORECASE) or ":" not in param:
                logger.warning(
                    "Parameter update request must start with (add|set|rm):, skipping %s"
                )
            command, param = param.split(":", 1)
            self.update_param(command.lower(), param)

    def update_param(self, command, param):
        """
        Given a parameter, update the configuration on the fly if it's in set/add/remove
        """
        # If we are given a list, assume is key and value at end
        if isinstance(param, list):
            # If one given, assume old format
            if len(param) == 1:
                param = param[0]
            elif len(param) == 2:
                key, value = param
            elif len(param) != 2:
                logger.exit(
                    f"When providing a list, it must be a [key, value]. Found {param}"
                )

        # With a string, assume splittling by :
        if isinstance(param, str):
            if ":" not in param:
                logger.exit(
                    "Param %s is missing a :, should be key:value pair. Skipping."
                    % param
                )
            key, value = param.rsplit(":", 1)

        if command == "set":
            self.set(key, value)
            logger.info("Updated %s to be %s" % (key, value))
        elif command == "add":
            self.add(key, value)
            logger.info("Added %s to %s" % (key, value))
        elif command == "remove":
            self.remove(key, value)
            logger.info("Removed %s from %s" % (key, value))


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
