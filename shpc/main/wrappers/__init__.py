__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2022, Vanessa Sochat"
__license__ = "MPL 2.0"

from .base import WrapperScript
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

    constructor_kwargs = {
        "settings": settings,
        "config": config,
        "container": container,
        "image": image,
        **kwargs,
    }

    # Default wrapper for this container technology. Will be used for all
    # aliases (unless overriden)
    default_wrapper = None
    default_template_name = settings.wrapper_scripts.get(container.command)
    if default_template_name:
        default_wrapper = WrapperScript(
            wrapper_template=default_template_name, **constructor_kwargs
        )
        # No extra parameters -> only look in the global locations
        default_wrapper.load_template()

    # Container level wrapper scripts (allow eventually supporting custom podman)
    scripts = {
        "singularity": config.singularity_scripts,
        "docker": config.docker_scripts,
        "podman": config.docker_scripts,
    }
    # Additional commands defined in the custom container.yaml script section
    listing = scripts.get(container.templatefile, [])
    container_wrappers = {}
    for alias, template_name in listing.items():
        wrapper = WrapperScript(wrapper_template=template_name, **constructor_kwargs)
        # Template wrapper scripts may live alongside container.yaml
        wrapper.load_template(include_container_dir=True)
        container_wrappers[alias] = wrapper

    # Command aliases
    for alias in aliases:
        # Allow overriding the template name in the scripts section
        if alias["name"] in container_wrappers:
            wrapper = container_wrappers.pop(alias["name"])
        else:
            wrapper = default_wrapper
        if wrapper:
            # NB: alias is a dictionary
            generated += wrapper.generate(alias["name"], alias)

    # Additional commands defined in the scripts sections
    for alias, wrapper in container_wrappers.items():
        # NB: alias is a string
        generated += wrapper.generate(alias, alias)

    return list(set(generated))
