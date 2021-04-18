---
layout: container
name:  "poldracklab/mriqc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/poldracklab/mriqc/container.yaml"
updated_at: "2021-04-18 08:28:06.838878"
container_url: ""
aliases:
 - "mriqc"

versions:
 - "0.16.1"
description: "Automatic prediction of quality and visual reporting of MRI scans."
---

This module is a singularity container wrapper for poldracklab/mriqc.
Automatic prediction of quality and visual reporting of MRI scans.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install poldracklab/mriqc
```

Or a specific version:

```bash
$ shpc install poldracklab/mriqc:0.16.1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load poldracklab/mriqc/0.16.1
$ module help poldracklab/mriqc/0.16.1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### poldracklab-mriqc-run:

```bash
$ singularity run <container>
```

#### poldracklab-mriqc-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### poldracklab-mriqc-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### poldracklab-mriqc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### poldracklab-mriqc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### mriqc
       
```bash
$ singularity exec <container> /usr/local/miniconda/bin/mriqc
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