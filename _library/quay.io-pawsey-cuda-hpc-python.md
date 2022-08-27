---
layout: container
name:  "quay.io/pawsey/cuda-hpc-python"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/pawsey/cuda-hpc-python/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/pawsey/cuda-hpc-python/container.yaml"
updated_at: "2022-08-27 01:37:34.818485"
latest: "2022.03"
container_url: "https://quay.io/repository/pawsey/cuda-hpc-python"
aliases:
 - "python"
 - "python3"
versions:
 - "2021.09"
 - "2021.09-hdf5mpi"
 - "2022.03"
 - "2022.03-hdf5mpi"
description: "Base Python images with popular packages for HPC workflows, with CUDA support."
config: {"docker": "quay.io/pawsey/cuda-hpc-python", "url": "https://quay.io/repository/pawsey/cuda-hpc-python", "maintainer": "@marcodelapierre", "description": "Base Python images with popular packages for HPC workflows, with CUDA support.", "latest": {"2022.03": "sha256:9d0c078fd2854217dfcbfff9483193848c6dc0e80308d15d567c7eaa88f9bfd1"}, "tags": {"2021.09": "sha256:4785a7b1ea3013c276be0b34664d477935961ac5cc89cced3105edddc011a661", "2021.09-hdf5mpi": "sha256:904e55e2d760ac6c0e9db759c86c8942a3873e9009f7bfad05ec8258fbe7a29a", "2022.03": "sha256:9d0c078fd2854217dfcbfff9483193848c6dc0e80308d15d567c7eaa88f9bfd1", "2022.03-hdf5mpi": "sha256:74d5953fb12c9cdc0657d8edc3135f1001d11de9a0f5c2ab4ac55238aac405b2"}, "aliases": {"python": "/usr/local/bin/python", "python3": "/usr/local/bin/python3"}, "env": {"PYTHONSTARTUP": "", "PYTHONUSERBASE": ""}, "features": {"home": true, "gpu": true}}
---

This module is a singularity container wrapper for quay.io/pawsey/cuda-hpc-python.
Base Python images with popular packages for HPC workflows, with CUDA support.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/pawsey/cuda-hpc-python
```

Or a specific version:

```bash
$ shpc install quay.io/pawsey/cuda-hpc-python:2021.09
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/pawsey/cuda-hpc-python/2021.09
$ module help quay.io/pawsey/cuda-hpc-python/2021.09
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cuda-hpc-python-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cuda-hpc-python-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cuda-hpc-python-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cuda-hpc-python-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cuda-hpc-python-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cuda-hpc-python-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### python
       
```bash
$ singularity exec <container> /usr/local/bin/python
$ podman run --it --rm --entrypoint /usr/local/bin/python   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3
       
```bash
$ singularity exec <container> /usr/local/bin/python3
$ podman run --it --rm --entrypoint /usr/local/bin/python3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3   -v ${PWD} -w ${PWD} <container> -c " $@"
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