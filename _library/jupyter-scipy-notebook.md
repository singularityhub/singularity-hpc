---
layout: container
name:  "jupyter/scipy-notebook"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/jupyter/scipy-notebook/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/jupyter/scipy-notebook/container.yaml"
updated_at: "2022-08-27 01:37:04.056389"
latest: "2022-06-27"
container_url: "https://hub.docker.com/r/jupyter/scipy-notebook"
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
description: "Jupyter Notebook Scientific Python Stack from https://github.com/jupyter/docker-stacks"
config: {"docker": "jupyter/scipy-notebook", "url": "https://hub.docker.com/r/jupyter/scipy-notebook", "maintainer": "@vsoch", "description": "Jupyter Notebook Scientific Python Stack from https://github.com/jupyter/docker-stacks", "latest": {"2022-06-27": "sha256:b3c7535c6ad691d307275277f2cea9c8f69c13dbe3626ffb1cec6e9801d96c5e"}, "tags": {"4.0": "sha256:c650887d0bb8ec6fe899b58c2a8dec896e4e2c93b70135caabaa11cbe4d0d456", "latest": "sha256:b3c7535c6ad691d307275277f2cea9c8f69c13dbe3626ffb1cec6e9801d96c5e", "2022-04-05": "sha256:5918de55073c2a7b24e57d855b9a1501a4e84c89d1c745d10523a1773175a126", "2022-03-28": "sha256:075ce0799346a1a340fee08d08a4c4a10391a3bd29a8963c1c5355d24ac93b1c", "2022-02-28": "sha256:e51cb4700af349c040bbf83c7f7a3c5fb94edb97df3071be48d5eae6c03d2f5b", "2022-01-31": "sha256:9d8aff70bdc79eb8c80579da39b9583326bc332d248416f06ef20f954d0b64a6", "2021-12-27": "sha256:41911b6f333f464a05b503636e6fb03005f2c11e72c272476c49eaf57770fa80", "2022-04-25": "sha256:c9e051d007f7806bb316db203470e7cbe37598e73b0c3e9f0c7816dd93757f0c", "2022-05-31": "sha256:80433463497b4041c904b530c9452542ac0239c2c50142a22e05ec27d214281c", "2022-06-27": "sha256:b3c7535c6ad691d307275277f2cea9c8f69c13dbe3626ffb1cec6e9801d96c5e"}, "aliases": [{"name": "run-notebook", "command": "jupyter notebook --no-browser --port=$(shuf -i 2000-65000 -n 1) --ip 0.0.0.0"}]}
---

This module is a singularity container wrapper for jupyter/scipy-notebook.
Jupyter Notebook Scientific Python Stack from https://github.com/jupyter/docker-stacks
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install jupyter/scipy-notebook
```

Or a specific version:

```bash
$ shpc install jupyter/scipy-notebook:4.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load jupyter/scipy-notebook/4.0
$ module help jupyter/scipy-notebook/4.0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### scipy-notebook-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### scipy-notebook-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### scipy-notebook-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### scipy-notebook-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### scipy-notebook-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### scipy-notebook-inspect-deffile:

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