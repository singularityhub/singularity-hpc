---
layout: container
name:  "biocontainers/bowtie2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/biocontainers/bowtie2/container.yaml"
updated_at: "2021-04-19 23:54:55.086460"
container_url: ""
aliases:
 - "bowtie2"

 - "bowtie2-inspect"

 - "bowtie2-build"

versions:
 - "v2.4.1_cv1"
description: "Bowtie 2 is an ultrafast and memory-efficient tool for aligning sequencing reads to long reference sequences."
---

This module is a singularity container wrapper for biocontainers/bowtie2.
Bowtie 2 is an ultrafast and memory-efficient tool for aligning sequencing reads to long reference sequences.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install biocontainers/bowtie2
```

Or a specific version:

```bash
$ shpc install biocontainers/bowtie2:v2.4.1_cv1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load biocontainers/bowtie2/v2.4.1_cv1
$ module help biocontainers/bowtie2/v2.4.1_cv1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### biocontainers-bowtie2-run:

```bash
$ singularity run <container>
```

#### biocontainers-bowtie2-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### biocontainers-bowtie2-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### biocontainers-bowtie2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### biocontainers-bowtie2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bowtie2
       
```bash
$ singularity exec <container> /usr/local/bin/bowtie2
```


#### bowtie2-inspect
       
```bash
$ singularity exec <container> /usr/local/bin/bowtie2-inspect
```


#### bowtie2-build
       
```bash
$ singularity exec <container> /usr/local/bin/bowtie2-build
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