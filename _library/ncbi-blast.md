---
layout: container
name:  "ncbi/blast"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ncbi/blast/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/ncbi/blast/container.yaml"
updated_at: "2022-08-27 01:37:07.261060"
latest: "2.13.0"
container_url: "https://hub.docker.com/r/ncbi/blast"

versions:
 - "2.11.0"
 - "2.12.0"
 - "latest"
 - "2.13.0"
description: "The Basic Local Alignment Search Tool (BLAST) finds regions of local similarity between sequences."
config: {"docker": "ncbi/blast", "url": "https://hub.docker.com/r/ncbi/blast", "maintainer": "@vsoch", "description": "The Basic Local Alignment Search Tool (BLAST) finds regions of local similarity between sequences.", "latest": {"2.13.0": "sha256:ae7aaf7dbb861d8c2e4c59738101d98548ea5578cd412bffa0b24a6aca8ceced"}, "tags": {"2.11.0": "sha256:6591661d046e5d5d4c5c45baf8bcfcc8b9188590f87b25dc1f625cb29383b922", "2.12.0": "sha256:367f06bf5d5fc9f6ea2dd24bee7571e3b5be589175a902c257261f3f41784517", "latest": "sha256:ae7aaf7dbb861d8c2e4c59738101d98548ea5578cd412bffa0b24a6aca8ceced", "2.13.0": "sha256:ae7aaf7dbb861d8c2e4c59738101d98548ea5578cd412bffa0b24a6aca8ceced"}}
---

This module is a singularity container wrapper for ncbi/blast.
The Basic Local Alignment Search Tool (BLAST) finds regions of local similarity between sequences.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ncbi/blast
```

Or a specific version:

```bash
$ shpc install ncbi/blast:2.11.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ncbi/blast/2.11.0
$ module help ncbi/blast/2.11.0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### blast-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### blast-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### blast-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### blast-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### blast-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### blast-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### blast

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