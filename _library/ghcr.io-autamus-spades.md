---
layout: container
name:  "ghcr.io/autamus/spades"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/spades/container.yaml"
updated_at: "2021-06-27 03:46:16.534481"
container_url: "https://github.com/orgs/autamus/packages/container/package/spades"
aliases:
 - "spades-bwa"

 - "spades-convert-bin-to-fasta"

 - "spades-core"

 - "spades-corrector-core"

 - "spades-gbuilder"

 - "spades-gmapper"

 - "spades-gsimplifier"

 - "spades-hammer"

 - "spades-ionhammer"

 - "spades-kmer-estimating"

 - "spades-kmercount"

 - "spades-read-filter"

 - "spades-truseq-scfcorrection"

 - "spades.py"

 - "spaligner"

versions:
 - "3.15.2"
 - "latest"
description: "St. Petersburg genome assembler – an assembly toolkit containing various assembly pipelines."
---

This module is a singularity container wrapper for ghcr.io/autamus/spades.
St. Petersburg genome assembler – an assembly toolkit containing various assembly pipelines.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install ghcr.io/autamus/spades
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/spades:3.15.2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/spades/3.15.2
$ module help ghcr.io/autamus/spades/3.15.2
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


#### spades-bwa
       
```bash
$ singularity exec <container> /opt/view/bin/spades-bwa
$ podman run --it --rm --entrypoint /opt/view/bin/spades-bwa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/spades-bwa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-convert-bin-to-fasta
       
```bash
$ singularity exec <container> /opt/view/bin/spades-convert-bin-to-fasta
$ podman run --it --rm --entrypoint /opt/view/bin/spades-convert-bin-to-fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/spades-convert-bin-to-fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-core
       
```bash
$ singularity exec <container> /opt/view/bin/spades-core
$ podman run --it --rm --entrypoint /opt/view/bin/spades-core   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/spades-core   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-corrector-core
       
```bash
$ singularity exec <container> /opt/view/bin/spades-corrector-core
$ podman run --it --rm --entrypoint /opt/view/bin/spades-corrector-core   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/spades-corrector-core   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-gbuilder
       
```bash
$ singularity exec <container> /opt/view/bin/spades-gbuilder
$ podman run --it --rm --entrypoint /opt/view/bin/spades-gbuilder   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/spades-gbuilder   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-gmapper
       
```bash
$ singularity exec <container> /opt/view/bin/spades-gmapper
$ podman run --it --rm --entrypoint /opt/view/bin/spades-gmapper   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/spades-gmapper   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-gsimplifier
       
```bash
$ singularity exec <container> /opt/view/bin/spades-gsimplifier
$ podman run --it --rm --entrypoint /opt/view/bin/spades-gsimplifier   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/spades-gsimplifier   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-hammer
       
```bash
$ singularity exec <container> /opt/view/bin/spades-hammer
$ podman run --it --rm --entrypoint /opt/view/bin/spades-hammer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/spades-hammer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-ionhammer
       
```bash
$ singularity exec <container> /opt/view/bin/spades-ionhammer
$ podman run --it --rm --entrypoint /opt/view/bin/spades-ionhammer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/spades-ionhammer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-kmer-estimating
       
```bash
$ singularity exec <container> /opt/view/bin/spades-kmer-estimating
$ podman run --it --rm --entrypoint /opt/view/bin/spades-kmer-estimating   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/spades-kmer-estimating   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-kmercount
       
```bash
$ singularity exec <container> /opt/view/bin/spades-kmercount
$ podman run --it --rm --entrypoint /opt/view/bin/spades-kmercount   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/spades-kmercount   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-read-filter
       
```bash
$ singularity exec <container> /opt/view/bin/spades-read-filter
$ podman run --it --rm --entrypoint /opt/view/bin/spades-read-filter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/spades-read-filter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-truseq-scfcorrection
       
```bash
$ singularity exec <container> /opt/view/bin/spades-truseq-scfcorrection
$ podman run --it --rm --entrypoint /opt/view/bin/spades-truseq-scfcorrection   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/spades-truseq-scfcorrection   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades.py
       
```bash
$ singularity exec <container> /opt/view/bin/spades.py
$ podman run --it --rm --entrypoint /opt/view/bin/spades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/spades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spaligner
       
```bash
$ singularity exec <container> /opt/view/bin/spaligner
$ podman run --it --rm --entrypoint /opt/view/bin/spaligner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/spaligner   -v ${PWD} -w ${PWD} <container> -c " $@"
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