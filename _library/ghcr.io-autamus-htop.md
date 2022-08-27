---
layout: container
name:  "ghcr.io/autamus/htop"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/htop/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/ghcr.io/autamus/htop/container.yaml"
updated_at: "2022-08-27 02:52:35.225134"
latest: "3.1.1"
container_url: "https://github.com/orgs/autamus/packages/container/package/htop"
aliases:
 - "htop"
versions:
 - "2.2.0"
 - "3.1.1"
 - "latest"
description: "htop is an interactive text-mode process viewer for Unix systems. https://github.com/hishamhm/htop"
config: {"docker": "ghcr.io/autamus/htop", "url": "https://github.com/orgs/autamus/packages/container/package/htop", "maintainer": "@vsoch", "description": "htop is an interactive text-mode process viewer for Unix systems. https://github.com/hishamhm/htop", "latest": {"3.1.1": "sha256:b048e55631aa8b1712ae9f05636e698096d6816b23e8388b0718df70cd82f378"}, "tags": {"2.2.0": "sha256:861a0982efda17ecdb78c271c330a9056ba9edf61c8fc390afbf7692d15b239b", "3.1.1": "sha256:b048e55631aa8b1712ae9f05636e698096d6816b23e8388b0718df70cd82f378", "latest": "sha256:b048e55631aa8b1712ae9f05636e698096d6816b23e8388b0718df70cd82f378"}, "aliases": {"htop": "/opt/view/bin/htop"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/htop.
htop is an interactive text-mode process viewer for Unix systems. https://github.com/hishamhm/htop
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/htop
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/htop:2.2.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/htop/2.2.0
$ module help ghcr.io/autamus/htop/2.2.0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### htop-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### htop-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### htop-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### htop-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### htop-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### htop-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### htop
       
```bash
$ singularity exec <container> /opt/view/bin/htop
$ podman run --it --rm --entrypoint /opt/view/bin/htop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/htop   -v ${PWD} -w ${PWD} <container> -c " $@"
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