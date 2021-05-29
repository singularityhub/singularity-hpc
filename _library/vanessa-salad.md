---
layout: container
name:  "vanessa/salad"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/vanessa/salad/container.yaml"
updated_at: "2021-05-29 01:53:51.380296"
container_url: "https://hub.docker.com/r/vanessa/salad"
aliases:
 - "salad"

versions:
 - "latest"
description: "A container all about fork and spoon puns."
---

This module is a singularity container wrapper for vanessa/salad.
A container all about fork and spoon puns.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install vanessa/salad
```

Or a specific version:

```bash
$ shpc install vanessa/salad:latest
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load vanessa/salad/latest
$ module help vanessa/salad/latest
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### vanessa-salad-run:

```bash
$ singularity run <container>
```

#### vanessa-salad-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### vanessa-salad-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### vanessa-salad-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### vanessa-salad-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### salad
       
```bash
$ singularity exec <container> /code/salad
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