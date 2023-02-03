#!/usr/bin/env python3

# This script uses count data from https://github.com/singularityhub/shpc-registry-cache
# to:

# - Subsetting to those in a container, including counts
# - Rank ordering from least to greatest (lower frequency is a more unique command)
# - Including any counts with a frequency < 10
# - Above that, including the next N, but don't go over max_count (1000)
# - Use these to generate a new container.yaml for the file (if it does not exist yet)

# It requires a local clone of shpc-registry-cache with a counts file available,
# along with a json file with commands found there.
# Usage:
# python update.py --cache ../shpc-registry-cache --registry $PWD

import argparse
import os
import sys

from container_discovery.cache import iter_new_cache

from shpc.main import get_client

here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, here)

from helpers import add_container  # noqa


def get_parser():
    parser = argparse.ArgumentParser(
        description="SHPC Container Adder",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument("--cache", help="Path to cache with counts.json.")
    parser.add_argument(
        "--registry", help="Path to registry root.", default=os.getcwd()
    )
    parser.add_argument(
        "--url", help="URL optionally with format string %s for entry_name"
    )
    parser.add_argument("--maintainer", help="Author", default="@vsoch")
    parser.add_argument(
        "--min-count-inclusion",
        help="Include all executables under this count",
        default=10,
        type=int,
        dest="min_count",
    )
    parser.add_argument(
        "--max-count-inclusion",
        help="Do not include counts over this value",
        default=1000,
        type=int,
        dest="max_count",
    )
    parser.add_argument(
        "--additional-count-inclusion",
        help="Author",
        default=25,
        type=int,
        dest="add_count",
    )
    return parser


def main():
    parser = get_parser()

    # If an error occurs while parsing the arguments, the interpreter will exit with value 2
    args, extra = parser.parse_known_args()

    # Show args to the user
    print("            maintainer: %s" % args.maintainer)
    print("              registry: %s" % args.registry)
    print("                 cache: %s" % args.cache)

    cli = get_client()
    cli.settings.registry = [args.registry]
    cli.reload_registry()

    for path in args.registry, args.cache:
        if not os.path.exists(path):
            sys.exit(f"{path} does not exist")

    for entry in iter_new_cache(args.cache, registry=args.registry):
        aliases = entry.filter_aliases(
            add_count=args.add_count, min_count=args.min_count, max_count=args.max_count
        )

        # Now add the container, and use the tag
        container = f"{entry.image}:{entry.tag}"
        entry_name = entry.image.split(os.sep)[-1]

        # First derive and save the aliases - we can filter based
        try:
            add_container(
                cli,
                container,
                args.maintainer,
                entry_name,
                aliases=aliases,
                url=args.url,
            )
        except Exception as e:
            print(f"Issue adding container {container}: {e}")


if __name__ == "__main__":
    main()
