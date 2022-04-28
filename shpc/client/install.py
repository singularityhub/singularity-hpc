__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021-2022, Vanessa Sochat"
__license__ = "MPL 2.0"

from shpc.logger import logger


def main(args, parser, extra, subparser):

    from shpc.main import get_client

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

    # It doesn't make sense to define view and no view
    if args.view and args.no_view:
        logger.exit("Conflicting arguments --view and --no-view, choose one.")

    # And do the install
    cli.install(
        args.install_recipe, view=args.view, disable_view=args.no_view, force=args.force
    )
