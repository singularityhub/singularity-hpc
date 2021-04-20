---
layout: container
name:  "rocker/shiny"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/rocker/shiny/container.yaml"
updated_at: "2021-04-20 03:12:48.486290"
container_url: ""
aliases:
 - "rocker-shiny-run"

 - "shiny-server"

versions:
 - "latest"
description: "Docker image with R + Shiny."
---

This module is a singularity container wrapper for rocker/shiny.
Docker image with R + Shiny.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install rocker/shiny
```

Or a specific version:

```bash
$ shpc install rocker/shiny:latest
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load rocker/shiny/latest
$ module help rocker/shiny/latest
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### rocker-shiny-run:

```bash
$ singularity run <container>
```

#### rocker-shiny-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### rocker-shiny-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### rocker-shiny-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rocker-shiny-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### rocker-shiny-run
       
```bash
$ singularity exec <container> /bin/bash
```


#### shiny-server
       
```bash
$ singularity exec <container> /opt/shiny-server
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