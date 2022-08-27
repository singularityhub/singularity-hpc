---
layout: container
name:  "quay.io/biocontainers/cutadapt"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cutadapt/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/cutadapt/container.yaml"
updated_at: "2022-08-27 02:54:17.239451"
latest: "3.7--py38hbff2b2d_0"
container_url: "https://quay.io/repository/biocontainers/cutadapt"
aliases:
 - "cutadapt"
versions:
 - "3.4--py36h4c5857e_0"
 - "3.4--py38h4a8c8d9_1"
 - "3.5--py39h38f01e4_0"
 - "3.7--py38hbff2b2d_0"
description: "Trim adapters from high-throughput sequencing reads"
config: {"docker": "quay.io/biocontainers/cutadapt", "url": "https://quay.io/repository/biocontainers/cutadapt", "maintainer": "@sarahbeecroft", "description": "Trim adapters from high-throughput sequencing reads", "latest": {"3.7--py38hbff2b2d_0": "sha256:c2201f010d14f6beed26e2fee75d2b8418c1413c457ccb6862b27e75913ce1ff"}, "tags": {"3.4--py36h4c5857e_0": "sha256:53a1f7ff0f9d78fc02e594b3a63ad4ceb84e2834639a23d4e90bcc9c1a1196a0", "3.4--py38h4a8c8d9_1": "sha256:489eda33229f60e7ca8e0397f95c775d53d6f40fa0baed04386e3726d4e9e136", "3.5--py39h38f01e4_0": "sha256:7df6dc446d6a920fa78319113f05d15e79240aee0829f08ee5ebef2f8d4775a4", "3.7--py38hbff2b2d_0": "sha256:c2201f010d14f6beed26e2fee75d2b8418c1413c457ccb6862b27e75913ce1ff"}, "aliases": {"cutadapt": "/usr/local/bin/cutadapt"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cutadapt.
Trim adapters from high-throughput sequencing reads
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cutadapt
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cutadapt:3.4--py36h4c5857e_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cutadapt/3.4--py36h4c5857e_0
$ module help quay.io/biocontainers/cutadapt/3.4--py36h4c5857e_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cutadapt-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cutadapt-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cutadapt-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cutadapt-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cutadapt-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cutadapt-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cutadapt
       
```bash
$ singularity exec <container> /usr/local/bin/cutadapt
$ podman run --it --rm --entrypoint /usr/local/bin/cutadapt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cutadapt   -v ${PWD} -w ${PWD} <container> -c " $@"
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