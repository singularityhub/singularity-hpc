---
layout: container
name:  "rocker/rstudio"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/rocker/rstudio/container.yaml"
updated_at: "2021-04-20 03:20:22.159694"
container_url: ""
aliases:
 - "rocker-rstudio-run"

 - "R"

 - "Rscript"

 - "rserver"

 - "rserver-pam"

 - "rsession"

 - "rstudio-server"

versions:
 - "latest"
description: "Rstudio server image"
---

This module is a singularity container wrapper for rocker/rstudio.
Rstudio server image
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install rocker/rstudio
```

Or a specific version:

```bash
$ shpc install rocker/rstudio:latest
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load rocker/rstudio/latest
$ module help rocker/rstudio/latest
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### rocker-rstudio-run:

```bash
$ singularity run <container>
```

#### rocker-rstudio-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### rocker-rstudio-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### rocker-rstudio-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rocker-rstudio-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### rocker-rstudio-run
       
```bash
$ singularity exec <container> /bin/bash
```


#### R
       
```bash
$ singularity exec <container> /usr/local/bin/R
```


#### Rscript
       
```bash
$ singularity exec <container> /usr/local/bin/Rscript
```


#### rserver
       
```bash
$ singularity exec <container> /usr/lib/rstudio-server/bin/rserver
```


#### rserver-pam
       
```bash
$ singularity exec <container> /usr/lib/rstudio-server/bin/rserver-pam
```


#### rsession
       
```bash
$ singularity exec <container> /usr/lib/rstudio-server/bin/rsession
```


#### rstudio-server
       
```bash
$ singularity exec <container> /usr/lib/rstudio-server/bin/rstudio-server
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