---
layout: container
name:  "biocontainers/bamtools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/biocontainers/bamtools/container.yaml"
updated_at: "2021-05-14 14:53:30.542753"
container_url: "https://hub.docker.com/r/biocontainers/bamtools"
aliases:
 - "bamtools"

versions:
 - "v2.5.1dfsg-3-deb_cv1"
description: "BamTools is a toolkit for handling BAM files."
---

This module is a singularity container wrapper for biocontainers/bamtools.
BamTools is a toolkit for handling BAM files.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install biocontainers/bamtools
```

Or a specific version:

```bash
$ shpc install biocontainers/bamtools:v2.5.1dfsg-3-deb_cv1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load biocontainers/bamtools/v2.5.1dfsg-3-deb_cv1
$ module help biocontainers/bamtools/v2.5.1dfsg-3-deb_cv1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### biocontainers-bamtools-run:

```bash
$ singularity run <container>
```

#### biocontainers-bamtools-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### biocontainers-bamtools-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### biocontainers-bamtools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### biocontainers-bamtools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bamtools
       
```bash
$ singularity exec <container> /usr/bin/bamtools
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