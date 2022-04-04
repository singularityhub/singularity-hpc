---
layout: container
name:  "ghcr.io/autamus/plasma"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/plasma/container.yaml"
updated_at: "2022-04-04 23:52:59.714591"
container_url: "https://github.com/orgs/autamus/packages/container/package/plasma"
aliases:
 - "plasmatest"

versions:
 - "20.9.20"
 - "21.8.29"
description: "Parallel Linear Algebra Software for Multicore Architectures, PLASMA is a software package for solving problems in dense linear algebra using multicore processors and Xeon Phi coprocessors."
---

This module is a singularity container wrapper for ghcr.io/autamus/plasma.
Parallel Linear Algebra Software for Multicore Architectures, PLASMA is a software package for solving problems in dense linear algebra using multicore processors and Xeon Phi coprocessors.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/plasma
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/plasma:20.9.20
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/plasma/20.9.20
$ module help ghcr.io/autamus/plasma/20.9.20
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### plasma-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### plasma-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### plasma-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### plasma-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### plasma-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### plasma-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### plasmatest
       
```bash
$ singularity exec <container> /opt/view/bin/plasmatest
$ podman run --it --rm --entrypoint /opt/view/bin/plasmatest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/plasmatest   -v ${PWD} -w ${PWD} <container> -c " $@"
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