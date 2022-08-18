__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021-2022, Vanessa Sochat"
__license__ = "MPL 2.0"

import shpc.utils


def main(args, parser, extra, subparser):

    from shpc.main import get_client

    shpc.utils.ensure_no_extra(extra)

    cli = get_client(quiet=args.quiet, settings_file=args.settings_file)
    cli.update(args.module_name, dryrun=args.dryrun, filters=args.filters)
