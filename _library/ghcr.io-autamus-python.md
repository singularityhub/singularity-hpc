---
layout: container
name:  "ghcr.io/autamus/python"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/python/container.yaml"
updated_at: "2021-07-27 22:26:56.213305"
container_url: "https://github.com/orgs/autamus/packages/container/package/python"
aliases:
 - "pydoc3"

 - "pydoc3.8"

 - "python"

 - "python-config"

 - "python3"

 - "python3-config"

 - "python3.8"

 - "python3.8-config"

 - "python3.8-gdb.py"

versions:
 - "3.9.5"
 - "3.9.6"
 - "latest"
description: "An interpreted, high-level and general-purpose programming language."
---

This module is a singularity container wrapper for ghcr.io/autamus/python.
An interpreted, high-level and general-purpose programming language.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install ghcr.io/autamus/python
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/python:3.9.5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/python/3.9.5
$ module help ghcr.io/autamus/python/3.9.5
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


#### pydoc3
       
```bash
$ singularity exec <container> /opt/view/bin/pydoc3
$ podman run --it --rm --entrypoint /opt/view/bin/pydoc3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/pydoc3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.8
       
```bash
$ singularity exec <container> /opt/view/bin/pydoc3.8
$ podman run --it --rm --entrypoint /opt/view/bin/pydoc3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/pydoc3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python
       
```bash
$ singularity exec <container> /opt/view/bin/python
$ podman run --it --rm --entrypoint /opt/view/bin/python   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/python   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python-config
       
```bash
$ singularity exec <container> /opt/view/bin/python-config
$ podman run --it --rm --entrypoint /opt/view/bin/python-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/python-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3
       
```bash
$ singularity exec <container> /opt/view/bin/python3
$ podman run --it --rm --entrypoint /opt/view/bin/python3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/python3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3-config
       
```bash
$ singularity exec <container> /opt/view/bin/python3-config
$ podman run --it --rm --entrypoint /opt/view/bin/python3-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/python3-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.8
       
```bash
$ singularity exec <container> /opt/view/bin/python3.8
$ podman run --it --rm --entrypoint /opt/view/bin/python3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/python3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.8-config
       
```bash
$ singularity exec <container> /opt/view/bin/python3.8-config
$ podman run --it --rm --entrypoint /opt/view/bin/python3.8-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/python3.8-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.8-gdb.py
       
```bash
$ singularity exec <container> /opt/view/bin/python3.8-gdb.py
$ podman run --it --rm --entrypoint /opt/view/bin/python3.8-gdb.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/python3.8-gdb.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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