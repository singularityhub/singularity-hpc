---
layout: container
name:  "bids/spm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/bids/spm/container.yaml"
updated_at: "2021-05-09 15:34:35.168004"
container_url: "https://hub.docker.com/r/bids/spm"
aliases:
 - "spm12"

versions:
 - "latest"
 - "v0.0.20"
description: "The implementation of the theoretical concepts of Statistical Parametric Mapping in a complete analysis package."
---

This module is a singularity container wrapper for bids/spm.
The implementation of the theoretical concepts of Statistical Parametric Mapping in a complete analysis package.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install bids/spm
```

Or a specific version:

```bash
$ shpc install bids/spm:latest
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load bids/spm/latest
$ module help bids/spm/latest
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### bids-spm-run:

```bash
$ singularity run <container>
```

#### bids-spm-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### bids-spm-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### bids-spm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bids-spm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### spm12
       
```bash
$ singularity exec <container> /opt/spm12/spm12
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