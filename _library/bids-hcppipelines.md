---
layout: container
name:  "bids/hcppipelines"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/bids/hcppipelines/container.yaml"
updated_at: "2021-04-18 06:36:57.392070"
container_url: ""

versions:
 - "latest"
description: "BIDS-ified HPC Piplines to process MRI data for the Human Connectome Project (https://github.com/BIDS-Apps/HCPPipelines)"
---

This module is a singularity container wrapper for bids/hcppipelines.
BIDS-ified HPC Piplines to process MRI data for the Human Connectome Project (https://github.com/BIDS-Apps/HCPPipelines)
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install bids/hcppipelines
```

Or a specific version:

```bash
$ shpc install bids/hcppipelines:latest
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load bids/hcppipelines/latest
$ module help bids/hcppipelines/latest
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### bids-hcppipelines-run:

```bash
$ singularity run <container>
```

#### bids-hcppipelines-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### bids-hcppipelines-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### bids-hcppipelines-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bids-hcppipelines-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bids-hcppipelines

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