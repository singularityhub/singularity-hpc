---
layout: container
name:  "quay.io/biocontainers/bedtools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bedtools/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bedtools/container.yaml"
updated_at: "2022-08-27 02:54:11.868390"
latest: "2.30.0--h468198e_3"
container_url: "https://quay.io/repository/biocontainers/bedtools"
aliases:
 - "bedtools"
versions:
 - "2.30.0--hc088bd4_0"
 - "2.30.0--h7d7f7ad_1"
 - "2.30.0--h468198e_3"
description: "Bedtools is the swiss army knife for genome arithmetic."
config: {"docker": "quay.io/biocontainers/bedtools", "url": "https://quay.io/repository/biocontainers/bedtools", "maintainer": "@marcodelapierre", "description": "Bedtools is the swiss army knife for genome arithmetic.", "latest": {"2.30.0--h468198e_3": "sha256:7824178c95ca5aefdd0f19a9092f8a2434ee51d830517eeb840e5b08efb4d7f1"}, "tags": {"2.30.0--hc088bd4_0": "sha256:b0018bd0a10853e19ee92f6d46d8d12f1c41e516845105e1f02c91b4d7b961b1", "2.30.0--h7d7f7ad_1": "sha256:a2e163619a608525ff784ee296c6925bb75fdc243573fe07edad8c91ee1ad83d", "2.30.0--h468198e_3": "sha256:7824178c95ca5aefdd0f19a9092f8a2434ee51d830517eeb840e5b08efb4d7f1"}, "aliases": {"bedtools": "/usr/local/bin/bedtools"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bedtools.
Bedtools is the swiss army knife for genome arithmetic.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bedtools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bedtools:2.30.0--hc088bd4_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bedtools/2.30.0--hc088bd4_0
$ module help quay.io/biocontainers/bedtools/2.30.0--hc088bd4_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bedtools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bedtools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bedtools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bedtools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bedtools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bedtools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bedtools
       
```bash
$ singularity exec <container> /usr/local/bin/bedtools
$ podman run --it --rm --entrypoint /usr/local/bin/bedtools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedtools   -v ${PWD} -w ${PWD} <container> -c " $@"
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