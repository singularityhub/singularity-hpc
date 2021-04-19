---
layout: container
name:  "ghcr.io/autamus/geos"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/geos/container.yaml"
updated_at: "2021-04-19 23:55:02.455111"
container_url: ""
aliases:
 - "geos-config"

versions:
 - "latest"
description: "GEOS is a C++11 library for performing operations on two-dimensional vector geometries."
---

This module is a singularity container wrapper for ghcr.io/autamus/geos.
GEOS is a C++11 library for performing operations on two-dimensional vector geometries.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install ghcr.io/autamus/geos
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/geos:latest
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/geos/latest
$ module help ghcr.io/autamus/geos/latest
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### ghcr.io-autamus-geos-run:

```bash
$ singularity run <container>
```

#### ghcr.io-autamus-geos-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### ghcr.io-autamus-geos-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### ghcr.io-autamus-geos-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ghcr.io-autamus-geos-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### geos-config
       
```bash
$ singularity exec <container> /opt/view/bin/geos-config
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