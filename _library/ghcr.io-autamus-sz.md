---
layout: container
name:  "ghcr.io/autamus/sz"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/sz/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/ghcr.io/autamus/sz/container.yaml"
updated_at: "2022-08-27 02:53:33.519068"
latest: "2.1.12"
container_url: "https://github.com/orgs/autamus/packages/container/package/sz"
aliases:
 - "sz"
versions:
 - "2.1.11.1"
 - "2.1.11.2"
 - "2.1.12"
description: "Error-bounded Lossy Compressor for HPC Data"
config: {"docker": "ghcr.io/autamus/sz", "url": "https://github.com/orgs/autamus/packages/container/package/sz", "maintainer": "@vsoch", "description": "Error-bounded Lossy Compressor for HPC Data", "latest": {"2.1.12": "sha256:649aef4ed106ca1974f8705a68ce4e7fef9e526864463a4f482104c2a2e4ef9e"}, "tags": {"2.1.11.1": "sha256:105b13a7a85021b85ca58e6e8bf15c5926cfc05f0c53e0f6994f31d224376818", "2.1.11.2": "sha256:005382147560fde81a40902ed87e25ec9de2309d88508bd406502cb175c9b71f", "2.1.12": "sha256:649aef4ed106ca1974f8705a68ce4e7fef9e526864463a4f482104c2a2e4ef9e"}, "aliases": {"sz": "/opt/view/bin/sz"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/sz.
Error-bounded Lossy Compressor for HPC Data
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/sz
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/sz:2.1.11.1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/sz/2.1.11.1
$ module help ghcr.io/autamus/sz/2.1.11.1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sz-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sz-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sz-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sz-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sz-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sz-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### sz
       
```bash
$ singularity exec <container> /opt/view/bin/sz
$ podman run --it --rm --entrypoint /opt/view/bin/sz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/sz   -v ${PWD} -w ${PWD} <container> -c " $@"
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