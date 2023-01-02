__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021-2023, Vanessa Sochat"
__license__ = "MPL 2.0"

from .base import ModuleBase


class Client(ModuleBase):
    def __init__(self, **kwargs):
        """
        An Lmod client generates an lmod recipe for install
        """
        # With Lmod, the symlink names must end with `.lua` too
        self.symlink_extension = ".lua"
        self.module_extension = "lua"
        super(Client, self).__init__(**kwargs)
