---
layout: container
name:  "bids/baracus"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/bids/baracus/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/bids/baracus/container.yaml"
updated_at: "2022-08-27 01:35:09.838536"
latest: "dev7"
container_url: "https://hub.docker.com/r/bids/baracus"

versions:
 - "latest"
 - "v1.1.4"
 - "dev7"
 - "unstable"
description: "Brain-Age Regression Analysis and Computation Utility Software (https://github.com/BIDS-Apps/baracus)"
config: {"docker": "bids/baracus", "url": "https://hub.docker.com/r/bids/baracus", "maintainer": "@vsoch", "description": "Brain-Age Regression Analysis and Computation Utility Software (https://github.com/BIDS-Apps/baracus)", "latest": {"dev7": "sha256:6b47fc45ec68e1cbcff5f844a076a36a272ee43fb13217f8f9832abf01a6906a"}, "tags": {"latest": "sha256:8e42305ab7321fcdb468c22a87b5a9b248866a5821e64721200f927c2019dcb4", "v1.1.4": "sha256:8e42305ab7321fcdb468c22a87b5a9b248866a5821e64721200f927c2019dcb4", "dev7": "sha256:6b47fc45ec68e1cbcff5f844a076a36a272ee43fb13217f8f9832abf01a6906a", "unstable": "sha256:8e42305ab7321fcdb468c22a87b5a9b248866a5821e64721200f927c2019dcb4"}, "filter": ["v*"]}
---

This module is a singularity container wrapper for bids/baracus.
Brain-Age Regression Analysis and Computation Utility Software (https://github.com/BIDS-Apps/baracus)
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install bids/baracus
```

Or a specific version:

```bash
$ shpc install bids/baracus:latest
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load bids/baracus/latest
$ module help bids/baracus/latest
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### baracus-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### baracus-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### baracus-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### baracus-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### baracus-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### baracus-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### baracus

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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