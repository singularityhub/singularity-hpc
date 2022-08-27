---
layout: container
name:  "ghcr.io/autamus/clingo"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/clingo/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/ghcr.io/autamus/clingo/container.yaml"
updated_at: "2022-08-27 02:52:07.081546"
latest: "5.5.1"
container_url: "https://github.com/orgs/autamus/packages/container/package/clingo"
aliases:
 - "clingo"
 - "gringo"
versions:
 - "5.4.1"
 - "5.5.0"
 - "5.5.1"
 - "latest"
description: "An ASP system to ground and solve logic programs."
config: {"docker": "ghcr.io/autamus/clingo", "url": "https://github.com/orgs/autamus/packages/container/package/clingo", "maintainer": "@vsoch", "description": "An ASP system to ground and solve logic programs.", "latest": {"5.5.1": "sha256:dc453ee2098625ad56dbafc7a9bfae656ba2577d3931b99edf1a836ac0635961"}, "tags": {"5.4.1": "sha256:c98a480f85a68063dfb9c4cb6eedfbe0cf84a1af737b73ef2d94213fffd91ff5", "5.5.0": "sha256:3abad0093b96f7f8336c2259f77410cc154656aa6f3dfbd482d2a05786b81bca", "5.5.1": "sha256:dc453ee2098625ad56dbafc7a9bfae656ba2577d3931b99edf1a836ac0635961", "latest": "sha256:dc453ee2098625ad56dbafc7a9bfae656ba2577d3931b99edf1a836ac0635961"}, "aliases": {"clingo": "/opt/view/bin/clingo", "gringo": "/opt/view/bin/gringo"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/clingo.
An ASP system to ground and solve logic programs.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/clingo
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/clingo:5.4.1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/clingo/5.4.1
$ module help ghcr.io/autamus/clingo/5.4.1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### clingo-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### clingo-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### clingo-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### clingo-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### clingo-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### clingo-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### clingo
       
```bash
$ singularity exec <container> /opt/view/bin/clingo
$ podman run --it --rm --entrypoint /opt/view/bin/clingo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/clingo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gringo
       
```bash
$ singularity exec <container> /opt/view/bin/gringo
$ podman run --it --rm --entrypoint /opt/view/bin/gringo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/gringo   -v ${PWD} -w ${PWD} <container> -c " $@"
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