---
layout: container
name:  "bids/mrtrix3_connectome"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/bids/mrtrix3_connectome/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/bids/mrtrix3_connectome/container.yaml"
updated_at: "2022-08-27 01:35:13.561066"
latest: "chrisfilo-patch-1"
container_url: "https://hub.docker.com/r/bids/mrtrix3_connectome"

versions:
 - "latest"
 - "chrisfilo-patch-1"
 - "0.5.1"
 - "0.4.2"
 - "0.3.0"
 - "0.2.2"
description: "Generation and subsequent group analysis of structural connectomes generated from diffusion MRI data (via the MRtrix3 software package). https://github.com/BIDS-Apps/MRtrix3_connectome"
config: {"docker": "bids/mrtrix3_connectome", "url": "https://hub.docker.com/r/bids/mrtrix3_connectome", "maintainer": "@vsoch", "description": "Generation and subsequent group analysis of structural connectomes generated from diffusion MRI data (via the MRtrix3 software package). https://github.com/BIDS-Apps/MRtrix3_connectome", "latest": {"chrisfilo-patch-1": "sha256:f93055ee1fc5204c69140eef0a71c83d6b672a12c37dd8cf4c34e08d05b21776"}, "tags": {"latest": "sha256:f3e7a20ac3eb1ca674b9896ff3b04a595192f9923f853fcc573e1ca42fa4ebaf", "chrisfilo-patch-1": "sha256:f93055ee1fc5204c69140eef0a71c83d6b672a12c37dd8cf4c34e08d05b21776", "0.5.1": "sha256:f3e7a20ac3eb1ca674b9896ff3b04a595192f9923f853fcc573e1ca42fa4ebaf", "0.4.2": "sha256:3d701b0846038289e18e7571c7072056f1f81daa70ab3159bb48cec9d88f6ecf", "0.3.0": "sha256:64440966249b693da6733d7200d8eebcb4c0f1320f245e826227fb9f1d46a042", "0.2.2": "sha256:a0205a41f34cdc6d8b289fd28f6be46f98c2b7fdf14eaa05b793db28bea5bbdb"}, "filter": ["v*"]}
---

This module is a singularity container wrapper for bids/mrtrix3_connectome.
Generation and subsequent group analysis of structural connectomes generated from diffusion MRI data (via the MRtrix3 software package). https://github.com/BIDS-Apps/MRtrix3_connectome
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install bids/mrtrix3_connectome
```

Or a specific version:

```bash
$ shpc install bids/mrtrix3_connectome:latest
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load bids/mrtrix3_connectome/latest
$ module help bids/mrtrix3_connectome/latest
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mrtrix3_connectome-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mrtrix3_connectome-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mrtrix3_connectome-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mrtrix3_connectome-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mrtrix3_connectome-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mrtrix3_connectome-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### mrtrix3_connectome

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