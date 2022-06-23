---
layout: container
name:  "ghcr.io/autamus/pandaseq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/pandaseq/container.yaml"
updated_at: "2022-06-23 04:31:14.115217"
container_url: "https://github.com/orgs/autamus/packages/container/package/pandaseq"
aliases:
 - "pandaseq"

 - "pandaseq-checkid"

 - "pandaseq-diff"

 - "pandaseq-hang"

 - "pandaxs"

versions:
 - "2.11"
 - "latest"
description: "A program to align Illumina reads, optionally with PCR primers embedded in the sequence, and reconstruct an overlapping sequence."
---

This module is a singularity container wrapper for ghcr.io/autamus/pandaseq.
A program to align Illumina reads, optionally with PCR primers embedded in the sequence, and reconstruct an overlapping sequence.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/pandaseq
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/pandaseq:2.11
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/pandaseq/2.11
$ module help ghcr.io/autamus/pandaseq/2.11
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pandaseq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pandaseq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pandaseq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pandaseq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pandaseq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pandaseq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pandaseq
       
```bash
$ singularity exec <container> /opt/view/bin/pandaseq
$ podman run --it --rm --entrypoint /opt/view/bin/pandaseq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/pandaseq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pandaseq-checkid
       
```bash
$ singularity exec <container> /opt/view/bin/pandaseq-checkid
$ podman run --it --rm --entrypoint /opt/view/bin/pandaseq-checkid   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/pandaseq-checkid   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pandaseq-diff
       
```bash
$ singularity exec <container> /opt/view/bin/pandaseq-diff
$ podman run --it --rm --entrypoint /opt/view/bin/pandaseq-diff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/pandaseq-diff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pandaseq-hang
       
```bash
$ singularity exec <container> /opt/view/bin/pandaseq-hang
$ podman run --it --rm --entrypoint /opt/view/bin/pandaseq-hang   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/pandaseq-hang   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pandaxs
       
```bash
$ singularity exec <container> /opt/view/bin/pandaxs
$ podman run --it --rm --entrypoint /opt/view/bin/pandaxs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/pandaxs   -v ${PWD} -w ${PWD} <container> -c " $@"
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