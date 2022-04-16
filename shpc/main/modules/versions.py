__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021-2022, Vanessa Sochat"
__license__ = "MPL 2.0"

import shpc.utils as utils
import shpc.main.modules.template as templatectl

import os


def _tcl_no_default_version(self, version_file, tag=None):
    """
    No default version (default version in False or None).
    We generate a file with a non-existent version number.
    """
    template = self.template.load("default_version")
    utils.write_file(version_file, template.render())
    # TCL module_sys or True default version, don't generate a .version file


def _lua_module_sys_default_version(self, version_file, tag=None):
    """
    default version (default version in module_sys or True).
    We generate a file with a non-existent version number.
    """
    template = self.template.load("default_version")
    utils.write_file(version_file, template.render())

    # LMOD False or null, don't generate a .version file


def get_version_writer(module_type):
    """
    Return a version writer depending on the module type
    """
    VersionClass = VersionFile
    VersionClass.module_extension = module_type
    if module_type == "tcl":
        VersionClass._no_default_version = _tcl_no_default_version
    if module_type == "lua":
        VersionClass._module_sys_default_version = _lua_module_sys_default_version
    return VersionClass


class VersionFile:
    """
    A VersionFile is a handler to write version files
    """

    def __init__(self, settings):
        self.settings = settings
        self.template = templatectl.Template(settings)

    # Module software can choose how to handle each of these cases
    def _no_default_version(self, version_file, tag):
        return

    def _module_sys_default_version(self, version_file, tag):
        return

    def _set_default_version(self, version_file, tag):
        """
        Set the default version to the given tag
        """
        template = self.template.load("default_version")
        utils.write_file(version_file, template.render(version=tag))

    def write(self, version_dir, latest_tag_installed=None):
        """
        Write a .version file, if there is a template for it.
        """
        if not os.path.exists(version_dir):
            # Happens when uninstalling the last version of a tool
            return

        version_file = os.path.join(version_dir, ".version")

        # No default versions
        if not self.settings.default_version:
            return self._no_default_version(version_file, latest_tag_installed)

        # allow the module software to control versions
        if self.settings.default_version == "module_sys":
            return self._module_sys_default_version(version_file, latest_tag_installed)

        # First or last installed
        if latest_tag_installed and (self.settings.default_version == "last_installed"):
            tag = latest_tag_installed
        else:
            # The versions we actually have
            found = [x for x in os.listdir(version_dir) if x != ".version"]
            if len(found) == 1:
                tag = found[0]
            else:
                if self.settings.default_version == "first_installed":
                    selector = min
                else:
                    selector = max
                tag = selector(
                    found,
                    key=lambda x: utils.creation_date(os.path.join(version_dir, x)),
                )

        # Write the .version file
        return self._set_default_version(version_file, tag)
