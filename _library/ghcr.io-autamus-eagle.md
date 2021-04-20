---
layout: container
name:  "ghcr.io/autamus/eagle"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/eagle/container.yaml"
updated_at: "2021-04-20 01:49:24.811601"
container_url: ""
aliases:
 - "eagle"

 - "eagle-nm"

 - "eagle-rc"

versions:
 - "latest"
description: "Explicit Alternative Genome Likelihood Evaluator"
---

This module is a singularity container wrapper for ghcr.io/autamus/eagle.
Explicit Alternative Genome Likelihood Evaluator
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install ghcr.io/autamus/eagle
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/eagle:latest
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/eagle/latest
$ module help ghcr.io/autamus/eagle/latest
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### ghcr.io-autamus-eagle-run:

```bash
$ singularity run <container>
```

#### ghcr.io-autamus-eagle-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### ghcr.io-autamus-eagle-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### ghcr.io-autamus-eagle-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ghcr.io-autamus-eagle-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### eagle
       
```bash
$ singularity exec <container> /opt/view/bin/eagle
```


#### eagle-nm
       
```bash
$ singularity exec <container> /opt/view/bin/eagle-nm
```


#### eagle-rc
       
```bash
$ singularity exec <container> /opt/view/bin/eagle-rc
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