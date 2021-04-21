---
layout: container
name:  "ghcr.io/autamus/bart"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/bart/container.yaml"
updated_at: "2021-04-21 06:04:12.272764"
container_url: ""
aliases:
 - "bart"

 - "bartview"

versions:
 - "0.6.00"
 - "latest"
description: "BART: Toolbox for Computational Magnetic Resonance Imaging"
---

This module is a singularity container wrapper for ghcr.io/autamus/bart.
BART: Toolbox for Computational Magnetic Resonance Imaging
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install ghcr.io/autamus/bart
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/bart:0.6.00
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/bart/0.6.00
$ module help ghcr.io/autamus/bart/0.6.00
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### ghcr.io-autamus-bart-run:

```bash
$ singularity run <container>
```

#### ghcr.io-autamus-bart-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### ghcr.io-autamus-bart-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### ghcr.io-autamus-bart-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ghcr.io-autamus-bart-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bart
       
```bash
$ singularity exec <container> /opt/view/bin/bart
```


#### bartview
       
```bash
$ singularity exec <container> /opt/view/bin/bartview
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