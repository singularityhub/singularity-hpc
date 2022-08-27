---
layout: container
name:  "quay.io/pawsey/openfoam"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/pawsey/openfoam/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/pawsey/openfoam/container.yaml"
updated_at: "2022-08-27 02:54:33.443102"
latest: "v2012"
container_url: "https://quay.io/repository/pawsey/openfoam"

versions:
 - "v2012"
 - "v2006"
 - "v1912"
 - "v1812"
 - "v1712"
description: "OpenFOAM (openfoam.com) images built on top of MPICH."
config: {"docker": "quay.io/pawsey/openfoam", "url": "https://quay.io/repository/pawsey/openfoam", "maintainer": "@marcodelapierre", "description": "OpenFOAM (openfoam.com) images built on top of MPICH.", "latest": {"v2012": "sha256:916191b7cbdeeed8ff3697eefe91bd60415b96ba9d3d1127bca2473942355fc8"}, "tags": {"v2012": "sha256:916191b7cbdeeed8ff3697eefe91bd60415b96ba9d3d1127bca2473942355fc8", "v2006": "sha256:c1222ddcd389bd3daabe5a5fd7ccc5f9aa1737a4b5ccc622a35e0d487305c8f7", "v1912": "sha256:ad68ad8e13252915300b29dcdb5803bca9bed68fa5099265c7071ace7f9e3330", "v1812": "sha256:6197994d3eba966ab9c8cbdcfde97bdd67313fab55ada09d9665e974a0ef707a", "v1712": "sha256:ac766f92b678cf9c70aefaa914bcad3837675e57dae38554220ec9024a4a3dc9"}, "overrides": {"v1712": "aliases/v1712.yaml", "v1812": "aliases/v1812.yaml", "v1912": "aliases/v1912.yaml", "v2006": "aliases/v2006.yaml", "v2012": "aliases/v2012.yaml"}}
---

This module is a singularity container wrapper for quay.io/pawsey/openfoam.
OpenFOAM (openfoam.com) images built on top of MPICH.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/pawsey/openfoam
```

Or a specific version:

```bash
$ shpc install quay.io/pawsey/openfoam:v2012
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/pawsey/openfoam/v2012
$ module help quay.io/pawsey/openfoam/v2012
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### openfoam-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### openfoam-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### openfoam-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### openfoam-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### openfoam-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### openfoam-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### openfoam

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