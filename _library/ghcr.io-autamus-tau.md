---
layout: container
name:  "ghcr.io/autamus/tau"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/tau/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/ghcr.io/autamus/tau/container.yaml"
updated_at: "2022-08-27 02:53:34.880625"
latest: "2.31"
container_url: "https://github.com/orgs/autamus/packages/container/package/tau"

versions:
 - "2.30.1"
 - "2.30.2"
 - "2.31"
 - "latest"
description: "A portable profiling and tracing toolkit for performance analysis of parallel programs written in Fortran, C, C++, UPC, Java, Python."
config: {"docker": "ghcr.io/autamus/tau", "url": "https://github.com/orgs/autamus/packages/container/package/tau", "maintainer": "@vsoch", "description": "A portable profiling and tracing toolkit for performance analysis of parallel programs written in Fortran, C, C++, UPC, Java, Python.", "latest": {"2.31": "sha256:89d061bfaf921f102528f1e2ab06741041e0bec28f197b2a81f9ef2aa438088e"}, "tags": {"2.30.1": "sha256:3df1deaa0fcecedafae828a493afbf49a0df3c201fd1f4d261f8246e05d538be", "2.30.2": "sha256:e85557bb38b25bfe39a28258f209c2d5c9c15cfc3860f1bcb49de316391db958", "2.31": "sha256:89d061bfaf921f102528f1e2ab06741041e0bec28f197b2a81f9ef2aa438088e", "latest": "sha256:89d061bfaf921f102528f1e2ab06741041e0bec28f197b2a81f9ef2aa438088e"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/tau.
A portable profiling and tracing toolkit for performance analysis of parallel programs written in Fortran, C, C++, UPC, Java, Python.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/tau
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/tau:2.30.1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/tau/2.30.1
$ module help ghcr.io/autamus/tau/2.30.1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### tau-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### tau-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### tau-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### tau-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### tau-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### tau-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### tau

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