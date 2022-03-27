---
layout: container
name:  "quay.io/biocontainers/gatk4"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/quay.io/biocontainers/gatk4/container.yaml"
updated_at: "2022-03-27 18:03:34.301478"
container_url: "https://quay.io/repository/biocontainers/gatk4"
aliases:
 - "gatk"

versions:
 - "4.1.9.0--py39_0"
 - "4.2.0.0--0"
 - "4.2.2.0--hdfd78af_0"
 - "4.2.3.0--hdfd78af_0"
 - "4.2.4.0--hdfd78af_0"
 - "4.2.4.1--hdfd78af_0"
 - "4.2.5.0--hdfd78af_0"
description: "An open source toolkit frequently used by most genomic research and clinical analyses"
---

This module is a singularity container wrapper for quay.io/biocontainers/gatk4.
An open source toolkit frequently used by most genomic research and clinical analyses
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gatk4
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gatk4:4.1.9.0--py39_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gatk4/4.1.9.0--py39_0
$ module help quay.io/biocontainers/gatk4/4.1.9.0--py39_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gatk4-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gatk4-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gatk4-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gatk4-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gatk4-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gatk4-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gatk
       
```bash
$ singularity exec <container> /usr/local/bin/gatk
$ podman run --it --rm --entrypoint /usr/local/bin/gatk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gatk   -v ${PWD} -w ${PWD} <container> -c " $@"
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