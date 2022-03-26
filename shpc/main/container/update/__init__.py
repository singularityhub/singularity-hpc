__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021-2022, Vanessa Sochat"
__license__ = "MPL 2.0"

from .docker import DockerImage


def get_container_tag(container_name, tag=None):
    """
    Given a container name, get the latest list of tags and digests.
    This can be extended when we have a container updater.
    """
    image = DockerImage(container_name)

    # Get a specific tag
    tag = tag or "latest"
    digest = image.digest(tag)
    return {tag: digest}
