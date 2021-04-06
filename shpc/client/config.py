__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021, Vanessa Sochat"
__license__ = "MPL 2.0"

from shpc.logger import logger


def main(args, parser, extra):

    from shpc.main import get_client

    cli = get_client(quiet=args.quiet, settings_file=args.settings_file)

    # For each new setting, update and save!
    for param in args.params:
        key, value = param.split(":", 1)
        logger.info("Updating %s to be %s" % (key, value))
        cli.settings.set(key, value)

    # Save settings
    cli.settings.save()
