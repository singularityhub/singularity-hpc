---
layout: container
name:  "nvcr.io/nvidia-hpcvis/paraview"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/nvcr.io/nvidia-hpcvis/paraview/container.yaml"
updated_at: "2021-07-20 19:36:43.234324"
container_url: "https://ngc.nvidia.com/catalog/containers/nvidia-hpcvis:paraview/tags"
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

When you install this module, you'll be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### -run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### -shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### -exec:

```bash
$ singularity exec -s /bin/sh <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### -inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### -inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### -inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pvdataserver
       
```bash
$ singularity exec <container> /opt/paraview/bin/pvdataserver
$ podman run --it --rm --entrypoint /opt/paraview/bin/pvdataserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/paraview/bin/pvdataserver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pvrenderserver
       
```bash
$ singularity exec <container> /opt/paraview/bin/pvrenderserver
$ podman run --it --rm --entrypoint /opt/paraview/bin/pvrenderserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/paraview/bin/pvrenderserver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pvbatch
       
```bash
$ singularity exec <container> /opt/paraview/bin/pvbatch
$ podman run --it --rm --entrypoint /opt/paraview/bin/pvbatch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/paraview/bin/pvbatch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pypython
       
```bash
$ singularity exec <container> /opt/paraview/bin/pvpython
$ podman run --it --rm --entrypoint /opt/paraview/bin/pvpython   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/paraview/bin/pvpython   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pvserver
       
```bash
$ singularity exec <container> /opt/paraview/bin/pvserver
$ podman run --it --rm --entrypoint /opt/paraview/bin/pvserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/paraview/bin/pvserver   -v ${PWD} -w ${PWD} <container> -c " $@"
```



In the above, the `<container>` directive will reference an actual container provided
by the module, for the version you have chosen to load. An environment file in the
module folder will also be bound. Note that although a container
might provide custom commands, every container exposes unique exec, shell, run, and
inspect aliases. For anycommands above, you can export:

 - SINGULARITY_OPTS: to define custom options for singularity (e.g., --debug)
 - SINGULARITY_COMMAND_OPTS: to define custom options for the command (e.g., -b)
 - PODMAN_OPTS: to define custom options for podman or docker
 - PODMAN_COMMAND_OPTS: to define custom options for the command

<br>
  
### Install

You can install shpc locally (for yourself or your user base) as follows:

```bash
$ git clone https://github.com/singularityhub/singularity-hpc
$ cd singularity-hpc
$ pip install -e .
```

Have any questions, or want to request a new module or version? [ask for help!](https://github.com/singularityhub/singularity-hpc/issues)