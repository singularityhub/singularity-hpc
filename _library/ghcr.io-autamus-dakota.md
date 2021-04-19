---
layout: container
name:  "ghcr.io/autamus/dakota"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/dakota/container.yaml"
updated_at: "2021-04-19 23:54:18.430904"
container_url: ""
aliases:
 - "dakota"

 - "dakota_library_mode"

 - "dakota_library_split"

 - "dakota_order_input"

 - "dakota_restart_util"

versions:
 - "latest"
description: "The Dakota project delivers both state-of-the-art research and robust, usable software for optimization and UQ. Broadly, the Dakota software's advanced parametric analyses enable design exploration, model calibration, risk analysis, and quantification of margins and uncertainty with computational models."
---

This module is a singularity container wrapper for ghcr.io/autamus/dakota.
The Dakota project delivers both state-of-the-art research and robust, usable software for optimization and UQ. Broadly, the Dakota software's advanced parametric analyses enable design exploration, model calibration, risk analysis, and quantification of margins and uncertainty with computational models.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install ghcr.io/autamus/dakota
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/dakota:latest
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/dakota/latest
$ module help ghcr.io/autamus/dakota/latest
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### ghcr.io-autamus-dakota-run:

```bash
$ singularity run <container>
```

#### ghcr.io-autamus-dakota-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### ghcr.io-autamus-dakota-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### ghcr.io-autamus-dakota-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ghcr.io-autamus-dakota-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dakota
       
```bash
$ singularity exec <container> /opt/view/bin/dakota
```


#### dakota_library_mode
       
```bash
$ singularity exec <container> /opt/view/bin/dakota_library_mode
```


#### dakota_library_split
       
```bash
$ singularity exec <container> /opt/view/bin/dakota_library_split
```


#### dakota_order_input
       
```bash
$ singularity exec <container> /opt/view/bin/dakota_order_input
```


#### dakota_restart_util
       
```bash
$ singularity exec <container> /opt/view/bin/dakota_restart_util
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