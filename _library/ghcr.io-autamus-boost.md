---
layout: container
name:  "ghcr.io/autamus/boost"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/boost/container.yaml"
updated_at: "2021-04-20 02:21:02.089926"
container_url: ""

versions:
 - "1.75.0"
 - "latest"
description: "The Boost project provides free peer-reviewed portable C++ source libraries."
---

This module is a singularity container wrapper for ghcr.io/autamus/boost.
The Boost project provides free peer-reviewed portable C++ source libraries.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install ghcr.io/autamus/boost
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/boost:1.75.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/boost/1.75.0
$ module help ghcr.io/autamus/boost/1.75.0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### ghcr.io-autamus-boost-run:

```bash
$ singularity run <container>
```

#### ghcr.io-autamus-boost-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### ghcr.io-autamus-boost-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### ghcr.io-autamus-boost-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ghcr.io-autamus-boost-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### ghcr.io-autamus-boost

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