---
layout: container
name:  "bids/broccoli"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/bids/broccoli/container.yaml"
updated_at: "2021-04-20 03:18:58.882653"
container_url: ""

versions:
 - "enh_v"
description: "BROCCOLI is a software for analysis of fMRI (functional magnetic resonance imaging) data and is written in OpenCL (Open Computing Language).  (https://github.com/BIDS-Apps/BROCCOLI)"
---

This module is a singularity container wrapper for bids/broccoli.
BROCCOLI is a software for analysis of fMRI (functional magnetic resonance imaging) data and is written in OpenCL (Open Computing Language).  (https://github.com/BIDS-Apps/BROCCOLI)
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install bids/broccoli
```

Or a specific version:

```bash
$ shpc install bids/broccoli:enh_v
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load bids/broccoli/enh_v
$ module help bids/broccoli/enh_v
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### bids-broccoli-run:

```bash
$ singularity run <container>
```

#### bids-broccoli-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### bids-broccoli-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### bids-broccoli-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bids-broccoli-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bids-broccoli

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