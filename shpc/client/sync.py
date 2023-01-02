__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021-2023, Vanessa Sochat"
__license__ = "MPL 2.0"

import os

import shpc.logger as logger
import shpc.utils


def sync_registry(args, parser, extra, subparser):

    from shpc.main import get_client

    shpc.utils.ensure_no_extra(extra)
    cli = get_client(quiet=args.quiet, settings_file=args.settings_file)

    # One off custom registry, reload
    if args.registry:
        cli.settings.registry = [args.registry]
        cli.reload_registry()

    if args.config_file and not os.path.exists(args.config_file):
        logger.exit("%s does not exist." % args.config_file)

    cli.registry.sync(
        args.module_name,
        dryrun=args.dryrun,
        tag=args.tag,
        config_file=args.config_file,
        upgrade_all=args.upgrade_all,
        add_new=not args.existing_only,
    )
