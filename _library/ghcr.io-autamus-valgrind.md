---
layout: container
name:  "ghcr.io/autamus/valgrind"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/valgrind/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/ghcr.io/autamus/valgrind/container.yaml"
updated_at: "2022-08-27 02:53:40.894876"
latest: "3.17.0"
container_url: "https://github.com/orgs/autamus/packages/container/package/valgrind"
aliases:
 - "valgrind"
 - "valgrind-di-server"
 - "valgrind-listener"
versions:
 - "3.17.0"
 - "latest"
description: "A suite of tools for debugging and profiling. "
config: {"docker": "ghcr.io/autamus/valgrind", "url": "https://github.com/orgs/autamus/packages/container/package/valgrind", "maintainer": "@vsoch", "description": "A suite of tools for debugging and profiling. ", "latest": {"3.17.0": "sha256:8d76ab0b31cb1ee748abd9618c101efeb3806507c1d31a5638b90c7feacb9e6b"}, "tags": {"3.17.0": "sha256:8d76ab0b31cb1ee748abd9618c101efeb3806507c1d31a5638b90c7feacb9e6b", "latest": "sha256:8d76ab0b31cb1ee748abd9618c101efeb3806507c1d31a5638b90c7feacb9e6b"}, "aliases": {"valgrind": "/opt/view/bin/valgrind", "valgrind-di-server": "/opt/view/bin/valgrind-di-server", "valgrind-listener": "/opt/view/bin/valgrind-listener"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/valgrind.
A suite of tools for debugging and profiling. 
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/valgrind
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/valgrind:3.17.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/valgrind/3.17.0
$ module help ghcr.io/autamus/valgrind/3.17.0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### valgrind-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### valgrind-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### valgrind-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### valgrind-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### valgrind-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### valgrind-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### valgrind
       
```bash
$ singularity exec <container> /opt/view/bin/valgrind
$ podman run --it --rm --entrypoint /opt/view/bin/valgrind   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/valgrind   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### valgrind-di-server
       
```bash
$ singularity exec <container> /opt/view/bin/valgrind-di-server
$ podman run --it --rm --entrypoint /opt/view/bin/valgrind-di-server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/valgrind-di-server   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### valgrind-listener
       
```bash
$ singularity exec <container> /opt/view/bin/valgrind-listener
$ podman run --it --rm --entrypoint /opt/view/bin/valgrind-listener   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/valgrind-listener   -v ${PWD} -w ${PWD} <container> -c " $@"
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