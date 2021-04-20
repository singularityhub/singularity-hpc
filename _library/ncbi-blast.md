---
layout: container
name:  "ncbi/blast"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ncbi/blast/container.yaml"
updated_at: "2021-04-20 03:11:25.438213"
container_url: ""

versions:
 - "2.11.0"
 - "latest"
description: "The Basic Local Alignment Search Tool (BLAST) finds regions of local similarity between sequences."
---

This module is a singularity container wrapper for ncbi/blast.
The Basic Local Alignment Search Tool (BLAST) finds regions of local similarity between sequences.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install ncbi/blast
```

Or a specific version:

```bash
$ shpc install ncbi/blast:2.11.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ncbi/blast/2.11.0
$ module help ncbi/blast/2.11.0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### ncbi-blast-run:

```bash
$ singularity run <container>
```

#### ncbi-blast-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### ncbi-blast-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### ncbi-blast-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ncbi-blast-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### ncbi-blast

```bash
$ singularity run <container>
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