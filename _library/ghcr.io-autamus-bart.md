---
layout: container
name:  "ghcr.io/autamus/bart"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/bart/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/ghcr.io/autamus/bart/container.yaml"
updated_at: "2022-08-27 02:51:53.602481"
latest: "0.7.00"
container_url: "https://github.com/orgs/autamus/packages/container/package/bart"
aliases:
 - "bart"
 - "bartview"
versions:
 - "0.6.00"
 - "0.7.00"
 - "latest"
description: "BART: Toolbox for Computational Magnetic Resonance Imaging"
config: {"docker": "ghcr.io/autamus/bart", "url": "https://github.com/orgs/autamus/packages/container/package/bart", "maintainer": "@vsoch", "description": "BART: Toolbox for Computational Magnetic Resonance Imaging", "latest": {"0.7.00": "sha256:a1a2217839b53ae07791d91ec357b73ce4c6295cc85857b11101e5c39c0e4ebb"}, "tags": {"0.6.00": "sha256:b34a28af344baff78aa6496214b647295b42291ca99031ce2d4cec30fff2ae13", "0.7.00": "sha256:a1a2217839b53ae07791d91ec357b73ce4c6295cc85857b11101e5c39c0e4ebb", "latest": "sha256:a1a2217839b53ae07791d91ec357b73ce4c6295cc85857b11101e5c39c0e4ebb"}, "aliases": {"bart": "/opt/view/bin/bart", "bartview": "/opt/view/bin/bartview"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/bart.
BART: Toolbox for Computational Magnetic Resonance Imaging
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/bart
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/bart:0.6.00
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/bart/0.6.00
$ module help ghcr.io/autamus/bart/0.6.00
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bart-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bart-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bart-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bart-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bart-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bart-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bart
       
```bash
$ singularity exec <container> /opt/view/bin/bart
$ podman run --it --rm --entrypoint /opt/view/bin/bart   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/bart   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bartview
       
```bash
$ singularity exec <container> /opt/view/bin/bartview
$ podman run --it --rm --entrypoint /opt/view/bin/bartview   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/bartview   -v ${PWD} -w ${PWD} <container> -c " $@"
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