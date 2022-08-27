---
layout: container
name:  "nvcr.io/hpc/gromacs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/nvcr.io/hpc/gromacs/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/nvcr.io/hpc/gromacs/container.yaml"
updated_at: "2022-08-27 01:37:09.369576"
latest: "2022.1"
container_url: "https://ngc.nvidia.com/catalog/containers/hpc:gromacs/tags"
aliases:
 - "python"
versions:
 - "2020.2"
 - "2020.2-arm64"
 - "2021"
 - "2021.3"
 - "2020.2-x86_64"
 - "2022.1"
description: "GROMACS is a popular molecular dynamics application used to simulate proteins and lipids."
config: {"docker": "nvcr.io/hpc/gromacs", "url": "https://ngc.nvidia.com/catalog/containers/hpc:gromacs/tags", "maintainer": "@vsoch", "description": "GROMACS is a popular molecular dynamics application used to simulate proteins and lipids.", "latest": {"2022.1": "sha256:1a300919fef314b2b42b4f252eb92052ccb912eaed066f1cd3f1415038a6cbce"}, "tags": {"2020.2": "sha256:2d51288e7b0cacc3c33fdde07a2b81a803c243411ccb805e03179fa2554b8daa", "2020.2-arm64": "sha256:2b8c453a5fc709f19e48c76d2b8403d1a5248eef2f05c1429df23b77e1c06b33", "2021": "sha256:aa095dcdb175e10132a5862204bf91e6f374f72ba9f2360d9ff5c45ae67785fd", "2021.3": "sha256:bfa887d5bebc48fe551873a240ecd0a2bb87f7c3d67f0178233304b5b779cedc", "2020.2-x86_64": "sha256:b76a847b8f85bab0a5605a97b774583650132d8f413c0d878ffbdc381a04472a", "2022.1": "sha256:1a300919fef314b2b42b4f252eb92052ccb912eaed066f1cd3f1415038a6cbce"}, "filter": ["^((?!arm).)*$"], "features": {"gpu": true}, "aliases": {"python": "/usr/bin/python"}}
---

This module is a singularity container wrapper for nvcr.io/hpc/gromacs.
GROMACS is a popular molecular dynamics application used to simulate proteins and lipids.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install nvcr.io/hpc/gromacs
```

Or a specific version:

```bash
$ shpc install nvcr.io/hpc/gromacs:2020.2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load nvcr.io/hpc/gromacs/2020.2
$ module help nvcr.io/hpc/gromacs/2020.2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gromacs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gromacs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gromacs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gromacs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gromacs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gromacs-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### python
       
```bash
$ singularity exec <container> /usr/bin/python
$ podman run --it --rm --entrypoint /usr/bin/python   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/python   -v ${PWD} -w ${PWD} <container> -c " $@"
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