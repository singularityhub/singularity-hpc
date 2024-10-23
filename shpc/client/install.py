__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021-2024, Vanessa Sochat"
__license__ = "MPL 2.0"

import shpc.utils
from shpc.logger import logger


def main(args, parser, extra, subparser):
    from shpc.main import get_client

    shpc.utils.ensure_no_extra(extra)

    if args.install_recipe.startswith("gh://"):
        args.container_tech = "singularity-deploy"

    cli = get_client(
        quiet=args.quiet,
        settings_file=args.settings_file,
        module_sys=args.module_sys,
        container_tech=args.container_tech,
    )

    # Update config settings on the fly
    cli.settings.update_params(args.config_params)

    # Get the list of the user's installed software
    installed_software = cli.list(return_modules=True)

    # Upgrade a specific installed software
    if args.upgrade:
        # Check if the user specified a version
        if ":" in args.install_recipe:
            logger.exit(
                "Please do not include the software version when using --upgrade argument."
            )
        # Check if the specific software is installed
        if args.install_recipe not in installed_software:
            logger.exit(
                f"You cannot carry out an upgrade on {args.install_recipe} because you do not have it installed.\nInstall it first before attempting an upgrade.",
                0,
            )

        # Does the user just want a dry-run?
        if args.dryrun:
            version_info = upgrade(
                args.install_recipe, cli, args, dryrun=True
            )  # This returns the latest version if its available, else returns None
            if version_info:
                logger.info(
                    f"You do not have the latest version installed.\nLatest version avaiable is {version_info}"
                )
            else:
                logger.info(
                    f"You have the latest version of {args.install_recipe} installed."
                )

        # Upgade the software
        else:
            upgrade(
                args.install_recipe,
                cli,
                args,
                dryrun=False,
            )

    # Install a new software
    else:
        cli.install(
            args.install_recipe,
            force=args.force,
            container_image=args.container_image,
            keep_path=args.keep_path,
        )
        if cli.settings.default_view and not args.no_view:
            cli.view_install(
                cli.settings.default_view,
                args.install_recipe,
                force=args.force,
                container_image=args.container_image,
            )


def upgrade(name, cli, args, dryrun=False):
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
            logger.info(f"You have the latest version of {name} installed already")
        return None  # No upgrade necessary

    else:
        if dryrun:
            return (
                latest_version_tag  # Return the latest version for upgrade information
            )
        print(f"Upgrading {name} to its latest version. Version {latest_version_tag}")

        # Get the list of views the software was in
        views_with_module = set()
        view_dir = cli.new_module(name).module_dir
        for view_name, entry in cli.views.items():
            if entry.exists(view_dir):
                views_with_module.add(view_name)

        # Ask if the user wants to unintall old versions
        if not cli.uninstall(name):
            logger.info(f"Old versions of {name} were preserved")

        # Install the latest version
        cli.install(name)

        # Install the latest version to views where the outdated version was found
        if views_with_module:
            msg = f"Do you also want to install the latest version of {name} to the view(s) of the previous version(s)?"
            if shpc.utils.confirm_action(msg):
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
