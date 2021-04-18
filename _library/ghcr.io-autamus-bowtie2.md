---
layout: container
name:  "ghcr.io/autamus/bowtie2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/bowtie2/container.yaml"
updated_at: "2021-04-18 08:04:35.640232"
container_url: ""
aliases:
 - "bowtie2"

 - "bowtie2-align-l"

 - "bowtie2-align-s"

 - "bowtie2-build"

 - "bowtie2-build-l"

 - "bowtie2-build-s"

 - "bowtie2-inspect"

 - "bowtie2-inspect-l"

 - "bowtie2-inspect-s"

versions:
 - "latest"
description: "Bowtie 2 is an ultrafast and memory-efficient tool for aligning sequencing reads to long reference sequences."
---

This module is a singularity container wrapper for ghcr.io/autamus/bowtie2.
Bowtie 2 is an ultrafast and memory-efficient tool for aligning sequencing reads to long reference sequences.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install ghcr.io/autamus/bowtie2
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/bowtie2:latest
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/bowtie2/latest
$ module help ghcr.io/autamus/bowtie2/latest
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### ghcr.io-autamus-bowtie2-run:

```bash
$ singularity run <container>
```

#### ghcr.io-autamus-bowtie2-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### ghcr.io-autamus-bowtie2-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### ghcr.io-autamus-bowtie2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ghcr.io-autamus-bowtie2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bowtie2
       
```bash
$ singularity exec <container> /opt/view/bin/bowtie2
```


#### bowtie2-align-l
       
```bash
$ singularity exec <container> /opt/view/bin/bowtie2-align-l
```


#### bowtie2-align-s
       
```bash
$ singularity exec <container> /opt/view/bin/bowtie2-align-s
```


#### bowtie2-build
       
```bash
$ singularity exec <container> /opt/view/bin/bowtie2-build
```


#### bowtie2-build-l
       
```bash
$ singularity exec <container> /opt/view/bin/bowtie2-build-l
```


#### bowtie2-build-s
       
```bash
$ singularity exec <container> /opt/view/bin/bowtie2-build-s
```


#### bowtie2-inspect
       
```bash
$ singularity exec <container> /opt/view/bin/bowtie2-inspect
```


#### bowtie2-inspect-l
       
```bash
$ singularity exec <container> /opt/view/bin/bowtie2-inspect-l
```


#### bowtie2-inspect-s
       
```bash
$ singularity exec <container> /opt/view/bin/bowtie2-inspect-s
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