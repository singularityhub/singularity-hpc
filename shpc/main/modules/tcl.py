__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021-2022, Vanessa Sochat"
__license__ = "MPL 2.0"

from .base import ModuleBase


class Client(ModuleBase):
    def __init__(self, **kwargs):
        """
        An Lmod client generates an lmod recipe for install
        """
        # The extension is technically not required, but we still set one for clarity
        self.module_extension = "tcl"
        # Except for symlink, since the goal is to have short names
        self.symlink_extension = ""
        super(Client, self).__init__(**kwargs)
