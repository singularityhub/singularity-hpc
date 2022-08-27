---
layout: container
name:  "ghcr.io/autamus/protobuf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/protobuf/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/ghcr.io/autamus/protobuf/container.yaml"
updated_at: "2022-08-27 02:53:14.710250"
latest: "3.19.1"
container_url: "https://github.com/orgs/autamus/packages/container/package/protobuf"
aliases:
 - "protoc"
 - "protoc-3.15.8.0"
versions:
 - "3.15.8"
 - "3.16.0"
 - "3.17.0"
 - "3.17.2"
 - "3.17.3"
 - "3.19.1"
 - "latest"
 - "3.19.0"
 - "3.18.1"
description: "Protocol Buffers is a method of serializing structured data. It is useful in developing programs to communicate with each other over a network or for storing data."
config: {"docker": "ghcr.io/autamus/protobuf", "url": "https://github.com/orgs/autamus/packages/container/package/protobuf", "maintainer": "@vsoch", "description": "Protocol Buffers is a method of serializing structured data. It is useful in developing programs to communicate with each other over a network or for storing data.", "latest": {"3.19.1": "sha256:bbad046ff3c66a409408450a654286501157655a142290dbf5b7970bbd61d8d4"}, "tags": {"3.15.8": "sha256:f257c20871d7dd135053e650c14a39c4203a1623ac5b9178e70b1ac2052f923f", "3.16.0": "sha256:fc8106e5c6ffa0400f41af5be4f3977c09cf9b511e5863563b61d56c458b8836", "3.17.0": "sha256:6811579bc7127ce010e005c2bb3e57af3e1c7c5ea2190faf1e8fda3f89d3f17c", "3.17.2": "sha256:3cd03dad858afdc7cd91a297c52a66e5eb4ff59f3e7107b693bc3d172e53e228", "3.17.3": "sha256:435965c13c09ca0a55f411f093a5131001ff6005f793eb9f94ffca87daf71409", "3.19.1": "sha256:bbad046ff3c66a409408450a654286501157655a142290dbf5b7970bbd61d8d4", "latest": "sha256:bbad046ff3c66a409408450a654286501157655a142290dbf5b7970bbd61d8d4", "3.19.0": "sha256:ab53e8b3371f85530959fd237a6f402a19b6ae493769e94e02d9c5d1ab028146", "3.18.1": "sha256:0869af2d9f106c0f28b9ce00f16355ecd986395f72a49d810d814916cf40ee17"}, "aliases": {"protoc": "/opt/view/bin/protoc", "protoc-3.15.8.0": "/opt/view/bin/protoc-3.15.8.0"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/protobuf.
Protocol Buffers is a method of serializing structured data. It is useful in developing programs to communicate with each other over a network or for storing data.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/protobuf
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/protobuf:3.15.8
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/protobuf/3.15.8
$ module help ghcr.io/autamus/protobuf/3.15.8
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### protobuf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### protobuf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### protobuf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### protobuf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### protobuf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### protobuf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### protoc
       
```bash
$ singularity exec <container> /opt/view/bin/protoc
$ podman run --it --rm --entrypoint /opt/view/bin/protoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/protoc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-3.15.8.0
       
```bash
$ singularity exec <container> /opt/view/bin/protoc-3.15.8.0
$ podman run --it --rm --entrypoint /opt/view/bin/protoc-3.15.8.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/protoc-3.15.8.0   -v ${PWD} -w ${PWD} <container> -c " $@"
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