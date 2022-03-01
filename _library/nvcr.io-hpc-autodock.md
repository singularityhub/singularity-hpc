---
layout: container
name:  "nvcr.io/hpc/autodock"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/nvcr.io/hpc/autodock/container.yaml"
updated_at: "2022-03-01 01:39:24.809297"
container_url: "https://ngc.nvidia.com/catalog/containers/hpc:autodock"
aliases:
 - "autodock"

versions:
 - "2020.06"
 - "2020.06-arm64"
description: "The AutoDock-GPU Suite is a growing collection of methods for computational docking and virtual screening, for use in structure-based drug discovery and exploration of the basic mechanisms of biomolecular structure and function. More info on AutoDock-GPU be located at https://ccsb.scripps.edu/autodock/ and https://github.com/ccsb-scripps/AutoDock-GPU#usage."
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

When you install this module, you'll be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### -run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### -shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### -exec:

```bash
$ singularity exec -s /bin/sh <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### -inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### -inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### -inspect-deffile:

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