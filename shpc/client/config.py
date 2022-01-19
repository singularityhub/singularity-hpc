__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021-2022, Vanessa Sochat"
__license__ = "MPL 2.0"

import shpc.defaults as defaults
from shpc.logger import logger
import sys


def main(args, parser, extra, subparser):

    from shpc.main import get_client

    # If nothing provided, show help
    if not args.params:
        print(subparser.format_help())
        sys.exit(0)

    # The first "param" is either set of get
    command = args.params.pop(0)

    # If the user wants the central config file
    if args.central:
        args.settings_file = defaults.default_settings_file

    validate = True if not command == "edit" else False
    cli = get_client(
        quiet=args.quiet, settings_file=args.settings_file, validate=validate
    )

    # For each new setting, update and save!
    if command == "inituser":
        return cli.settings.inituser()
    if command == "edit":
        return cli.settings.edit()
    elif command in ["set", "add", "remove"]:
        for param in args.params:
            if ":" not in param:
                logger.warning(
                    "Param %s is missing a :, should be key:value pair. Skipping."
                    % param
                )
                continue

            key, value = param.split(":", 1)
            if command == "set":
                cli.settings.set(key, value)
                logger.info("Updated %s to be %s" % (key, value))
            elif command == "add":
                cli.settings.add(key, value)
                logger.info("Added %s to %s" % (key, value))
            elif command == "remove":
                cli.settings.remove(key, value)
                logger.info("Removed %s from %s" % (key, value))

        # Save settings
        cli.settings.save()

    # For each get request, print the param pair
    elif command == "get":
        for key in args.params:
            value = cli.settings.get(key)
            value = value or "is unset"
            logger.info("%s %s" % (key.ljust(30), value))

    else:
        logger.error("%s is not a recognized command." % command)
