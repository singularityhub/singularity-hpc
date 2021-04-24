---
layout: container
name:  "ghcr.io/autamus/stringtie"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/stringtie/container.yaml"
updated_at: "2021-04-24 00:29:06.929043"
container_url: ""
aliases:
 - "stringtie"

versions:
 - "2.1.5"
 - "latest"
description: "StringTie is a fast and highly efficient assembler of RNA-Seq alignments into potential transcripts."
---

This module is a singularity container wrapper for ghcr.io/autamus/stringtie.
StringTie is a fast and highly efficient assembler of RNA-Seq alignments into potential transcripts.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install ghcr.io/autamus/stringtie
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/stringtie:2.1.5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/stringtie/2.1.5
$ module help ghcr.io/autamus/stringtie/2.1.5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### ghcr.io-autamus-stringtie-run:

```bash
$ singularity run <container>
```

#### ghcr.io-autamus-stringtie-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### ghcr.io-autamus-stringtie-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### ghcr.io-autamus-stringtie-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ghcr.io-autamus-stringtie-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### stringtie
       
```bash
$ singularity exec <container> /opt/view/bin/stringtie
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