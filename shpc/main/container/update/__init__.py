__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021-2022, Vanessa Sochat"
__license__ = "MPL 2.0"

from shpc.logger import logger

from .diff import print_diff
from .docker import DockerImage
from .versions import filter_versions

assert print_diff


def update_config_tags(config, filters=None):
    """
    Given a container config, update the latest tags
    """
    # Both docker and oras are from OCI registries
    if config.docker or config.oras:
        uri = config.docker or config.oras

        logger.info("Looking for updated digests for %s" % uri)
        latest_tags = get_latest_tags(uri)

        # Notice this API call truncates at 50
        versions = filter_versions(latest_tags, filters=filters or config.filter)

        # Get list of current tags, and update with new versions
        current_tags = dict(config.get("tags", {}))

        # Now do the same practice as before - try to derive what is latest
        sorted_tags = filter_versions(
            list(current_tags.keys()), max_length=len(current_tags)
        )

        # Only take the earliest back, e.g., if current tags have 1.3 as earliest
        # do not add a 1.2 we find in versions
        earliest_tag = get_earliest_tag(sorted_tags)

        # Only try to derive earliest if we have numbers
        recent_versions = versions
        if earliest_tag:
            recent_versions = []
            for version in versions:
                if version < earliest_tag:
                    break
                recent_versions.append(version)

        # Now update current tags
        current_tags.update(
            {
                x.vstring: "unknown"
                for x in recent_versions
                if x.vstring not in current_tags
            }
        )

        # Get updated hashes
        tags = list(current_tags.keys())
        for tag in tags:
            try:
                digest = get_container_tag(uri, tag)
            except:
                digest = {tag: current_tags[tag]}

            if not digest or digest[tag] == "unknown":
                del current_tags[tag]
            else:
                current_tags[tag] = digest[tag]

        # Sort them again, just for versions
        sorted_tags = filter_versions(
            list(current_tags.keys()), max_length=len(current_tags)
        )

        # Filter down to those with version strings to get latest
        versioned_tags = [x for x in sorted_tags if x.version]
        if not versioned_tags:
            versioned_tags = sorted_tags

        # Newest at end again
        versioned_tags.sort()

        # Update latest and the rest
        if sorted_tags:
            config.set(
                "latest",
                {versioned_tags[-1].vstring: current_tags[versioned_tags[-1].vstring]},
            )
            config.set("tags", {x: v for x, v in current_tags.items()})

    return config


def get_earliest_tag(sorted_tags):
    """
    Given a list of sorted tags, try to find the earliest. If we cannot,
    return None. This assumes a list sorted with latest at the beginning.
    """
    earliest_tags = list(reversed(sorted_tags))
    earliest_tag = None
    idx = 0
    while not earliest_tag and idx < len(earliest_tags):
        earliest_tag = earliest_tags[idx]
        if not earliest_tag.version:
            earliest_tag = None
            idx += 1
    return earliest_tag


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
