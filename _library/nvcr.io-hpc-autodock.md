---
layout: container
name:  "nvcr.io/hpc/autodock"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/nvcr.io/hpc/autodock/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/nvcr.io/hpc/autodock/container.yaml"
updated_at: "2022-08-27 02:53:57.050309"
latest: "2020.06"
container_url: "https://ngc.nvidia.com/catalog/containers/hpc:autodock"
aliases:
 - "autodock"
versions:
 - "2020.06"
 - "2020.06-arm64"
 - "2020.06-x86_64"
description: "The AutoDock-GPU Suite is a growing collection of methods for computational docking and virtual screening, for use in structure-based drug discovery and exploration of the basic mechanisms of biomolecular structure and function. More info on AutoDock-GPU be located at https://ccsb.scripps.edu/autodock/ and https://github.com/ccsb-scripps/AutoDock-GPU#usage."
config: {"docker": "nvcr.io/hpc/autodock", "url": "https://ngc.nvidia.com/catalog/containers/hpc:autodock", "maintainer": "@vsoch", "description": "The AutoDock-GPU Suite is a growing collection of methods for computational docking and virtual screening, for use in structure-based drug discovery and exploration of the basic mechanisms of biomolecular structure and function. More info on AutoDock-GPU be located at https://ccsb.scripps.edu/autodock/ and https://github.com/ccsb-scripps/AutoDock-GPU#usage.", "latest": {"2020.06": "sha256:a968fa5391281f168e1daf5a4fccfbd0d8228d794ee693ba1a637e5147c3b798"}, "tags": {"2020.06": "sha256:a968fa5391281f168e1daf5a4fccfbd0d8228d794ee693ba1a637e5147c3b798", "2020.06-arm64": "sha256:2d881faf0b20866826a2f0ebbd87ed9791b64222489814901a090e5ed1aa3252", "2020.06-x86_64": "sha256:0bc28fe0b15b172241f785079782447251139ad0ef0b978f3f1483d5caa9e56d"}, "filter": ["^((?!arm).)*$"], "features": {"gpu": true}, "aliases": {"autodock": "/opt/AutoDock-GPU/bin/autodock_gpu_128wi"}}
---

This module is a singularity container wrapper for nvcr.io/hpc/autodock.
The AutoDock-GPU Suite is a growing collection of methods for computational docking and virtual screening, for use in structure-based drug discovery and exploration of the basic mechanisms of biomolecular structure and function. More info on AutoDock-GPU be located at https://ccsb.scripps.edu/autodock/ and https://github.com/ccsb-scripps/AutoDock-GPU#usage.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install nvcr.io/hpc/autodock
```

Or a specific version:

```bash
$ shpc install nvcr.io/hpc/autodock:2020.06
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load nvcr.io/hpc/autodock/2020.06
$ module help nvcr.io/hpc/autodock/2020.06
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### autodock-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### autodock-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### autodock-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### autodock-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### autodock-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### autodock-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### autodock
       
```bash
$ singularity exec <container> /opt/AutoDock-GPU/bin/autodock_gpu_128wi
$ podman run --it --rm --entrypoint /opt/AutoDock-GPU/bin/autodock_gpu_128wi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/AutoDock-GPU/bin/autodock_gpu_128wi   -v ${PWD} -w ${PWD} <container> -c " $@"
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