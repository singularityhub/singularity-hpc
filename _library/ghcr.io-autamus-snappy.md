---
layout: container
name:  "ghcr.io/autamus/snappy"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/snappy/container.yaml"
updated_at: "2021-04-20 02:23:16.999650"
container_url: ""

versions:
 - "latest"
description: "Snappy (previously known as Zippy) is a fast data compression and decompression library written in C++ by Google based on ideas from LZ77 and open-sourced in 2011."
---

This module is a singularity container wrapper for ghcr.io/autamus/snappy.
Snappy (previously known as Zippy) is a fast data compression and decompression library written in C++ by Google based on ideas from LZ77 and open-sourced in 2011.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install ghcr.io/autamus/snappy
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/snappy:latest
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/snappy/latest
$ module help ghcr.io/autamus/snappy/latest
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### ghcr.io-autamus-snappy-run:

```bash
$ singularity run <container>
```

#### ghcr.io-autamus-snappy-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### ghcr.io-autamus-snappy-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### ghcr.io-autamus-snappy-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ghcr.io-autamus-snappy-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### ghcr.io-autamus-snappy

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