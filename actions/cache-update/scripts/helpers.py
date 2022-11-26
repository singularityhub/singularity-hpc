import shpc.utils


def add_container(cli, container, maintainer, entry_name, aliases, url=None):
    """
    Add a container from a unique resource identifier.
    """
    print(f"Generating container entry for {container}")
    module_name = container.split(":")[0]
    container_yaml = cli.add(image="docker://" + container, module_name=module_name)

    # First clean up commented lines - not intended for automation
    toclean = shpc.utils.read_file(container_yaml).split("\n")
    lines = [x for x in toclean if not (x.strip().startswith("#") or not x.strip())]
    shpc.utils.write_file(container_yaml, "\n".join(lines))

    # Now read in as yaml (without comments)
    result = shpc.utils.read_yaml(container_yaml)
    result["maintainer"] = maintainer
    result[
        "description"
    ] = f"singularity registry hpc automated addition for {entry_name}"

    if not url:
        url = "https://singularity-hpc.readthedocs.io/"
    try:
        result["url"] = url % entry_name
    except Exception:
        result["url"] = url

    if aliases:
        result["aliases"] = aliases
    shpc.utils.write_yaml(result, container_yaml)
