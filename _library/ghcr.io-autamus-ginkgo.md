---
layout: container
name:  "ghcr.io/autamus/ginkgo"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/ginkgo/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/ghcr.io/autamus/ginkgo/container.yaml"
updated_at: "2022-08-27 02:52:24.492071"
latest: "1.4.0"
container_url: "https://github.com/orgs/autamus/packages/container/package/ginkgo"

versions:
 - "1.3.0"
 - "1.4.0"
 - "latest"
description: "High-performance linear algebra library for manycore systems, with a focus on sparse solution of linear systems."
config: {"docker": "ghcr.io/autamus/ginkgo", "url": "https://github.com/orgs/autamus/packages/container/package/ginkgo", "maintainer": "@vsoch", "description": "High-performance linear algebra library for manycore systems, with a focus on sparse solution of linear systems.", "latest": {"1.4.0": "sha256:fed53880b12e60a5ce006c0e8499583f6dab449cf05c27c8932299a63a51e845"}, "tags": {"1.3.0": "sha256:39a4a6df46bf92043cc4915aa5e379710897af41c46e2c672a4431b8f80a80b4", "1.4.0": "sha256:fed53880b12e60a5ce006c0e8499583f6dab449cf05c27c8932299a63a51e845", "latest": "sha256:fed53880b12e60a5ce006c0e8499583f6dab449cf05c27c8932299a63a51e845"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/ginkgo.
High-performance linear algebra library for manycore systems, with a focus on sparse solution of linear systems.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/ginkgo
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/ginkgo:1.3.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/ginkgo/1.3.0
$ module help ghcr.io/autamus/ginkgo/1.3.0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ginkgo-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ginkgo-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ginkgo-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ginkgo-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ginkgo-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ginkgo-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### ginkgo

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