---
layout: container
name:  "ghcr.io/autamus/julia"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/julia/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/ghcr.io/autamus/julia/container.yaml"
updated_at: "2022-08-27 01:36:09.346681"
latest: "1.7.0.rc.2"
container_url: "https://github.com/orgs/autamus/packages/container/package/julia"
aliases:
 - "julia"
versions:
 - "1.6.0"
 - "1.6.1"
 - "1.6.2"
 - "1.6.3"
 - "1.7.0.rc.2"
 - "latest"
description: "Julia is a high-level, high-performance, dynamic programming language."
config: {"docker": "ghcr.io/autamus/julia", "url": "https://github.com/orgs/autamus/packages/container/package/julia", "maintainer": "@vsoch", "description": "Julia is a high-level, high-performance, dynamic programming language.", "latest": {"1.7.0.rc.2": "sha256:8deb90f4aaa4e779d80e0c7d04c99b9364c2f4545e4b9ca197d25dc58ccf4cc3"}, "tags": {"1.6.0": "sha256:e898f6e5faced775bca53c9e8cd28f56f1b6d42a719d06678a7012ab9f21f32e", "1.6.1": "sha256:527b37ce591be6b704efcb8019f16dbb0163f12433d0af8258153c892b33998d", "1.6.2": "sha256:34ef0a0fbfdca83bb05bf05faddb180d8dd82d7c5ab19fc405b478003d58d9de", "1.6.3": "sha256:f84fc45e71f4995278758398961231c088bfbbcd92d698a1d0ccb16de41f80f5", "1.7.0.rc.2": "sha256:8deb90f4aaa4e779d80e0c7d04c99b9364c2f4545e4b9ca197d25dc58ccf4cc3", "latest": "sha256:8deb90f4aaa4e779d80e0c7d04c99b9364c2f4545e4b9ca197d25dc58ccf4cc3"}, "aliases": {"julia": "/opt/view/bin/julia"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/julia.
Julia is a high-level, high-performance, dynamic programming language.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/julia
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/julia:1.6.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/julia/1.6.0
$ module help ghcr.io/autamus/julia/1.6.0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### julia-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### julia-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### julia-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### julia-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### julia-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### julia-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### julia
       
```bash
$ singularity exec <container> /opt/view/bin/julia
$ podman run --it --rm --entrypoint /opt/view/bin/julia   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/julia   -v ${PWD} -w ${PWD} <container> -c " $@"
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