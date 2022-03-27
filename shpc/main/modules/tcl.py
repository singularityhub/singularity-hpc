__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021-2022, Vanessa Sochat"
__license__ = "MPL 2.0"

from .base import ModuleBase
import shpc.utils as utils


class Client(ModuleBase):
    def __init__(self, **kwargs):
        """
        An Lmod client generates an lmod recipe for install
        """
        super(Client, self).__init__(**kwargs)
        self.module_extension = "tcl"

    def _no_default_version(self, version_file, tag=None):
        """
        No default version (default version in False or None).
        We generate a file with a non-existent version number.
        """
        template = self._load_template("default_version")
        utils.write_file(version_file, template.render())

    # TCL module_sys or True default version, don't generate a .version file
