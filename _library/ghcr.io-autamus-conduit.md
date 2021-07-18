---
layout: container
name:  "ghcr.io/autamus/conduit"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/conduit/container.yaml"
updated_at: "2021-07-18 00:55:16.266316"
container_url: "https://github.com/orgs/autamus/packages/container/package/conduit"
aliases:
 - "conduit_blueprint_verify"

 - "conduit_relay_entangle.py"

 - "conduit_relay_io_convert"

 - "conduit_relay_io_ls"

 - "conduit_relay_node_viewer"

 - "conduit_staging"

 - "conduit_staging.sh"

versions:
 - "0.7.2"
description: "Conduit is an open source project from Lawrence Livermore National Laboratory that provides an intuitive model for describing hierarchical scientific data in C++, C, Fortran, and Python."
---

This module is a singularity container wrapper for ghcr.io/autamus/conduit.
Conduit is an open source project from Lawrence Livermore National Laboratory that provides an intuitive model for describing hierarchical scientific data in C++, C, Fortran, and Python.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install ghcr.io/autamus/conduit
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/conduit:0.7.2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/conduit/0.7.2
$ module help ghcr.io/autamus/conduit/0.7.2
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


#### conduit_blueprint_verify
       
```bash
$ singularity exec <container> /opt/view/bin/conduit_blueprint_verify
$ podman run --it --rm --entrypoint /opt/view/bin/conduit_blueprint_verify   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/conduit_blueprint_verify   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### conduit_relay_entangle.py
       
```bash
$ singularity exec <container> /opt/view/bin/conduit_relay_entangle.py
$ podman run --it --rm --entrypoint /opt/view/bin/conduit_relay_entangle.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/conduit_relay_entangle.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### conduit_relay_io_convert
       
```bash
$ singularity exec <container> /opt/view/bin/conduit_relay_io_convert
$ podman run --it --rm --entrypoint /opt/view/bin/conduit_relay_io_convert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/conduit_relay_io_convert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### conduit_relay_io_ls
       
```bash
$ singularity exec <container> /opt/view/bin/conduit_relay_io_ls
$ podman run --it --rm --entrypoint /opt/view/bin/conduit_relay_io_ls   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/conduit_relay_io_ls   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### conduit_relay_node_viewer
       
```bash
$ singularity exec <container> /opt/view/bin/conduit_relay_node_viewer
$ podman run --it --rm --entrypoint /opt/view/bin/conduit_relay_node_viewer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/conduit_relay_node_viewer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### conduit_staging
       
```bash
$ singularity exec <container> /opt/view/bin/conduit_staging
$ podman run --it --rm --entrypoint /opt/view/bin/conduit_staging   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/conduit_staging   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### conduit_staging.sh
       
```bash
$ singularity exec <container> /opt/view/bin/conduit_staging.sh
$ podman run --it --rm --entrypoint /opt/view/bin/conduit_staging.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/conduit_staging.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
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