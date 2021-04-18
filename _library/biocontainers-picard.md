---
layout: container
name:  "biocontainers/picard"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/biocontainers/picard/container.yaml"
updated_at: "2021-04-18 12:53:05.262484"
container_url: ""
aliases:
 - "picard"

versions:
 - "v1.139_cv3"
description: "Java CLI tools for manipulating HTS data and formats"
---

This module is a singularity container wrapper for biocontainers/picard.
Java CLI tools for manipulating HTS data and formats
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install biocontainers/picard
```

Or a specific version:

```bash
$ shpc install biocontainers/picard:v1.139_cv3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load biocontainers/picard/v1.139_cv3
$ module help biocontainers/picard/v1.139_cv3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### biocontainers-picard-run:

```bash
$ singularity run <container>
```

#### biocontainers-picard-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### biocontainers-picard-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### biocontainers-picard-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### biocontainers-picard-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### picard
       
```bash
$ singularity exec <container> java -jar /opt/conda/bin/picard.jar
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