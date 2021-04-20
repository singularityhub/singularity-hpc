---
layout: container
name:  "biocontainers/plink1.9"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/biocontainers/plink1.9/container.yaml"
updated_at: "2021-04-20 03:12:59.313981"
container_url: ""
aliases:
 - "plink"

versions:
 - "v1.90b6.6-181012-1-deb_cv1"
description: "An update to PLINK, a free, open-source whole genome association analysis toolset, designed to perform a range of basic, large-scale analyses in a computationally efficient manner."
---

This module is a singularity container wrapper for biocontainers/plink1.9.
An update to PLINK, a free, open-source whole genome association analysis toolset, designed to perform a range of basic, large-scale analyses in a computationally efficient manner.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install biocontainers/plink1.9
```

Or a specific version:

```bash
$ shpc install biocontainers/plink1.9:v1.90b6.6-181012-1-deb_cv1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load biocontainers/plink1.9/v1.90b6.6-181012-1-deb_cv1
$ module help biocontainers/plink1.9/v1.90b6.6-181012-1-deb_cv1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### biocontainers-plink1.9-run:

```bash
$ singularity run <container>
```

#### biocontainers-plink1.9-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### biocontainers-plink1.9-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### biocontainers-plink1.9-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### biocontainers-plink1.9-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### plink
       
```bash
$ singularity exec <container> /usr/bin/plink1.9
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