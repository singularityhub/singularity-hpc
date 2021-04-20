---
layout: container
name:  "ghcr.io/autamus/mpfr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/mpfr/container.yaml"
updated_at: "2021-04-20 02:48:48.181415"
container_url: ""

versions:
 - "latest"
description: "The MPFR library is a C library for multiple-precision floating-point computations with correct rounding."
---

This module is a singularity container wrapper for ghcr.io/autamus/mpfr.
The MPFR library is a C library for multiple-precision floating-point computations with correct rounding.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install ghcr.io/autamus/mpfr
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/mpfr:latest
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/mpfr/latest
$ module help ghcr.io/autamus/mpfr/latest
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### ghcr.io-autamus-mpfr-run:

```bash
$ singularity run <container>
```

#### ghcr.io-autamus-mpfr-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### ghcr.io-autamus-mpfr-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### ghcr.io-autamus-mpfr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ghcr.io-autamus-mpfr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### ghcr.io-autamus-mpfr

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