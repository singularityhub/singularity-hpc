---
layout: container
name:  "ghcr.io/autamus/grass"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/grass/container.yaml"
updated_at: "2022-03-22 12:57:59.680177"
container_url: "https://github.com/orgs/autamus/packages/container/package/grass"
aliases:
 - "grass78"

versions:
 - "7.8.5"
 - "7.8.6"
 - "latest"
description: "GRASS GIS (https://grass.osgeo.org/) is a Geographic Information System used for geospatial data management and analysis, image processing, graphics/map production, spatial modeling, and visualization."
---

This module is a singularity container wrapper for ghcr.io/autamus/grass.
GRASS GIS (https://grass.osgeo.org/) is a Geographic Information System used for geospatial data management and analysis, image processing, graphics/map production, spatial modeling, and visualization.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/grass
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/grass:7.8.5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/grass/7.8.5
$ module help ghcr.io/autamus/grass/7.8.5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### grass-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### grass-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### grass-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### grass-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### grass-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### grass-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### grass78
       
```bash
$ singularity exec <container> /opt/view/bin/grass78
$ podman run --it --rm --entrypoint /opt/view/bin/grass78   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/grass78   -v ${PWD} -w ${PWD} <container> -c " $@"
```



In the above, the `<container>` directive will reference an actual container provided
by the module, for the version you have chosen to load. An environment file in the
module folder will also be bound. Note that although a container
might provide custom commands, every container exposes unique exec, shell, run, and
inspect aliases. For anycommands above, you can export:

 - SINGULARITY_OPTS: to define custom options for singularity (e.g., --debug)
 - SINGULARITY_COMMAND_OPTS: to define custom options for the command (e.g., -b)
 - PODMAN_OPTS: to define custom options for podman or docker
 - PODMAN_COMMAND_OPTS: to define custom options for the command

<br>
  
### Install

You can install shpc locally (for yourself or your user base) as follows:

```bash
$ git clone https://github.com/singularityhub/singularity-hpc
$ cd singularity-hpc
$ pip install -e .
```

Have any questions, or want to request a new module or version? [ask for help!](https://github.com/singularityhub/singularity-hpc/issues)