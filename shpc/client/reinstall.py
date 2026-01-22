__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021-2024, Vanessa Sochat"
__license__ = "MPL 2.0"

import shpc.utils
from shpc.logger import logger


def main(args, parser, extra, subparser):
    from shpc.main import get_client

    shpc.utils.ensure_no_extra(extra)

    cli = get_client(
        quiet=args.quiet,
        settings_file=args.settings_file,
        module_sys=args.module_sys,
        container_tech=args.container_tech,
    )

    # Update config settings on the fly
    cli.settings.update_params(args.config_params)

    # Check if user entered an incomplete command
    if not args.reinstall_recipe and not args.all:
        subparser.error(
            "You must specify a recipe to reinstall or use --all to reinstall all installed software."
        )

    # Reinstall all software
    if args.all:
        # Check if the user typed an invalid argument combination
        if args.reinstall_recipe:
            logger.exit(
                "You cannot specify a recipe with --all. Use shpc reinstall --all to reinstall all installed software."
            )

        # Check if the user has any software installed
        installed_software = cli.list(return_modules=True)
        if not installed_software:
            logger.exit("You currently don't have any installed software to reinstall.")

        # Reinstall all installed software
        print("Reinstalling all installed software...")
        for software in installed_software.keys():
            reinstall(software, cli, args, update_containers=args.update_containers)
        logger.info("All software reinstalled.")

    # Reinstall a specific software
    else:
        # Add namespace
        name = cli.add_namespace(args.reinstall_recipe)

        # Reinstall the software
        reinstall(name, cli, args, update_containers=args.update_containers)


def reinstall(name, cli, args, update_containers=False):
    """
    Reinstall a specific version or all versions of a software.
    """
    # Check if the provided recipe is known in any registry
    try:
        cli._load_container(name)
    except SystemExit:
        # Give additional messages relating to shpc reinstall, to the original exit message in _load_container function
        logger.exit(
            "This means it cannot be reinstalled because it is not installed, and cannot be installed because it is not known in any registry.\nPlease check the name or try a different recipe."
        )

    # Check if the software or version is installed
    installed_versions = cli.list(return_modules=True).get(name.split(":")[0], [])
    if not installed_versions:
        logger.exit(
            f"You currently don't have '{name}' installed.\nTry: shpc install", 0
        )

    # Determine if a specific version is requested
    specific_version = ":" in name
    if specific_version and name.split(":")[1] not in installed_versions:
        logger.exit(
            f"You currently don't have '{name}' installed.\nTry: shpc install", 0
        )

    # Handle reinstallation logic
    if specific_version:
        print(f"Reinstalling {name}...")
        reinstall_version(name, cli, args, update_containers)
        logger.info(f"Successfully reinstalled {name}.")
    else:
        print(f"Reinstalling all versions of {name}...")
        for version in installed_versions:
            version_name = f"{name}:{version}"
            reinstall_version(version_name, cli, args, update_containers)
        logger.info(f"Successfully reinstalled all versions of {name}.")


def reinstall_version(name, cli, args, update_containers):
    """
    Sub-function to handle the actual reinstallation
    """
    # Get the list of views the software was in
    views_with_module = set()
    views_dir = cli.new_module(name).module_dir
    for view_name, entry in cli.views.items():
        if entry.exists(views_dir):
            views_with_module.add(view_name)

    # Uninstallation process. By default, uninstall without prompting the user and keep the container except the user wants a complete reinstall
    cli.uninstall(name, force=True, keep_container=not update_containers)

    # Display a helpful message to the user about the state of the container during reinstall process
    if not update_containers:
        print(
            "Container was successfully preserved, module files and wrapper scripts will be overwritten..."
        )
    else:
        print("No container was preserved, all files will be overwritten...")

    # Installation process
    cli.install(name)

    # Restore the software to the captured views
    print(
        f"Restoring {name} to the views it was uninstalled from during reinstallation"
    )
    for view_name in views_with_module:
        cli.view_install(view_name, name)
        logger.info(f"Restored {name} to view: {view_name}")
