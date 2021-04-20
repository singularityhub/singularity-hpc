---
layout: container
name:  "bids/rshrf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/bids/rshrf/container.yaml"
updated_at: "2021-04-20 03:20:26.960100"
container_url: ""
aliases:
 - "rsHRF"

versions:
 - "latest"
description: "Resting state HRF estimation and deconvolution (https://github.com/BIDS-Apps/rsHRF)"
---

This module is a singularity container wrapper for bids/rshrf.
Resting state HRF estimation and deconvolution (https://github.com/BIDS-Apps/rsHRF)
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install bids/rshrf
```

Or a specific version:

```bash
$ shpc install bids/rshrf:latest
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load bids/rshrf/latest
$ module help bids/rshrf/latest
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### bids-rshrf-run:

```bash
$ singularity run <container>
```

#### bids-rshrf-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### bids-rshrf-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### bids-rshrf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bids-rshrf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### rsHRF
       
```bash
$ singularity exec <container> /usr/bin/rsHRF
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