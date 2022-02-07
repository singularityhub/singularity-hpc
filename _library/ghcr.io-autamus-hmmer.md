---
layout: container
name:  "ghcr.io/autamus/hmmer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/hmmer/container.yaml"
updated_at: "2022-02-07 11:14:42.364875"
container_url: "https://github.com/orgs/autamus/packages/container/package/hmmer"
aliases:
 - "hmmalign"

 - "hmmbuild"

 - "hmmconvert"

 - "hmmemit"

 - "hmmfetch"

 - "hmmlogo"

 - "hmmpgmd"

 - "hmmpgmd_shard"

 - "hmmpress"

 - "hmmscan"

 - "hmmsearch"

 - "hmmsim"

 - "hmmstat"

versions:
 - "3.3"
 - "3.3.2"
 - "latest"
description: "HMMER is used for searching sequence databases for sequence homologs, and for making sequence alignments."
---

This module is a singularity container wrapper for ghcr.io/autamus/hmmer.
HMMER is used for searching sequence databases for sequence homologs, and for making sequence alignments.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install ghcr.io/autamus/hmmer
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/hmmer:3.3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/hmmer/3.3
$ module help ghcr.io/autamus/hmmer/3.3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### -run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### -shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### -exec:

```bash
$ singularity exec -s /bin/sh <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### -inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### -inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### -inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### hmmalign
       
```bash
$ singularity exec <container> /opt/view/bin/hmmalign
$ podman run --it --rm --entrypoint /opt/view/bin/hmmalign   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/hmmalign   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmbuild
       
```bash
$ singularity exec <container> /opt/view/bin/hmmbuild
$ podman run --it --rm --entrypoint /opt/view/bin/hmmbuild   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/hmmbuild   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmconvert
       
```bash
$ singularity exec <container> /opt/view/bin/hmmconvert
$ podman run --it --rm --entrypoint /opt/view/bin/hmmconvert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/hmmconvert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmemit
       
```bash
$ singularity exec <container> /opt/view/bin/hmmemit
$ podman run --it --rm --entrypoint /opt/view/bin/hmmemit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/hmmemit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmfetch
       
```bash
$ singularity exec <container> /opt/view/bin/hmmfetch
$ podman run --it --rm --entrypoint /opt/view/bin/hmmfetch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/hmmfetch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmlogo
       
```bash
$ singularity exec <container> /opt/view/bin/hmmlogo
$ podman run --it --rm --entrypoint /opt/view/bin/hmmlogo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/hmmlogo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmpgmd
       
```bash
$ singularity exec <container> /opt/view/bin/hmmpgmd
$ podman run --it --rm --entrypoint /opt/view/bin/hmmpgmd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/hmmpgmd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmpgmd_shard
       
```bash
$ singularity exec <container> /opt/view/bin/hmmpgmd_shard
$ podman run --it --rm --entrypoint /opt/view/bin/hmmpgmd_shard   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/hmmpgmd_shard   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmpress
       
```bash
$ singularity exec <container> /opt/view/bin/hmmpress
$ podman run --it --rm --entrypoint /opt/view/bin/hmmpress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/hmmpress   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmscan
       
```bash
$ singularity exec <container> /opt/view/bin/hmmscan
$ podman run --it --rm --entrypoint /opt/view/bin/hmmscan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/hmmscan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmsearch
       
```bash
$ singularity exec <container> /opt/view/bin/hmmsearch
$ podman run --it --rm --entrypoint /opt/view/bin/hmmsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/hmmsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmsim
       
```bash
$ singularity exec <container> /opt/view/bin/hmmsim
$ podman run --it --rm --entrypoint /opt/view/bin/hmmsim   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/hmmsim   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmstat
       
```bash
$ singularity exec <container> /opt/view/bin/hmmstat
$ podman run --it --rm --entrypoint /opt/view/bin/hmmstat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/hmmstat   -v ${PWD} -w ${PWD} <container> -c " $@"
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