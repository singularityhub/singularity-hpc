---
layout: container
name:  "ghcr.io/autamus/iq-tree"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/iq-tree/container.yaml"
updated_at: "2021-04-18 06:11:57.089313"
container_url: ""
aliases:
 - "iq-tree2"

versions:
 - "latest"
description: "IQ-TREE (http://www.iqtree.org, last accessed February 6, 2020) is a user-friendly and widely used software package for phylogenetic inference using maximum likelihood."
---

This module is a singularity container wrapper for ghcr.io/autamus/iq-tree.
IQ-TREE (http://www.iqtree.org, last accessed February 6, 2020) is a user-friendly and widely used software package for phylogenetic inference using maximum likelihood.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install ghcr.io/autamus/iq-tree
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/iq-tree:latest
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/iq-tree/latest
$ module help ghcr.io/autamus/iq-tree/latest
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### ghcr.io-autamus-iq-tree-run:

```bash
$ singularity run <container>
```

#### ghcr.io-autamus-iq-tree-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### ghcr.io-autamus-iq-tree-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### ghcr.io-autamus-iq-tree-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ghcr.io-autamus-iq-tree-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### iq-tree2
       
```bash
$ singularity exec <container> /opt/view/bin/iq-tree2
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