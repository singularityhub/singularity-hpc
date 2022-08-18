__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021-2022, Vanessa Sochat"
__license__ = "MPL 2.0"

import re

import shpc.main.container as container
import shpc.utils
from shpc.logger import logger


def main(args, parser, extra, subparser):

    shpc.utils.ensure_no_extra(extra)

    # We currently support GitHub and Docker URIs
    if not re.search("^(gh|docker)", args.uri):
        logger.exit("unique resource identifier %s is not recognized." % args.uri)

    client = container.SingularityContainer()
    client.pull(args.uri, args.path)
