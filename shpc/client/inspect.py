__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021-2022, Vanessa Sochat"
__license__ = "MPL 2.0"


import json


def main(args, parser, extra, subparser):

    from shpc.main import get_client

    cli = get_client(
        quiet=args.quiet,
        settings_file=args.settings_file,
        container_tech=args.container_tech,
    )
    metadata = cli.inspect(args.module_name)

    # Case 1: dump entire thing as json
    if args.json:
        print(json.dumps(metadata, indent=4))

    # Case 2: they want a runscript
    elif args.runscript:
        runscript = metadata.get("attributes", {}).get("runscript")
        print(runscript)

    # Case 3: pretty print the whole thing
    else:

        # Inspect Singularity formatted metadata
        if "attributes" in metadata:
            for key, value in metadata.get("attributes", {}).items():
                # skip the runscript
                if key == "runscript":
                    continue
                print("👉️ %s 👈️" % key.upper())
                if isinstance(value, str):
                    print(value)
                elif isinstance(value, dict):
                    for k, v in value.items():
                        print("%s : %s" % (k, v))
                print()

        # Podman and docker oci manifests
        elif isinstance(metadata, list):

            def print_value(key, value):
                if not value:
                    return
                if isinstance(value, (str, int)):
                    print("👉️ %s 👈️" % key.upper())
                    print(value)
                elif isinstance(value, dict):
                    for k, v in value.items():
                        print_value(k, v)
                elif isinstance(value, list):
                    print("👉️ %s 👈️" % key.upper())
                    print("\n".join(value))
                print()

            for key in [
                "Os",
                "Architecture",
                "Author",
                "Size",
                "Labels",
                "RepoTags",
                "Config",
            ]:
                value = metadata[0].get(key)
                print_value(key, value)
