__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2022-2023, Vanessa Sochat"
__license__ = "MPL 2.0"

import os

from jinja2 import Template

from shpc.logger import logger

from .base import WrapperScript

# These functions are under the generate namespace, so you can assume
# they generate the content being referenced


def alias_wrappers(aliases, default_wrapper, constructor_kwargs):
    """
    Given a set of aliases and a default wrapper, generate alias-specific wrappers.
    """
    container = constructor_kwargs["container"]
    generated = []
    custom_wrapper_option_name = "%s_script" % container.templatefile
    for alias in aliases:
        # Allow overriding the template name in the script option
        if custom_wrapper_option_name in alias:
            wrapper = WrapperScript(
                alias[custom_wrapper_option_name], **constructor_kwargs
            )
            wrapper.load_template(include_container_dir=True)
        elif default_wrapper:
            wrapper = default_wrapper
        else:
            logger.exit(
                "Can't generate a wrapper script for '%s' as there is no template defined for %s"
                % (alias["name"], container.templatefile)
            )

        # NB: alias is a dictionary
        generated += wrapper.generate(alias["name"], alias)
    return generated


def custom_container_wrappers(constructor_kwargs):
    """
    Generate wrappers for scripts defined in the container.yaml
    """
    container = constructor_kwargs["container"]
    config = constructor_kwargs["config"]

    generated = []
    scripts = {
        "singularity": config.singularity_scripts,
        "docker": config.docker_scripts,
        "podman": config.docker_scripts,
    }
    # Additional commands defined in the custom container.yaml script section
    listing = scripts.get(container.templatefile) or {}
    for alias, template_name in listing.items():
        wrapper = WrapperScript(template_name, **constructor_kwargs)
        # Template wrapper scripts may live alongside container.yaml
        wrapper.load_template(include_container_dir=True)
        # NB: alias is a string
        generated += wrapper.generate(alias, alias)
    return generated


def container_wrappers(constructor_kwargs):
    """
    Generate wrappers for exec / shell / run etc.
    """
    # We use the config preference against the settings to generate the prefix
    # E.g., module "python" would generate python-shell <tool>-shell
    config = constructor_kwargs["config"]
    settings = constructor_kwargs["settings"]
    container = constructor_kwargs["container"]

    template = Template(settings.module_name)

    # docker templates are also for podman
    command = container.command
    if command == "podman":
        command = "docker"

    # Prepare template file-names with prefix (e.g., python)
    prefix = template.render(parsed_name=config.name)
    template_names = {
        f"{prefix}-shell": os.path.join(command, "shell.sh"),
        f"{prefix}-container": os.path.join(command, "container.sh"),
        f"{prefix}-exec": os.path.join(command, "exec.sh"),
        f"{prefix}-run": os.path.join(command, "run.sh"),
    }

    # Only singularity has inspect-runscript / inspect-deffile
    if command == "singularity":
        template_names.update(
            {
                f"{prefix}-inspect-deffile": os.path.join(
                    container.command, "inspect-deffile.sh"
                ),
                f"{prefix}-inspect-runscript": os.path.join(
                    container.command, "inspect-runscript.sh"
                ),
            }
        )
    else:
        template_names.update(
            {f"{prefix}-inspect": os.path.join(command, "inspect.sh")}
        )

    generated = []
    for script, template_name in template_names.items():
        wrapper = WrapperScript(template_name, **constructor_kwargs)
        wrapper.load_template()
        generated += wrapper.generate(script)
    return generated
