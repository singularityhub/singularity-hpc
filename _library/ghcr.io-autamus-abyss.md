---
layout: container
name:  "ghcr.io/autamus/abyss"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/abyss/container.yaml"
updated_at: "2021-04-20 02:21:44.024745"
container_url: ""
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

When you install this module, you'll be able to load it to make the following commands accessible:

#### ghcr.io-autamus-abyss-run:

```bash
$ singularity run <container>
```

#### ghcr.io-autamus-abyss-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### ghcr.io-autamus-abyss-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### ghcr.io-autamus-abyss-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ghcr.io-autamus-abyss-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### abyss-align
       
```bash
$ singularity exec <container> /opt/view/bin/abyss-align
```


#### abyss-bloom
       
```bash
$ singularity exec <container> /opt/view/bin/abyss-bloom
```


#### abyss-bloom-dbg
       
```bash
$ singularity exec <container> /opt/view/bin/abyss-bloom-dbg
```


#### abyss-bloom-dist.mk
       
```bash
$ singularity exec <container> /opt/view/bin/abyss-bloom-dist.mk
```


#### abyss-bowtie
       
```bash
$ singularity exec <container> /opt/view/bin/abyss-bowtie
```


#### abyss-bowtie2
       
```bash
$ singularity exec <container> /opt/view/bin/abyss-bowtie2
```


#### abyss-bwa
       
```bash
$ singularity exec <container> /opt/view/bin/abyss-bwa
```


#### abyss-bwamem
       
```bash
$ singularity exec <container> /opt/view/bin/abyss-bwamem
```


#### abyss-bwasw
       
```bash
$ singularity exec <container> /opt/view/bin/abyss-bwasw
```


#### abyss-db-csv
       
```bash
$ singularity exec <container> /opt/view/bin/abyss-db-csv
```


#### abyss-db-txt
       
```bash
$ singularity exec <container> /opt/view/bin/abyss-db-txt
```


#### abyss-dida
       
```bash
$ singularity exec <container> /opt/view/bin/abyss-dida
```


#### abyss-fac
       
```bash
$ singularity exec <container> /opt/view/bin/abyss-fac
```


#### abyss-fatoagp
       
```bash
$ singularity exec <container> /opt/view/bin/abyss-fatoagp
```


#### abyss-filtergraph
       
```bash
$ singularity exec <container> /opt/view/bin/abyss-filtergraph
```


#### abyss-fixmate
       
```bash
$ singularity exec <container> /opt/view/bin/abyss-fixmate
```


#### abyss-fixmate-ssq
       
```bash
$ singularity exec <container> /opt/view/bin/abyss-fixmate-ssq
```


#### abyss-gapfill
       
```bash
$ singularity exec <container> /opt/view/bin/abyss-gapfill
```


#### abyss-gc
       
```bash
$ singularity exec <container> /opt/view/bin/abyss-gc
```


#### abyss-index
       
```bash
$ singularity exec <container> /opt/view/bin/abyss-index
```


#### abyss-junction
       
```bash
$ singularity exec <container> /opt/view/bin/abyss-junction
```


#### abyss-kaligner
       
```bash
$ singularity exec <container> /opt/view/bin/abyss-kaligner
```


#### abyss-layout
       
```bash
$ singularity exec <container> /opt/view/bin/abyss-layout
```


#### abyss-longseqdist
       
```bash
$ singularity exec <container> /opt/view/bin/abyss-longseqdist
```


#### abyss-map
       
```bash
$ singularity exec <container> /opt/view/bin/abyss-map
```


#### abyss-map-ssq
       
```bash
$ singularity exec <container> /opt/view/bin/abyss-map-ssq
```


#### abyss-mergepairs
       
```bash
$ singularity exec <container> /opt/view/bin/abyss-mergepairs
```


#### abyss-overlap
       
```bash
$ singularity exec <container> /opt/view/bin/abyss-overlap
```


#### abyss-paired-dbg
       
```bash
$ singularity exec <container> /opt/view/bin/abyss-paired-dbg
```


#### abyss-paired-dbg-mpi
       
```bash
$ singularity exec <container> /opt/view/bin/abyss-paired-dbg-mpi
```


#### abyss-pe
       
```bash
$ singularity exec <container> /opt/view/bin/abyss-pe
```


#### abyss-samtoafg
       
```bash
$ singularity exec <container> /opt/view/bin/abyss-samtoafg
```


#### abyss-scaffold
       
```bash
$ singularity exec <container> /opt/view/bin/abyss-scaffold
```


#### abyss-sealer
       
```bash
$ singularity exec <container> /opt/view/bin/abyss-sealer
```


#### abyss-stack-size
       
```bash
$ singularity exec <container> /opt/view/bin/abyss-stack-size
```


#### abyss-tabtomd
       
```bash
$ singularity exec <container> /opt/view/bin/abyss-tabtomd
```


#### abyss-todot
       
```bash
$ singularity exec <container> /opt/view/bin/abyss-todot
```


#### abyss-tofastq
       
```bash
$ singularity exec <container> /opt/view/bin/abyss-tofastq
```



In the above, the `<container>` directive will reference an actual container provided
by the module, for the version you have chosen to load. Note that although a container
might provide custom commands, every container exposes unique exec, shell, run, and
inspect aliases. For each of the above, you can export:

 - SINGULARITY_OPTS: to define custom options for singularity (e.g., --debug)
 - SINGULARITY_COMMAND_OPTS: to define custom options for the command (e.g., -b)

<br>
  
### Install

You can install shpc locally (for yourself or your user base) as follows:

```bash
$ git clone https://github.com/singularityhub/singularity-hpc
$ cd singularity-hpc
$ pip install -e .
```

Have any questions, or want to request a new module or version? [ask for help!](https://github.com/singularityhub/singularity-hpc/issues)