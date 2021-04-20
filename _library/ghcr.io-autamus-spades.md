---
layout: container
name:  "ghcr.io/autamus/spades"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/spades/container.yaml"
updated_at: "2021-04-20 02:17:42.429917"
container_url: ""
aliases:
 - "spades.py"

 - "spades-bwa"

 - "spades-gbuilder"

 - "spades-ionhammer"

 - "spades-truseq-scfcorrection"

 - "spades-convert-bin-to-fasta"

 - "spades-gmapper"

 - "spades-kmer-estimating"

 - "spades-core"

 - "spades-gsimplifier"

 - "spades-kmercount"

 - "spades-corrector-core"

 - "spades-hammer"

 - "spaligner"

 - "spades-read-filter"

versions:
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
$ shpc install ghcr.io/autamus/spades:latest
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/spades/latest
$ module help ghcr.io/autamus/spades/latest
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### ghcr.io-autamus-spades-run:

```bash
$ singularity run <container>
```

#### ghcr.io-autamus-spades-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### ghcr.io-autamus-spades-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### ghcr.io-autamus-spades-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ghcr.io-autamus-spades-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### spades.py
       
```bash
$ singularity exec <container> /opt/view/bin/spades.py
```


#### spades-bwa
       
```bash
$ singularity exec <container> /opt/view/bin/spades-bwa
```


#### spades-gbuilder
       
```bash
$ singularity exec <container> /opt/view/bin/spades-gbuilder
```


#### spades-ionhammer
       
```bash
$ singularity exec <container> /opt/view/bin/spades-ionhammer
```


#### spades-truseq-scfcorrection
       
```bash
$ singularity exec <container> /opt/view/bin/spades-truseq-scfcorrection
```


#### spades-convert-bin-to-fasta
       
```bash
$ singularity exec <container> /opt/view/bin/spades-convert-bin-to-fasta
```


#### spades-gmapper
       
```bash
$ singularity exec <container> /opt/view/bin/spades-gmapper
```


#### spades-kmer-estimating
       
```bash
$ singularity exec <container> /opt/view/bin/spades-kmer-estimating
```


#### spades-core
       
```bash
$ singularity exec <container> /opt/view/bin/spades-core
```


#### spades-gsimplifier
       
```bash
$ singularity exec <container> /opt/view/bin/spades-gsimplifier
```


#### spades-kmercount
       
```bash
$ singularity exec <container> /opt/view/bin/spades-kmercount
```


#### spades-corrector-core
       
```bash
$ singularity exec <container> /opt/view/bin/spades-corrector-core
```


#### spades-hammer
       
```bash
$ singularity exec <container> /opt/view/bin/spades-hammer
```


#### spaligner
       
```bash
$ singularity exec <container> /opt/view/bin/spaligner
```


#### spades-read-filter
       
```bash
$ singularity exec <container> /opt/view/bin/spades-read-filter
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