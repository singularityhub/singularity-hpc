---
layout: container
name:  "quay.io/biocontainers/mummer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mummer/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/mummer/container.yaml"
updated_at: "2022-08-27 01:37:29.517360"
latest: "3.23--pl5321h1b792b2_13"
container_url: "https://quay.io/repository/biocontainers/mummer"
aliases:
 - "mummer"
versions:
 - "3.23--pl526_7"
 - "3.23--pl526he1b5a44_11"
 - "3.23--pl5321h1b792b2_13"
description: "MUMmer is a system for rapidly aligning entire genomes in complete or in draft form."
config: {"docker": "quay.io/biocontainers/mummer", "url": "https://quay.io/repository/biocontainers/mummer", "maintainer": "@sarahbeecroft", "description": "MUMmer is a system for rapidly aligning entire genomes in complete or in draft form.", "latest": {"3.23--pl5321h1b792b2_13": "sha256:913c4cccaa59758830527f30e476d46d02253e98c5f4e481112d1f581696475f"}, "tags": {"3.23--pl526_7": "sha256:21462ca45429aaeebb0a298d5ae830aa7c299771166c762bea2b5bde20db43f8", "3.23--pl526he1b5a44_11": "sha256:2a0b6a706b92f2507d033bef6d3e4fe6bca2104f44e870447b414cfa34e67c38", "3.23--pl5321h1b792b2_13": "sha256:913c4cccaa59758830527f30e476d46d02253e98c5f4e481112d1f581696475f"}, "aliases": {"mummer": "/usr/local/bin/mummer"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mummer.
MUMmer is a system for rapidly aligning entire genomes in complete or in draft form.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mummer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mummer:3.23--pl526_7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mummer/3.23--pl526_7
$ module help quay.io/biocontainers/mummer/3.23--pl526_7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mummer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mummer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mummer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mummer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mummer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mummer-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### mummer
       
```bash
$ singularity exec <container> /usr/local/bin/mummer
$ podman run --it --rm --entrypoint /usr/local/bin/mummer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mummer   -v ${PWD} -w ${PWD} <container> -c " $@"
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