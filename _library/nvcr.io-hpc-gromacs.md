---
layout: container
name:  "nvcr.io/hpc/gromacs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/nvcr.io/hpc/gromacs/container.yaml"
updated_at: "2021-04-20 02:21:47.961620"
container_url: ""
aliases:
 - "python"

versions:
 - "2020.2"
description: "GROMACS is a popular molecular dynamics application used to simulate proteins and lipids."
---

This module is a singularity container wrapper for nvcr.io/hpc/gromacs.
GROMACS is a popular molecular dynamics application used to simulate proteins and lipids.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install nvcr.io/hpc/gromacs
```

Or a specific version:

```bash
$ shpc install nvcr.io/hpc/gromacs:2020.2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load nvcr.io/hpc/gromacs/2020.2
$ module help nvcr.io/hpc/gromacs/2020.2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### nvcr.io-hpc-gromacs-run:

```bash
$ singularity run <container>
```

#### nvcr.io-hpc-gromacs-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### nvcr.io-hpc-gromacs-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### nvcr.io-hpc-gromacs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### nvcr.io-hpc-gromacs-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### python
       
```bash
$ singularity exec --nv <container> /usr/bin/python
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