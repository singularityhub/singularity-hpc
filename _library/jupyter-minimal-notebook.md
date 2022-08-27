---
layout: container
name:  "jupyter/minimal-notebook"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/jupyter/minimal-notebook/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/jupyter/minimal-notebook/container.yaml"
updated_at: "2022-08-27 02:53:48.972768"
latest: "2022-06-27"
container_url: "https://hub.docker.com/r/jupyter/minimal-notebook"
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
description: "Jupyter Minimal Notebook from https://github.com/jupyter/docker-stacks"
config: {"docker": "jupyter/minimal-notebook", "url": "https://hub.docker.com/r/jupyter/minimal-notebook", "maintainer": "@vsoch", "description": "Jupyter Minimal Notebook from https://github.com/jupyter/docker-stacks", "latest": {"2022-06-27": "sha256:bf498f5be6836f67dcf2ee298b3b0c04366ae9afcc6123716f795e6f5fb49d53"}, "tags": {"4.0": "sha256:6f9d189494fe091700681eb39b429dfe1420ad0717697c2e2293779fcb80cd1e", "latest": "sha256:bf498f5be6836f67dcf2ee298b3b0c04366ae9afcc6123716f795e6f5fb49d53", "2022-04-05": "sha256:81d41c8b10bce94a01aa5b6df1a12ca1f0946b42f378b8221297e6612100377d", "2022-03-28": "sha256:2207739da5b641fed8845913d97bd41cffb372470d97bf5f5be164706ade78b1", "2022-02-28": "sha256:3369a21d4377037e239223b165f44aec62a76e8cbafae15528eff5f4dc159bc8", "2022-01-31": "sha256:f403b4917f873629cc934941deec6015155351d40fb8d485493d2bd6ad719a5c", "2021-12-27": "sha256:1866eaf6a7fc0fc9564650a296625a6a4be24f4c392c95d9b547b92483dad99d", "2022-04-25": "sha256:bf5f9018016b090e59e9abf87531e0031c1535a39d89fe87c7a34e064d330bc0", "2022-05-31": "sha256:31c63280671cec569a03e6e738fee04f08ff6dae2d080ab6f57cc650ec8c7838", "2022-06-27": "sha256:bf498f5be6836f67dcf2ee298b3b0c04366ae9afcc6123716f795e6f5fb49d53"}, "features": {"home": true}, "aliases": [{"name": "run-notebook", "command": "jupyter notebook --no-browser --port=$(shuf -i 2000-65000 -n 1) --ip 0.0.0.0"}]}
---

This module is a singularity container wrapper for jupyter/minimal-notebook.
Jupyter Minimal Notebook from https://github.com/jupyter/docker-stacks
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install jupyter/minimal-notebook
```

Or a specific version:

```bash
$ shpc install jupyter/minimal-notebook:4.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load jupyter/minimal-notebook/4.0
$ module help jupyter/minimal-notebook/4.0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### minimal-notebook-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### minimal-notebook-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### minimal-notebook-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### minimal-notebook-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### minimal-notebook-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### minimal-notebook-inspect-deffile:

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