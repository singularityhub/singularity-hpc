__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2020-2021, Vanessa Sochat"
__license__ = "MPL 2.0"

from shpc.logger import logger
import shpc.utils as utils
import os


def init_db(self, db_path=None):
    """
    initialize the database, meaning we just set the name to be dummy.
    """

    # Database Setup, use default if uri not provided
    self.database = "dummy"
