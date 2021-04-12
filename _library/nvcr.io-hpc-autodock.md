---
layout: container
name:  "nvcr.io/hpc/autodock"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/nvcr.io/hpc/autodock/container.yaml"
updated_at: "2021-04-12 00:19:44.353169"
container_url: ""
aliases:
 - "autodock-gpu"

versions:
 - "2020.06"
---

This module is a singularity container wrapper for nvcr.io/hpc/autodock.
The AutoDock-GPU Suite is a growing collection of methods for computational docking and virtual screening, for use in structure-based drug discovery and exploration of the basic mechanisms of biomolecular structure and function. More info on AutoDock-GPU be located at https://ccsb.scripps.edu/autodock/ and https://github.com/ccsb-scripps/AutoDock-GPU#usage.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install nvcr.io/hpc/autodock
```

Or a specific version:

```bash
$ shpc install nvcr.io/hpc/autodock:2020.06
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load nvcr.io/hpc/autodock/2020.06
$ module help nvcr.io/hpc/autodock/2020.06
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### nvcr.io-hpc-autodock-run:

```bash
$ singularity run <container>
```

#### nvcr.io-hpc-autodock-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### nvcr.io-hpc-autodock-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### nvcr.io-hpc-autodock-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### nvcr.io-hpc-autodock-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### autodock-gpu
       
```bash
$ singularity exec --nv <container> /opt/AutoDock-GPU/bin/autodock_gpu_128wi
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