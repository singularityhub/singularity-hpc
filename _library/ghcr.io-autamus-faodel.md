---
layout: container
name:  "ghcr.io/autamus/faodel"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/faodel/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/ghcr.io/autamus/faodel/container.yaml"
updated_at: "2022-08-27 02:52:16.410190"
latest: "1.2108.1"
container_url: "https://github.com/orgs/autamus/packages/container/package/faodel"
aliases:
 - "faodel"
versions:
 - "1.1906.1"
 - "1.2108.1"
 - "latest"
description: "Flexible, Asynchronous, Object Data-Exchange Libraries"
config: {"docker": "ghcr.io/autamus/faodel", "url": "https://github.com/orgs/autamus/packages/container/package/faodel", "maintainer": "@vsoch", "description": "Flexible, Asynchronous, Object Data-Exchange Libraries", "latest": {"1.2108.1": "sha256:2ce5c210992fc449059368cab300f11cb796569ad5ef6a6dc798826981b35b67"}, "tags": {"1.1906.1": "sha256:60f42cef7751dea8354b3d3cc2575f671daefc1d5c3dd925871952e7a899a5e1", "1.2108.1": "sha256:2ce5c210992fc449059368cab300f11cb796569ad5ef6a6dc798826981b35b67", "latest": "sha256:2ce5c210992fc449059368cab300f11cb796569ad5ef6a6dc798826981b35b67"}, "aliases": {"faodel": "/opt/view/bin/faodel"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/faodel.
Flexible, Asynchronous, Object Data-Exchange Libraries
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/faodel
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/faodel:1.1906.1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/faodel/1.1906.1
$ module help ghcr.io/autamus/faodel/1.1906.1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### faodel-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### faodel-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### faodel-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### faodel-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### faodel-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### faodel-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### faodel
       
```bash
$ singularity exec <container> /opt/view/bin/faodel
$ podman run --it --rm --entrypoint /opt/view/bin/faodel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/faodel   -v ${PWD} -w ${PWD} <container> -c " $@"
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