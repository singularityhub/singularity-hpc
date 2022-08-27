---
layout: container
name:  "tensorflow/tensorflow"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/tensorflow/tensorflow/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/tensorflow/tensorflow/container.yaml"
updated_at: "2022-08-27 02:54:43.025913"
latest: "2.9.1"
container_url: "https://hub.docker.com/r/tensorflow/tensorflow"
aliases:
 - "python"
versions:
 - "2.5.0-custom-op-gpu-ubuntu16"
 - "2.5.0rc0-gpu-jupyter"
 - "2.6.0"
 - "2.6.0rc0-gpu-jupyter"
 - "2.7.0"
 - "2.7.0rc0"
 - "2.8.0"
 - "2.8.0rc0"
 - "latest-gpu"
 - "2.7.1-gpu"
 - "2.7.1"
 - "2.6.1"
 - "2.5.1"
 - "2.9.0rc1"
 - "2.9.1"
 - "2.8.2"
 - "2.7.3"
description: "An end-to-end open source platform for machine learning."
config: {"docker": "tensorflow/tensorflow", "url": "https://hub.docker.com/r/tensorflow/tensorflow", "maintainer": "@vsoch", "description": "An end-to-end open source platform for machine learning.", "latest": {"2.9.1": "sha256:a5c8c8995f16c63a9dbb59e586bed2e15dbf1024ac08065aaaad053c5173f83e"}, "tags": {"2.5.0-custom-op-gpu-ubuntu16": "sha256:478bee6f0691b48d74adc3fcffe3e9ececf35df5c02860cc51a2c48b1d92c730", "2.5.0rc0-gpu-jupyter": "sha256:9808e04142b09482bb6b3d1738430ae7472a214dd38e086d41e481b376fa9abd", "2.6.0": "sha256:773d5ce09e4ce003db02740c6a372a8a9f43be2bac23544d8f452bfec5347c53", "2.6.0rc0-gpu-jupyter": "sha256:358b5bf90aaf4e56813ff22f2981d86fab7ddc59552b0be6022ae04d6a9f43c3", "2.7.0": "sha256:31e09cf438a41f12c759cc8cc79c6b0fbb0db5abfc3de8169e916c8c9ac38dc5", "2.7.0rc0": "sha256:abbc457c9b7c0725d7d0db885dbb313db3d0ae25733b083900a508efb672af94", "2.8.0": "sha256:7c01f75d58fadc2cd1109d5baac1925ed131e05925d840b1b49363c794d1c4db", "2.8.0rc0": "sha256:11e5d21a786da523d2f7de530c083d5c72a06e02c8895c84595d107c579027a1", "latest-gpu": "sha256:a34c2420739cd5a7b5662449bc21eb32d3d1c98063726ae2bd7db819cc93d72f", "2.7.1-gpu": "sha256:581575fc3a736398f0dff9e950f57f2e6d808296267ac98325451a0b1d101dd0", "2.7.1": "sha256:c9940aa904694a1e5dc4ad3add3c933de45091d5b48e37e94993f19d1d213205", "2.6.1": "sha256:8f343633898c500138979065b62ecb50be4a29f8e7adfadd8f0b168d2642eab1", "2.5.1": "sha256:07d837eced57184599f50944a47e10a23584dae666dc93aa9a762b1111651fa7", "2.9.0rc1": "sha256:2faf5970c62fb58bb6a5281bc5467d82bc6765fe0572cc72ccbca78f50d9e0be", "2.9.1": "sha256:a5c8c8995f16c63a9dbb59e586bed2e15dbf1024ac08065aaaad053c5173f83e", "2.8.2": "sha256:5abc48f6a1ccdf73f052fa60939583f96ead8b3a4f33c0ac5ccf1baf13d12786", "2.7.3": "sha256:be6652df4285e5c1781bccc1dea53a0290e380373ba53f8edb41092a4478dc06"}, "filter": ["2[.]*"], "features": {"gpu": true}, "aliases": {"python": "/usr/local/bin/python"}}
---

This module is a singularity container wrapper for tensorflow/tensorflow.
An end-to-end open source platform for machine learning.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install tensorflow/tensorflow
```

Or a specific version:

```bash
$ shpc install tensorflow/tensorflow:2.5.0-custom-op-gpu-ubuntu16
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load tensorflow/tensorflow/2.5.0-custom-op-gpu-ubuntu16
$ module help tensorflow/tensorflow/2.5.0-custom-op-gpu-ubuntu16
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


#### python
       
```bash
$ singularity exec <container> /usr/local/bin/python
$ podman run --it --rm --entrypoint /usr/local/bin/python   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python   -v ${PWD} -w ${PWD} <container> -c " $@"
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