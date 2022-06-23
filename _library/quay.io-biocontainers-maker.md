---
layout: container
name:  "quay.io/biocontainers/maker"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/quay.io/biocontainers/maker/container.yaml"
updated_at: "2022-06-23 04:34:15.207170"
container_url: "https://quay.io/repository/biocontainers/maker"
aliases:
 - "maker"

versions:
 - "2.31.11--pl526h61907ee_0"
 - "3.01.03--pl526hb8757ab_0"
 - "3.01.03--pl5262h8f1cd36_2"
 - "2.31.11--pl5262hec0a270_1"
description: "A portable and easily configurable genome annotation pipeline"
---

This module is a singularity container wrapper for quay.io/biocontainers/maker.
A portable and easily configurable genome annotation pipeline
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/maker
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/maker:2.31.11--pl526h61907ee_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/maker/2.31.11--pl526h61907ee_0
$ module help quay.io/biocontainers/maker/2.31.11--pl526h61907ee_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### maker-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### maker-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### maker-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### maker-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### maker-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### maker-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### maker
       
```bash
$ singularity exec <container> /usr/local/bin/maker
$ podman run --it --rm --entrypoint /usr/local/bin/maker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/maker   -v ${PWD} -w ${PWD} <container> -c " $@"
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