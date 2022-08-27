---
layout: container
name:  "ghcr.io/autamus/bowtie2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/bowtie2/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/ghcr.io/autamus/bowtie2/container.yaml"
updated_at: "2022-08-27 01:35:36.693761"
latest: "2.4.2"
container_url: "https://github.com/orgs/autamus/packages/container/package/bowtie2"
aliases:
 - "bowtie2"
 - "bowtie2-align-l"
 - "bowtie2-align-s"
 - "bowtie2-build"
 - "bowtie2-build-l"
 - "bowtie2-build-s"
 - "bowtie2-inspect"
 - "bowtie2-inspect-l"
 - "bowtie2-inspect-s"
versions:
 - "2.4.2"
 - "latest"
description: "Bowtie 2 is an ultrafast and memory-efficient tool for aligning sequencing reads to long reference sequences."
config: {"docker": "ghcr.io/autamus/bowtie2", "url": "https://github.com/orgs/autamus/packages/container/package/bowtie2", "maintainer": "@vsoch", "description": "Bowtie 2 is an ultrafast and memory-efficient tool for aligning sequencing reads to long reference sequences.", "latest": {"2.4.2": "sha256:07e6dc7e0266026723139ab53f73bc08f6e1143c6aadf146f7d0f5c14a5b3a22"}, "tags": {"2.4.2": "sha256:07e6dc7e0266026723139ab53f73bc08f6e1143c6aadf146f7d0f5c14a5b3a22", "latest": "sha256:07e6dc7e0266026723139ab53f73bc08f6e1143c6aadf146f7d0f5c14a5b3a22"}, "aliases": {"bowtie2": "/opt/view/bin/bowtie2", "bowtie2-align-l": "/opt/view/bin/bowtie2-align-l", "bowtie2-align-s": "/opt/view/bin/bowtie2-align-s", "bowtie2-build": "/opt/view/bin/bowtie2-build", "bowtie2-build-l": "/opt/view/bin/bowtie2-build-l", "bowtie2-build-s": "/opt/view/bin/bowtie2-build-s", "bowtie2-inspect": "/opt/view/bin/bowtie2-inspect", "bowtie2-inspect-l": "/opt/view/bin/bowtie2-inspect-l", "bowtie2-inspect-s": "/opt/view/bin/bowtie2-inspect-s"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/bowtie2.
Bowtie 2 is an ultrafast and memory-efficient tool for aligning sequencing reads to long reference sequences.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/bowtie2
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/bowtie2:2.4.2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/bowtie2/2.4.2
$ module help ghcr.io/autamus/bowtie2/2.4.2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bowtie2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bowtie2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bowtie2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bowtie2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bowtie2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bowtie2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bowtie2
       
```bash
$ singularity exec <container> /opt/view/bin/bowtie2
$ podman run --it --rm --entrypoint /opt/view/bin/bowtie2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/bowtie2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-align-l
       
```bash
$ singularity exec <container> /opt/view/bin/bowtie2-align-l
$ podman run --it --rm --entrypoint /opt/view/bin/bowtie2-align-l   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/bowtie2-align-l   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-align-s
       
```bash
$ singularity exec <container> /opt/view/bin/bowtie2-align-s
$ podman run --it --rm --entrypoint /opt/view/bin/bowtie2-align-s   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/bowtie2-align-s   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-build
       
```bash
$ singularity exec <container> /opt/view/bin/bowtie2-build
$ podman run --it --rm --entrypoint /opt/view/bin/bowtie2-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/bowtie2-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-build-l
       
```bash
$ singularity exec <container> /opt/view/bin/bowtie2-build-l
$ podman run --it --rm --entrypoint /opt/view/bin/bowtie2-build-l   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/bowtie2-build-l   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-build-s
       
```bash
$ singularity exec <container> /opt/view/bin/bowtie2-build-s
$ podman run --it --rm --entrypoint /opt/view/bin/bowtie2-build-s   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/bowtie2-build-s   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-inspect
       
```bash
$ singularity exec <container> /opt/view/bin/bowtie2-inspect
$ podman run --it --rm --entrypoint /opt/view/bin/bowtie2-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/bowtie2-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-inspect-l
       
```bash
$ singularity exec <container> /opt/view/bin/bowtie2-inspect-l
$ podman run --it --rm --entrypoint /opt/view/bin/bowtie2-inspect-l   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/bowtie2-inspect-l   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-inspect-s
       
```bash
$ singularity exec <container> /opt/view/bin/bowtie2-inspect-s
$ podman run --it --rm --entrypoint /opt/view/bin/bowtie2-inspect-s   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/bowtie2-inspect-s   -v ${PWD} -w ${PWD} <container> -c " $@"
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