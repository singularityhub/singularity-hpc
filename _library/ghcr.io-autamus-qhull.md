---
layout: container
name:  "ghcr.io/autamus/qhull"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/qhull/container.yaml"
updated_at: "2021-05-10 15:19:12.800214"
container_url: "https://github.com/orgs/autamus/packages/container/package/qhull"
aliases:
 - "qconvex"

 - "qdelaunay"

 - "qhalf"

 - "qhull"

 - "qvoronoi"

 - "rbox"

versions:
 - "2020.1"
 - "latest"
description: "Snappy (previously known as Zippy) is a fast data compression and decompression library written in C++ by Google based on ideas from LZ77 and open-sourced in 2011."
---

This module is a singularity container wrapper for ghcr.io/autamus/qhull.
Snappy (previously known as Zippy) is a fast data compression and decompression library written in C++ by Google based on ideas from LZ77 and open-sourced in 2011.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install ghcr.io/autamus/qhull
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/qhull:2020.1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/qhull/2020.1
$ module help ghcr.io/autamus/qhull/2020.1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### ghcr.io-autamus-qhull-run:

```bash
$ singularity run <container>
```

#### ghcr.io-autamus-qhull-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### ghcr.io-autamus-qhull-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### ghcr.io-autamus-qhull-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ghcr.io-autamus-qhull-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### qconvex
       
```bash
$ singularity exec <container> /opt/view/bin/qconvex
```


#### qdelaunay
       
```bash
$ singularity exec <container> /opt/view/bin/qdelaunay
```


#### qhalf
       
```bash
$ singularity exec <container> /opt/view/bin/qhalf
```


#### qhull
       
```bash
$ singularity exec <container> /opt/view/bin/qhull
```


#### qvoronoi
       
```bash
$ singularity exec <container> /opt/view/bin/qvoronoi
```


#### rbox
       
```bash
$ singularity exec <container> /opt/view/bin/rbox
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