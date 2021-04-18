---
layout: container
name:  "ghcr.io/autamus/fastqc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/fastqc/container.yaml"
updated_at: "2021-04-18 20:39:43.154885"
container_url: ""
aliases:
 - "fastqc"

versions:
 - "latest"
description: "A quality control tool for high throughput sequence data."
---

This module is a singularity container wrapper for ghcr.io/autamus/fastqc.
A quality control tool for high throughput sequence data.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install ghcr.io/autamus/fastqc
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/fastqc:latest
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/fastqc/latest
$ module help ghcr.io/autamus/fastqc/latest
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### ghcr.io-autamus-fastqc-run:

```bash
$ singularity run <container>
```

#### ghcr.io-autamus-fastqc-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### ghcr.io-autamus-fastqc-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### ghcr.io-autamus-fastqc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ghcr.io-autamus-fastqc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fastqc
       
```bash
$ singularity exec <container> /opt/view/bin/fastqc
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