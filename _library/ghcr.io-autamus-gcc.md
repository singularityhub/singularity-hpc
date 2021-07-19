---
layout: container
name:  "ghcr.io/autamus/gcc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/gcc/container.yaml"
updated_at: "2021-07-19 23:53:02.832149"
container_url: "https://github.com/orgs/autamus/packages/container/package/gcc"
aliases:
 - "c++"

 - "cpp"

 - "g++"

 - "gcc"

 - "gcc-ar"

 - "gcc-nm"

 - "gcc-ranlib"

 - "gcov"

 - "gcov-dump"

 - "gcov-tool"

 - "gfortran"

 - "zstd"

versions:
 - "10.3.0"
 - "11.1.0"
 - "latest"
description: "The GNU Compiler Collection"
---

This module is a singularity container wrapper for ghcr.io/autamus/gcc.
The GNU Compiler Collection
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install ghcr.io/autamus/gcc
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/gcc:10.3.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/gcc/10.3.0
$ module help ghcr.io/autamus/gcc/10.3.0
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


#### c++
       
```bash
$ singularity exec <container> /opt/view/bin/c++
$ podman run --it --rm --entrypoint /opt/view/bin/c++   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/c++   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cpp
       
```bash
$ singularity exec <container> /opt/view/bin/cpp
$ podman run --it --rm --entrypoint /opt/view/bin/cpp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/cpp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### g++
       
```bash
$ singularity exec <container> /opt/view/bin/g++
$ podman run --it --rm --entrypoint /opt/view/bin/g++   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/g++   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gcc
       
```bash
$ singularity exec <container> /opt/view/bin/gcc
$ podman run --it --rm --entrypoint /opt/view/bin/gcc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/gcc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gcc-ar
       
```bash
$ singularity exec <container> /opt/view/bin/gcc-ar
$ podman run --it --rm --entrypoint /opt/view/bin/gcc-ar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/gcc-ar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gcc-nm
       
```bash
$ singularity exec <container> /opt/view/bin/gcc-nm
$ podman run --it --rm --entrypoint /opt/view/bin/gcc-nm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/gcc-nm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gcc-ranlib
       
```bash
$ singularity exec <container> /opt/view/bin/gcc-ranlib
$ podman run --it --rm --entrypoint /opt/view/bin/gcc-ranlib   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/gcc-ranlib   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gcov
       
```bash
$ singularity exec <container> /opt/view/bin/gcov
$ podman run --it --rm --entrypoint /opt/view/bin/gcov   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/gcov   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gcov-dump
       
```bash
$ singularity exec <container> /opt/view/bin/gcov-dump
$ podman run --it --rm --entrypoint /opt/view/bin/gcov-dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/gcov-dump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gcov-tool
       
```bash
$ singularity exec <container> /opt/view/bin/gcov-tool
$ podman run --it --rm --entrypoint /opt/view/bin/gcov-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/gcov-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gfortran
       
```bash
$ singularity exec <container> /opt/view/bin/gfortran
$ podman run --it --rm --entrypoint /opt/view/bin/gfortran   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/gfortran   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zstd
       
```bash
$ singularity exec <container> /opt/view/bin/zstd
$ podman run --it --rm --entrypoint /opt/view/bin/zstd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/zstd   -v ${PWD} -w ${PWD} <container> -c " $@"
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