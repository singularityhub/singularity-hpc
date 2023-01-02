__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021-2023, Vanessa Sochat"
__license__ = "MPL 2.0"

import os

import shpc.main.modules.template as templatectl
import shpc.utils as utils


class VersionFile:
    """
    A VersionFile is a handler to write version files
    """

    def __init__(self, settings, module_extension):
        self.settings = settings
        self.module_extension = module_extension
        self.template = templatectl.Template(settings)

    def _no_default_version(self, version_file, tag):
        if self.module_extension == "tcl":
            template = self.template.load("default_version")
            utils.write_file(version_file, template.render())
        # LMOD (lua) False or null, don't generate a .version file

    def _module_sys_default_version(self, version_file, tag):
        if self.module_extension == "lua":
            template = self.template.load("default_version")
            utils.write_file(version_file, template.render())
        # TCL module_sys or True default version, don't generate a .version file

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
        if self.settings.default_version in [False, None]:
            return self._no_default_version(version_file, latest_tag_installed)

        # allow the module software to control versions
        if self.settings.default_version in [True, "module_sys"]:
            return self._module_sys_default_version(version_file, latest_tag_installed)

        # First or last installed
        if latest_tag_installed and self.settings.default_version == "last_installed":
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
