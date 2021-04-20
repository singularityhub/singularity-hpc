---
layout: container
name:  "ghcr.io/autamus/pandaseq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/pandaseq/container.yaml"
updated_at: "2021-04-20 02:20:06.091395"
container_url: ""
aliases:
 - "pandaseq"

 - "pandaseq-checkid"

 - "pandaseq-diff"

 - "pandaseq-hang"

 - "pandaxs"

versions:
 - "latest"
description: "A program to align Illumina reads, optionally with PCR primers embedded in the sequence, and reconstruct an overlapping sequence."
---

This module is a singularity container wrapper for ghcr.io/autamus/pandaseq.
A program to align Illumina reads, optionally with PCR primers embedded in the sequence, and reconstruct an overlapping sequence.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install ghcr.io/autamus/pandaseq
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/pandaseq:latest
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/pandaseq/latest
$ module help ghcr.io/autamus/pandaseq/latest
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### ghcr.io-autamus-pandaseq-run:

```bash
$ singularity run <container>
```

#### ghcr.io-autamus-pandaseq-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### ghcr.io-autamus-pandaseq-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### ghcr.io-autamus-pandaseq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ghcr.io-autamus-pandaseq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pandaseq
       
```bash
$ singularity exec <container> /opt/view/bin/pandaseq
```


#### pandaseq-checkid
       
```bash
$ singularity exec <container> /opt/view/bin/pandaseq-checkid
```


#### pandaseq-diff
       
```bash
$ singularity exec <container> /opt/view/bin/pandaseq-diff
```


#### pandaseq-hang
       
```bash
$ singularity exec <container> /opt/view/bin/pandaseq-hang
```


#### pandaxs
       
```bash
$ singularity exec <container> /opt/view/bin/pandaxs
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