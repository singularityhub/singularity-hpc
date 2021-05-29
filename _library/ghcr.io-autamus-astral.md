---
layout: container
name:  "ghcr.io/autamus/astral"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/astral/container.yaml"
updated_at: "2021-05-29 01:53:08.678236"
container_url: "https://github.com/orgs/autamus/packages/container/package/astral"
aliases:
 - "astral"

versions:
 - "5.7.1"
 - "latest"
description: "ASTRAL is a tool for estimating an unrooted species tree given a set of unrooted gene trees."
---

This module is a singularity container wrapper for ghcr.io/autamus/astral.
ASTRAL is a tool for estimating an unrooted species tree given a set of unrooted gene trees.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install ghcr.io/autamus/astral
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/astral:5.7.1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/astral/5.7.1
$ module help ghcr.io/autamus/astral/5.7.1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### ghcr.io-autamus-astral-run:

```bash
$ singularity run <container>
```

#### ghcr.io-autamus-astral-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### ghcr.io-autamus-astral-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### ghcr.io-autamus-astral-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ghcr.io-autamus-astral-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### astral
       
```bash
$ singularity exec <container> /opt/view/bin/astral
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