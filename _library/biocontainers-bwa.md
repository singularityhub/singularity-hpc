---
layout: container
name:  "biocontainers/bwa"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/biocontainers/bwa/container.yaml"
updated_at: "2021-04-18 08:29:03.477544"
container_url: ""
aliases:
 - "bwa"

versions:
 - "0.7.15"
 - "v0.7.17_cv1"
description: "BWA is a software package for mapping low-divergent sequences against a large reference genome, such as the human genome."
---

This module is a singularity container wrapper for biocontainers/bwa.
BWA is a software package for mapping low-divergent sequences against a large reference genome, such as the human genome.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install biocontainers/bwa
```

Or a specific version:

```bash
$ shpc install biocontainers/bwa:0.7.15
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load biocontainers/bwa/0.7.15
$ module help biocontainers/bwa/0.7.15
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### biocontainers-bwa-run:

```bash
$ singularity run <container>
```

#### biocontainers-bwa-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### biocontainers-bwa-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### biocontainers-bwa-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### biocontainers-bwa-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bwa
       
```bash
$ singularity exec <container> /opt/conda/bin/bwa
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