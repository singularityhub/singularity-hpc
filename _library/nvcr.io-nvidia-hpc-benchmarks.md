---
layout: container
name:  "nvcr.io/nvidia/hpc-benchmarks"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/nvcr.io/nvidia/hpc-benchmarks/container.yaml"
updated_at: "2021-05-22 15:47:00.963808"
container_url: "https://ngc.nvidia.com/catalog/containers/nvidia:hpc-benchmarks/tags"

versions:
 - "20.10-hpl"
description: "The NVIDIA HPC-Benchmarks collection provides three NVIDIA accelerated HPC benchmarks: HPL-NVIDIA, HPL-AI-NVIDIA, and HPCG-NVIDIA."
---

This module is a singularity container wrapper for nvcr.io/nvidia/hpc-benchmarks.
The NVIDIA HPC-Benchmarks collection provides three NVIDIA accelerated HPC benchmarks: HPL-NVIDIA, HPL-AI-NVIDIA, and HPCG-NVIDIA.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install nvcr.io/nvidia/hpc-benchmarks
```

Or a specific version:

```bash
$ shpc install nvcr.io/nvidia/hpc-benchmarks:20.10-hpl
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load nvcr.io/nvidia/hpc-benchmarks/20.10-hpl
$ module help nvcr.io/nvidia/hpc-benchmarks/20.10-hpl
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### nvcr.io-nvidia-hpc-benchmarks-run:

```bash
$ singularity run <container>
```

#### nvcr.io-nvidia-hpc-benchmarks-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### nvcr.io-nvidia-hpc-benchmarks-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### nvcr.io-nvidia-hpc-benchmarks-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### nvcr.io-nvidia-hpc-benchmarks-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### nvcr.io-nvidia-hpc-benchmarks

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