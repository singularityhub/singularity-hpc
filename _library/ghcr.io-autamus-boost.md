---
layout: container
name:  "ghcr.io/autamus/boost"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/boost/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/ghcr.io/autamus/boost/container.yaml"
updated_at: "2022-08-27 02:51:58.985308"
latest: "1.78.0"
container_url: "https://github.com/orgs/autamus/packages/container/package/boost"

versions:
 - "1.75.0"
 - "1.77.0"
 - "1.78.0"
 - "latest"
 - "1.76.0"
description: "The Boost project provides free peer-reviewed portable C++ source libraries."
config: {"docker": "ghcr.io/autamus/boost", "url": "https://github.com/orgs/autamus/packages/container/package/boost", "maintainer": "@vsoch", "description": "The Boost project provides free peer-reviewed portable C++ source libraries.", "latest": {"1.78.0": "sha256:14823770b03cd5289b491afdfc3fb9f64e3730f41abf770bc6055a4232b4081b"}, "tags": {"1.75.0": "sha256:a6d7914225fde46cdab70d01619de67a0162a9a3c7a2361563aff66dbd05c1e2", "1.77.0": "sha256:70ab543402b4f24532639460dd6db289762b0f48c847fbde9cbf148d2aeafd2e", "1.78.0": "sha256:14823770b03cd5289b491afdfc3fb9f64e3730f41abf770bc6055a4232b4081b", "latest": "sha256:14823770b03cd5289b491afdfc3fb9f64e3730f41abf770bc6055a4232b4081b", "1.76.0": "sha256:655fb10e42f73a9ed8ef67e9c2aa53ead1864800bf4488e864709113529c1f5f"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/boost.
The Boost project provides free peer-reviewed portable C++ source libraries.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/boost
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/boost:1.75.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/boost/1.75.0
$ module help ghcr.io/autamus/boost/1.75.0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### boost-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### boost-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### boost-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### boost-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### boost-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### boost-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### boost

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