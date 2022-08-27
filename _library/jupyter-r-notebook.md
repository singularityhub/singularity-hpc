---
layout: container
name:  "jupyter/r-notebook"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/jupyter/r-notebook/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/jupyter/r-notebook/container.yaml"
updated_at: "2022-08-27 01:37:03.529414"
latest: "2022-06-27"
container_url: "https://hub.docker.com/r/jupyter/r-notebook"
aliases:
 - "run-notebook"
versions:
 - "4.0"
 - "latest"
 - "2022-04-05"
 - "2022-03-28"
 - "2022-02-28"
 - "2022-01-31"
 - "2021-12-27"
 - "2022-04-25"
 - "2022-05-31"
 - "2022-06-27"
description: "Jupyter R Notebook from https://github.com/jupyter/docker-stacks"
config: {"docker": "jupyter/r-notebook", "url": "https://hub.docker.com/r/jupyter/r-notebook", "maintainer": "@vsoch", "description": "Jupyter R Notebook from https://github.com/jupyter/docker-stacks", "latest": {"2022-06-27": "sha256:b9e7130edc6570925a7379c99e6f6942251aed7ba7cd70b79b2e239074824808"}, "tags": {"4.0": "sha256:8c9e0ae86ef780855cba13e48adbcd9a43a12f93e61fe424a1e3398700ce0b51", "latest": "sha256:b9e7130edc6570925a7379c99e6f6942251aed7ba7cd70b79b2e239074824808", "2022-04-05": "sha256:359d683a3bb6170092a88073eb5ced9887fe0546cdaff2ec17ca22b5649c7cf2", "2022-03-28": "sha256:2a998dd7d8372da07ef9d73b2e7afe1805cba6ca443d55887f3dc56d6fc7e256", "2022-02-28": "sha256:81c62ae6524ea0186cbfec7090e43eba34677f933cf3667f6cfe8c4dda89a531", "2022-01-31": "sha256:b198e6a85bf510b3002d9538a635b36881f1a1adf79b1970ea52807350ef76a9", "2021-12-27": "sha256:babb83abc48997b96837546134ded6c0422185afb9772cb699eb3c46017cd9fa", "2022-04-25": "sha256:79591614ec63c61a7021eaf569fe264da5d020fa82f943a333693dbb90e30686", "2022-05-31": "sha256:67d8f19a23a7bb54918ebbb59ec4149d8605c2f19a045bf6e332f504640994d0", "2022-06-27": "sha256:b9e7130edc6570925a7379c99e6f6942251aed7ba7cd70b79b2e239074824808"}, "aliases": [{"name": "run-notebook", "command": "jupyter notebook --no-browser --port=$(shuf -i 2000-65000 -n 1) --ip 0.0.0.0"}]}
---

This module is a singularity container wrapper for jupyter/r-notebook.
Jupyter R Notebook from https://github.com/jupyter/docker-stacks
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install jupyter/r-notebook
```

Or a specific version:

```bash
$ shpc install jupyter/r-notebook:4.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load jupyter/r-notebook/4.0
$ module help jupyter/r-notebook/4.0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-notebook-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-notebook-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-notebook-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-notebook-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-notebook-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-notebook-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### run-notebook
       
```bash
$ singularity exec <container> jupyter notebook --no-browser --port=$(shuf -i 2000-65000 -n 1) --ip 0.0.0.0
$ podman run --it --rm --entrypoint    -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint    -v ${PWD} -w ${PWD} <container> -c " $@"
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