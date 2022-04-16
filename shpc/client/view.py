__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2022, Vanessa Sochat"
__license__ = "MPL 2.0"

import shpc.main.modules.views as views
from shpc.logger import logger
import sys


def main(args, parser, extra, subparser):

    from shpc.main import get_client

    # If nothing provided or less than 2 (view name and command) show help
    if not args.params or len(args.params) < 2:
        print(subparser.format_help())
        sys.exit(0)

    # The first "param" is either create, get, install, uninstall, or edit
    valid_commands = ["create", "delete", "get", "install", "uninstall", "edit"]
    command = args.params.pop(0)
    if command not in valid_commands:
        logger.exit(
            "%s is not a valid command. Choices are: %s"
            % (command, ",".join(valid_commands))
        )

    # The view handler is to create / delete
    view_handler = views.ViewsHandler(settings_file=args.settings_file)
    view_handler.settings.update_params(args.config_params)
    view_name = args.params.pop(0)

    # Take custom action depending on the command
    if command == "create":
        view_handler.create(view_name)
        return

    if command == "delete":
        view_handler.delete(view_name, force=args.force)
        return

    if command == "edit":
        view_handler.edit(view_name)
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
        cli.install(module_name, view=view_name, disable_view=False, force=args.force)

    if command == "uninstall":
        cli.uninstall(module_name, view=view_name, force=args.force)
