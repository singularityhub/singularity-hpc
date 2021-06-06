__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021, Vanessa Sochat"
__license__ = "MPL 2.0"


from shpc.logger import logger
from .docker import DockerContainer
import shpc.main.templates
import shpc.utils

import os


class PodmanContainer(DockerContainer):
    """
    A Podman container controller, which is the same as Docker.
    """

    # The module technology adds extensions here
    templatefile = "docker"
    command = "podman"

    def __init__(self):
        if shpc.utils.which("podman")["return_code"] != 0:
            logger.exit("podman is required to use the podman base.")
        super(PodmanContainer, self).__init__()

    def shell(self, image):
        """
        Interactive shell into a container image.
        """
        os.system(
            "podman run -it --rm --entrypoint %s %s"
            % (self.settings.podman_shell, image)
        )
