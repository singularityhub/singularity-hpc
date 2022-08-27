---
layout: container
name:  "ghcr.io/autamus/amrex"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/amrex/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/ghcr.io/autamus/amrex/container.yaml"
updated_at: "2022-08-27 02:51:48.867412"
latest: "22.01"
container_url: "https://github.com/orgs/autamus/packages/container/package/amrex"

versions:
 - "21.06"
 - "21.07"
 - "21.08"
 - "21.10"
 - "21.11"
 - "22.01"
 - "21.09"
description: "AMReX is a publicly available software framework designed for building massively parallel block- structured adaptive mesh refinement (AMR) applications."
config: {"docker": "ghcr.io/autamus/amrex", "url": "https://github.com/orgs/autamus/packages/container/package/amrex", "maintainer": "@vsoch", "description": "AMReX is a publicly available software framework designed for building massively parallel block- structured adaptive mesh refinement (AMR) applications.", "latest": {"22.01": "sha256:7cb21a53bc86d27eaea42b37d58352da5d35bf621fa682459ad5699269c9eb81"}, "tags": {"21.06": "sha256:b2e48c43f50f3899e53df008e2f2b260858a74e63d42918b970bd53730f07908", "21.07": "sha256:4084a79d6bd543109f0ba96797ce8955dd8e62d41a15ad292b5ce28ea7433a95", "21.08": "sha256:947d49d53818e622c10fca6277edd8c150ae914f7068673b8c50b6975404a727", "21.10": "sha256:e0d0bfefa77232674175ed0f8932a78601fa324c8d01a3347ab07f06c5d57bc5", "21.11": "sha256:a9d6a7c439daf797b9c62d64be10917697b7040d950586c8e2689837f7ef722a", "22.01": "sha256:7cb21a53bc86d27eaea42b37d58352da5d35bf621fa682459ad5699269c9eb81", "21.09": "sha256:54f5022dfacc514dcb575b5a704d05e8de67caf126d0886d46db748a9605c6e9"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/amrex.
AMReX is a publicly available software framework designed for building massively parallel block- structured adaptive mesh refinement (AMR) applications.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/amrex
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/amrex:21.06
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/amrex/21.06
$ module help ghcr.io/autamus/amrex/21.06
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### amrex-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### amrex-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### amrex-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### amrex-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### amrex-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### amrex-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### amrex

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