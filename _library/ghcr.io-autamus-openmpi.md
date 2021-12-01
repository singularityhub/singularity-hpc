---
layout: container
name:  "ghcr.io/autamus/openmpi"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/openmpi/container.yaml"
updated_at: "2021-12-01 18:37:30.724032"
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
description: "An open source Message Passing Interface implementation."
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