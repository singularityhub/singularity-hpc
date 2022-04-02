__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021-2022, Vanessa Sochat"
__license__ = "MPL 2.0"


def main(args, parser, extra, subparser):

    from shpc.main import get_client

    cli = get_client(quiet=args.quiet, settings_file=args.settings_file)
    cli.update(args.module_name, dryrun=args.dryrun)