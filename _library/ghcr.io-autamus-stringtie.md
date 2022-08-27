---
layout: container
name:  "ghcr.io/autamus/stringtie"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/stringtie/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/ghcr.io/autamus/stringtie/container.yaml"
updated_at: "2022-08-27 02:53:32.157273"
latest: "2.1.7"
container_url: "https://github.com/orgs/autamus/packages/container/package/stringtie"
aliases:
 - "stringtie"
versions:
 - "2.1.5"
 - "2.1.6"
 - "2.1.7"
 - "latest"
description: "StringTie is a fast and highly efficient assembler of RNA-Seq alignments into potential transcripts."
config: {"docker": "ghcr.io/autamus/stringtie", "url": "https://github.com/orgs/autamus/packages/container/package/stringtie", "maintainer": "@vsoch", "description": "StringTie is a fast and highly efficient assembler of RNA-Seq alignments into potential transcripts.", "latest": {"2.1.7": "sha256:d076165e92438fcee137f81868f524a9a03b4eab802abadf52d14f38adffe0b7"}, "tags": {"2.1.5": "sha256:17ad259efefe11dea4baf80631a189d2d1ff6c5ff59c339dfadf9c30806668f1", "2.1.6": "sha256:ff3ded2da21df79de3d53c61140d02dd0caea7603037663d8560986d3e345c8c", "2.1.7": "sha256:d076165e92438fcee137f81868f524a9a03b4eab802abadf52d14f38adffe0b7", "latest": "sha256:b46c04536a9458bccf9ea7130d415f1f6a7e03d8838c7f7fc4a6debd1dc79ed0"}, "aliases": {"stringtie": "/opt/view/bin/stringtie"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/stringtie.
StringTie is a fast and highly efficient assembler of RNA-Seq alignments into potential transcripts.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/stringtie
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/stringtie:2.1.5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/stringtie/2.1.5
$ module help ghcr.io/autamus/stringtie/2.1.5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### stringtie-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### stringtie-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### stringtie-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### stringtie-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### stringtie-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### stringtie-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### stringtie
       
```bash
$ singularity exec <container> /opt/view/bin/stringtie
$ podman run --it --rm --entrypoint /opt/view/bin/stringtie   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/stringtie   -v ${PWD} -w ${PWD} <container> -c " $@"
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