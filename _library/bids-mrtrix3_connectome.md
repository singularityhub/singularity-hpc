---
layout: container
name:  "bids/mrtrix3_connectome"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/bids/mrtrix3_connectome/container.yaml"
updated_at: "2021-04-18 16:56:04.328186"
container_url: ""

versions:
 - "latest"
description: "Generation and subsequent group analysis of structural connectomes generated from diffusion MRI data (via the MRtrix3 software package). https://github.com/BIDS-Apps/MRtrix3_connectome"
---

This module is a singularity container wrapper for bids/mrtrix3_connectome.
Generation and subsequent group analysis of structural connectomes generated from diffusion MRI data (via the MRtrix3 software package). https://github.com/BIDS-Apps/MRtrix3_connectome
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install bids/mrtrix3_connectome
```

Or a specific version:

```bash
$ shpc install bids/mrtrix3_connectome:latest
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load bids/mrtrix3_connectome/latest
$ module help bids/mrtrix3_connectome/latest
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### bids-mrtrix3_connectome-run:

```bash
$ singularity run <container>
```

#### bids-mrtrix3_connectome-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### bids-mrtrix3_connectome-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### bids-mrtrix3_connectome-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bids-mrtrix3_connectome-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bids-mrtrix3_connectome

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