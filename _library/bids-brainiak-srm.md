---
layout: container
name:  "bids/brainiak-srm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/bids/brainiak-srm/container.yaml"
updated_at: "2021-04-20 00:26:22.004812"
container_url: ""

versions:
 - "latest"
description: "Shared Response Model (SRM) from the Brain Imaging Analysis Kit (BrainIAK) (https://github.com/BIDS-Apps/brainiak-srm)"
---

This module is a singularity container wrapper for bids/brainiak-srm.
Shared Response Model (SRM) from the Brain Imaging Analysis Kit (BrainIAK) (https://github.com/BIDS-Apps/brainiak-srm)
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install bids/brainiak-srm
```

Or a specific version:

```bash
$ shpc install bids/brainiak-srm:latest
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load bids/brainiak-srm/latest
$ module help bids/brainiak-srm/latest
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### bids-brainiak-srm-run:

```bash
$ singularity run <container>
```

#### bids-brainiak-srm-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### bids-brainiak-srm-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### bids-brainiak-srm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bids-brainiak-srm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bids-brainiak-srm

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