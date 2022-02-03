---
layout: container
name:  "ghcr.io/autamus/libpng"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/libpng/container.yaml"
updated_at: "2022-02-03 22:45:34.521722"
container_url: "https://github.com/orgs/autamus/packages/container/package/libpng"
aliases:
 - "libpng-config"

 - "libpng16-config"

 - "png-fix-itxt"

 - "pngfix"

versions:
 - "1.6.37"
 - "latest"
description: "libpng is the official PNG reference library."
---

This module is a singularity container wrapper for ghcr.io/autamus/libpng.
libpng is the official PNG reference library.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install ghcr.io/autamus/libpng
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/libpng:1.6.37
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/libpng/1.6.37
$ module help ghcr.io/autamus/libpng/1.6.37
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


#### libpng-config
       
```bash
$ singularity exec <container> /opt/view/bin/libpng-config
$ podman run --it --rm --entrypoint /opt/view/bin/libpng-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/libpng-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### libpng16-config
       
```bash
$ singularity exec <container> /opt/view/bin/libpng16-config
$ podman run --it --rm --entrypoint /opt/view/bin/libpng16-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/libpng16-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### png-fix-itxt
       
```bash
$ singularity exec <container> /opt/view/bin/png-fix-itxt
$ podman run --it --rm --entrypoint /opt/view/bin/png-fix-itxt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/png-fix-itxt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pngfix
       
```bash
$ singularity exec <container> /opt/view/bin/pngfix
$ podman run --it --rm --entrypoint /opt/view/bin/pngfix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/pngfix   -v ${PWD} -w ${PWD} <container> -c " $@"
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