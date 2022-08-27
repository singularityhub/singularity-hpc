---
layout: container
name:  "ghcr.io/autamus/zlib"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/zlib/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/ghcr.io/autamus/zlib/container.yaml"
updated_at: "2022-08-27 01:36:59.843579"
latest: "1.2.11"
container_url: "https://github.com/orgs/autamus/packages/container/package/zlib"

versions:
 - "1.2.11"
 - "latest"
 - "1.2.12"
description: "zlib is a software library used for data compression. zlib was written by Jean-loup Gailly and Mark Adler and is an abstraction of the DEFLATE compression algorithm used in their gzip file compression program."
config: {"docker": "ghcr.io/autamus/zlib", "url": "https://github.com/orgs/autamus/packages/container/package/zlib", "maintainer": "@vsoch", "description": "zlib is a software library used for data compression. zlib was written by Jean-loup Gailly and Mark Adler and is an abstraction of the DEFLATE compression algorithm used in their gzip file compression program.", "latest": {"1.2.11": "sha256:cf12c3a0b8a366a6d83e9a8656adf5f17fd1d4fb92243e86c385f1507a5388d9"}, "tags": {"1.2.11": "sha256:cf12c3a0b8a366a6d83e9a8656adf5f17fd1d4fb92243e86c385f1507a5388d9", "latest": "sha256:a57e1ffe54a233fc14ec4fa91fd70b3dc10ccbe386ee2e231c1cc4cdb9a7705f", "1.2.12": "sha256:a57e1ffe54a233fc14ec4fa91fd70b3dc10ccbe386ee2e231c1cc4cdb9a7705f"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/zlib.
zlib is a software library used for data compression. zlib was written by Jean-loup Gailly and Mark Adler and is an abstraction of the DEFLATE compression algorithm used in their gzip file compression program.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/zlib
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/zlib:1.2.11
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/zlib/1.2.11
$ module help ghcr.io/autamus/zlib/1.2.11
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### zlib-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### zlib-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### zlib-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### zlib-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### zlib-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### zlib-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### zlib

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