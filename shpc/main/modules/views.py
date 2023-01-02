__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2022-2023, Vanessa Sochat"
__license__ = "MPL 2.0"

import os
import shutil
import sys

import jsonschema

import shpc.main.modules.template as templatectl
import shpc.main.modules.versions as versions
import shpc.main.schemas as schemas
import shpc.main.settings as settings
import shpc.utils as utils
from shpc.logger import logger

# Supported variables and defaults
supported_view_variables = {"system_modules": [], "depends_on": []}


# Shared functions
def get_view_module_path(extension):
    """
    Get a view module file name based on an extension
    """
    modulefile_extension = ".lua" if extension == "lua" else ""
    return ".view_module%s" % modulefile_extension


class ViewModule:
    """
    A ViewModule is a .view_module written to the base of a view.
    The symlinked module files always attempt to load it, and it is allowed
    to silently fail if it does not exist. In a view it can exist if the
    user has customized the view with system modules, etc.
    """

    def __init__(self, settings, module_extension):
        self.settings = settings
        self.module_extension = module_extension
        self.template = templatectl.Template(settings)

    def write(self, view_dir, view_config):
        """
        Write a .view_module file in a root view directory based on a config.
        """
        if not os.path.exists(view_dir):
            return
        template = self.template.load("view_module.%s" % self.module_extension)

        # Assemble the .view_module.<extension> full path
        view_module_file = os.path.join(
            view_dir, get_view_module_path(self.module_extension)
        )
        out = template.render(
            system_modules=view_config["view"].get("system_modules", []),
            depends_on=view_config["view"].get("depends_on", []),
        )
        utils.write_file(view_module_file, out)
        logger.info(
            "Wrote updated .view_module.%s: %s"
            % (self.module_extension, view_module_file)
        )


class ViewsHandler:
    """
    A controller for creating or otherwise interacting with views.
    This is intended to create and delete. Interactions like installing or
    uninstalling modules must be done in context of an shpc module install.
    """

    def __init__(self, settings_file, module_sys):
        self.settings = settings.Settings(settings_file)
        self.module_sys = module_sys or self.settings.module_sys
        self.module_sys = "lua" if self.module_sys == "lmod" else "tcl"
        self.view_module = ViewModule(self.settings, self.module_sys)

    def view_path(self, name):
        """
        Get the path to a named view
        """
        return os.path.join(self.settings.views_base, name)

    def view_config(self, name):
        """
        Get the path to a view config
        """
        return os.path.join(self.view_path(name), "view.yaml")

    def exists(self, name):
        """
        Return True or false if a named view exists or not.
        """
        return os.path.exists(self.view_path(name))

    def _variable_checks(self, view_name, var_name):
        """
        Ensure a view exists and a variable name is valid
        """
        if not self.exists(view_name):
            logger.exit("View %s does not exist." % view_name)
        if var_name not in supported_view_variables:
            logger.exit(
                "Variable %s is not supported, supported choices are %s"
                % (var_name, ", ".join(supported_view_variables))
            )

    def add_variable(self, view_name, var_name, values):
        """
        Add a variable to a view. The variable name should be first in a list
        of params.
        """
        self._variable_checks(view_name, var_name)
        cfg = self.load_config(view_name)
        changes, cfg = self._add_variable(var_name, values, cfg)

        # If we have changes, write the view module and updated config
        if changes:
            self.save_view_module(view_name, cfg)

    def _add_variable(self, var_name, values, cfg):
        """
        Given a variable name and value, add to a view. This is the helper
        function to add_variable that handles different types
        """
        # Assume the value can be a single value or list
        if not isinstance(values, list):
            values = [values]

        changes = False
        if var_name not in cfg["view"]:
            cfg["view"][var_name] = supported_view_variables[var_name]

        # Add based on type (currently we only support list)
        if isinstance(cfg["view"][var_name], list):
            for value in values:
                if value not in cfg["view"][var_name]:
                    cfg["view"][var_name].append(value)
                    changes = True
        return changes, cfg

    def remove_variable(self, view_name, var_name, values):
        """
        Remove a variable from a view.
        """
        self._variable_checks(view_name, var_name)
        cfg = self.load_config(view_name)
        changes, cfg = self._remove_variable(var_name, values, cfg)
        if changes:
            self.save_view_module(view_name, cfg)
        else:
            logger.warning("No matches found. No changes were made to the view.")

    def _remove_variable(self, var_name, values, cfg):
        """
        Given a variable name and value, remove from a view.
        """
        # Assume the value can be a single value or list
        if not isinstance(values, list):
            values = [values]

        # Cut out early if the key isn't there
        changes = False
        if var_name not in cfg["view"]:
            return changes, cfg

        # Add based on type (currently we only support list)
        if isinstance(cfg["view"][var_name], list):
            for value in values:
                if value in cfg["view"][var_name]:
                    cfg["view"][var_name] = [
                        x for x in cfg["view"][var_name] if x != value
                    ]
                    changes = True
        return changes, cfg

    def create(self, name):
        """
        Create a new named view. By default, it is empty (no modules)
        """
        if self.exists(name):
            logger.exit(
                "View %s already exists. Delete it first to re-create it." % name
            )

        view_root = self.view_path(name)
        utils.mkdir_p(view_root)

        # Add a default template there
        self.generate_view_config(name)
        logger.info("View %s was created in %s" % (name, view_root))

    def list_views(self, out=None):
        """
        List all views available.
        """
        out = out or sys.stdout
        for name in os.listdir(self.settings.views_base):
            out.write("%s\n" % name.rjust(30))

    def list(self, name=None, out=None):
        """
        List modules installed to a view
        """
        # If no name provided, list all views known
        if not name:
            self.list_views(out=out)
            return

        cfg = self.load_config(name)
        out = out or sys.stdout
        for module in cfg["view"]["modules"]:
            out.write("%s\n" % module.rjust(30))

    def save_view_module(self, view_name, cfg):
        """
        Save of a view module includes the view.yaml and the .view_module
        """
        self.save_config(view_name, cfg)
        view_dir = os.path.dirname(self.view_config(view_name))
        self.view_module.write(view_dir, cfg)

    def save_config(self, name, cfg):
        """
        Save a config for a named view, assuring it validates first.
        """
        view_config = self.view_config(name)
        jsonschema.validate(instance=cfg, schema=schemas.views)
        utils.write_yaml(cfg, view_config)

    def load_config(self, name):
        """
        Load and validate a named view config. Exit if the view does not exist.
        """
        if not self.exists(name):
            logger.exit("View %s does not exist." % name)
        view_config = self.view_config(name)
        cfg = utils.read_yaml(view_config)
        jsonschema.validate(instance=cfg, schema=schemas.views)
        return cfg

    def delete(self, name, force=False):
        """
        Delete a named view.
        """
        if not self.exists(name):
            logger.exit("View %s does not exist and cannot be deleted." % name)

        view_root = self.view_path(name)
        if not force and not utils.confirm_action(
            "Are you sure you want to delete view %s" % name
        ):
            logger.exit("Not deleting view %s." % view_root)

        # This should be all symlinks plus the config
        shutil.rmtree(view_root)
        logger.info("%s has been deleted." % view_root)

    def edit(self, name):
        """
        Open an editor to edit a named view.
        """
        if not self.exists(name):
            logger.exit("View %s does not exist and cannot be edited." % name)
        self.settings.edit(self.view_config(name))

    def generate_view_config(self, name):
        """
        Generate an empty view config. system_modules/depends_on are not supported yet.
        """
        cfg = {
            "view": {
                "name": name,
                "modules": [],
                "system_modules": [],
                "depends_on": [],
            }
        }
        self.save_config(name, cfg)


class View:
    """
    An shpc view is created from a core module install.
    """

    def __init__(self, name, settings, symlink_extension, module_extension, modulefile):
        """
        init of a view must be done when it exists, and from the base.ModuleBase
        (instantiated with either lmod or tcl). There is no concept of a view
        without this central installation.
        """
        self.name = name
        self.settings = settings
        self.symlink_extension = symlink_extension
        self.module_extension = module_extension
        self.versionfile = versions.VersionFile(self.settings, self.module_extension)
        self.modulefile = modulefile
        self.reload()

    @property
    def path(self):
        """
        The path is guaranteed to exist because the View is not instantiated
        if it does not.
        """
        return os.path.join(self.settings.views_base, self.name)

    @property
    def module_path(self):
        """
        Path to view module, with needed extension.
        """
        return os.path.join(self.path, get_view_module_path(self.module_extension))

    def reload(self):
        """
        Reload the view's config (given a change)
        """
        self._config = utils.read_yaml(self.config_path)

    def symlink_exists(self, module_dir):
        """
        Return True or false if the view to a specific version exists or not.
        This check is looking for a symlink.
        """
        return os.path.islink(self.get_symlink_path(module_dir))

    def exists(self, module_dir):
        """
        Determine if a specific version is symlinked OR there is a matching
        directory for a module. This exists is intended for looking to see
        if a module_dir pattern (either to a directory or version) exists.
        E.g.,:

        shpc uninstall ghcr.io/autamus/clingo:5.5.1 will link to a lua file
        shpc uninstall ghcr.io/autamus/clingo will point to a directory.
        """
        symlink_path = self.get_symlink_dir(module_dir, has_version=False)
        return os.path.exists(symlink_path) or self.symlink_exists(module_dir)

    def _sub_module_base(self, path):
        return path.replace(self.settings.module_base, "$module_base")

    def _sub_views_base(self, path):
        return path.replace(self.settings.views_base, "$views_base")

    @property
    def config_path(self):
        """
        Get the config path to the view
        """
        return os.path.join(self.path, "view.yaml")

    def confirm_install(self, module_dir, force=False):
        """
        Check if a module install exists under a view. A module install to a view
        is a symbolic link, so here we are checking for existence of that. If
        force is True, we continue even if it already exists.
        """
        if self.symlink_exists(module_dir):
            if force:
                logger.info(
                    "Overwriting view %s install of %s, as requested"
                    % (self.name, module_dir)
                )
            elif not utils.confirm_action(
                "%s in view %s already exists, are you sure you want to overwrite"
                % (self._sub_module_base(module_dir), self.name)
            ):
                sys.exit(0)

    def get_symlink_path(self, module_dir):
        """
        Get the symlink path of a module installed to the view
        """
        # $root_dir/$view_name/$module_dir + extension
        return self.get_symlink_dir(module_dir) + self.symlink_extension

    def get_symlink_dir(self, module_dir, has_version=True):
        """
        If a directory of a symlink is provided, return it without module extension
        """
        # $root_dir/$view_name/$module_dir
        return os.path.join(self.path, self.module_slug(module_dir, has_version))

    def module_slug(self, module_dir, has_version=True):
        """
        Get the module short name based on the original module path.
        """
        if has_version:
            return os.path.join(*module_dir.split(os.sep)[-2:])
        return os.path.join(*module_dir.split(os.sep)[-1:])

    def module_name(self, module_dir, has_version=True):
        """
        Retrieve the original module name, which is the unique id.
        """
        dirname = module_dir.replace(self.settings.module_base + os.sep, "")

        # Without a version, we return the full directory name
        if not has_version:
            return dirname

        # Otherwise the last "directory" is actually the version
        name, version = dirname.rsplit(os.sep, 1)
        return "%s:%s" % (name, version)

    def install(self, module_dir):
        """
        Install a module to the view, which is a symbolic link.
        """
        symlink_path = self.get_symlink_path(module_dir)

        # If there is a previous link, unlink and re-create it.
        if os.path.exists(symlink_path):
            os.unlink(symlink_path)
        symlink_dir = os.path.dirname(symlink_path)

        # If the parent directory doesn't exist, make it
        if not os.path.exists(symlink_dir):
            utils.mkdir_p(symlink_dir)

        # The target for the symlink is the original module file
        symlink_target = os.path.join(module_dir, self.modulefile)

        # Courtesy print to get an easier to read path
        logger.info(
            "Creating link %s -> %s"
            % (
                self._sub_module_base(symlink_target),
                self._sub_views_base(symlink_path),
            )
        )

        # Create the symbolic link and version file
        os.symlink(symlink_target, symlink_path)
        self.versionfile.write(os.path.dirname(symlink_path))
        self.add_module(module_dir)

    def save(self):
        """
        Save the config to file, validating first.
        """
        jsonschema.validate(instance=self._config, schema=schemas.views)
        utils.write_yaml(self._config, self.config_path)

    def add_module(self, module_dir):
        """
        Given the name of a module directory from the main root, add to the
        list of installed for the view.
        """
        module_uid = self.module_name(module_dir)
        if module_uid not in self._config["view"]["modules"]:
            self._config["view"]["modules"].append(module_uid)
            self.save()

    def remove_module(self, module_dir, has_version=False):
        """
        Given the name of a module directory or path from the main root, remove.
        """
        module_uid = self.module_name(module_dir, has_version)
        updated = []
        change = False
        for module in self._config["view"]["modules"]:

            # This will match an entire dirname (if all delted) or a specific version
            if module_uid not in module:
                updated.append(module)
            else:
                change = True

        # Only update if there is a change
        if change:
            self._config["view"]["modules"] = updated
            self.save()

    def create_symlink(self, module_dir):
        """
        Create the symlink if desired by the user!
        """
        symlink_path = self.get_symlink_path(module_dir)
        if os.path.exists(symlink_path):
            os.unlink(symlink_path)
        symlink_dir = os.path.dirname(symlink_path)

        # If the parent directory doesn't exist, make it
        if not os.path.exists(symlink_dir):
            utils.mkdir_p(symlink_dir)

        symlink_target = os.path.join(module_dir, self.modulefile)
        logger.info("Creating link %s -> %s" % (symlink_target, symlink_path))

        # Create the symbolic link!
        os.symlink(symlink_target, symlink_path)

        # Create .version
        self.versionfile.write(os.path.dirname(symlink_path))

    def uninstall(self, module_dir):
        """
        Uninstall of a module means removal of symlink directories if they exist.
        This can either be for a specific version (a lua file) or the entire
        view directory with the module
        """
        # Case 1: delete a specific symlinked module
        if self.symlink_exists(module_dir):
            self._uninstall_version(module_dir)
            self.remove_module(module_dir, has_version=True)
            return

        # Case 2: delete an entire symlink tree (no version provided)
        symlink_path = self.get_symlink_dir(module_dir, has_version=False)
        if os.path.exists(symlink_path):
            utils.remove_to_base(symlink_path, self.path)
            logger.info("%s has been removed." % symlink_path)
            self.remove_module(module_dir, has_version=False)

    def _uninstall_version(self, module_dir):
        """
        Install a specific version expects a $view/$module/$version.lua
        """
        symlinked_module = self.get_symlink_path(module_dir)

        if os.path.islink(symlinked_module):
            # Remove and clean up directories that become empty
            utils.remove_to_base(symlinked_module, self.path)
            logger.info("%s has been removed." % symlinked_module)

            # Update .version
            self.versionfile.write(os.path.dirname(symlinked_module))
        elif os.path.exists(symlinked_module):
            logger.error("%s exists and is not a symlink!" % symlinked_module)
