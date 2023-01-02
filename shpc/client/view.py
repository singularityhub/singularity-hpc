__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2023, Vanessa Sochat"
__license__ = "MPL 2.0"

import os
import sys

import jsonschema

import shpc.main.modules.views as views
import shpc.main.schemas as schemas
import shpc.utils as utils
from shpc.logger import logger
from shpc.main import get_client


def create_from_file(
    view_name,
    filename,
    module_sys=None,
    settings_file=None,
    quiet=False,
    config_params=None,
    force=False,
):
    """
    Create a view from file
    """
    if not os.path.exists(filename):
        logger.exit("%s does not exist." % filename)

    view_handler = views.ViewsHandler(
        settings_file=settings_file, module_sys=module_sys
    )
    view_handler.settings.update_params(config_params)

    # Create the view
    view_handler.create(view_name)

    # Load and validate here, then create the view, install
    cfg = utils.read_yaml(filename)
    jsonschema.validate(instance=cfg, schema=schemas.views)

    # At this point we only potentially have modules to install
    install_modules = cfg["view"]["modules"]
    if not install_modules:
        return

    # The client controls install, uninstall, and edit of views
    cli = get_client(quiet=quiet, settings_file=settings_file)
    cli.settings.update_params(config_params)

    # Extra modules to install
    for install_module in install_modules:

        # TODO: can we cut out early if already installed?
        cli.install(install_module, force=force)
        cli.view_install(view_name, install_module, force=force)


def main(args, parser, extra, subparser):

    utils.ensure_no_extra(extra)

    # If nothing provided or less than 2 (view name and command) show help
    if not args.params:
        print(subparser.format_help())
        sys.exit(0)

    # The first "param" is either create, get, install, uninstall, or edit
    valid_commands = [
        "add",
        "create",
        "delete",
        "edit",
        "get",
        "install",
        "list",
        "remove",
        "uninstall",
    ]
    command = args.params.pop(0)
    if command not in valid_commands:
        logger.exit(
            "%s is not a valid command. Choices are: %s"
            % (command, ",".join(valid_commands))
        )

    # The view handler is to create / delete
    view_handler = views.ViewsHandler(
        settings_file=args.settings_file, module_sys=args.module_sys
    )
    view_handler.settings.update_params(args.config_params)

    # If command is list and no view name, list views available
    if command == "list" and not args.params:
        view_handler.list()
        return

    # If nothing provided or less than 2 (view name and command) show help
    if not args.params:
        print(subparser.format_help())
        sys.exit(0)

    # At this point we are expected to have a view name
    view_name = args.params.pop(0)
    if command == "delete":
        view_handler.delete(view_name, force=args.force)
        return

    if command == "edit":
        view_handler.edit(view_name)
        return

    if command == "list":
        view_handler.list(view_name)
        return

    # Add a variable (e.g., system-module) to a view
    if command in ["add", "remove"]:
        if len(args.params) < 2:
            logger.exit("You are required to add a <variable> <value>")
        var_name = args.params.pop(0)

        if command == "add":
            view_handler.add_variable(view_name, var_name, args.params)
        else:
            view_handler.remove_variable(view_name, var_name, args.params)
        return

    # Take custom action depending on the command
    if command == "create":

        # Create the view
        if not args.params:
            view_handler.create(view_name)

        # If we have another argument, it's a file to install from
        else:
            filename = args.params.pop(0)
            create_from_file(
                view_name,
                filename,
                settings_file=args.settings_file,
                quiet=args.quiet,
                module_sys=args.module_sys,
                config_params=args.config_params,
                force=args.force,
            )
        return

    # The client controls install, uninstall, and edit of views
    cli = get_client(quiet=args.quiet, settings_file=args.settings_file)
    cli.settings.update_params(args.config_params)

    # All of the remaining commands require the view to exist
    if command in ["get", "install", "uninstall"] and view_name not in cli.views:
        logger.exit("View %s does not exist. Create it first." % view_name)

    # If we get here, we have an existing view
    view = cli.views[view_name]
    if command == "get":
        print(view.path)
        return

    # This is an install / uninstall - a module name is required
    if not args.params:
        logger.exit("A module name is required to install or uninstall")

    # We assume wanting to install to a view means installing to the module root
    # We don't make it hard to require them to install to the root first
    module_name = args.params.pop(0)
    if command == "install":
        cli.install(module_name, force=args.force)
        cli.view_install(view_name, module_name, force=args.force)

    if command == "uninstall":
        cli.view_uninstall(view_name, module_name, force=args.force)
