---
layout: container
name:  "ghcr.io/autamus/cfitsio"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/cfitsio/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/ghcr.io/autamus/cfitsio/container.yaml"
updated_at: "2022-08-27 02:52:05.063544"
latest: "4.0.0"
container_url: "https://github.com/orgs/autamus/packages/container/package/cfitsio"

versions:
 - "3.49"
 - "4.0.0"
 - "latest"
description: "CFITSIO is a library of C and Fortran subroutines for reading and writing data files in FITS (Flexible Image Transport System) data format."
config: {"docker": "ghcr.io/autamus/cfitsio", "url": "https://github.com/orgs/autamus/packages/container/package/cfitsio", "maintainer": "@vsoch", "description": "CFITSIO is a library of C and Fortran subroutines for reading and writing data files in FITS (Flexible Image Transport System) data format.", "latest": {"4.0.0": "sha256:30056262bf72403df091b0f112816ffc84e3e664fb9c9866272bc55f7b697e42"}, "tags": {"3.49": "sha256:eca430653a52ec08feb642747d4e3f9d70f9d585f0bf9eea092673d81140bacc", "4.0.0": "sha256:30056262bf72403df091b0f112816ffc84e3e664fb9c9866272bc55f7b697e42", "latest": "sha256:30056262bf72403df091b0f112816ffc84e3e664fb9c9866272bc55f7b697e42"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/cfitsio.
CFITSIO is a library of C and Fortran subroutines for reading and writing data files in FITS (Flexible Image Transport System) data format.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/cfitsio
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/cfitsio:3.49
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/cfitsio/3.49
$ module help ghcr.io/autamus/cfitsio/3.49
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cfitsio-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cfitsio-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cfitsio-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cfitsio-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cfitsio-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cfitsio-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### cfitsio

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