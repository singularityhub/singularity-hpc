---
layout: container
name:  "rocker/ml"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/rocker/ml/container.yaml"
updated_at: "2021-04-18 08:01:40.415907"
container_url: ""
aliases:
 - "rocker-ml-run"

 - "R"

 - "Rscript"

 - "rserver"

 - "rserver-pam"

 - "rsession"

 - "rstudio-server"

versions:
 - "latest"
description: "Docker images with R + machine learning libraries (CPU versions)."
---

This module is a singularity container wrapper for rocker/ml.
Docker images with R + machine learning libraries (CPU versions).
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install rocker/ml
```

Or a specific version:

```bash
$ shpc install rocker/ml:latest
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load rocker/ml/latest
$ module help rocker/ml/latest
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### rocker-ml-run:

```bash
$ singularity run <container>
```

#### rocker-ml-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### rocker-ml-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### rocker-ml-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rocker-ml-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### rocker-ml-run
       
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