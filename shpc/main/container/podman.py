__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021-2023, Vanessa Sochat"
__license__ = "MPL 2.0"


from .docker import DockerContainer


class PodmanContainer(DockerContainer):
    """
    A Podman container controller, which is the same as Docker.
    """

    # The module technology adds extensions here
    templatefile = "docker"
    command = "podman"

    @property
    def shell_path(self):
        """
        Return the path of the shell to use with this container.
        """
        return self.settings.podman_shell
