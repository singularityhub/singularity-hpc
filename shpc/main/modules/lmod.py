__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021, Vanessa Sochat"
__license__ = "MPL 2.0"

from shpc.main.modules import ModuleBase


class Client(ModuleBase):
    def __init__(self, **kwargs):
        """
        An Lmod client generates an lmod recipe for install
        """
        super(Client, self).__init__(**kwargs)
        self.module_extension = "lua"
