---
layout: container
name:  "quay.io/biocontainers/star"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/star/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/star/container.yaml"
updated_at: "2022-08-27 01:37:32.170980"
latest: "2.7.10a--h9ee0642_0"
container_url: "https://quay.io/repository/biocontainers/star"
aliases:
 - "STAR"
versions:
 - "2.7.8a--h9ee0642_1"
 - "2.7.9a--h9ee0642_0"
 - "2.7.10a--h9ee0642_0"
description: "Spliced Transcripts Alignment to a Reference."
config: {"docker": "quay.io/biocontainers/star", "url": "https://quay.io/repository/biocontainers/star", "maintainer": "@audreystott", "description": "Spliced Transcripts Alignment to a Reference.", "latest": {"2.7.10a--h9ee0642_0": "sha256:8e4a22498462f54b924cec7dd28dc53b3f277b736497e7105036f63361aad1f4"}, "tags": {"2.7.8a--h9ee0642_1": "sha256:b30f079606cb90aa8c4c8ebf96f4e7988e8e4c475bb842d75a76311b3d39cacd", "2.7.9a--h9ee0642_0": "sha256:d80ae2e0354e890d55ad0009e9ad9667d1113a679659071e6e02d50e46c8bba1", "2.7.10a--h9ee0642_0": "sha256:8e4a22498462f54b924cec7dd28dc53b3f277b736497e7105036f63361aad1f4"}, "aliases": {"STAR": "/usr/local/bin/STAR"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/star.
Spliced Transcripts Alignment to a Reference.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/star
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/star:2.7.8a--h9ee0642_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/star/2.7.8a--h9ee0642_1
$ module help quay.io/biocontainers/star/2.7.8a--h9ee0642_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### star-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### star-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### star-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### star-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### star-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### star-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### STAR
       
```bash
$ singularity exec <container> /usr/local/bin/STAR
$ podman run --it --rm --entrypoint /usr/local/bin/STAR   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/STAR   -v ${PWD} -w ${PWD} <container> -c " $@"
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