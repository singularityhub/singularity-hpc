__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2022-2023, Vanessa Sochat"
__license__ = "MPL 2.0"


from . import generators as gen
from .base import WrapperScript


def generate(image, container, config, **kwargs):
    """
    Generate one or more wrapper scripts for a container.

    Required arguments for all include container (class), image (path), settings
    All kwargs go in optional. The core set of constructor kwargs are provided
    to each wrapper generator. This can be extended to include custom arguments.
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

    # Default wrapper for container technology, used for aliases unless overridden
    default_wrapper = load_default_wrapper(constructor_kwargs)

    # Generate wrappers for command aliases
    generated += gen.alias_wrappers(aliases, default_wrapper, constructor_kwargs)

    # Generate wrappers for container interactions
    generated += gen.container_wrappers(constructor_kwargs)

    # Container level wrapper scripts (allow eventually supporting custom podman)
    generated += gen.custom_container_wrappers(constructor_kwargs)
    return list(set(generated))


def load_default_wrapper(constructor_kwargs):
    """
    Given a container and user settings, load a default wrapper.
    """
    default_wrapper = None
    container = constructor_kwargs["container"]
    settings = constructor_kwargs["settings"]

    default_template_name = settings.wrapper_scripts.get(container.command)
    if default_template_name:
        default_wrapper = WrapperScript(default_template_name, **constructor_kwargs)
        # include_container_dir not set -> only look in the global locations
        default_wrapper.load_template()
    return default_wrapper
