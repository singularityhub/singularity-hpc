---
layout: container
name:  "ghcr.io/autamus/cfitsio"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/cfitsio/container.yaml"
updated_at: "2021-04-20 03:11:16.396758"
container_url: ""

versions:
 - "3.49"
 - "latest"
description: "CFITSIO is a library of C and Fortran subroutines for reading and writing data files in FITS (Flexible Image Transport System) data format."
---

This module is a singularity container wrapper for ghcr.io/autamus/cfitsio.
CFITSIO is a library of C and Fortran subroutines for reading and writing data files in FITS (Flexible Image Transport System) data format.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install ghcr.io/autamus/cfitsio
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/cfitsio:3.49
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/cfitsio/3.49
$ module help ghcr.io/autamus/cfitsio/3.49
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### ghcr.io-autamus-cfitsio-run:

```bash
$ singularity run <container>
```

#### ghcr.io-autamus-cfitsio-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### ghcr.io-autamus-cfitsio-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### ghcr.io-autamus-cfitsio-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ghcr.io-autamus-cfitsio-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### ghcr.io-autamus-cfitsio

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