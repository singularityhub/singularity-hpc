---
layout: container
name:  "ghcr.io/autamus/libxpm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/libxpm/container.yaml"
updated_at: "2021-04-20 03:16:45.343989"
container_url: ""

versions:
 - "latest"
description: "The X PixMap image format is an extension of the monochrome X BitMap format specified in the X protocol, and is commonly used in traditional X applications."
---

This module is a singularity container wrapper for ghcr.io/autamus/libxpm.
The X PixMap image format is an extension of the monochrome X BitMap format specified in the X protocol, and is commonly used in traditional X applications.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install ghcr.io/autamus/libxpm
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/libxpm:latest
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/libxpm/latest
$ module help ghcr.io/autamus/libxpm/latest
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### ghcr.io-autamus-libxpm-run:

```bash
$ singularity run <container>
```

#### ghcr.io-autamus-libxpm-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### ghcr.io-autamus-libxpm-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### ghcr.io-autamus-libxpm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ghcr.io-autamus-libxpm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### ghcr.io-autamus-libxpm

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