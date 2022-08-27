---
layout: container
name:  "quay.io/biocontainers/clustalo"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/clustalo/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/clustalo/container.yaml"
updated_at: "2022-08-27 01:37:24.217611"
latest: "1.2.4--h87f3376_5"
container_url: "https://quay.io/repository/biocontainers/clustalo"
aliases:
 - "clustalo"
versions:
 - "1.2.4--1"
 - "1.2.4--he1b5a44_3"
 - "1.2.4--h87f3376_5"
description: "Multiple sequence alignment program for aligning 3+ sequences together"
config: {"docker": "quay.io/biocontainers/clustalo", "url": "https://quay.io/repository/biocontainers/clustalo", "maintainer": "@sarahbeecroft", "description": "Multiple sequence alignment program for aligning 3+ sequences together", "latest": {"1.2.4--h87f3376_5": "sha256:7e636b5b9836aa37d704a4d5e593843ca77221741c333b5a225357c93d75b6a0"}, "tags": {"1.2.4--1": "sha256:ca8cccff20860fee28aec2ca408657d9ef03009991c438a23ab41b45d6f9bcf9", "1.2.4--he1b5a44_3": "sha256:6703d1623f640ddf7212d7541eea083e2327988c28b7952efc8f6cbe5bf785d1", "1.2.4--h87f3376_5": "sha256:7e636b5b9836aa37d704a4d5e593843ca77221741c333b5a225357c93d75b6a0"}, "aliases": {"clustalo": "/usr/local/bin/clustalo"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/clustalo.
Multiple sequence alignment program for aligning 3+ sequences together
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/clustalo
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/clustalo:1.2.4--1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/clustalo/1.2.4--1
$ module help quay.io/biocontainers/clustalo/1.2.4--1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### clustalo-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### clustalo-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### clustalo-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### clustalo-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### clustalo-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### clustalo-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### clustalo
       
```bash
$ singularity exec <container> /usr/local/bin/clustalo
$ podman run --it --rm --entrypoint /usr/local/bin/clustalo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clustalo   -v ${PWD} -w ${PWD} <container> -c " $@"
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