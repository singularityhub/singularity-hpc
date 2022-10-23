__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021-2022, Vanessa Sochat"
__license__ = "MPL 2.0"

import shpc.utils


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

    # And do the install
    cli.install(args.install_recipe, force=args.force)
    if cli.settings.default_view and not args.no_view:
        cli.view_install(
            cli.settings.default_view, args.install_recipe, force=args.force
        )
