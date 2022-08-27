---
layout: container
name:  "nvcr.io/nvidia/digits"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/nvcr.io/nvidia/digits/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/nvcr.io/nvidia/digits/container.yaml"
updated_at: "2022-08-27 01:37:12.531863"
latest: "21.09-tensorflow-py3"
container_url: "https://ngc.nvidia.com/catalog/containers/nvidia:digits/tags"
aliases:
 - "python"
versions:
 - "21.02-tensorflow-py3"
 - "21.03-tensorflow-py3"
 - "21.04-tensorflow-py3"
 - "21.05-tensorflow-py3"
 - "21.06-tensorflow-py3"
 - "21.08-tensorflow-py3"
 - "21.09-tensorflow-py3"
 - "21.07-tensorflow-py3"
description: "The NVIDIA Deep Learning GPU Training System (DIGITS) puts the power of deep learning into the hands of engineers and data scientists."
config: {"docker": "nvcr.io/nvidia/digits", "url": "https://ngc.nvidia.com/catalog/containers/nvidia:digits/tags", "maintainer": "@vsoch", "description": "The NVIDIA Deep Learning GPU Training System (DIGITS) puts the power of deep learning into the hands of engineers and data scientists.", "latest": {"21.09-tensorflow-py3": "sha256:2cd85ac9a8373804ae5242aeb36d2a438aabe2d349d07851b02ab0bb2309574d"}, "tags": {"21.02-tensorflow-py3": "sha256:f5973e9b4a4424b4d394d7c42cf0aee5259dbdcce58d8a9815fae081ce99020f", "21.03-tensorflow-py3": "sha256:ad2aa71d8650ea403437f86fc9a33760af8a20d980f64d660e8ef649e0d9296d", "21.04-tensorflow-py3": "sha256:b72344b124b07742f5a908566c5f1905edc3d58956e446db925cf153facdf9f9", "21.05-tensorflow-py3": "sha256:92132672c1d985ebdfad13089cb1ead353e96df960788eed4b6eafd932613546", "21.06-tensorflow-py3": "sha256:fbe881eeb906edb58e67f7220617da648af74cac190fe4c14bb7646209eb5b89", "21.08-tensorflow-py3": "sha256:0e6009fb379ef17aef8f5cacb87f5a251c7762e0042acc6073533bad34625989", "21.09-tensorflow-py3": "sha256:2cd85ac9a8373804ae5242aeb36d2a438aabe2d349d07851b02ab0bb2309574d", "21.07-tensorflow-py3": "sha256:84a670644b33b6e1bfe19f67779517110ec6cb5a6082fb3ed974c79cc5a01389"}, "aliases": {"python": "/usr/bin/python"}, "features": {"gpu": true}}
---

This module is a singularity container wrapper for nvcr.io/nvidia/digits.
The NVIDIA Deep Learning GPU Training System (DIGITS) puts the power of deep learning into the hands of engineers and data scientists.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install nvcr.io/nvidia/digits
```

Or a specific version:

```bash
$ shpc install nvcr.io/nvidia/digits:21.02-tensorflow-py3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load nvcr.io/nvidia/digits/21.02-tensorflow-py3
$ module help nvcr.io/nvidia/digits/21.02-tensorflow-py3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### digits-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### digits-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### digits-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### digits-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### digits-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### digits-inspect-deffile:

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