__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2022, Vanessa Sochat"
__license__ = "MPL 2.0"

from shpc.logger import logger
import shpc.main.modules.versions as versions
import shpc.main.settings as settings
import shpc.main.schemas as schemas
import shpc.utils as utils

import shutil
import jsonschema
import os
import sys


class ViewsHandler:
    """
    A controller for creating or otherwise interacting with views.
    This is intended to create and delete. Interactions like installing or
    uninstalling modules must be done in context of an shpc module install.
    """

    def __init__(self, settings_file):
        self.settings = settings.Settings(settings_file)

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

        out = out or sys.stdout
        if not self.exists(name):
            logger.exit("View %s does not exist." % name)
        view_config = self.view_config(name)
        cfg = utils.read_yaml(view_config)
        jsonschema.validate(instance=cfg, schema=schemas.views)
        for module in cfg["view"]["modules"]:
            out.write("%s\n" % module.rjust(30))

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
        Generate an empty view config. system_modules are not supported yet.
        """
        view_config = self.view_config(name)
        cfg = {"view": {"name": name, "modules": [], "system_modules": []}}
        jsonschema.validate(instance=cfg, schema=schemas.views)
        utils.write_yaml(cfg, view_config)


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
        self._config = utils.read_yaml(self.config_path)

    @property
    def path(self):
        """
        The path is guaranteed to exist because the View is not instantiated
        if it does not.
        """
        return os.path.join(self.settings.views_base, self.name)

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
        # TODO if we want to customize this with additional module load
        # requirements, we will need to create a copy of this file
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
