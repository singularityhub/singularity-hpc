---
layout: container
name:  "ghcr.io/autamus/htslib"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/htslib/container.yaml"
updated_at: "2021-04-20 03:16:08.807144"
container_url: ""
aliases:
 - "htsfile"

versions:
 - "latest"
description: "A C library for reading/writing high-throughput sequencing data."
---

This module is a singularity container wrapper for ghcr.io/autamus/htslib.
A C library for reading/writing high-throughput sequencing data.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install ghcr.io/autamus/htslib
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/htslib:latest
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/htslib/latest
$ module help ghcr.io/autamus/htslib/latest
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### ghcr.io-autamus-htslib-run:

```bash
$ singularity run <container>
```

#### ghcr.io-autamus-htslib-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### ghcr.io-autamus-htslib-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### ghcr.io-autamus-htslib-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ghcr.io-autamus-htslib-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### htsfile
       
```bash
$ singularity exec <container> /opt/view/bin/htsfile
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