---
layout: container
name:  "r-base"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/r-base/container.yaml"
updated_at: "2022-04-01 23:46:36.542922"
container_url: "https://hub.docker.com/_/r-base"
aliases:
 - "R"

 - "Rscript"

versions:
 - "4.1.0"
 - "4.1.1"
 - "4.1.2"
 - "latest"
description: "R is a system for statistical computation and graphics."
---

This module is a singularity container wrapper for r-base.
R is a system for statistical computation and graphics.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install r-base
```

Or a specific version:

```bash
$ shpc install r-base:4.1.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load r-base/4.1.0
$ module help r-base/4.1.0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-base-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-base-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-base-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-base-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-base-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-base-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### R
       
```bash
$ singularity exec <container> /usr/bin/R
$ podman run --it --rm --entrypoint /usr/bin/R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Rscript
       
```bash
$ singularity exec <container> /usr/bin/Rscript
$ podman run --it --rm --entrypoint /usr/bin/Rscript   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/Rscript   -v ${PWD} -w ${PWD} <container> -c " $@"
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