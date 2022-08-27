---
layout: container
name:  "poldracklab/mriqc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/poldracklab/mriqc/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/poldracklab/mriqc/container.yaml"
updated_at: "2022-08-27 02:54:07.126761"
latest: "0.16.1"
container_url: "https://hub.docker.com/r/poldracklab/mriqc"
aliases:
 - "mriqc"
versions:
 - "0.16.1"
description: "Automatic prediction of quality and visual reporting of MRI scans."
config: {"docker": "poldracklab/mriqc", "latest": {"0.16.1": "sha256:cbaeda87ca5f7a0f86816ac4a56fc28fef0ac88f392be7a9037371f8d7f48e53"}, "tags": {"0.16.1": "sha256:cbaeda87ca5f7a0f86816ac4a56fc28fef0ac88f392be7a9037371f8d7f48e53"}, "filter": ["2[.]*"], "maintainer": "@vsoch", "description": "Automatic prediction of quality and visual reporting of MRI scans.", "url": "https://hub.docker.com/r/poldracklab/mriqc", "aliases": {"mriqc": "/usr/local/miniconda/bin/mriqc"}}
---

This module is a singularity container wrapper for poldracklab/mriqc.
Automatic prediction of quality and visual reporting of MRI scans.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install poldracklab/mriqc
```

Or a specific version:

```bash
$ shpc install poldracklab/mriqc:0.16.1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load poldracklab/mriqc/0.16.1
$ module help poldracklab/mriqc/0.16.1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mriqc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mriqc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mriqc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mriqc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mriqc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mriqc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### mriqc
       
```bash
$ singularity exec <container> /usr/local/miniconda/bin/mriqc
$ podman run --it --rm --entrypoint /usr/local/miniconda/bin/mriqc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/miniconda/bin/mriqc   -v ${PWD} -w ${PWD} <container> -c " $@"
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