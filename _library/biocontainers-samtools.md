---
layout: container
name:  "biocontainers/samtools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/biocontainers/samtools/container.yaml"
updated_at: "2021-04-20 02:19:30.415056"
container_url: ""
aliases:
 - "samtools"

versions:
 - "v1.9-4-deb_cv1"
description: "Samtools is a suite of programs for interacting with high-throughput sequencing data."
---

This module is a singularity container wrapper for biocontainers/samtools.
Samtools is a suite of programs for interacting with high-throughput sequencing data.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install biocontainers/samtools
```

Or a specific version:

```bash
$ shpc install biocontainers/samtools:v1.9-4-deb_cv1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load biocontainers/samtools/v1.9-4-deb_cv1
$ module help biocontainers/samtools/v1.9-4-deb_cv1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### biocontainers-samtools-run:

```bash
$ singularity run <container>
```

#### biocontainers-samtools-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### biocontainers-samtools-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### biocontainers-samtools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### biocontainers-samtools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### samtools
       
```bash
$ singularity exec <container> /usr/bin/samtools
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