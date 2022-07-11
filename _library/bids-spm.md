---
layout: container
name:  "bids/spm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/bids/spm/container.yaml"
updated_at: "2022-07-11 07:51:22.187697"
container_url: "https://hub.docker.com/r/bids/spm"
aliases:
 - "spm12"

versions:
 - "latest"
 - "v0.0.20"
 - "chrisfilo-patch-1"
 - "enh_various"
description: "The implementation of the theoretical concepts of Statistical Parametric Mapping in a complete analysis package."
---

This module is a singularity container wrapper for bids/spm.
The implementation of the theoretical concepts of Statistical Parametric Mapping in a complete analysis package.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install bids/spm
```

Or a specific version:

```bash
$ shpc install bids/spm:latest
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load bids/spm/latest
$ module help bids/spm/latest
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### spm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### spm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### spm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### spm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### spm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### spm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### spm12
       
```bash
$ singularity exec <container> /opt/spm12/spm12
$ podman run --it --rm --entrypoint /opt/spm12/spm12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/spm12/spm12   -v ${PWD} -w ${PWD} <container> -c " $@"
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