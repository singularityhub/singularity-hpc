---
layout: container
name:  "ghcr.io/autamus/qhull"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/qhull/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/ghcr.io/autamus/qhull/container.yaml"
updated_at: "2022-08-27 02:53:18.046566"
latest: "2020.2"
container_url: "https://github.com/orgs/autamus/packages/container/package/qhull"
aliases:
 - "qconvex"
 - "qdelaunay"
 - "qhalf"
 - "qhull"
 - "qvoronoi"
 - "rbox"
versions:
 - "2020.1"
 - "2020.2"
 - "latest"
description: "Snappy (previously known as Zippy) is a fast data compression and decompression library written in C++ by Google based on ideas from LZ77 and open-sourced in 2011."
config: {"docker": "ghcr.io/autamus/qhull", "url": "https://github.com/orgs/autamus/packages/container/package/qhull", "maintainer": "@vsoch", "description": "Snappy (previously known as Zippy) is a fast data compression and decompression library written in C++ by Google based on ideas from LZ77 and open-sourced in 2011.", "latest": {"2020.2": "sha256:dd6a7a89a88741ecc4856d025fcdc04304375133a7697b1abdd3fea21e8cb9ca"}, "tags": {"2020.1": "sha256:eeeb21a12856b1a4864df42b5399958305f47fb2aa4cae967319648f18fa9d86", "2020.2": "sha256:dd6a7a89a88741ecc4856d025fcdc04304375133a7697b1abdd3fea21e8cb9ca", "latest": "sha256:dd6a7a89a88741ecc4856d025fcdc04304375133a7697b1abdd3fea21e8cb9ca"}, "aliases": {"qconvex": "/opt/view/bin/qconvex", "qdelaunay": "/opt/view/bin/qdelaunay", "qhalf": "/opt/view/bin/qhalf", "qhull": "/opt/view/bin/qhull", "qvoronoi": "/opt/view/bin/qvoronoi", "rbox": "/opt/view/bin/rbox"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/qhull.
Snappy (previously known as Zippy) is a fast data compression and decompression library written in C++ by Google based on ideas from LZ77 and open-sourced in 2011.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/qhull
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/qhull:2020.1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/qhull/2020.1
$ module help ghcr.io/autamus/qhull/2020.1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### qhull-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### qhull-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### qhull-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### qhull-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### qhull-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### qhull-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### qconvex
       
```bash
$ singularity exec <container> /opt/view/bin/qconvex
$ podman run --it --rm --entrypoint /opt/view/bin/qconvex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/qconvex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qdelaunay
       
```bash
$ singularity exec <container> /opt/view/bin/qdelaunay
$ podman run --it --rm --entrypoint /opt/view/bin/qdelaunay   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/qdelaunay   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qhalf
       
```bash
$ singularity exec <container> /opt/view/bin/qhalf
$ podman run --it --rm --entrypoint /opt/view/bin/qhalf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/qhalf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qhull
       
```bash
$ singularity exec <container> /opt/view/bin/qhull
$ podman run --it --rm --entrypoint /opt/view/bin/qhull   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/qhull   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qvoronoi
       
```bash
$ singularity exec <container> /opt/view/bin/qvoronoi
$ podman run --it --rm --entrypoint /opt/view/bin/qvoronoi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/qvoronoi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rbox
       
```bash
$ singularity exec <container> /opt/view/bin/rbox
$ podman run --it --rm --entrypoint /opt/view/bin/rbox   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/rbox   -v ${PWD} -w ${PWD} <container> -c " $@"
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