---
layout: container
name:  "quay.io/biocontainers/mrbayes"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mrbayes/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/mrbayes/container.yaml"
updated_at: "2022-08-27 01:37:28.459727"
latest: "3.2.7--h5465cc4_4"
container_url: "https://quay.io/repository/biocontainers/mrbayes"
aliases:
 - "mb"
versions:
 - "3.2.6--0"
 - "3.2.7a--hcee41ef_0"
 - "3.2.7--h19cf415_2"
 - "3.2.7--h5465cc4_4"
description: "A program for Bayesian inference and model choice across a wide range of phylogenetic and evolutionary models"
config: {"docker": "quay.io/biocontainers/mrbayes", "url": "https://quay.io/repository/biocontainers/mrbayes", "maintainer": "@sarahbeecroft", "description": "A program for Bayesian inference and model choice across a wide range of phylogenetic and evolutionary models", "latest": {"3.2.7--h5465cc4_4": "sha256:c07cbbd563dec595ac4bf4aaedd87ce4c0fcc548ff92bc48a8a7d5cd151ec0a1"}, "tags": {"3.2.6--0": "sha256:a81b94e4659014c25c5840b01f1f5ba5b635d2ce061134e2911f55f974c49b3f", "3.2.7a--hcee41ef_0": "sha256:bf64e9bd6a35d0b7e132a7766b89a8787ee1fb4cb269cc97f62fd3ab78b2e422", "3.2.7--h19cf415_2": "sha256:893140dd1c0019013652f77f379641cadf1c43d7d96b9cef35cf8d1475f25991", "3.2.7--h5465cc4_4": "sha256:c07cbbd563dec595ac4bf4aaedd87ce4c0fcc548ff92bc48a8a7d5cd151ec0a1"}, "aliases": {"mb": "/usr/local/bin/mb"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mrbayes.
A program for Bayesian inference and model choice across a wide range of phylogenetic and evolutionary models
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mrbayes
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mrbayes:3.2.6--0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mrbayes/3.2.6--0
$ module help quay.io/biocontainers/mrbayes/3.2.6--0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mrbayes-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mrbayes-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mrbayes-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mrbayes-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mrbayes-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mrbayes-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### mb
       
```bash
$ singularity exec <container> /usr/local/bin/mb
$ podman run --it --rm --entrypoint /usr/local/bin/mb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mb   -v ${PWD} -w ${PWD} <container> -c " $@"
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