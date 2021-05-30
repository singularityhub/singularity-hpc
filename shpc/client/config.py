__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021, Vanessa Sochat"
__license__ = "MPL 2.0"

from shpc.logger import logger
import sys


def main(args, parser, extra, subparser):

    from shpc.main import get_client

    cli = get_client(quiet=args.quiet, settings_file=args.settings_file)

    # If nothing provided, show help
    if not args.params:
        print(subparser.format_help())
        sys.exit(0)

    # The first "param" is either set of get
    command = args.params.pop(0)

    # For each new setting, update and save!
    if command == "edit":
        return cli.settings.edit()
    elif command == "set":
        for param in args.params:
            if ":" not in param:
                logger.warning(
                    "Param %s is missing a :, should be key:value pair. Skipping."
                    % param
                )
                continue
            key, value = param.split(":", 1)
            logger.info("Updating %s to be %s" % (key, value))
            cli.settings.set(key, value)

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
