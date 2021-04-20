---
layout: container
name:  "nvcr.io/nvidia-hpcvis/paraview"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/nvcr.io/nvidia-hpcvis/paraview/container.yaml"
updated_at: "2021-04-20 03:16:54.138374"
container_url: ""
aliases:
 - "pvdataserver"

 - "pvrenderserver"

 - "pvbatch"

 - "pypython"

 - "pvserver"

versions:
 - "egl-py3-5.9.0"
description: "ParaView is one of the most popular visualization software for analyzing HPC datasets."
---

This module is a singularity container wrapper for nvcr.io/nvidia-hpcvis/paraview.
ParaView is one of the most popular visualization software for analyzing HPC datasets.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install nvcr.io/nvidia-hpcvis/paraview
```

Or a specific version:

```bash
$ shpc install nvcr.io/nvidia-hpcvis/paraview:egl-py3-5.9.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load nvcr.io/nvidia-hpcvis/paraview/egl-py3-5.9.0
$ module help nvcr.io/nvidia-hpcvis/paraview/egl-py3-5.9.0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### nvcr.io-nvidia-hpcvis-paraview-run:

```bash
$ singularity run <container>
```

#### nvcr.io-nvidia-hpcvis-paraview-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### nvcr.io-nvidia-hpcvis-paraview-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### nvcr.io-nvidia-hpcvis-paraview-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### nvcr.io-nvidia-hpcvis-paraview-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pvdataserver
       
```bash
$ singularity exec <container> /opt/paraview/bin/pvdataserver
```


#### pvrenderserver
       
```bash
$ singularity exec <container> /opt/paraview/bin/pvrenderserver
```


#### pvbatch
       
```bash
$ singularity exec <container> /opt/paraview/bin/pvbatch
```


#### pypython
       
```bash
$ singularity exec <container> /opt/paraview/bin/pvpython
```


#### pvserver
       
```bash
$ singularity exec <container> /opt/paraview/bin/pvserver
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