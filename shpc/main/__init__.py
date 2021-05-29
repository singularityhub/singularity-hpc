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
    # The name of the module
    module = kwargs.get("module")

    # Load user settings to add to client, and container technology
    settings = Settings(kwargs.get("settings_file"))
    container = kwargs.get("container_tech") or settings.container_tech

    # Use the user provided module OR the default
    module = module or settings.get("module_sys", "lmod")

    # Determine the client based on the module name (defaults to base client)
    if module == "lmod":
        from .lmod import Client
    elif module == "tcl":
        from .tcl import Client
    else:
        from .client import Client

    # Add the container operator
    if container == "singularity":
        from .container import SingularityContainer
        Client._container = SingularityContainer()

    elif container == "podman"
        from .container import PodmanContainer
        Client._container = PodmanContainer()

    # Give the user a warning:
    if not check_install():
        logger.warning("Singularity is not installed, functionality might be limited.")
    Client.quiet = quiet
    Client.settings = settings
    return Client()
