---
layout: container
name:  "ghcr.io/autamus/ed"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/ed/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/ghcr.io/autamus/ed/container.yaml"
updated_at: "2022-08-27 01:35:48.853575"
latest: "1.4"
container_url: "https://github.com/orgs/autamus/packages/container/package/ed"
aliases:
 - "ed"
 - "red"
versions:
 - "1.4"
 - "latest"
description: "GNU ed is a line-oriented text editor used to create, display, modify and otherwise manipulate text files, both interactively and via shell scripts https://www.gnu.org/software/ed."
config: {"docker": "ghcr.io/autamus/ed", "url": "https://github.com/orgs/autamus/packages/container/package/ed", "maintainer": "@vsoch", "description": "GNU ed is a line-oriented text editor used to create, display, modify and otherwise manipulate text files, both interactively and via shell scripts https://www.gnu.org/software/ed.", "latest": {"1.4": "sha256:929b50c85da110bc4b23c0cb3a86719e0d973324b834900e08d7e5f000d8352c"}, "tags": {"1.4": "sha256:929b50c85da110bc4b23c0cb3a86719e0d973324b834900e08d7e5f000d8352c", "latest": "sha256:929b50c85da110bc4b23c0cb3a86719e0d973324b834900e08d7e5f000d8352c"}, "aliases": {"ed": "/opt/view/bin/ed", "red": "/opt/view/bin/red"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/ed.
GNU ed is a line-oriented text editor used to create, display, modify and otherwise manipulate text files, both interactively and via shell scripts https://www.gnu.org/software/ed.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/ed
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/ed:1.4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/ed/1.4
$ module help ghcr.io/autamus/ed/1.4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ed-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ed-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ed-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ed-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ed-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ed-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ed
       
```bash
$ singularity exec <container> /opt/view/bin/ed
$ podman run --it --rm --entrypoint /opt/view/bin/ed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/ed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### red
       
```bash
$ singularity exec <container> /opt/view/bin/red
$ podman run --it --rm --entrypoint /opt/view/bin/red   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/red   -v ${PWD} -w ${PWD} <container> -c " $@"
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