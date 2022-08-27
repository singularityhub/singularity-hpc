---
layout: container
name:  "ghcr.io/autamus/petsc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/petsc/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/ghcr.io/autamus/petsc/container.yaml"
updated_at: "2022-08-27 02:53:08.087305"
latest: "3.16.3"
container_url: "https://github.com/orgs/autamus/packages/container/package/petsc"

versions:
 - "3.15.1"
 - "3.15.3"
 - "3.16.0"
 - "3.16.1"
 - "3.16.2"
 - "3.16.3"
 - "3.15.4"
 - "latest"
description: "PETSc is a suite of data structures and routines for the scalable (parallel) solution of scientific applications modeled by partial differential equations."
config: {"docker": "ghcr.io/autamus/petsc", "url": "https://github.com/orgs/autamus/packages/container/package/petsc", "maintainer": "@vsoch", "description": "PETSc is a suite of data structures and routines for the scalable (parallel) solution of scientific applications modeled by partial differential equations.", "latest": {"3.16.3": "sha256:4200e5372abe7d262b3330f888a335594ce5bc0ef0931350c7f06bf1821c0adc"}, "tags": {"3.15.1": "sha256:3593285d718d4d953cd1ebb331c74590c7888530c4573eb2d3629bdc81800a2a", "3.15.3": "sha256:e96aca1906a647d74f3819ee9a93adaeb0625a76cc1705a1f2e9092b395c25dc", "3.16.0": "sha256:9bc11f80ca9bc61d191cfbd06a9fa929dc8e10d498d90a1d98226aea4ef54842", "3.16.1": "sha256:1af847f6c0d660cef371d7307a8db2730c8e67896c0d4d560d8a8ef1123e0cca", "3.16.2": "sha256:365f866d35ae39295b33ec64b9fd3e52fec0bba1b3218dd7e251f9daff0e52a6", "3.16.3": "sha256:4200e5372abe7d262b3330f888a335594ce5bc0ef0931350c7f06bf1821c0adc", "3.15.4": "sha256:9aa8dbdafc8dee8dba07ae209a65bb44caa0697c0d654ad66367937aa7156942", "latest": "sha256:4200e5372abe7d262b3330f888a335594ce5bc0ef0931350c7f06bf1821c0adc"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/petsc.
PETSc is a suite of data structures and routines for the scalable (parallel) solution of scientific applications modeled by partial differential equations.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/petsc
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/petsc:3.15.1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/petsc/3.15.1
$ module help ghcr.io/autamus/petsc/3.15.1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### petsc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### petsc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### petsc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### petsc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### petsc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### petsc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### petsc

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