__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021-2022, Vanessa Sochat"
__license__ = "MPL 2.0"

from shpc.logger import logger
from .docker import DockerImage
from .versions import filter_versions


def update_config_tags(config):
    """
    Given a container config, update the latest tags
    """
    if config.docker:
        logger.info("Looking for updated digests for %s" % config.docker)
        latest_tags = get_latest_tags(config.docker)

        # Notice this API call truncates at 50
        versions = filter_versions(latest_tags, filters=config.filters)

        # Get list of current tags, and update with new versions
        current_tags = dict(config.get("tags", {}))
        current_tags.update({x.vstring: "unknown" for x in versions})

        # Get updated hashes
        for tag, _ in current_tags.items():
            digest = get_container_tag(config.docker, tag)
            if digest:
                current_tags[tag] = digest[tag]

        # Now do the same practice as before - try to derive what is latest
        sorted_tags = filter_versions(
            list(current_tags.keys()), max_length=len(current_tags)
        )

        # Update latest and the rest
        if sorted_tags:
            config.set(
                "latest", {sorted_tags[0].vstring: current_tags[sorted_tags[0].vstring]}
            )
            config.set(
                "tags", {x.vstring: current_tags[x.vstring] for x in sorted_tags}
            )

    return config


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


def get_latest_tags(container_name, tag=None):
    """
    Given a container name, get the latest tags.
    """
    image = DockerImage(container_name)
    return image.tags()
