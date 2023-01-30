__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021-2023, Vanessa Sochat"
__license__ = "MPL 2.0"

import shpc.utils
from shpc.logger import logger


def main(args, parser, extra, subparser):

    from shpc.main import get_client

    shpc.utils.ensure_no_extra(extra)

    cli = get_client(
        quiet=args.quiet,
        settings_file=args.settings_file,
        module_sys=args.module_sys,
        container_tech=args.container_tech,
    )

    # Update config settings on the fly
    cli.settings.update_params(args.config_params)
    if args.uninstall_all:
        if not args.force:
            if not shpc.utils.confirm_uninstall("all modules?"):
                return
        for module_name in cli.list(return_modules=True):
            cli.uninstall(module_name, force=True)

    else:
        if not args.uninstall_recipe:
            logger.exit("Please provide a recipe to uninstall or select --all")
        cli.uninstall(args.uninstall_recipe, force=args.force)
