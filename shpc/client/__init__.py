#!/usr/bin/env python

__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021, Vanessa Sochat"
__license__ = "MPL 2.0"

import shpc
from shpc.logger import setup_logger
import argparse
import sys
import os


def get_parser():
    parser = argparse.ArgumentParser(description="Singularity Registry (HPC)")

    # Global Variables
    parser.add_argument(
        "--debug",
        dest="debug",
        help="use verbose logging to debug.",
        default=False,
        action="store_true",
    )

    parser.add_argument(
        "--quiet",
        dest="quiet",
        help="suppress additional output.",
        default=False,
        action="store_true",
    )

    parser.add_argument(
        "--settings-file",
        dest="settings_file",
        help="custom path to settings file.",
    )

    parser.add_argument(
        "--version",
        dest="version",
        help="suppress additional output.",
        default=False,
        action="store_true",
    )

    description = "actions for Singularity Registry HPC"
    subparsers = parser.add_subparsers(
        help="shpc actions",
        title="actions",
        description=description,
        dest="command",
    )

    # print version and exit
    subparsers.add_parser("version", help="show software version")

    # Local shell with client loaded
    shell = subparsers.add_parser(
        "shell", help="shell into a Python session with a client."
    )

    # List local containers and collections
    images = subparsers.add_parser(
        "images", help="list local images, optionally with query"
    )

    # Install a known recipe from the registry
    install = subparsers.add_parser("install", help="install a registry recipe.")
    install.add_argument(
        "install_recipe", help="recipe to install (name:version)", type=str
    )

    # List known recipes
    listing = subparsers.add_parser("list", help="list known registry recipes.")

    # List local containers and collections
    inspect = subparsers.add_parser("inspect", help="inspect an image in your database")

    inspect.add_argument("query", help="image search query to inspect", type=str)

    # Get path to an image
    get = subparsers.add_parser("get", help="get an image path from your storage")

    get.add_argument("query", help="image search query to inspect", type=str)

    # Add an image file
    add = subparsers.add_parser("add", help="add an image to local storage")

    add.add_argument("image", help="full path to image file", type=str)

    add.add_argument(
        "--name", dest="name", help='name of image, in format "library/image"', type=str
    )

    add.add_argument(
        "--copy",
        dest="copy",
        help="copy the image instead of moving it.",
        default=False,
        action="store_true",
    )

    config = subparsers.add_parser("config", help="update configuration settings.")
    config.add_argument(
        "params",
        nargs="*",
        help="one or more key value pairs, in format key:value to update.",
        type=str,
    )

    mv = subparsers.add_parser("mv", help="move an image and update database")

    mv.add_argument("name", help="image name or uri to move from database", type=str)

    mv.add_argument("path", help="directory or image file to move image.", type=str)

    rm = subparsers.add_parser("rm", help="remove an image from the local database")

    rm.add_argument("image", help='name of image, in format "library/image"', type=str)

    # List or search containers and collections
    search = subparsers.add_parser("search", help="search remote images")

    search.add_argument(
        "query",
        nargs="*",
        help="image search query, don't specify for all",
        type=str,
        default="*",
    )

    # List or search labels
    labels = subparsers.add_parser("labels", help="query for labels")

    labels.add_argument(
        "--key",
        "-k",
        dest="key",
        help="A label key to search for",
        type=str,
        default=None,
    )

    labels.add_argument(
        "--value",
        "-v",
        dest="value",
        help="A value to search for",
        type=str,
        default=None,
    )

    # Remove
    delete = subparsers.add_parser("delete", help="delete an image from a remote.")

    delete.add_argument(
        "--force",
        "-f",
        dest="force",
        help="don't prompt before deletion",
        default=False,
        action="store_true",
    )

    delete.add_argument("image", help="full path to image file", type=str)

    return parser


def main():
    """main is the entrypoint to the singularity-hpc client."""

    parser = get_parser()

    def help(return_code=0):
        """print help, including the software version and active client
        and exit with return code.
        """

        version = shpc.__version__

        print("\nSingularity Registry (HPC) Client v%s" % version)
        parser.print_help()
        sys.exit(return_code)

    # If the user didn't provide any arguments, show the full help
    if len(sys.argv) == 1:
        help()

    # If an error occurs while parsing the arguments, the interpreter will exit with value 2
    args, extra = parser.parse_known_args()

    if args.debug is True:
        os.environ["MESSAGELEVEL"] = "DEBUG"

    # Show the version and exit
    if args.command == "version" or args.version:
        print(shpc.__version__)
        sys.exit(0)

    setup_logger(
        quiet=args.quiet,
        debug=args.debug,
    )

    # Does the user want a shell?
    if args.command == "add":
        from .add import main
    if args.command == "config":
        from .config import main
    elif args.command == "get":
        from .get import main
    elif args.command == "delete":
        from .delete import main
    elif args.command == "install":
        from .install import main
    elif args.command == "inspect":
        from .inspect import main
    elif args.command == "images":
        from .images import main
    elif args.command == "labels":
        from .labels import main
    elif args.command == "list":
        from .listing import main
    elif args.command == "mv":
        from .mv import main
    elif args.command == "rm":
        from .rm import main
    elif args.command == "search":
        from .search import main
    elif args.command == "shell":
        from .shell import main

    # Pass on to the correct parser
    return_code = 0
    try:
        main(args=args, parser=parser, extra=extra)
        sys.exit(return_code)
    except UnboundLocalError:
        return_code = 1

    help(return_code)


if __name__ == "__main__":
    main()
