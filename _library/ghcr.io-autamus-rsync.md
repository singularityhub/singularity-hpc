---
layout: container
name:  "ghcr.io/autamus/rsync"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/rsync/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/ghcr.io/autamus/rsync/container.yaml"
updated_at: "2022-08-27 02:53:22.058938"
latest: "3.2.3"
container_url: "https://github.com/orgs/autamus/packages/container/package/rsync"
aliases:
 - "rsync"
 - "rsync-ssl"
versions:
 - "3.2.2"
 - "3.2.3"
description: "An open source utility that provides fast incremental file transfer. https://rsync.samba.org/"
config: {"docker": "ghcr.io/autamus/rsync", "url": "https://github.com/orgs/autamus/packages/container/package/rsync", "maintainer": "@vsoch", "description": "An open source utility that provides fast incremental file transfer. https://rsync.samba.org/", "latest": {"3.2.3": "sha256:370c0624084a02e3d919cb17847bdad4f7b79d4258d016e3aaac0b4de49492b0"}, "tags": {"3.2.2": "sha256:99c4780710b1d844ca8998dea4c59b2d3b54c28ac206dc3ee580ca2c34f455d1", "3.2.3": "sha256:370c0624084a02e3d919cb17847bdad4f7b79d4258d016e3aaac0b4de49492b0"}, "aliases": {"rsync": "/opt/view/bin/rsync", "rsync-ssl": "/opt/view/bin/rsync-ssl"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/rsync.
An open source utility that provides fast incremental file transfer. https://rsync.samba.org/
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/rsync
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/rsync:3.2.2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/rsync/3.2.2
$ module help ghcr.io/autamus/rsync/3.2.2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rsync-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rsync-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rsync-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rsync-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rsync-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rsync-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### rsync
       
```bash
$ singularity exec <container> /opt/view/bin/rsync
$ podman run --it --rm --entrypoint /opt/view/bin/rsync   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/rsync   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rsync-ssl
       
```bash
$ singularity exec <container> /opt/view/bin/rsync-ssl
$ podman run --it --rm --entrypoint /opt/view/bin/rsync-ssl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/rsync-ssl   -v ${PWD} -w ${PWD} <container> -c " $@"
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