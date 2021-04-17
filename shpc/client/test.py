__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021, Vanessa Sochat"
__license__ = "MPL 2.0"


def main(args, parser, extra, subparser):

    from shpc.main import get_client

    cli = get_client(
        quiet=args.quiet,
        settings_file=args.settings_file,
        module=args.module,
        container_tech=args.container_tech,
    )

    cli.test(
        args.module_name,
        test_exec=args.test_exec,
        stage=args.stage,
        skip_module=args.skip_module,
        test_commands=args.commands,
        template=args.template,
    )
