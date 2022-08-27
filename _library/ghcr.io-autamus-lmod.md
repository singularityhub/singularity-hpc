---
layout: container
name:  "ghcr.io/autamus/lmod"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/lmod/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/ghcr.io/autamus/lmod/container.yaml"
updated_at: "2022-08-27 02:52:48.595670"
latest: "8.6.3"
container_url: "https://github.com/orgs/autamus/packages/container/package/lmod"
aliases:
 - "module"
versions:
 - "8.3"
 - "8.5.6"
 - "8.5.9"
 - "8.5.12"
 - "8.5.13"
 - "8.5.27"
 - "8.6.3"
 - "latest"
description: "The Persistence of Vision Ray Tracer, most commonly acronymed as POV-Ray, is a cross-platform ray-tracing program that generates images from a text-based scene description."
config: {"docker": "ghcr.io/autamus/lmod", "url": "https://github.com/orgs/autamus/packages/container/package/lmod", "maintainer": "@vsoch", "description": "The Persistence of Vision Ray Tracer, most commonly acronymed as POV-Ray, is a cross-platform ray-tracing program that generates images from a text-based scene description.", "latest": {"8.6.3": "sha256:1e89a1881f275ad1fc80fc90ee4fc6bf3cc52d8a979089f7025abc439c48a293"}, "tags": {"8.3": "sha256:617368ca58439b0b8e1c94f9e8dc01189a3abfbcdbf75593686ea6eb6d75a122", "8.5.6": "sha256:e1d218f6aac7b1859a7bbb5e848fc0c5f9b14f1ea841a6463b2e7e56d6824160", "8.5.9": "sha256:4ad379f1077be000a7846525fdcda7996682d544e2b3c10328ecf952f6f56704", "8.5.12": "sha256:fb282e72fa034814e678888743305594ce332ac3bc1f249243f233bf441f46ec", "8.5.13": "sha256:3d60a1053639f0bbcf33c85c938b8de8b564684bba38bb1e6dc366a640c0067c", "8.5.27": "sha256:33e27300e48d9e68ae49abf54fab040b319e4f541b1fbab374f593075975ffbc", "8.6.3": "sha256:1e89a1881f275ad1fc80fc90ee4fc6bf3cc52d8a979089f7025abc439c48a293", "latest": "sha256:1e89a1881f275ad1fc80fc90ee4fc6bf3cc52d8a979089f7025abc439c48a293"}, "aliases": {"module": ". /opt/view/lmod/8.3/init/profile && module"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/lmod.
The Persistence of Vision Ray Tracer, most commonly acronymed as POV-Ray, is a cross-platform ray-tracing program that generates images from a text-based scene description.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/lmod
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/lmod:8.3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/lmod/8.3
$ module help ghcr.io/autamus/lmod/8.3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### lmod-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### lmod-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### lmod-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### lmod-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### lmod-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### lmod-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### module
       
```bash
$ singularity exec <container> . /opt/view/lmod/8.3/init/profile && module
$ podman run --it --rm --entrypoint .   -v ${PWD} -w ${PWD} <container> -c "/opt/view/lmod/8.3/init/profile && module $@"
$ docker run --it --rm --entrypoint .   -v ${PWD} -w ${PWD} <container> -c "/opt/view/lmod/8.3/init/profile && module $@"
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