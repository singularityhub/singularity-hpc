---
layout: container
name:  "biocontainers/tabix"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/biocontainers/tabix/container.yaml"
updated_at: "2021-04-18 21:15:30.207789"
container_url: ""
aliases:
 - "tabix"

versions:
 - "v1.9-11-deb_cv1"
description: "Fast retrieval of sequence features from generic TAB-delimited files."
---

This module is a singularity container wrapper for biocontainers/tabix.
Fast retrieval of sequence features from generic TAB-delimited files.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install biocontainers/tabix
```

Or a specific version:

```bash
$ shpc install biocontainers/tabix:v1.9-11-deb_cv1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load biocontainers/tabix/v1.9-11-deb_cv1
$ module help biocontainers/tabix/v1.9-11-deb_cv1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### biocontainers-tabix-run:

```bash
$ singularity run <container>
```

#### biocontainers-tabix-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### biocontainers-tabix-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### biocontainers-tabix-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### biocontainers-tabix-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### tabix
       
```bash
$ singularity exec <container> /usr/bin/tabix
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