__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2023, Vanessa Sochat"
__license__ = "MPL 2.0"

import shpc.utils


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

    # Specify custom registry to add
    if args.registry:
        cli.settings.registry = [args.registry]
        cli.reload_registry()

    # No module id is akin to "remove all"
    cli.remove(args.module_id)
