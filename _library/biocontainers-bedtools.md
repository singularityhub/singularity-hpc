---
layout: container
name:  "biocontainers/bedtools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/biocontainers/bedtools/container.yaml"
updated_at: "2021-04-29 15:05:06.073629"
container_url: ""
aliases:
 - "bedtools"

versions:
 - "v2.27.1dfsg-4-deb_cv1"
description: "a powerful toolset for genome arithmetic"
---

This module is a singularity container wrapper for biocontainers/bedtools.
a powerful toolset for genome arithmetic
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install biocontainers/bedtools
```

Or a specific version:

```bash
$ shpc install biocontainers/bedtools:v2.27.1dfsg-4-deb_cv1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load biocontainers/bedtools/v2.27.1dfsg-4-deb_cv1
$ module help biocontainers/bedtools/v2.27.1dfsg-4-deb_cv1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### biocontainers-bedtools-run:

```bash
$ singularity run <container>
```

#### biocontainers-bedtools-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### biocontainers-bedtools-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### biocontainers-bedtools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### biocontainers-bedtools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bedtools
       
```bash
$ singularity exec <container> /usr/bin/bedtools
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