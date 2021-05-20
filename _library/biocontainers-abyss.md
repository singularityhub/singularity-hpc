---
layout: container
name:  "biocontainers/abyss"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/biocontainers/abyss/container.yaml"
updated_at: "2021-05-20 15:24:49.813573"
container_url: "https://hub.docker.com/r/biocontainers/abyss"
aliases:
 - "abyss-fixmate"

 - "abyss-pe"

versions:
 - "v2.1.5-7-deb_cv1"
description: "A de novo, parallel, paired-end sequence assembler that is designed for short reads. See https://www.bcgsc.ca/resources/software/abyss."
---

This module is a singularity container wrapper for biocontainers/abyss.
A de novo, parallel, paired-end sequence assembler that is designed for short reads. See https://www.bcgsc.ca/resources/software/abyss.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install biocontainers/abyss
```

Or a specific version:

```bash
$ shpc install biocontainers/abyss:v2.1.5-7-deb_cv1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load biocontainers/abyss/v2.1.5-7-deb_cv1
$ module help biocontainers/abyss/v2.1.5-7-deb_cv1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### biocontainers-abyss-run:

```bash
$ singularity run <container>
```

#### biocontainers-abyss-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### biocontainers-abyss-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### biocontainers-abyss-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### biocontainers-abyss-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### abyss-fixmate
       
```bash
$ singularity exec <container> /usr/bin/abyss-fixmate
```


#### abyss-pe
       
```bash
$ singularity exec <container> /usr/bin/abyss-pe
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