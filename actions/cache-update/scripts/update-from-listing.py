#!/usr/bin/env python3

# This script updates the registry from a listing. An existing list
# of containers is required to not retrieve tags for uris that already exist

import argparse
import os
import sys

from container_discovery.listing import iter_tags

import shpc.utils
from shpc.main import get_client

here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, here)
from helpers import add_container  # noqa


def get_parser():
    parser = argparse.ArgumentParser(
        description="SHPC Container Adder",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument("--listing", help="Path to cache with counts.json.")
    parser.add_argument(
        "--namespace", help="Namespace to add to containers in listing."
    )
    parser.add_argument(
        "--registry", help="Path to registry root.", default=os.getcwd()
    )
    parser.add_argument(
        "--url", help="URL optionally with format string %s for entry_name"
    )
    parser.add_argument("--maintainer", help="Author", default="@vsoch")
    return parser


def main():
    parser = get_parser()

    # If an error occurs while parsing the arguments, the interpreter will exit with value 2
    args, extra = parser.parse_known_args()

    # Show args to the user
    print("  maintainer: %s" % args.maintainer)
    print("    registry: %s" % args.registry)
    print("   namespace: %s" % args.namespace)
    print("     listing: %s" % args.listing)

    cli = get_client()
    cli.settings.registry = [args.registry]
    cli.reload_registry()

    for path in args.registry, args.listing:
        if not os.path.exists(path):
            sys.exit(f"{path} does not exist")

    # Read into listing of containers
    containers = [
        x.strip() for x in shpc.utils.read_file(args.listing).split("\n") if x.strip()
    ]

    # If a namespace is provided, add to listing
    if args.namespace:
        containers = ["%s/%s" % (args.namespace, x) for x in containers]

    # Listing of existing containers
    existing = list(cli.registry.iter_registry())

    # Do a diff between lists, get tag for container if not added
    # This checks the registry and ensures the path doesn't already exist
    for container in iter_tags(containers, existing, args.registry):
        # We assume we cannot get aliases here
        try:
            add_container(
                cli,
                container,
                args.maintainer,
                container,
                aliases=[],
                url=args.url,
            )
        except Exception as e:
            print(f"Issue adding container {container}: {e}")


if __name__ == "__main__":
    main()
