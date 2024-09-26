__author__ = "Ausbeth Aguguo"
__copyright__ = "Copyright 2021-2024, Ausbeth Aguguo"
__license__ = "MPL 2.0"

import shpc.utils as utils
from shpc.logger import logger


def main(args, parser, extra, subparser):
    from shpc.main import get_client

    utils.ensure_no_extra(extra)

    cli = get_client(quiet=args.quiet, settings_file=args.settings_file)

    # Update config settings on the fly
    cli.settings.update_params(args.config_params)

    # Check if user entered an incomplete command
    if not args.upgrade_recipe and not args.upgrade_all:
        subparser.error(
            "Incomplete command. The following arguments are required: upgrade_recipe, --all, or -h for more details"
        )

    # Get the list of installed software
    installed_software = cli.list(return_modules=True)

    # Ensure the user has software installed before carrying out upgrade
    if not installed_software:
        logger.exit(
            "Cannot perform shpc upgrade because you currently do not have any software installed.",
            0,
        )

    # Upgrade a specific installed software
    if args.upgrade_recipe:
        # Check if the provided recipe is known in any registry
        try:
            cli._load_container(args.upgrade_recipe)
        except SystemExit:
            # Give additional messages relating to shpc upgrade, to the original exit message in _load_container function
            logger.exit(
                "This means it cannot be upgraded because it is not installed, and cannot be installed because it is not known in any registry.\nPlease check the name or try a different recipe."
            )
        # Check if the user typed an invalid argument combination
        if args.upgrade_all:
            logger.exit(
                "Cannot use '--all' with a specific recipe. Please choose one option."
            )
        # Check if the user specified a version
        if ":" in args.upgrade_recipe:
            logger.exit("Please use 'shpc upgrade recipe' without including a version.")
        # Check if the specific software is installed
        if args.upgrade_recipe not in installed_software:
            logger.exit(
                f"You currently do not have {args.upgrade_recipe} installed.\nYou can install it with this command: shpc install {args.upgrade_recipe}",
                0,
            )

        # Does the user just want a dry-run of the specific software?
        if args.dryrun:
            version_info = upgrade(
                args.upgrade_recipe, cli, args, dryrun=True
            )  # This returns the latest version if its available, else returns None
            if version_info:
                logger.info(
                    f"You do not have the latest version installed.\nLatest version avaiable is {version_info}"
                )
            else:
                logger.info(
                    f"You have the latest version of {args.upgrade_recipe} installed."
                )

        # Upgade the software
        else:
            upgrade(args.upgrade_recipe, cli, args, dryrun=False, force=args.force)

    # Upgrade all installed software
    elif args.upgrade_all:
        # Store the number of all outdated software
        num_outdated = 0

        # Does the user just want a dry-run of all software?
        if args.dryrun:
            print("Performing a dry-run on all your software...")
            for software in installed_software.keys():
                version_info = upgrade(software, cli, args, dryrun=True)
                if version_info:
                    logger.info(
                        f"{software} is outdated. Latest version available is {version_info}"
                    )
                    num_outdated += 1
                else:
                    logger.info(f"{software} is up to date.")
            # Provide a report on the dry-run
            if num_outdated == 0:
                logger.info("All your software are currently up to date.")
            else:
                logger.info(f"You have a total of {num_outdated} outdated software.")

        # Upgrade all software
        else:
            print("Checking your list to upgrade outdated software...")
            for software in installed_software.keys():
                # Attempt upgrade on each software
                upgrade_info = upgrade(
                    software, cli, args, dryrun=False, force=args.force
                )
                # Count actual upgrades
                if upgrade_info:
                    num_outdated += 1
            if num_outdated == 0:
                logger.info("No upgrade needed. All your software are up to date.")
            else:
                logger.info(
                    f"Updated {num_outdated} outdated software from your list\nAll your software are now up to date."
                )


def upgrade(name, cli, args, dryrun=False, force=False):
    """
    Upgrade a software to its latest version. Or preview available upgrades from the user's software list
    """
    # Add namespace
    name = cli.add_namespace(name)

    # Load the container configuration for the specified recipe
    config = cli._load_container(name)

    # Store the installed versions and the latest version tag
    installed_versions = cli.list(pattern=name, return_modules=True)
    latest_version_tag = get_latest_version(name, config)

    # Compare the latest version with the user's installed version
    if any(latest_version_tag in versions for versions in installed_versions.values()):
        if not dryrun:
            logger.info("You have the latest version of " + name + " installed already")
        return None  # No upgrade necessary

    else:
        if dryrun:
            return (
                latest_version_tag  # Return the latest version for upgrade information
            )
        print(
            "Upgrading "
            + name
            + " to its latest version. Version "
            + latest_version_tag
        )

        # Get the list of views the software was in
        views_with_module = set()
        view_dir = cli.new_module(name).module_dir
        for view_name, entry in cli.views.items():
            if entry.exists(view_dir):
                views_with_module.add(view_name)

        # Ask if the user wants to unintall old versions
        if not cli.uninstall(name, force=force):
            logger.info("Old versions of " + name + " were preserved")

        # Install the latest version
        cli.install(name)

        # Install the latest version to views where the outdated version was found
        if views_with_module:
            msg = f"Do you also want to install the latest version of {name} to the view(s) of the previous version(s)?"
            if utils.confirm_action(msg, force=force):
                for view_name in views_with_module:
                    cli.view_install(view_name, name)
                    logger.info(
                        f"Installed the latest version of {name} to view: {view_name}"
                    )

        return latest_version_tag  # Upgrade occured


def get_latest_version(name, config):
    """
    Given an added namespace of a recipe and a loaded container configuration of that namespace,
    Retrieve the latest version tag.
    """
    latest_version_info = config.get("latest")
    if not latest_version_info:
        logger.exit(f"No latest version found for {name}")

    # Extract the latest version tag
    latest_version_tag = list(latest_version_info.keys())[0]
    return latest_version_tag
