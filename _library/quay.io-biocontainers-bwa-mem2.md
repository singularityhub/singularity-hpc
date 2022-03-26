---
layout: container
name:  "quay.io/biocontainers/bwa-mem2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/quay.io/biocontainers/bwa-mem2/container.yaml"
updated_at: "2022-03-26 02:39:38.813078"
container_url: "https://quay.io/repository/biocontainers/bwa-mem2"
aliases:
 - "bwa-mem2"

versions:
 - "2.2.1--h9a82719_1"
 - "2.2.1--hd03093a_2"
description: "Bwa-mem2 is the next version of the bwa-mem algorithm in BWA."
---

This module is a singularity container wrapper for quay.io/biocontainers/bwa-mem2.
Bwa-mem2 is the next version of the bwa-mem algorithm in BWA.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bwa-mem2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bwa-mem2:2.2.1--h9a82719_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bwa-mem2/2.2.1--h9a82719_1
$ module help quay.io/biocontainers/bwa-mem2/2.2.1--h9a82719_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bwa-mem2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bwa-mem2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bwa-mem2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bwa-mem2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bwa-mem2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bwa-mem2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bwa-mem2
       
```bash
$ singularity exec <container> /usr/local/bin/bwa-mem2
$ podman run --it --rm --entrypoint /usr/local/bin/bwa-mem2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwa-mem2   -v ${PWD} -w ${PWD} <container> -c " $@"
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