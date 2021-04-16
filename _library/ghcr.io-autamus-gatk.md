---
layout: container
name:  "ghcr.io/autamus/gatk"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/gatk/container.yaml"
updated_at: "2021-04-16 04:04:14.341586"
container_url: ""
aliases:
 - "gatk"

versions:
 - "latest"
description: "GATK (pronounced 'Gee-ay-tee-kay', not 'Gat-kay'), stands for GenomeAnalysisToolkit. It is a collection of command-line tools for analyzing high-throughput sequencing data with a primary focus on variant discovery."
---

This module is a singularity container wrapper for ghcr.io/autamus/gatk.
GATK (pronounced 'Gee-ay-tee-kay', not 'Gat-kay'), stands for GenomeAnalysisToolkit. It is a collection of command-line tools for analyzing high-throughput sequencing data with a primary focus on variant discovery.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install ghcr.io/autamus/gatk
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/gatk:latest
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/gatk/latest
$ module help ghcr.io/autamus/gatk/latest
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### ghcr.io-autamus-gatk-run:

```bash
$ singularity run <container>
```

#### ghcr.io-autamus-gatk-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### ghcr.io-autamus-gatk-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### ghcr.io-autamus-gatk-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ghcr.io-autamus-gatk-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gatk
       
```bash
$ singularity exec <container> /opt/view/bin/gatk
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