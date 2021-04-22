---
layout: container
name:  "singularityhub/singularity-deploy"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/singularityhub/singularity-deploy/container.yaml"
updated_at: "2021-04-22 23:21:25.046890"
container_url: ""
aliases:
 - "salad"

versions:
 - "0.0.12"
 - "salad"
description: "Example shpc container using Singularity Deploy, build and serve from GitHub releases."
---

This module is a singularity container wrapper for singularityhub/singularity-deploy.
Example shpc container using Singularity Deploy, build and serve from GitHub releases.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install singularityhub/singularity-deploy
```

Or a specific version:

```bash
$ shpc install singularityhub/singularity-deploy:0.0.12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load singularityhub/singularity-deploy/0.0.12
$ module help singularityhub/singularity-deploy/0.0.12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### singularityhub-singularity-deploy-run:

```bash
$ singularity run <container>
```

#### singularityhub-singularity-deploy-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### singularityhub-singularity-deploy-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### singularityhub-singularity-deploy-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### singularityhub-singularity-deploy-inspect-deffile:

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