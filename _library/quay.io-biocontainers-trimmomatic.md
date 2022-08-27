---
layout: container
name:  "quay.io/biocontainers/trimmomatic"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/trimmomatic/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/trimmomatic/container.yaml"
updated_at: "2022-08-27 01:37:32.696889"
latest: "0.39--hdfd78af_2"
container_url: "https://quay.io/repository/biocontainers/trimmomatic"
aliases:
 - "trimmomatic"
versions:
 - "0.39--0"
 - "0.39--hdfd78af_2"
description: "A flexible read trimming tool for Illumina NGS data."
config: {"docker": "quay.io/biocontainers/trimmomatic", "url": "https://quay.io/repository/biocontainers/trimmomatic", "maintainer": "@audreystott", "description": "A flexible read trimming tool for Illumina NGS data.", "latest": {"0.39--hdfd78af_2": "sha256:b52e7e3159fda36b7b5c119a9a1e673e6a63e480eff8617b689c031f76998870"}, "tags": {"0.39--0": "sha256:8301349be3aef6d65d803dbb8a58ec4e4e2323867e94182a6684ebd4b28661bb", "0.39--hdfd78af_2": "sha256:b52e7e3159fda36b7b5c119a9a1e673e6a63e480eff8617b689c031f76998870"}, "aliases": {"trimmomatic": "/usr/local/bin/trimmomatic"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/trimmomatic.
A flexible read trimming tool for Illumina NGS data.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/trimmomatic
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/trimmomatic:0.39--0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/trimmomatic/0.39--0
$ module help quay.io/biocontainers/trimmomatic/0.39--0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### trimmomatic-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### trimmomatic-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### trimmomatic-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### trimmomatic-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### trimmomatic-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### trimmomatic-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### trimmomatic
       
```bash
$ singularity exec <container> /usr/local/bin/trimmomatic
$ podman run --it --rm --entrypoint /usr/local/bin/trimmomatic   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trimmomatic   -v ${PWD} -w ${PWD} <container> -c " $@"
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