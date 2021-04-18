---
layout: container
name:  "quay.io/vgteam/vg"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/quay.io/vgteam/vg/container.yaml"
updated_at: "2021-04-18 06:37:35.095842"
container_url: ""
aliases:
 - "vg"

versions:
 - "latest"
description: "Tools for working with genomic variation graphs. https://github.com/vgteam/vg"
---

This module is a singularity container wrapper for quay.io/vgteam/vg.
Tools for working with genomic variation graphs. https://github.com/vgteam/vg
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install quay.io/vgteam/vg
```

Or a specific version:

```bash
$ shpc install quay.io/vgteam/vg:latest
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/vgteam/vg/latest
$ module help quay.io/vgteam/vg/latest
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### quay.io-vgteam-vg-run:

```bash
$ singularity run <container>
```

#### quay.io-vgteam-vg-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### quay.io-vgteam-vg-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### quay.io-vgteam-vg-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### quay.io-vgteam-vg-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### vg
       
```bash
$ singularity exec <container> /vg/bin/vg
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