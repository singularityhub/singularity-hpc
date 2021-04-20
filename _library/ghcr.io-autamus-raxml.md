---
layout: container
name:  "ghcr.io/autamus/raxml"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/raxml/container.yaml"
updated_at: "2021-04-20 02:19:24.435127"
container_url: ""
aliases:
 - "raxmlHPC"

 - "raxmlHPC-AVX"

 - "raxmlHPC-MPI"

 - "raxmlHPC-MPI-AVX"

 - "raxmlHPC-MPI-SSE3"

 - "raxmlHPC-SSE3"

versions:
 - "latest"
description: "RAxML (Randomized Axelerated Maximum Likelihood) is a popular program for phylogenetic analysis of large datasets under maximum likelihood."
---

This module is a singularity container wrapper for ghcr.io/autamus/raxml.
RAxML (Randomized Axelerated Maximum Likelihood) is a popular program for phylogenetic analysis of large datasets under maximum likelihood.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install ghcr.io/autamus/raxml
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/raxml:latest
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/raxml/latest
$ module help ghcr.io/autamus/raxml/latest
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### ghcr.io-autamus-raxml-run:

```bash
$ singularity run <container>
```

#### ghcr.io-autamus-raxml-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### ghcr.io-autamus-raxml-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### ghcr.io-autamus-raxml-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ghcr.io-autamus-raxml-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### raxmlHPC
       
```bash
$ singularity exec <container> /opt/view/bin/raxmlHPC
```


#### raxmlHPC-AVX
       
```bash
$ singularity exec <container> /opt/view/bin/raxmlHPC-AVX
```


#### raxmlHPC-MPI
       
```bash
$ singularity exec <container> /opt/view/bin/raxmlHPC-MPI
```


#### raxmlHPC-MPI-AVX
       
```bash
$ singularity exec <container> /opt/view/bin/raxmlHPC-MPI-AVX
```


#### raxmlHPC-MPI-SSE3
       
```bash
$ singularity exec <container> /opt/view/bin/raxmlHPC-MPI-SSE3
```


#### raxmlHPC-SSE3
       
```bash
$ singularity exec <container> /opt/view/bin/raxmlHPC-SSE3
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