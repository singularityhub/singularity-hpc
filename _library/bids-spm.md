---
layout: container
name:  "bids/spm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/bids/spm/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/bids/spm/container.yaml"
updated_at: "2022-08-27 01:35:15.690288"
latest: "chrisfilo-patch-1"
container_url: "https://hub.docker.com/r/bids/spm"
aliases:
 - "spm12"
versions:
 - "latest"
 - "v0.0.20"
 - "chrisfilo-patch-1"
 - "enh_various"
description: "The implementation of the theoretical concepts of Statistical Parametric Mapping in a complete analysis package."
config: {"docker": "bids/spm", "url": "https://hub.docker.com/r/bids/spm", "maintainer": "@vsoch", "description": "The implementation of the theoretical concepts of Statistical Parametric Mapping in a complete analysis package.", "latest": {"chrisfilo-patch-1": "sha256:a569a8fc2b9b4b99bea1ea0b61c3772961708ec1890080084ed008fe27846a44"}, "tags": {"latest": "sha256:e72a97f0aad8a4e635d7c1d92f6fbf38ee98cb117eba520e26bbc135c052255c", "v0.0.20": "sha256:e72a97f0aad8a4e635d7c1d92f6fbf38ee98cb117eba520e26bbc135c052255c", "chrisfilo-patch-1": "sha256:a569a8fc2b9b4b99bea1ea0b61c3772961708ec1890080084ed008fe27846a44", "enh_various": "sha256:e477c8a30722eafe8fc61592bf17b64c0afd5f737140589ef55d76ebc47bffd7"}, "aliases": {"spm12": "/opt/spm12/spm12"}, "filter": ["v*"]}
---

This module is a singularity container wrapper for bids/spm.
The implementation of the theoretical concepts of Statistical Parametric Mapping in a complete analysis package.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install bids/spm
```

Or a specific version:

```bash
$ shpc install bids/spm:latest
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load bids/spm/latest
$ module help bids/spm/latest
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### spm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### spm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### spm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### spm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### spm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### spm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### spm12
       
```bash
$ singularity exec <container> /opt/spm12/spm12
$ podman run --it --rm --entrypoint /opt/spm12/spm12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/spm12/spm12   -v ${PWD} -w ${PWD} <container> -c " $@"
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