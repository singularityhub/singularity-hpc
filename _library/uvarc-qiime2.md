---
layout: container
name:  "uvarc/qiime2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/uvarc/qiime2/container.yaml"
updated_at: "2021-04-20 02:17:15.169090"
container_url: ""

versions:
 - "2020.8"
description: "QIIME2. Same functionality as the official image but less than half the size. Includes packages Empress and PICRUSt2."
---

This module is a singularity container wrapper for uvarc/qiime2.
QIIME2. Same functionality as the official image but less than half the size. Includes packages Empress and PICRUSt2.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install uvarc/qiime2
```

Or a specific version:

```bash
$ shpc install uvarc/qiime2:2020.8
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load uvarc/qiime2/2020.8
$ module help uvarc/qiime2/2020.8
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### uvarc-qiime2-run:

```bash
$ singularity run <container>
```

#### uvarc-qiime2-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### uvarc-qiime2-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### uvarc-qiime2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### uvarc-qiime2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### uvarc-qiime2

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