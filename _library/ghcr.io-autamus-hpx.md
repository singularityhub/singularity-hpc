---
layout: container
name:  "ghcr.io/autamus/hpx"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/hpx/container.yaml"
updated_at: "2022-03-09 16:29:15.072360"
container_url: "https://github.com/orgs/autamus/packages/container/package/hpx"
aliases:
 - "hpxcxx"

 - "hpxrun.py"

versions:
 - "1.6.0"
 - "1.7.0"
 - "1.7.1"
description: "C++ runtime system for parallel and distributed applications."
---

This module is a singularity container wrapper for ghcr.io/autamus/hpx.
C++ runtime system for parallel and distributed applications.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/hpx
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/hpx:1.6.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/hpx/1.6.0
$ module help ghcr.io/autamus/hpx/1.6.0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### hpx-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### hpx-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### hpx-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### hpx-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### hpx-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### hpx-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### hpxcxx
       
```bash
$ singularity exec <container> /opt/view/bin/hpxcxx
$ podman run --it --rm --entrypoint /opt/view/bin/hpxcxx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/hpxcxx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hpxrun.py
       
```bash
$ singularity exec <container> /opt/view/bin/hpxrun.py
$ podman run --it --rm --entrypoint /opt/view/bin/hpxrun.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/hpxrun.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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