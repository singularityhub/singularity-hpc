---
layout: container
name:  "ghcr.io/autamus/gromacs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/gromacs/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/ghcr.io/autamus/gromacs/container.yaml"
updated_at: "2022-08-27 02:52:29.836157"
latest: "2021.4"
container_url: "https://github.com/orgs/autamus/packages/container/package/gromacs"

versions:
 - "2021.1"
 - "2021.2"
 - "2021.3"
 - "2021.4"
 - "latest"
 - "2021"
description: "A versatile package to perform molecular dynamics."
config: {"docker": "ghcr.io/autamus/gromacs", "url": "https://github.com/orgs/autamus/packages/container/package/gromacs", "maintainer": "@vsoch", "description": "A versatile package to perform molecular dynamics.", "latest": {"2021.4": "sha256:8588885dd5b1b7a2a77f42bd0e35909cc79c6aa7e7c686a38b1abc4bf8cc2e15"}, "tags": {"2021.1": "sha256:e71e16926ff1ad6b52ea027c9c3523bf254bc0f00be23599f9c8637f8c69dee3", "2021.2": "sha256:38ddac3b17d74a520a46ce07d6fe5935eee9e742adbba0047adb00b93db90ced", "2021.3": "sha256:4596c320fb5d514d6f5b5d0203bd457944e38b5a055642d9bf40b7a262320229", "2021.4": "sha256:8588885dd5b1b7a2a77f42bd0e35909cc79c6aa7e7c686a38b1abc4bf8cc2e15", "latest": "sha256:8588885dd5b1b7a2a77f42bd0e35909cc79c6aa7e7c686a38b1abc4bf8cc2e15", "2021": "sha256:57de89d219419e05e2aa8ecab95d06c72855c811c95090db287e714287ba95c0"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/gromacs.
A versatile package to perform molecular dynamics.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/gromacs
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/gromacs:2021.1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/gromacs/2021.1
$ module help ghcr.io/autamus/gromacs/2021.1
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



#### gromacs

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