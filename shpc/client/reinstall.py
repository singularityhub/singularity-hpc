__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021-2022, Vanessa Sochat"
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

    # It doesn't make sense to give a module name and --all
    if args.reinstall_recipe and args.all:
        logger.exit("Conflicting arguments reinstall_recipe and --all, choose one.")
    # One option must be present
    if not args.reinstall_recipe and not args.all:
        logger.exit("Missing arguments: provide reinstall_recipe or --all.")

    # And do the reinstall
    cli.reinstall(
        args.reinstall_recipe,
        upgrade=False,
        force=args.force,
    )
