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

    def delete(self, name, force=False):
        """
        Delete a named view.
        """
        if self.exists(name):
            logger.exit("View does not exist and cannot be deleted." % name)

        view_root = self.view_path(name)
        if not force and not utils.confirm_action:
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

    def __init__(self, name, settings, symlink_extension, module_extension):
        self.name = name
        self.settings = settings
        self.symlink_extension = symlink_extension
        self.module_extension = module_extension
        self.versionfile = versions.get_version_writer(self.module_extension)(
            self.settings
        )
        self._config = utils.read_yaml(self.config_path)

    @property
    def path(self):
        """
        The path is guaranteed to exist because the View is not instantiated
        if it does not.
        """
        return os.path.join(self.settings.views_base, self.name)

    def exists(self, module_dir):
        """
        Return True or false if the view exists or not.
        """
        return os.path.exists(self.get_symlink_path(module_dir))

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
        if self.exists(module_dir):
            if force:
                logger.info(
                    "Overwriting view %s install of %s, as requested"
                    % (self.name, module_dir)
                )
            elif not utils.confirm_action(
                "%s/%s already exists, are you sure you want to overwrite"
                % (self.name, module_dir)
            ):
                sys.exit(0)

    def get_symlink_path(self, module_dir):
        """
        Get the symlink path of a module installed to the view
        """
        # $root_dir/$view_name/$module_dir + extension
        return (
            os.path.join(self.path, self.module_name(module_dir))
            + self.symlink_extension
        )

    def module_name(self, module_dir):
        """
        Get the module name based on the original module path.
        """
        return os.path.join(module_dir.split(os.sep)[-2:])

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
        logger.info("Creating link %s -> %s" % (symlink_target, symlink_path))

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
        if module_uid not in self._config["modules"]:
            self._config["modules"].append(module_uid)
            self.save()

    def remove_module(self, module_dir):
        """
        Given the name of a module directory from the main root, remove.
        """
        module_uid = self.module_name(module_dir)
        if module_uid in self._config["modules"]:
            self._config["modules"] = [
                x for x in self._config["modules"] if x != module_uid
            ]
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
        self.write_version_file(os.path.dirname(symlink_path))

    def uninstall(self, module_dir):
        """
        Uninstall of a module means removal of symlink directories if they exist
        """
        # TODO load config and remove
        if not self.exists(module_dir):
            return

        symlinked_module = self.get_symlink_path(module_dir)

        if os.path.islink(symlinked_module):
            # Remove and clean up directories that become empty
            utils.remove_to_base(symlinked_module, self.path)
            logger.info("%s has been removed." % symlinked_module)

            # Update .version
            self.write_version_file(os.path.dirname(symlinked_module))
        elif os.path.exists(symlinked_module):
            logger.error("%s exists and is not a symlink!" % symlinked_module)
        elif self.settings.symlink_tree:
            # Should not happen. The symlink has someone already been deleted
            logger.warning("%s does not exist." % symlinked_module)
