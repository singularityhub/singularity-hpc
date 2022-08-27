---
layout: container
name:  "nvcr.io/nvidia/tensorflow"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/nvcr.io/nvidia/tensorflow/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/nvcr.io/nvidia/tensorflow/container.yaml"
updated_at: "2022-08-27 01:37:15.175574"
latest: "22.06-tf2-py3"
container_url: "https://ngc.nvidia.com/catalog/containers/nvidia:tensorflow/tags"

versions:
 - "21.02-tf1-py3"
 - "21.03-tf1-py3"
 - "21.04-tf1-py3"
 - "21.05-tf1-py3"
 - "21.06-tf1-py3"
 - "21.08-tf1-py3"
 - "21.10-tf1-py3"
 - "21.11-tf1-py3"
 - "21.12-tf1-py3"
 - "22.03-tf2-py3"
 - "22.02-tf2-py3"
 - "22.01-tf2-py3"
 - "21.12-tf2-py3"
 - "21.11-tf2-py3"
 - "22.04-tf2-py3"
 - "22.05-tf2-py3"
 - "22.06-tf2-py3"
description: "TensorFlow is an open-source software library for high-performance numerical computation. Its flexible architecture allows easy deployment of computation across a variety of platforms (CPUs, GPUs, TPUs), and from desktops to clusters of servers to mobile and edge devices."
config: {"docker": "nvcr.io/nvidia/tensorflow", "url": "https://ngc.nvidia.com/catalog/containers/nvidia:tensorflow/tags", "maintainer": "@vsoch", "description": "TensorFlow is an open-source software library for high-performance numerical computation. Its flexible architecture allows easy deployment of computation across a variety of platforms (CPUs, GPUs, TPUs), and from desktops to clusters of servers to mobile and edge devices.", "latest": {"22.06-tf2-py3": "sha256:ea76aabaa17ee0e308a443fa1e7666f98350865f266b02610a60791bd0feeb40"}, "tags": {"21.02-tf1-py3": "sha256:74f3e5f4a60a312df811ee5104baa189d158697953a91e7768f777895bb1d438", "21.03-tf1-py3": "sha256:addbbdccb193849d58083154458318b2aa9b7945d9975284291b08b4336415e1", "21.04-tf1-py3": "sha256:fb948e24013e079fbba954dc0ce025d3648d8b12d343cd07d24e7ca14b66ba5b", "21.05-tf1-py3": "sha256:a6a89e9ac5db5e67434785268b52df2a06df2fb437eed2abaf54df06db5e4f78", "21.06-tf1-py3": "sha256:e7248bb1c64f9d9bba0eae2906f7dc64efc8bd6b775915268a8b8e215f5a5850", "21.08-tf1-py3": "sha256:63d4ee297a200b7e3f28acad2dc7ce91b48ca2388d0aaa6c9996a6676b7c8fac", "21.10-tf1-py3": "sha256:d0735da72fff9c1e789c1cbc10a0ff7df7b08271236c667486f9cc7699da6e3d", "21.11-tf1-py3": "sha256:91efc28e1f304f8989c344a8cf7e4e06ac85d1ea1388d57480d3dabae60bf365", "21.12-tf1-py3": "sha256:315f7b44486b59d642ab6b52d626aa66ec432f8a4bf7eb793acc4e47af6ab165", "22.03-tf2-py3": "sha256:bafc7d96a17aab5bbc6f6aed0d2c44d2bcff05148fc9680741a0f2d4fb750420", "22.02-tf2-py3": "sha256:d1e40b32306d3f517da1c249972254f193d6a860e2383f393acbe719e74c13fb", "22.01-tf2-py3": "sha256:64274c3f12592c37ee57f839981d18c046be399a41fd234caedacd9d803d15f4", "21.12-tf2-py3": "sha256:afb70040bc7982a7b23219a6a71298c76904e1a815ea70203f1b52d8a8dad65b", "21.11-tf2-py3": "sha256:03e12291e8a03aaf70d0cba6ae994b9738b79f4b939bfe4d416ea3e53027bbad", "22.04-tf2-py3": "sha256:c7450cdb0fb3737411f415b89e1866547317b757db8db85c30a0fd58becc2ef0", "22.05-tf2-py3": "sha256:f57af74cd8bb2145f649fb440dc6231986f1c6fd2ccedaeaee8995b5f3be2389", "22.06-tf2-py3": "sha256:ea76aabaa17ee0e308a443fa1e7666f98350865f266b02610a60791bd0feeb40"}, "filter": ["21*"], "features": {"gpu": true}}
---

This module is a singularity container wrapper for nvcr.io/nvidia/tensorflow.
TensorFlow is an open-source software library for high-performance numerical computation. Its flexible architecture allows easy deployment of computation across a variety of platforms (CPUs, GPUs, TPUs), and from desktops to clusters of servers to mobile and edge devices.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install nvcr.io/nvidia/tensorflow
```

Or a specific version:

```bash
$ shpc install nvcr.io/nvidia/tensorflow:21.02-tf1-py3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load nvcr.io/nvidia/tensorflow/21.02-tf1-py3
$ module help nvcr.io/nvidia/tensorflow/21.02-tf1-py3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### tensorflow-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### tensorflow-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### tensorflow-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### tensorflow-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### tensorflow-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### tensorflow-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### tensorflow

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