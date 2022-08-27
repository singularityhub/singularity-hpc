---
layout: container
name:  "ghcr.io/autamus/kallisto"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/kallisto/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/ghcr.io/autamus/kallisto/container.yaml"
updated_at: "2022-08-27 01:36:09.870406"
latest: "0.46.2"
container_url: "https://github.com/orgs/autamus/packages/container/package/kallisto"
aliases:
 - "kallisto"
versions:
 - "0.46.2"
 - "latest"
description: "kallisto is a program for quantifying abundances of transcripts from bulk and single-cell RNA-Seq data, or more generally of target sequences using high-throughput sequencing reads."
config: {"docker": "ghcr.io/autamus/kallisto", "url": "https://github.com/orgs/autamus/packages/container/package/kallisto", "maintainer": "@vsoch", "description": "kallisto is a program for quantifying abundances of transcripts from bulk and single-cell RNA-Seq data, or more generally of target sequences using high-throughput sequencing reads.", "latest": {"0.46.2": "sha256:fe74aadc99ef7b850861fe476a54bdff56f8c967da9c2d2d589388e016bf5b82"}, "tags": {"0.46.2": "sha256:fe74aadc99ef7b850861fe476a54bdff56f8c967da9c2d2d589388e016bf5b82", "latest": "sha256:fe74aadc99ef7b850861fe476a54bdff56f8c967da9c2d2d589388e016bf5b82"}, "aliases": {"kallisto": "/opt/view/bin/kallisto"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/kallisto.
kallisto is a program for quantifying abundances of transcripts from bulk and single-cell RNA-Seq data, or more generally of target sequences using high-throughput sequencing reads.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/kallisto
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/kallisto:0.46.2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/kallisto/0.46.2
$ module help ghcr.io/autamus/kallisto/0.46.2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### kallisto-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### kallisto-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### kallisto-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### kallisto-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### kallisto-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### kallisto-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### kallisto
       
```bash
$ singularity exec <container> /opt/view/bin/kallisto
$ podman run --it --rm --entrypoint /opt/view/bin/kallisto   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/kallisto   -v ${PWD} -w ${PWD} <container> -c " $@"
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