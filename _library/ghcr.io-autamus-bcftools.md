---
layout: container
name:  "ghcr.io/autamus/bcftools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/bcftools/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/ghcr.io/autamus/bcftools/container.yaml"
updated_at: "2022-08-27 01:35:32.993390"
latest: "1.14"
container_url: "https://github.com/orgs/autamus/packages/container/package/bcftools"
aliases:
 - "bcftools"
versions:
 - "1.12"
 - "1.13"
 - "1.14"
 - "latest"
description: "BCFtools is a set of utilities that manipulate variant calls in the Variant Call Format (VCF) and its binary counterpart BCF."
config: {"docker": "ghcr.io/autamus/bcftools", "url": "https://github.com/orgs/autamus/packages/container/package/bcftools", "maintainer": "@vsoch", "description": "BCFtools is a set of utilities that manipulate variant calls in the Variant Call Format (VCF) and its binary counterpart BCF.", "latest": {"1.14": "sha256:6ae2e486b4e02bfcd0da8a4c3f7c4e39cbd0a3ffb04deb7209fc5d92712e042a"}, "tags": {"1.12": "sha256:b77a402c04d702bf2c4cac914552c2515e630d9e6ecf36fcd332469f026388d9", "1.13": "sha256:f362b16aec2b3fc6d1e6119882ff113066684432cfcb8882990c6d2a4ce2569a", "1.14": "sha256:6ae2e486b4e02bfcd0da8a4c3f7c4e39cbd0a3ffb04deb7209fc5d92712e042a", "latest": "sha256:6ae2e486b4e02bfcd0da8a4c3f7c4e39cbd0a3ffb04deb7209fc5d92712e042a"}, "aliases": {"bcftools": "/opt/view/bin/bcftools"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/bcftools.
BCFtools is a set of utilities that manipulate variant calls in the Variant Call Format (VCF) and its binary counterpart BCF.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/bcftools
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/bcftools:1.12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/bcftools/1.12
$ module help ghcr.io/autamus/bcftools/1.12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bcftools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bcftools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bcftools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bcftools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bcftools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bcftools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bcftools
       
```bash
$ singularity exec <container> /opt/view/bin/bcftools
$ podman run --it --rm --entrypoint /opt/view/bin/bcftools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/bcftools   -v ${PWD} -w ${PWD} <container> -c " $@"
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