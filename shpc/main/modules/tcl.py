__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021-2022, Vanessa Sochat"
__license__ = "MPL 2.0"

from shpc.main.modules import ModuleBase
import shpc.utils as utils
import os


class Client(ModuleBase):
    def __init__(self, **kwargs):
        """
        An Lmod client generates an lmod recipe for install
        """
        super(Client, self).__init__(**kwargs)
        self.module_extension = "tcl"
                
    def write_version_file(self, uri, tag):
        """
        Create the .version file, if there is a template for it.
        """
        version_dir = os.path.join(self.settings.module_base, uri)
        version_file = os.path.join(version_dir, ".version")

        # Case 1: no default version - generate a file with a non-existent version number
        if not self.settings.default_version:
            template = self._load_template("default_version")
            utils.write_file(version_file, template.render())
        
        # Case 2: default version but not automatic update (no version file, skip)
        # Case 3: default version and automatic update
        elif self.settings.default_version and self.settings.default_version_automatic is True:
            template = self._load_template("default_version")
            utils.write_file(version_file, template.render(version=tag.name))
