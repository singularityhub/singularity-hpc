---
layout: container
name:  "ghcr.io/autamus/jasper"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/jasper/container.yaml"
updated_at: "2022-03-15 23:30:58.678897"
container_url: "https://github.com/orgs/autamus/packages/container/package/jasper"
aliases:
 - "jasper"

 - "jpegtran"

versions:
 - "2.0.32"
 - "2.0.33"
 - "latest"
description: "JasPer is a collection of software (i.e., a library and application programs) for the coding and manipulation of images."
---

This module is a singularity container wrapper for ghcr.io/autamus/jasper.
JasPer is a collection of software (i.e., a library and application programs) for the coding and manipulation of images.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/jasper
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/jasper:2.0.32
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/jasper/2.0.32
$ module help ghcr.io/autamus/jasper/2.0.32
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### jasper-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### jasper-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### jasper-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### jasper-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### jasper-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### jasper-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### jasper
       
```bash
$ singularity exec <container> /opt/view/bin/jasper
$ podman run --it --rm --entrypoint /opt/view/bin/jasper   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/jasper   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jpegtran
       
```bash
$ singularity exec <container> /opt/view/bin/jpegtran
$ podman run --it --rm --entrypoint /opt/view/bin/jpegtran   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/jpegtran   -v ${PWD} -w ${PWD} <container> -c " $@"
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