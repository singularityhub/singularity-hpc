---
layout: container
name:  "ghcr.io/autamus/hypre"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/hypre/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/ghcr.io/autamus/hypre/container.yaml"
updated_at: "2022-08-27 02:52:36.581579"
latest: "2.23.0"
container_url: "https://github.com/orgs/autamus/packages/container/package/hypre"

versions:
 - "2.20.0"
 - "2.21.0"
 - "2.22.0"
 - "2.22.1"
 - "2.23.0"
 - "latest"
description: "A library of high performance preconditioners and solvers featuring multigrid methods for the solution of large, sparse linear systems of equations on massively parallel computers."
config: {"docker": "ghcr.io/autamus/hypre", "url": "https://github.com/orgs/autamus/packages/container/package/hypre", "maintainer": "@vsoch", "description": "A library of high performance preconditioners and solvers featuring multigrid methods for the solution of large, sparse linear systems of equations on massively parallel computers.", "latest": {"2.23.0": "sha256:2fe5bd7f87b499c503cc951fb41b7bb0b1e42da8dc755a93b35ec101c8802bc3"}, "tags": {"2.20.0": "sha256:764702fee4c12182bb8c894a727a2aff6deee547551fa2bcc4c6f6e0866bcee6", "2.21.0": "sha256:3983e937576b5cd835a40b7bef5ce254727381040304dfd470e629d1d5d02099", "2.22.0": "sha256:9dbedd069503b4e341ea582ed7c0f0a881edc48e5be448eda2990cd52f0cc147", "2.22.1": "sha256:4ad18841a1dd688480a43eb51bb62d46da8781ae68432aacb07426c7a7202d17", "2.23.0": "sha256:2fe5bd7f87b499c503cc951fb41b7bb0b1e42da8dc755a93b35ec101c8802bc3", "latest": "sha256:2fe5bd7f87b499c503cc951fb41b7bb0b1e42da8dc755a93b35ec101c8802bc3"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/hypre.
A library of high performance preconditioners and solvers featuring multigrid methods for the solution of large, sparse linear systems of equations on massively parallel computers.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/hypre
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/hypre:2.20.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/hypre/2.20.0
$ module help ghcr.io/autamus/hypre/2.20.0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### hypre-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### hypre-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### hypre-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### hypre-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### hypre-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### hypre-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### hypre

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