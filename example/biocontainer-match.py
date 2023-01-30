#!/usr/bin/env python3

# Match biocontainers on the local filesystem to registry entries.
# Install won't copy the container, but rather just use the provided path!
# You should still set up your module_base before doing this (as we need
# to write module files.

# **ALWAYS** dry run first!
#      python biocontainer-match.py --dry-run
# At the root of your depot do:
#      python biocontainer-match.py
# Force module reinstall (rewrite of module file)
#      python biocontainer-match.py --force
# From another directory do:
#     python biocontainer-match.py --containers /path/to/depot/root
# If the namespace ever changes:
#     python biocontainer-match.py --containers /path/to/depot/root --namespace quay.io/biocontainers
# Only one namespace is currently supported!

import argparse
import os
import re
import sys

from shpc.logger import logger
from shpc.main import get_client
from shpc.main.container import ContainerConfig


def get_parser():
    parser = argparse.ArgumentParser(
        description="SHPC BioContainer Adder",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument(
        "--dry-run",
        help="Dry run only! This will preview installs.",
        default=False,
        action="store_true",
    )
    parser.add_argument(
        "--force", help="Force reinstall of module", default=False, action="store_true"
    )
    parser.add_argument("--containers", help="Path to depot root.", default=os.getcwd())
    parser.add_argument(
        "--namespace",
        help="Namespace to use for containers (quay.io/biocontainers)",
        default="quay.io/biocontainers",
    )
    return parser


def main():

    parser = get_parser()

    # If an error occurs while parsing the arguments, the interpreter will exit with value 2
    args, extra = parser.parse_known_args()

    # Show args to the user
    print(" containers: %s" % args.containers)

    if not os.path.exists(args.containers):
        sys.exit(f"Path {args.containers} does not exist.")
    depot = os.path.abspath(args.containers)
    cli = get_client()

    # Keep a record of repos we've seen and don't repeat
    seen = set()

    # Ensure we start with the populated modules
    cli.registry.iter_modules()

    # Find all paths that match the pattern of a name:tag
    for path in os.listdir(depot):
        if not re.search("^(.*):(.*)$", path) or os.path.isdir(path):
            continue
        repo, tag = path.split(":", 1)

        # Don't need to parse twice
        if repo in seen:
            continue

        container = f"{args.namespace}/{repo}"
        tagged = f"{container}:{tag}"

        match = cli.registry.find(tagged)

        # We don't have an exact match but can share aliases
        if not match:
            match = cli.registry.find(container)

        if not match:
            logger.warning(f"Warning: no match for {path}")
            continue

        if args.dry_run:
            print(f"Would be installing {path} to {tagged}")
            seen.add(repo)
            continue

        # Note we need to install the correct version but using aliases
        # from the one we have (and they should be comparable)
        print(f"Installing {path} to {tagged} with aliases from {match.module}")

        # Make sure we use the full container path
        path = os.path.join(depot, path)

        # Create a new module, force the tag since the digest could be unknown
        module = cli.new_module(tagged)
        module.config = ContainerConfig(match)
        module.config.set_tag(tag, force=True)
        module.load_config(module.config, tagged)
        module.add_local_container(path, keep_path=True)

        # We found a match! Install it (forcing keep path to not copy the container)
        cli.install(
            tagged,
            force=args.force,
            module=module,
            container_image=path,
            keep_path=True,
        )
        seen.add(repo)


if __name__ == "__main__":
    main()
