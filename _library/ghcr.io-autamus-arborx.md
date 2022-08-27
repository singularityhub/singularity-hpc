---
layout: container
name:  "ghcr.io/autamus/arborx"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/arborx/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/ghcr.io/autamus/arborx/container.yaml"
updated_at: "2022-08-27 02:51:50.212155"
latest: "1.1"
container_url: "https://github.com/orgs/autamus/packages/container/package/arborx"

versions:
 - "1.0"
 - "1.1"
 - "latest"
description: "ArborX is a performance-portable library for geometric search"
config: {"docker": "ghcr.io/autamus/arborx", "url": "https://github.com/orgs/autamus/packages/container/package/arborx", "maintainer": "@vsoch", "description": "ArborX is a performance-portable library for geometric search", "latest": {"1.1": "sha256:e5970b877b4e9233373440babb70df8db1af648fbe94359f5e8225d833cb23fa"}, "tags": {"1.0": "sha256:d4c1d3e22344cf4c8f3d4b2a4a8f5532b303dc7a75a37c55c463a685b359a03b", "1.1": "sha256:e5970b877b4e9233373440babb70df8db1af648fbe94359f5e8225d833cb23fa", "latest": "sha256:e5970b877b4e9233373440babb70df8db1af648fbe94359f5e8225d833cb23fa"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/arborx.
ArborX is a performance-portable library for geometric search
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/arborx
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/arborx:1.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/arborx/1.0
$ module help ghcr.io/autamus/arborx/1.0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### arborx-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### arborx-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### arborx-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### arborx-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### arborx-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### arborx-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### arborx

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