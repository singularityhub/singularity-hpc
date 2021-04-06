__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021, Vanessa Sochat"
__license__ = "MPL 2.0"

import shpc.main.container as container


def main(args, parser, extra):

    if args.uri.startswith("gh://"):
        client = container.SingularityContainer()
        client.pull_gh(args.uri, args.path)
    else:
        logger.info("unique resource identifier %s is not recognized." % args.uri)
