---
layout: container
name:  "ghcr.io/autamus/proj"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/proj/container.yaml"
updated_at: "2021-09-01 01:10:24.772244"
container_url: "https://github.com/orgs/autamus/packages/container/package/proj"
aliases:
 - "proj"

 - "projinfo"

 - "projsync"

versions:
 - "7.2.1"
 - "8.1.0"
 - "latest"
description: "PROJ is a generic coordinate transformation software, that transforms coordinates from one coordinate reference system (CRS) to another."
---

This module is a singularity container wrapper for ghcr.io/autamus/proj.
PROJ is a generic coordinate transformation software, that transforms coordinates from one coordinate reference system (CRS) to another.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install ghcr.io/autamus/proj
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/proj:7.2.1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/proj/7.2.1
$ module help ghcr.io/autamus/proj/7.2.1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### -run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### -shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### -exec:

```bash
$ singularity exec -s /bin/sh <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### -inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### -inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### -inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### proj
       
```bash
$ singularity exec <container> /opt/view/bin/proj
$ podman run --it --rm --entrypoint /opt/view/bin/proj   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/proj   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### projinfo
       
```bash
$ singularity exec <container> /opt/view/bin/projinfo
$ podman run --it --rm --entrypoint /opt/view/bin/projinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/projinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### projsync
       
```bash
$ singularity exec <container> /opt/view/bin/projsync
$ podman run --it --rm --entrypoint /opt/view/bin/projsync   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/projsync   -v ${PWD} -w ${PWD} <container> -c " $@"
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