---
layout: container
name:  "ghcr.io/autamus/cufflinks"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/cufflinks/container.yaml"
updated_at: "2021-04-21 05:54:59.686757"
container_url: ""
aliases:
 - "cuffcompare"

 - "cuffdiff"

 - "cufflinks"

 - "cuffmerge"

 - "cuffnorm"

 - "cuffquant"

versions:
 - "2.2.1"
 - "latest"
description: "Cufflinks assembles transcripts, estimates their abundances, and tests for differential expression and regulation in RNA-Seq samples."
---

This module is a singularity container wrapper for ghcr.io/autamus/cufflinks.
Cufflinks assembles transcripts, estimates their abundances, and tests for differential expression and regulation in RNA-Seq samples.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install ghcr.io/autamus/cufflinks
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/cufflinks:2.2.1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/cufflinks/2.2.1
$ module help ghcr.io/autamus/cufflinks/2.2.1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### ghcr.io-autamus-cufflinks-run:

```bash
$ singularity run <container>
```

#### ghcr.io-autamus-cufflinks-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### ghcr.io-autamus-cufflinks-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### ghcr.io-autamus-cufflinks-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ghcr.io-autamus-cufflinks-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cuffcompare
       
```bash
$ singularity exec <container> /opt/view/bin/cuffcompare
```


#### cuffdiff
       
```bash
$ singularity exec <container> /opt/view/bin/cuffdiff
```


#### cufflinks
       
```bash
$ singularity exec <container> /opt/view/bin/cufflinks
```


#### cuffmerge
       
```bash
$ singularity exec <container> /opt/view/bin/cuffmerge
```


#### cuffnorm
       
```bash
$ singularity exec <container> /opt/view/bin/cuffnorm
```


#### cuffquant
       
```bash
$ singularity exec <container> /opt/view/bin/cuffquant
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