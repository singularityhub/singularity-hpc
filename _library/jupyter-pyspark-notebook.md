---
layout: container
name:  "jupyter/pyspark-notebook"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/jupyter/pyspark-notebook/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/jupyter/pyspark-notebook/container.yaml"
updated_at: "2022-08-27 01:37:03.000414"
latest: "2022-06-27"
container_url: "https://hub.docker.com/r/jupyter/pyspark-notebook"
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
description: "Jupyter Pyspark Notebook from https://github.com/jupyter/docker-stacks"
config: {"docker": "jupyter/pyspark-notebook", "url": "https://hub.docker.com/r/jupyter/pyspark-notebook", "maintainer": "@vsoch", "description": "Jupyter Pyspark Notebook from https://github.com/jupyter/docker-stacks", "latest": {"2022-06-27": "sha256:f638168ca91d7c9f7f9999b0a384390ea0a46385aac223b6000a439c486a7260"}, "tags": {"4.0": "sha256:2aa9a0183bcfe80cd9e2a6c0a52d797bd5b67d1e2db9437c7345c2404b5a86c1", "latest": "sha256:f638168ca91d7c9f7f9999b0a384390ea0a46385aac223b6000a439c486a7260", "2022-04-05": "sha256:69ce4a6eaff98d5129fd5f76d992f836371752b0bab8567610d16bb1bb32ea43", "2022-03-28": "sha256:4bd42fd3182bcb70feaaf14876bfb7a5658961438acc79fe552baea646a4be3d", "2022-02-28": "sha256:13186f8f50347924656e96eb0b36dbc0e7b8aa5c69f2594c4b21c45ac0146300", "2022-01-31": "sha256:cc0b2ad428aef8ed8a4557888b2fb2b50ab125ba6eb1fcb58642d270edd9d60b", "2021-12-27": "sha256:8c45b68c6c19329a9091fd3e7e1afc7594fa0b240fb74c2230433a9c2466e968", "2022-04-25": "sha256:afc64f790d390a9b3ffc1f4847c7e077e90e92f098c0b2c34bb1ed74e101fba0", "2022-05-31": "sha256:98cbb6331e50005429915dfcd4972d6f0e97cd29371122e7ec5649c11a84b048", "2022-06-27": "sha256:f638168ca91d7c9f7f9999b0a384390ea0a46385aac223b6000a439c486a7260"}, "aliases": [{"name": "run-notebook", "command": "jupyter notebook --no-browser --port=$(shuf -i 2000-65000 -n 1) --ip 0.0.0.0"}]}
---

This module is a singularity container wrapper for jupyter/pyspark-notebook.
Jupyter Pyspark Notebook from https://github.com/jupyter/docker-stacks
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install jupyter/pyspark-notebook
```

Or a specific version:

```bash
$ shpc install jupyter/pyspark-notebook:4.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load jupyter/pyspark-notebook/4.0
$ module help jupyter/pyspark-notebook/4.0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pyspark-notebook-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pyspark-notebook-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pyspark-notebook-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pyspark-notebook-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pyspark-notebook-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pyspark-notebook-inspect-deffile:

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