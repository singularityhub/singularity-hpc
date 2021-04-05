__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021, Vanessa Sochat"
__license__ = "MPL 2.0"


from .settings import Settings

from shpc.utils import check_install
from shpc.logger import logger


def get_client(quiet=False, **kwargs):
    """
    Get a singularity HPC client based on the backend (e.g., LMOD)
    and container technology (currently just Singularity) of interest.

    Parameters
    ==========
    quiet: if True, suppress most output about the client (e.g. speak)

    """
    # The name of the module and container technology to use
    module = kwargs.get("module")
    container = kwargs.get("container_tech")

    # Determine the client based on the module name (defaults to base client)
    if module == "lmod":
        from .lmod import Client
    else:
        from .client import Client

    # Add the container operator
    if container == "singularity":
        from .container import SingularityContainer

        Client._container = SingularityContainer()

    # Give the user a warning:
    if not check_install():
        logger.warning("Singularity is not installed, functionality might be limited.")
    Client.quiet = quiet

    # Load user settings, add to client
    settings = Settings(kwargs.get("settings_file"))
    sqlite_enabled = False

    # Add dummy or real database functions to the client (not currently needed)
    if not sqlite_enabled or settings.get("disable_database", False):
        # logger.warning("Database disabled. Install sqlalchemy for full functionality")
        from shpc.database.dummy import init_db

        Client._init_db = init_db
    else:
        logger.warning("Using a database is not yet supported, and may be removed.")
        from shpc.database.models import init_db

        # Add database actions
        Client._init_db = init_db

    # Initialize the database and client
    Client.settings = settings
    return Client()
