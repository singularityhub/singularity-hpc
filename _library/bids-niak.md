---
layout: container
name:  "bids/niak"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/bids/niak/container.yaml"
updated_at: "2021-04-20 02:17:28.407341"
container_url: ""

versions:
 - "latest"
description: "The neuroimaging analysis kit. Pipeline for preprocessing of fMRI and structural MRI scans http://niak.simexp-lab.org/ (https://github.com/BIDS-Apps/niak)"
---

This module is a singularity container wrapper for bids/niak.
The neuroimaging analysis kit. Pipeline for preprocessing of fMRI and structural MRI scans http://niak.simexp-lab.org/ (https://github.com/BIDS-Apps/niak)
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install bids/niak
```

Or a specific version:

```bash
$ shpc install bids/niak:latest
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load bids/niak/latest
$ module help bids/niak/latest
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### bids-niak-run:

```bash
$ singularity run <container>
```

#### bids-niak-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### bids-niak-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### bids-niak-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bids-niak-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bids-niak

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