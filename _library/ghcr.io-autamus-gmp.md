---
layout: container
name:  "ghcr.io/autamus/gmp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/gmp/container.yaml"
updated_at: "2021-05-07 08:58:42.807252"
container_url: ""
aliases:
 - "curl"

versions:
 - "6.2.1"
 - "latest"
description: "GMP is a free library for arbitrary precision arithmetic, operating on signed integers, rational numbers, and floating-point numbers."
---

This module is a singularity container wrapper for ghcr.io/autamus/gmp.
GMP is a free library for arbitrary precision arithmetic, operating on signed integers, rational numbers, and floating-point numbers.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install ghcr.io/autamus/gmp
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/gmp:6.2.1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/gmp/6.2.1
$ module help ghcr.io/autamus/gmp/6.2.1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### ghcr.io-autamus-gmp-run:

```bash
$ singularity run <container>
```

#### ghcr.io-autamus-gmp-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### ghcr.io-autamus-gmp-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### ghcr.io-autamus-gmp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ghcr.io-autamus-gmp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### curl
       
```bash
$ singularity exec <container> /opt/view/bin/curl
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