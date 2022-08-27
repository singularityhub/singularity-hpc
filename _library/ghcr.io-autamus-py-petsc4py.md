---
layout: container
name:  "ghcr.io/autamus/py-petsc4py"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/py-petsc4py/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/ghcr.io/autamus/py-petsc4py/container.yaml"
updated_at: "2022-08-27 02:53:16.713379"
latest: "3.16.3"
container_url: "https://github.com/orgs/autamus/packages/container/package/py-petsc4py"

versions:
 - "3.15.1"
 - "3.15.3"
 - "3.16.0"
 - "3.16.1"
 - "3.16.2"
 - "3.16.3"
 - "3.15.4"
 - "latest"
description: "This package provides Python bindings for the PETSc package."
config: {"docker": "ghcr.io/autamus/py-petsc4py", "url": "https://github.com/orgs/autamus/packages/container/package/py-petsc4py", "maintainer": "@vsoch", "description": "This package provides Python bindings for the PETSc package.", "latest": {"3.16.3": "sha256:59588352cc80b17872945168b4ca71feb8165b08918f27959ef19a6e92e2cfc0"}, "tags": {"3.15.1": "sha256:eb9a93ec9b97db483cf0e5a994f8c01c4ecc80c3d2e52fb6122c2416c272e243", "3.15.3": "sha256:32915ceef04da514ac620fd9f45c61cfead35fd23e0ef21de40072bbf2c98bf6", "3.16.0": "sha256:cce09490be0a51e85c2cfb892ff419214648373607b7644900fc8090aac22d88", "3.16.1": "sha256:08a755dbf04536a1803d2ae647d5c73fe7ec9b09c1fb47d5bbe69e5f287e1569", "3.16.2": "sha256:2e4c31552a93357040b21184265df445ead6f3bd7c8590bfb5308ce2f8c3029d", "3.16.3": "sha256:59588352cc80b17872945168b4ca71feb8165b08918f27959ef19a6e92e2cfc0", "3.15.4": "sha256:484d30391d9ed15b3c1505f94cf2ee1318298df0d16f9d0204c49885230f41cf", "latest": "sha256:59588352cc80b17872945168b4ca71feb8165b08918f27959ef19a6e92e2cfc0"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/py-petsc4py.
This package provides Python bindings for the PETSc package.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/py-petsc4py
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/py-petsc4py:3.15.1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/py-petsc4py/3.15.1
$ module help ghcr.io/autamus/py-petsc4py/3.15.1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### py-petsc4py-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### py-petsc4py-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### py-petsc4py-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### py-petsc4py-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### py-petsc4py-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### py-petsc4py-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### py-petsc4py

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