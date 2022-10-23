__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021-2022, Vanessa Sochat"
__license__ = "MPL 2.0"


import shpc.defaults
import shpc.utils
from shpc.logger import logger

from .settings import Settings


def get_client(quiet=False, **kwargs):
    """
    Get a singularity HPC client based on the backend (e.g., Lmod)
    and container technology (currently just Singularity) of interest.

    Parameters
    ==========
    quiet: if True, suppress most output about the client (e.g. speak)

    """
    # The name of the module system
    module_sys = kwargs.get("module_sys")
    validate = kwargs.get("validate", True)

    # Load user settings to add to client, and container technology
    settings = Settings(kwargs.get("settings_file"), validate)
    container = kwargs.get("container_tech") or settings.container_tech

    # Use the user provided module OR the default
    module_sys = module_sys or settings.get("module_sys", "lmod")

    # Determine the client based on the module name (defaults to base client)
    if module_sys == "lmod":
        from shpc.main.modules.lmod import Client
    elif module_sys == "tcl":
        from shpc.main.modules.tcl import Client
    else:
        from .client import Client

    # Add the container operator
    if container == "singularity":
        from shpc.main.container import SingularityContainer

        Client.container = SingularityContainer()

    elif container == "podman":
        from shpc.main.container import PodmanContainer

        Client.container = PodmanContainer()

    elif container == "docker":
        from shpc.main.container import DockerContainer

        Client.container = DockerContainer()

    # The containe should have access to settings too
    if hasattr(Client, "container"):
        Client.container.settings = settings

    # Give the user a warning:
    if not shpc.utils.check_install(container):
        logger.warning(
            "%s is not installed, functionality might be limited." % container.upper()
        )

    # Pass on settings and container to module too
    Client.quiet = quiet
    Client.settings = settings
    return Client()
