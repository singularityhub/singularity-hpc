---
layout: container
name:  "ghcr.io/autamus/openmpi"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/openmpi/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/ghcr.io/autamus/openmpi/container.yaml"
updated_at: "2022-08-27 01:36:26.675372"
latest: "4.1.2"
container_url: "https://github.com/orgs/autamus/packages/container/package/openmpi"
aliases:
 - "mpiCC"
 - "mpic++"
 - "mpicc"
 - "mpicxx"
 - "mpiexec"
 - "mpif77"
 - "mpif90"
 - "mpifort"
 - "mpirun"
 - "ompi-clean"
 - "ompi-server"
 - "ompi_info"
versions:
 - "4.1.1"
 - "4.1.2"
description: "An open source Message Passing Interface implementation."
config: {"docker": "ghcr.io/autamus/openmpi", "url": "https://github.com/orgs/autamus/packages/container/package/openmpi", "maintainer": "@vsoch", "description": "An open source Message Passing Interface implementation.", "latest": {"4.1.2": "sha256:bdd2678d73198138b3dbda082ea658cbc78fd6928497a8a8fb7cd54c3130ebd4"}, "tags": {"4.1.1": "sha256:571e607db699301e56d064f11e8c4d9f33bced922da04e018d679bf57649b7f4", "4.1.2": "sha256:bdd2678d73198138b3dbda082ea658cbc78fd6928497a8a8fb7cd54c3130ebd4"}, "aliases": {"mpiCC": "/opt/view/bin/mpiCC", "mpic++": "/opt/view/bin/mpic++", "mpicc": "/opt/view/bin/mpicc", "mpicxx": "/opt/view/bin/mpicxx", "mpiexec": "/opt/view/bin/mpiexec", "mpif77": "/opt/view/bin/mpif77", "mpif90": "/opt/view/bin/mpif90", "mpifort": "/opt/view/bin/mpifort", "mpirun": "/opt/view/bin/mpirun", "ompi-clean": "/opt/view/bin/ompi-clean", "ompi-server": "/opt/view/bin/ompi-server", "ompi_info": "/opt/view/bin/ompi_info"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/openmpi.
An open source Message Passing Interface implementation.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/openmpi
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/openmpi:4.1.1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/openmpi/4.1.1
$ module help ghcr.io/autamus/openmpi/4.1.1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### openmpi-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### openmpi-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### openmpi-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### openmpi-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### openmpi-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### openmpi-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### mpiCC
       
```bash
$ singularity exec <container> /opt/view/bin/mpiCC
$ podman run --it --rm --entrypoint /opt/view/bin/mpiCC   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/mpiCC   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mpic++
       
```bash
$ singularity exec <container> /opt/view/bin/mpic++
$ podman run --it --rm --entrypoint /opt/view/bin/mpic++   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/mpic++   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mpicc
       
```bash
$ singularity exec <container> /opt/view/bin/mpicc
$ podman run --it --rm --entrypoint /opt/view/bin/mpicc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/mpicc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mpicxx
       
```bash
$ singularity exec <container> /opt/view/bin/mpicxx
$ podman run --it --rm --entrypoint /opt/view/bin/mpicxx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/mpicxx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mpiexec
       
```bash
$ singularity exec <container> /opt/view/bin/mpiexec
$ podman run --it --rm --entrypoint /opt/view/bin/mpiexec   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/mpiexec   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mpif77
       
```bash
$ singularity exec <container> /opt/view/bin/mpif77
$ podman run --it --rm --entrypoint /opt/view/bin/mpif77   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/mpif77   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mpif90
       
```bash
$ singularity exec <container> /opt/view/bin/mpif90
$ podman run --it --rm --entrypoint /opt/view/bin/mpif90   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/mpif90   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mpifort
       
```bash
$ singularity exec <container> /opt/view/bin/mpifort
$ podman run --it --rm --entrypoint /opt/view/bin/mpifort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/mpifort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mpirun
       
```bash
$ singularity exec <container> /opt/view/bin/mpirun
$ podman run --it --rm --entrypoint /opt/view/bin/mpirun   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/mpirun   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ompi-clean
       
```bash
$ singularity exec <container> /opt/view/bin/ompi-clean
$ podman run --it --rm --entrypoint /opt/view/bin/ompi-clean   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/ompi-clean   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ompi-server
       
```bash
$ singularity exec <container> /opt/view/bin/ompi-server
$ podman run --it --rm --entrypoint /opt/view/bin/ompi-server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/ompi-server   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ompi_info
       
```bash
$ singularity exec <container> /opt/view/bin/ompi_info
$ podman run --it --rm --entrypoint /opt/view/bin/ompi_info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/ompi_info   -v ${PWD} -w ${PWD} <container> -c " $@"
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