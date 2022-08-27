---
layout: container
name:  "ghcr.io/autamus/cloc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/cloc/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/ghcr.io/autamus/cloc/container.yaml"
updated_at: "2022-08-27 01:35:43.048231"
latest: "1.90"
container_url: "https://github.com/orgs/autamus/packages/container/package/cloc"
aliases:
 - "cloc"
versions:
 - "1.88"
 - "1.90"
 - "latest"
description: "cloc is a command line program that takes file, directory, and/or archive names as inputs."
config: {"docker": "ghcr.io/autamus/cloc", "url": "https://github.com/orgs/autamus/packages/container/package/cloc", "maintainer": "@vsoch", "description": "cloc is a command line program that takes file, directory, and/or archive names as inputs.", "latest": {"1.90": "sha256:8e1450774c0513eb1d7b4b71cd1ccca744d004fae2142f078ba4f39a148be300"}, "tags": {"1.88": "sha256:d83cabface35c70df9484dff3f606a10f13432747a7570e238525e3722061c31", "1.90": "sha256:8e1450774c0513eb1d7b4b71cd1ccca744d004fae2142f078ba4f39a148be300", "latest": "sha256:8e1450774c0513eb1d7b4b71cd1ccca744d004fae2142f078ba4f39a148be300"}, "aliases": {"cloc": "/opt/view/bin/cloc"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/cloc.
cloc is a command line program that takes file, directory, and/or archive names as inputs.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/cloc
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/cloc:1.88
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/cloc/1.88
$ module help ghcr.io/autamus/cloc/1.88
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cloc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cloc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cloc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cloc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cloc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cloc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cloc
       
```bash
$ singularity exec <container> /opt/view/bin/cloc
$ podman run --it --rm --entrypoint /opt/view/bin/cloc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/cloc   -v ${PWD} -w ${PWD} <container> -c " $@"
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