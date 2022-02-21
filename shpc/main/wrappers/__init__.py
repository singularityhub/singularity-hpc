__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2022, Vanessa Sochat"
__license__ = "MPL 2.0"

from .scripts import get_wrapper_script
import os


here = os.path.abspath(os.path.dirname(__file__))


def generate(image, container, config, **kwargs):
    """
    Generate one or more wrapper scripts for a container.

    Required arguments for all include container (class), image (path), settings
    All kwargs go in optional. And this can be extended to include custom arguments.
    """
    # Return list of generated templates
    generated = []

    settings = container.settings
    aliases = kwargs.get("aliases", [])

    # Global wrapper scripts are generated via aliases
    for container_tech in ["docker", "podman", "singularity"]:
        template_name = settings.wrapper_scripts.get(container_tech)
        if template_name and aliases and container_tech == container.command:
            wrapper = get_wrapper_script(template_name)(
                settings=settings,
                wrapper_template=template_name,
                config=config,
                container=container,
                image=image,
                **kwargs
            )
            generated += wrapper.generate_aliases()

    # Container level wrapper scripts (allow eventually supporting custom podman)
    scripts = {
        "singularity": config.singularity_scripts,
        "docker": config.docker_scripts,
        "podman": config.docker_scripts,
    }
    for command, listing in scripts.items():

        # Don't look if no custom container.yaml scripts OR wrong container tech
        if not listing or container.templatefile != command:
            continue
        for alias, template_name in listing.items():
            wrapper = get_wrapper_script(template_name)(
                settings=settings,
                wrapper_template=template_name,
                config=config,
                container=container,
                image=image,
                **kwargs
            )
            generated += wrapper.generate(alias)

    return list(set(generated))
