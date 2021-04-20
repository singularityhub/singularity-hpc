---
layout: container
name:  "jupyter/r-notebook"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/jupyter/r-notebook/container.yaml"
updated_at: "2021-04-20 02:19:04.887459"
container_url: ""
aliases:
 - "run-notebook"

versions:
 - "latest"
description: "Jupyter R Notebook from https://github.com/jupyter/docker-stacks"
---

This module is a singularity container wrapper for jupyter/r-notebook.
Jupyter R Notebook from https://github.com/jupyter/docker-stacks
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install jupyter/r-notebook
```

Or a specific version:

```bash
$ shpc install jupyter/r-notebook:latest
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load jupyter/r-notebook/latest
$ module help jupyter/r-notebook/latest
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### jupyter-r-notebook-run:

```bash
$ singularity run <container>
```

#### jupyter-r-notebook-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### jupyter-r-notebook-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### jupyter-r-notebook-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### jupyter-r-notebook-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### run-notebook
       
```bash
$ singularity exec --home ${HOME} --bind ${HOME}/.local:/home/joyvan/.local <container> jupyter notebook --no-browser --port=$(shuf -i 2000-65000 -n 1) --ip 0.0.0.0
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