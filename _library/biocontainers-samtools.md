---
layout: container
name:  "biocontainers/samtools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/biocontainers/samtools/container.yaml"
updated_at: "2022-03-22 12:57:42.658027"
container_url: "https://hub.docker.com/r/biocontainers/samtools"
aliases:
 - "samtools"

versions:
 - "v1.9-4-deb_cv1"
description: "Samtools is a suite of programs for interacting with high-throughput sequencing data."
---

This module is a singularity container wrapper for biocontainers/samtools.
Samtools is a suite of programs for interacting with high-throughput sequencing data.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install biocontainers/samtools
```

Or a specific version:

```bash
$ shpc install biocontainers/samtools:v1.9-4-deb_cv1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load biocontainers/samtools/v1.9-4-deb_cv1
$ module help biocontainers/samtools/v1.9-4-deb_cv1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### samtools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### samtools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### samtools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### samtools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### samtools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### samtools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### samtools
       
```bash
$ singularity exec <container> /usr/bin/samtools
$ podman run --it --rm --entrypoint /usr/bin/samtools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/samtools   -v ${PWD} -w ${PWD} <container> -c " $@"
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