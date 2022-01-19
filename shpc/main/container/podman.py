__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021-2022, Vanessa Sochat"
__license__ = "MPL 2.0"


from .docker import DockerContainer

import os


class PodmanContainer(DockerContainer):
    """
    A Podman container controller, which is the same as Docker.
    """

    # The module technology adds extensions here
    templatefile = "docker"
    command = "podman"

    def shell(self, image):
        """
        Interactive shell into a container image.
        """
        os.system(
            "podman run -it --rm --entrypoint %s %s"
            % (self.settings.podman_shell, image)
        )
