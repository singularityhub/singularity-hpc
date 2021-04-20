---
layout: container
name:  "ghcr.io/autamus/beast2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/beast2/container.yaml"
updated_at: "2021-04-20 02:23:57.517049"
container_url: ""
aliases:
 - "beast"

 - "beasti"

 - "beauti"

 - "densitree"

 - "treeannotator"

versions:
 - "2.6.3"
 - "latest"
description: "BEAST 2 is a cross-platform program for Bayesian phylogenetic analysis of molecular sequences."
---

This module is a singularity container wrapper for ghcr.io/autamus/beast2.
BEAST 2 is a cross-platform program for Bayesian phylogenetic analysis of molecular sequences.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install ghcr.io/autamus/beast2
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/beast2:2.6.3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/beast2/2.6.3
$ module help ghcr.io/autamus/beast2/2.6.3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### ghcr.io-autamus-beast2-run:

```bash
$ singularity run <container>
```

#### ghcr.io-autamus-beast2-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### ghcr.io-autamus-beast2-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### ghcr.io-autamus-beast2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ghcr.io-autamus-beast2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### beast
       
```bash
$ singularity exec <container> /opt/view/bin/beast
```


#### beasti
       
```bash
$ singularity exec <container> /opt/view/bin/beasti
```


#### beauti
       
```bash
$ singularity exec <container> /opt/view/bin/beauti
```


#### densitree
       
```bash
$ singularity exec <container> /opt/view/bin/densitree
```


#### treeannotator
       
```bash
$ singularity exec <container> /opt/view/bin/treeannotator
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