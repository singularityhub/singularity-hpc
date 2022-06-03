---
layout: container
name:  "quay.io/biocontainers/canu"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/quay.io/biocontainers/canu/container.yaml"
updated_at: "2022-06-03 04:17:25.567836"
container_url: "https://quay.io/repository/biocontainers/canu"
aliases:
 - "canu"

versions:
 - "2.1.1--he1b5a44_0"
 - "2.1.1--he1b5a44_1"
 - "2.2--ha47f30e_0"
 - "2.1.1--h1b792b2_2"
description: "Canu is a fork of the celera assembler designed for high-noise single-molecule sequencing"
---

This module is a singularity container wrapper for quay.io/biocontainers/canu.
Canu is a fork of the celera assembler designed for high-noise single-molecule sequencing
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/canu
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/canu:2.1.1--he1b5a44_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/canu/2.1.1--he1b5a44_0
$ module help quay.io/biocontainers/canu/2.1.1--he1b5a44_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### canu-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### canu-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### canu-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### canu-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### canu-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### canu-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### canu
       
```bash
$ singularity exec <container> /usr/local/bin/canu
$ podman run --it --rm --entrypoint /usr/local/bin/canu   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/canu   -v ${PWD} -w ${PWD} <container> -c " $@"
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