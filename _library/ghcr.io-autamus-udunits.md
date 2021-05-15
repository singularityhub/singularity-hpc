---
layout: container
name:  "ghcr.io/autamus/udunits"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/udunits/container.yaml"
updated_at: "2021-05-15 14:10:11.474214"
container_url: "https://github.com/orgs/autamus/packages/container/package/udunits"
aliases:
 - "udunits2"

versions:
 - "2.2.28"
 - "latest"
description: "The UDUNITS package supports units of physical quantities. Its C library provides for arithmetic manipulation of units and for conversion of numeric values between compatible units."
---

This module is a singularity container wrapper for ghcr.io/autamus/udunits.
The UDUNITS package supports units of physical quantities. Its C library provides for arithmetic manipulation of units and for conversion of numeric values between compatible units.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install ghcr.io/autamus/udunits
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/udunits:2.2.28
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/udunits/2.2.28
$ module help ghcr.io/autamus/udunits/2.2.28
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### ghcr.io-autamus-udunits-run:

```bash
$ singularity run <container>
```

#### ghcr.io-autamus-udunits-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### ghcr.io-autamus-udunits-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### ghcr.io-autamus-udunits-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ghcr.io-autamus-udunits-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### udunits2
       
```bash
$ singularity exec <container> /opt/view/bin/udunits2
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