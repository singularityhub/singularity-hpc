---
layout: container
name:  "quay.io/biocontainers/salmon"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/salmon/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/salmon/container.yaml"
updated_at: "2022-08-27 02:54:23.939830"
latest: "1.9.0--h7e5ed60_0"
container_url: "https://quay.io/repository/biocontainers/salmon"
aliases:
 - "salmon"
versions:
 - "1.4.0--h84f40af_1"
 - "1.5.2--h84f40af_0"
 - "1.6.0--h84f40af_0"
 - "1.7.0--h84f40af_0"
 - "1.8.0--h7e5ed60_1"
 - "1.7.0--h10bb6b4_1"
 - "1.9.0--h7e5ed60_0"
description: "Salmon is a wicked-fast program to produce a highly-accurate, transcript-level quantification estimates from RNA-seq data."
config: {"docker": "quay.io/biocontainers/salmon", "url": "https://quay.io/repository/biocontainers/salmon", "maintainer": "@marcodelapierre", "description": "Salmon is a wicked-fast program to produce a highly-accurate, transcript-level quantification estimates from RNA-seq data.", "latest": {"1.9.0--h7e5ed60_0": "sha256:97bd11c4d683edf3cf04b7b877e6c0c2f4e0c0fd0e81d64f8ecff7c83565621c"}, "tags": {"1.4.0--h84f40af_1": "sha256:bad1f9d2ffeac08bf7087d706634f7724f978c4ba6f9c26eddca5aad004c8e4c", "1.5.2--h84f40af_0": "sha256:4ae09a47788f08317bd2f758ac4c8804c9e87d88caf500c449e18ac4794d0332", "1.6.0--h84f40af_0": "sha256:e1da9c3e2abe7c1cd36062b9fa13c336e69ee3dd9e1f285fb3736fed4bdf7b48", "1.7.0--h84f40af_0": "sha256:64d58a2c873b4bc9a68781653b58ed2ebfc1e20195da9308657f2fbf9f694ae1", "1.8.0--h7e5ed60_1": "sha256:a9cccd97c393306641308f208c4c3ed1f20aade9aab44361da315ae286a01cee", "1.7.0--h10bb6b4_1": "sha256:4b42a8bf872393e5207f101c2650dbd6a45f7bfde58ae68211e75e0aa668db6e", "1.9.0--h7e5ed60_0": "sha256:97bd11c4d683edf3cf04b7b877e6c0c2f4e0c0fd0e81d64f8ecff7c83565621c"}, "aliases": {"salmon": "/usr/local/bin/salmon"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/salmon.
Salmon is a wicked-fast program to produce a highly-accurate, transcript-level quantification estimates from RNA-seq data.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/salmon
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/salmon:1.4.0--h84f40af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/salmon/1.4.0--h84f40af_1
$ module help quay.io/biocontainers/salmon/1.4.0--h84f40af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### salmon-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### salmon-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### salmon-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### salmon-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### salmon-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### salmon-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### salmon
       
```bash
$ singularity exec <container> /usr/local/bin/salmon
$ podman run --it --rm --entrypoint /usr/local/bin/salmon   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/salmon   -v ${PWD} -w ${PWD} <container> -c " $@"
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