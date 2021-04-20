---
layout: container
name:  "nvcr.io/nvidia/caffe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/nvcr.io/nvidia/caffe/container.yaml"
updated_at: "2021-04-20 03:18:02.667757"
container_url: ""
aliases:
 - "python"

versions:
 - "20.03-py3"
description: "NVIDIA Caffe, also known as NVCaffe, is an NVIDIA-maintained fork of Berkeley Vision and Learning Center (BVLC) Caffe tuned for NVIDIA GPUs, particularly in multi-GPU configurations."
---

This module is a singularity container wrapper for nvcr.io/nvidia/caffe.
NVIDIA Caffe, also known as NVCaffe, is an NVIDIA-maintained fork of Berkeley Vision and Learning Center (BVLC) Caffe tuned for NVIDIA GPUs, particularly in multi-GPU configurations.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install nvcr.io/nvidia/caffe
```

Or a specific version:

```bash
$ shpc install nvcr.io/nvidia/caffe:20.03-py3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load nvcr.io/nvidia/caffe/20.03-py3
$ module help nvcr.io/nvidia/caffe/20.03-py3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### nvcr.io-nvidia-caffe-run:

```bash
$ singularity run <container>
```

#### nvcr.io-nvidia-caffe-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### nvcr.io-nvidia-caffe-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### nvcr.io-nvidia-caffe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### nvcr.io-nvidia-caffe-inspect-deffile:

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