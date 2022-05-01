---
layout: container
name:  "ghcr.io/autamus/abyss"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/abyss/container.yaml"
updated_at: "2022-05-01 04:16:48.047433"
container_url: "https://github.com/orgs/autamus/packages/container/package/abyss"
aliases:
 - "abyss-align"

 - "abyss-bloom"

 - "abyss-bloom-dbg"

 - "abyss-bloom-dist.mk"

 - "abyss-bowtie"

 - "abyss-bowtie2"

 - "abyss-bwa"

 - "abyss-bwamem"

 - "abyss-bwasw"

 - "abyss-db-csv"

 - "abyss-db-txt"

 - "abyss-dida"

 - "abyss-fac"

 - "abyss-fatoagp"

 - "abyss-filtergraph"

 - "abyss-fixmate"

 - "abyss-fixmate-ssq"

 - "abyss-gapfill"

 - "abyss-gc"

 - "abyss-index"

 - "abyss-junction"

 - "abyss-kaligner"

 - "abyss-layout"

 - "abyss-longseqdist"

 - "abyss-map"

 - "abyss-map-ssq"

 - "abyss-mergepairs"

 - "abyss-overlap"

 - "abyss-paired-dbg"

 - "abyss-paired-dbg-mpi"

 - "abyss-pe"

 - "abyss-samtoafg"

 - "abyss-scaffold"

 - "abyss-sealer"

 - "abyss-stack-size"

 - "abyss-tabtomd"

 - "abyss-todot"

 - "abyss-tofastq"

versions:
 - "2.3.0"
 - "2.3.1"
 - "2.3.2"
 - "2.3.3"
 - "2.3.4"
 - "latest"
description: "ABySS is a de novo, parallel, paired-end sequence assembler that is designed for short reads."
---

This module is a singularity container wrapper for ghcr.io/autamus/abyss.
ABySS is a de novo, parallel, paired-end sequence assembler that is designed for short reads.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/abyss
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/abyss:2.3.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/abyss/2.3.0
$ module help ghcr.io/autamus/abyss/2.3.0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### abyss-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### abyss-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### abyss-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### abyss-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### abyss-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### abyss-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### abyss-align
       
```bash
$ singularity exec <container> /opt/view/bin/abyss-align
$ podman run --it --rm --entrypoint /opt/view/bin/abyss-align   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/abyss-align   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### abyss-bloom
       
```bash
$ singularity exec <container> /opt/view/bin/abyss-bloom
$ podman run --it --rm --entrypoint /opt/view/bin/abyss-bloom   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/abyss-bloom   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### abyss-bloom-dbg
       
```bash
$ singularity exec <container> /opt/view/bin/abyss-bloom-dbg
$ podman run --it --rm --entrypoint /opt/view/bin/abyss-bloom-dbg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/abyss-bloom-dbg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### abyss-bloom-dist.mk
       
```bash
$ singularity exec <container> /opt/view/bin/abyss-bloom-dist.mk
$ podman run --it --rm --entrypoint /opt/view/bin/abyss-bloom-dist.mk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/abyss-bloom-dist.mk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### abyss-bowtie
       
```bash
$ singularity exec <container> /opt/view/bin/abyss-bowtie
$ podman run --it --rm --entrypoint /opt/view/bin/abyss-bowtie   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/abyss-bowtie   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### abyss-bowtie2
       
```bash
$ singularity exec <container> /opt/view/bin/abyss-bowtie2
$ podman run --it --rm --entrypoint /opt/view/bin/abyss-bowtie2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/abyss-bowtie2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### abyss-bwa
       
```bash
$ singularity exec <container> /opt/view/bin/abyss-bwa
$ podman run --it --rm --entrypoint /opt/view/bin/abyss-bwa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/abyss-bwa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### abyss-bwamem
       
```bash
$ singularity exec <container> /opt/view/bin/abyss-bwamem
$ podman run --it --rm --entrypoint /opt/view/bin/abyss-bwamem   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/abyss-bwamem   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### abyss-bwasw
       
```bash
$ singularity exec <container> /opt/view/bin/abyss-bwasw
$ podman run --it --rm --entrypoint /opt/view/bin/abyss-bwasw   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/abyss-bwasw   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### abyss-db-csv
       
```bash
$ singularity exec <container> /opt/view/bin/abyss-db-csv
$ podman run --it --rm --entrypoint /opt/view/bin/abyss-db-csv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/abyss-db-csv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### abyss-db-txt
       
```bash
$ singularity exec <container> /opt/view/bin/abyss-db-txt
$ podman run --it --rm --entrypoint /opt/view/bin/abyss-db-txt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/abyss-db-txt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### abyss-dida
       
```bash
$ singularity exec <container> /opt/view/bin/abyss-dida
$ podman run --it --rm --entrypoint /opt/view/bin/abyss-dida   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/abyss-dida   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### abyss-fac
       
```bash
$ singularity exec <container> /opt/view/bin/abyss-fac
$ podman run --it --rm --entrypoint /opt/view/bin/abyss-fac   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/abyss-fac   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### abyss-fatoagp
       
```bash
$ singularity exec <container> /opt/view/bin/abyss-fatoagp
$ podman run --it --rm --entrypoint /opt/view/bin/abyss-fatoagp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/abyss-fatoagp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### abyss-filtergraph
       
```bash
$ singularity exec <container> /opt/view/bin/abyss-filtergraph
$ podman run --it --rm --entrypoint /opt/view/bin/abyss-filtergraph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/abyss-filtergraph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### abyss-fixmate
       
```bash
$ singularity exec <container> /opt/view/bin/abyss-fixmate
$ podman run --it --rm --entrypoint /opt/view/bin/abyss-fixmate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/abyss-fixmate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### abyss-fixmate-ssq
       
```bash
$ singularity exec <container> /opt/view/bin/abyss-fixmate-ssq
$ podman run --it --rm --entrypoint /opt/view/bin/abyss-fixmate-ssq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/abyss-fixmate-ssq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### abyss-gapfill
       
```bash
$ singularity exec <container> /opt/view/bin/abyss-gapfill
$ podman run --it --rm --entrypoint /opt/view/bin/abyss-gapfill   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/abyss-gapfill   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### abyss-gc
       
```bash
$ singularity exec <container> /opt/view/bin/abyss-gc
$ podman run --it --rm --entrypoint /opt/view/bin/abyss-gc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/abyss-gc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### abyss-index
       
```bash
$ singularity exec <container> /opt/view/bin/abyss-index
$ podman run --it --rm --entrypoint /opt/view/bin/abyss-index   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/abyss-index   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### abyss-junction
       
```bash
$ singularity exec <container> /opt/view/bin/abyss-junction
$ podman run --it --rm --entrypoint /opt/view/bin/abyss-junction   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/abyss-junction   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### abyss-kaligner
       
```bash
$ singularity exec <container> /opt/view/bin/abyss-kaligner
$ podman run --it --rm --entrypoint /opt/view/bin/abyss-kaligner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/abyss-kaligner   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### abyss-layout
       
```bash
$ singularity exec <container> /opt/view/bin/abyss-layout
$ podman run --it --rm --entrypoint /opt/view/bin/abyss-layout   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/abyss-layout   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### abyss-longseqdist
       
```bash
$ singularity exec <container> /opt/view/bin/abyss-longseqdist
$ podman run --it --rm --entrypoint /opt/view/bin/abyss-longseqdist   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/abyss-longseqdist   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### abyss-map
       
```bash
$ singularity exec <container> /opt/view/bin/abyss-map
$ podman run --it --rm --entrypoint /opt/view/bin/abyss-map   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/abyss-map   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### abyss-map-ssq
       
```bash
$ singularity exec <container> /opt/view/bin/abyss-map-ssq
$ podman run --it --rm --entrypoint /opt/view/bin/abyss-map-ssq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/abyss-map-ssq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### abyss-mergepairs
       
```bash
$ singularity exec <container> /opt/view/bin/abyss-mergepairs
$ podman run --it --rm --entrypoint /opt/view/bin/abyss-mergepairs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/abyss-mergepairs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### abyss-overlap
       
```bash
$ singularity exec <container> /opt/view/bin/abyss-overlap
$ podman run --it --rm --entrypoint /opt/view/bin/abyss-overlap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/abyss-overlap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### abyss-paired-dbg
       
```bash
$ singularity exec <container> /opt/view/bin/abyss-paired-dbg
$ podman run --it --rm --entrypoint /opt/view/bin/abyss-paired-dbg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/abyss-paired-dbg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### abyss-paired-dbg-mpi
       
```bash
$ singularity exec <container> /opt/view/bin/abyss-paired-dbg-mpi
$ podman run --it --rm --entrypoint /opt/view/bin/abyss-paired-dbg-mpi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/abyss-paired-dbg-mpi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### abyss-pe
       
```bash
$ singularity exec <container> /opt/view/bin/abyss-pe
$ podman run --it --rm --entrypoint /opt/view/bin/abyss-pe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/abyss-pe   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### abyss-samtoafg
       
```bash
$ singularity exec <container> /opt/view/bin/abyss-samtoafg
$ podman run --it --rm --entrypoint /opt/view/bin/abyss-samtoafg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/abyss-samtoafg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### abyss-scaffold
       
```bash
$ singularity exec <container> /opt/view/bin/abyss-scaffold
$ podman run --it --rm --entrypoint /opt/view/bin/abyss-scaffold   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/abyss-scaffold   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### abyss-sealer
       
```bash
$ singularity exec <container> /opt/view/bin/abyss-sealer
$ podman run --it --rm --entrypoint /opt/view/bin/abyss-sealer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/abyss-sealer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### abyss-stack-size
       
```bash
$ singularity exec <container> /opt/view/bin/abyss-stack-size
$ podman run --it --rm --entrypoint /opt/view/bin/abyss-stack-size   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/abyss-stack-size   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### abyss-tabtomd
       
```bash
$ singularity exec <container> /opt/view/bin/abyss-tabtomd
$ podman run --it --rm --entrypoint /opt/view/bin/abyss-tabtomd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/abyss-tabtomd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### abyss-todot
       
```bash
$ singularity exec <container> /opt/view/bin/abyss-todot
$ podman run --it --rm --entrypoint /opt/view/bin/abyss-todot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/abyss-todot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### abyss-tofastq
       
```bash
$ singularity exec <container> /opt/view/bin/abyss-tofastq
$ podman run --it --rm --entrypoint /opt/view/bin/abyss-tofastq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/abyss-tofastq   -v ${PWD} -w ${PWD} <container> -c " $@"
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