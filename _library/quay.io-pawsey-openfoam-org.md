---
layout: container
name:  "quay.io/pawsey/openfoam-org"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/pawsey/openfoam-org/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/pawsey/openfoam-org/container.yaml"
updated_at: "2022-08-27 01:37:36.939260"
latest: "8"
container_url: "https://quay.io/repository/pawsey/openfoam-org"

versions:
 - "8"
 - "7"
 - "5.x"
 - "2.4.x"
 - "2.2.0"
description: "OpenFOAM (openfoam.org) images built on top of MPICH."
config: {"docker": "quay.io/pawsey/openfoam-org", "url": "https://quay.io/repository/pawsey/openfoam-org", "maintainer": "@marcodelapierre", "description": "OpenFOAM (openfoam.org) images built on top of MPICH.", "latest": {"8": "sha256:13eafb0fa58dafbdaacf8000886bdd3c9c63ee29c35f09a2cc1cdf44c1871226"}, "tags": {"8": "sha256:13eafb0fa58dafbdaacf8000886bdd3c9c63ee29c35f09a2cc1cdf44c1871226", "7": "sha256:3d427b3dec890193bb671185acefdc91fb126363b5f368d147603002b4708afe", "5.x": "sha256:301765ba65e135ad1954bc8dabfc1a76ad716000ae8142d0c0a61810b3dce922", "2.4.x": "sha256:526ed37410c31789c5da9f3dd5f842835989533181b0c7e7feafd1eaa683ff43", "2.2.0": "sha256:32f0a464f0ea128e6b68b58e90719c24b5acb962dc8b7b8767440f8d70ed9156"}, "overrides": {"2.2.0": "aliases/2.2.0.yaml", "2.4.x": "aliases/2.4.x.yaml", "5.x": "aliases/5.x.yaml", "7": "aliases/7.yaml", "8": "aliases/8.yaml"}}
---

This module is a singularity container wrapper for quay.io/pawsey/openfoam-org.
OpenFOAM (openfoam.org) images built on top of MPICH.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/pawsey/openfoam-org
```

Or a specific version:

```bash
$ shpc install quay.io/pawsey/openfoam-org:8
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/pawsey/openfoam-org/8
$ module help quay.io/pawsey/openfoam-org/8
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### openfoam-org-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### openfoam-org-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### openfoam-org-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### openfoam-org-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### openfoam-org-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### openfoam-org-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### openfoam-org

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