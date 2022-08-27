---
layout: container
name:  "ghcr.io/autamus/gsl"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/gsl/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/ghcr.io/autamus/gsl/container.yaml"
updated_at: "2022-08-27 02:52:30.499445"
latest: "2.7"
container_url: "https://github.com/orgs/autamus/packages/container/package/gsl"
aliases:
 - "gsl-config"
 - "gsl-histogram"
 - "gsl-randist"
versions:
 - "2.6"
 - "2.7"
 - "latest"
description: "The GNU Scientific Library."
config: {"docker": "ghcr.io/autamus/gsl", "url": "https://github.com/orgs/autamus/packages/container/package/gsl", "maintainer": "@vsoch", "description": "The GNU Scientific Library.", "latest": {"2.7": "sha256:674c111e37385d8e73910defd5d058d414e430837a7eceee687d8191eb2b1266"}, "tags": {"2.6": "sha256:e61cb98bef8557181282243129209b2472478525dae9dc44f34fd7381beb39f2", "2.7": "sha256:674c111e37385d8e73910defd5d058d414e430837a7eceee687d8191eb2b1266", "latest": "sha256:f45fadf32691d9d9863789138cc9a11c90865188165bc644758da56d49f304f9"}, "aliases": {"gsl-config": "/opt/view/bin/gsl-config", "gsl-histogram": "/opt/view/bin/gsl-histogram", "gsl-randist": "/opt/view/bin/gsl-randist"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/gsl.
The GNU Scientific Library.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/gsl
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/gsl:2.6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/gsl/2.6
$ module help ghcr.io/autamus/gsl/2.6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gsl-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gsl-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gsl-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gsl-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gsl-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gsl-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gsl-config
       
```bash
$ singularity exec <container> /opt/view/bin/gsl-config
$ podman run --it --rm --entrypoint /opt/view/bin/gsl-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/gsl-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gsl-histogram
       
```bash
$ singularity exec <container> /opt/view/bin/gsl-histogram
$ podman run --it --rm --entrypoint /opt/view/bin/gsl-histogram   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/gsl-histogram   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gsl-randist
       
```bash
$ singularity exec <container> /opt/view/bin/gsl-randist
$ podman run --it --rm --entrypoint /opt/view/bin/gsl-randist   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/gsl-randist   -v ${PWD} -w ${PWD} <container> -c " $@"
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