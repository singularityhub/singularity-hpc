__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021-2022, Vanessa Sochat"
__license__ = "MPL 2.0"


import sys

import shpc.utils
from shpc.logger import logger


def main(args, parser, extra, subparser):

    from shpc.main import get_client

    shpc.utils.ensure_no_extra(extra)

    cli = get_client(quiet=args.quiet, settings_file=args.settings_file)

    # Update config settings on the fly
    cli.settings.update_params(args.config_params)

    # Case 1: we need to unset a namespace
    if not args.namespace:
        sys.exit("Please choose: shpc use <namespace> or shpc unset.")

    command = args.namespace.pop(0)

    # Unset a namespace, does not need or consider additional arguments
    if command == "unset":
        logger.info("Unsetting all namespaces.")
        cli.settings.set("namespace", None)

    # use a namespace requires another argument (the namespace)
    elif command == "use":
        if not args.namespace:
            sys.exit("use must be followed by a namespace!")
        namespace = args.namespace[0]
        logger.info("Setting namespace %s" % namespace)
        cli.settings.set("namespace", namespace)

    cli.settings.save()
