---
layout: container
name:  "ghcr.io/autamus/muscle"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/muscle/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/ghcr.io/autamus/muscle/container.yaml"
updated_at: "2022-08-27 01:36:21.928122"
latest: "3.8.1551"
container_url: "https://github.com/orgs/autamus/packages/container/package/muscle"
aliases:
 - "muscle"
versions:
 - "3.8.1551"
 - "latest"
description: "Multiple Sequence Alignment."
config: {"docker": "ghcr.io/autamus/muscle", "url": "https://github.com/orgs/autamus/packages/container/package/muscle", "maintainer": "@vsoch", "description": "Multiple Sequence Alignment.", "latest": {"3.8.1551": "sha256:50a90119cc64b7424bd7d8d6c5fcc9251290ef257e4a753c457789ff7ec23bf3"}, "tags": {"3.8.1551": "sha256:50a90119cc64b7424bd7d8d6c5fcc9251290ef257e4a753c457789ff7ec23bf3", "latest": "sha256:50a90119cc64b7424bd7d8d6c5fcc9251290ef257e4a753c457789ff7ec23bf3"}, "aliases": {"muscle": "/opt/view/bin/muscle"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/muscle.
Multiple Sequence Alignment.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/muscle
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/muscle:3.8.1551
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/muscle/3.8.1551
$ module help ghcr.io/autamus/muscle/3.8.1551
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### muscle-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### muscle-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### muscle-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### muscle-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### muscle-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### muscle-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### muscle
       
```bash
$ singularity exec <container> /opt/view/bin/muscle
$ podman run --it --rm --entrypoint /opt/view/bin/muscle   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/muscle   -v ${PWD} -w ${PWD} <container> -c " $@"
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