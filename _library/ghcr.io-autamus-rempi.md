---
layout: container
name:  "ghcr.io/autamus/rempi"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/rempi/container.yaml"
updated_at: "2022-06-02 03:38:53.632096"
container_url: "https://github.com/orgs/autamus/packages/container/package/rempi"
aliases:
 - "rempi"

 - "rempi_record"

 - "rempi_replay"

 - "reset"

versions:
 - "1.1.0"
 - "latest"
description: "ReMPI is a record-and-replay tool for MPI applications."
---

This module is a singularity container wrapper for ghcr.io/autamus/rempi.
ReMPI is a record-and-replay tool for MPI applications.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/rempi
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/rempi:1.1.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/rempi/1.1.0
$ module help ghcr.io/autamus/rempi/1.1.0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rempi-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rempi-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rempi-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rempi-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rempi-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rempi-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### rempi
       
```bash
$ singularity exec <container> /opt/view/bin/rempi
$ podman run --it --rm --entrypoint /opt/view/bin/rempi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/rempi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rempi_record
       
```bash
$ singularity exec <container> /opt/view/bin/rempi_record
$ podman run --it --rm --entrypoint /opt/view/bin/rempi_record   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/rempi_record   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rempi_replay
       
```bash
$ singularity exec <container> /opt/view/bin/rempi_replay
$ podman run --it --rm --entrypoint /opt/view/bin/rempi_replay   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/rempi_replay   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### reset
       
```bash
$ singularity exec <container> /opt/view/bin/reset
$ podman run --it --rm --entrypoint /opt/view/bin/reset   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/reset   -v ${PWD} -w ${PWD} <container> -c " $@"
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