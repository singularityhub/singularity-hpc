---
layout: container
name:  "ghcr.io/autamus/omega-h"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/omega-h/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/ghcr.io/autamus/omega-h/container.yaml"
updated_at: "2022-08-27 02:53:00.660076"
latest: "9.34.6"
container_url: "https://github.com/orgs/autamus/packages/container/package/omega-h"

versions:
 - "9.32.5"
 - "9.33.3"
 - "9.34.6"
 - "9.34.5"
 - "latest"
description: "Omega_h is a C++11 library providing data structures and algorithms for adaptive discretizations."
config: {"docker": "ghcr.io/autamus/omega-h", "url": "https://github.com/orgs/autamus/packages/container/package/omega-h", "maintainer": "@vsoch", "description": "Omega_h is a C++11 library providing data structures and algorithms for adaptive discretizations.", "latest": {"9.34.6": "sha256:02def9b6a5c0f9aba1e538b8a36f8c31b5e6638af68462008b3aab1cd240a389"}, "tags": {"9.32.5": "sha256:34ff23ca78005b63181955a9d1e8eec9e7b95238a06e68b5b86892f1d62ac711", "9.33.3": "sha256:badd22d17ca9060051b7d44652cad72516c796edc7450d8560c35318c7bd014d", "9.34.6": "sha256:02def9b6a5c0f9aba1e538b8a36f8c31b5e6638af68462008b3aab1cd240a389", "9.34.5": "sha256:8b2ea55ac9427dd0b9a55e1bc705e68091146a7157d7f6a27ce1ad554e874e13", "latest": "sha256:02def9b6a5c0f9aba1e538b8a36f8c31b5e6638af68462008b3aab1cd240a389"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/omega-h.
Omega_h is a C++11 library providing data structures and algorithms for adaptive discretizations.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/omega-h
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/omega-h:9.32.5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/omega-h/9.32.5
$ module help ghcr.io/autamus/omega-h/9.32.5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### omega-h-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### omega-h-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### omega-h-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### omega-h-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### omega-h-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### omega-h-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### omega-h

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