---
layout: container
name:  "nvcr.io/nvidia/pytorch"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/nvcr.io/nvidia/pytorch/container.yaml"
updated_at: "2021-04-11 17:00:22.075672"
container_url: ""

versions:
 - "21.02-py3"
---

This module is a singularity container wrapper for nvcr.io/nvidia/pytorch.
PyTorch is a GPU accelerated tensor computational framework with a Python front end. Functionality can be easily extended with common Python libraries such as NumPy, SciPy, and Cython. Automatic differentiation is done with a tape-based system at both a functional and neural network layer level.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install nvcr.io/nvidia/pytorch
```

Or a specific version:

```bash
$ shpc install nvcr.io/nvidia/pytorch:21.02-py3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load nvcr.io/nvidia/pytorch/21.02-py3
$ module help nvcr.io/nvidia/pytorch/21.02-py3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### nvcr.io-nvidia-pytorch-run:

```bash
$ singularity run <container>
```

#### nvcr.io-nvidia-pytorch-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### nvcr.io-nvidia-pytorch-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### nvcr.io-nvidia-pytorch-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### nvcr.io-nvidia-pytorch-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### nvcr.io-nvidia-pytorch

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