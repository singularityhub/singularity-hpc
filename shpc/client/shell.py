__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021-2022, Vanessa Sochat"
__license__ = "MPL 2.0"


def main(args, parser, extra, subparser):

    lookup = {"ipython": ipython, "python": python, "bpython": bpython}
    shells = ["ipython", "python", "bpython"]

    # Case 1. shell into a container
    if args.module_name:
        client = create_client(args)
        return client.shell(args.module_name)

    # The default shell determined by the command line client
    shell = args.interpreter
    if shell is not None:
        shell = shell.lower()
        if shell in lookup:
            try:
                return lookup[shell](args)
            except ImportError:
                pass

    # Otherwise present order of liklihood to have on system
    for shell in shells:
        try:
            return lookup[shell](args)
        except ImportError:
            pass


def create_client(args):
    from shpc.main import get_client

    return get_client(
        quiet=args.quiet,
        settings_file=args.settings_file,
        module=args.module,
        container_tech=args.container_tech,
    )


def ipython(args):
    """
    Generate an IPython shell with the client.
    """
    client = create_client(args)
    from IPython import embed

    embed()


def bpython(args):
    """
    Generate an bpython shell with the client.
    """
    import bpython

    client = create_client(args)
    bpython.embed(locals_={"client": client})


def python(args):
    """
    Generate an python shell with the client.
    """
    import code

    client = create_client(args)
    code.interact(local={"client": client})
