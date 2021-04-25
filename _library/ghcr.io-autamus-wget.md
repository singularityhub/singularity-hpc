---
layout: container
name:  "ghcr.io/autamus/wget"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/wget/container.yaml"
updated_at: "2021-04-25 12:09:21.568278"
container_url: ""
aliases:
 - "wget"

versions:
 - "1.21.1"
 - "latest"
description: "GNU Wget is a free software package for retrieving files using HTTP, HTTPS, FTP and FTPS, the most widely used Internet protocols."
---

This module is a singularity container wrapper for ghcr.io/autamus/wget.
GNU Wget is a free software package for retrieving files using HTTP, HTTPS, FTP and FTPS, the most widely used Internet protocols.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install ghcr.io/autamus/wget
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/wget:1.21.1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/wget/1.21.1
$ module help ghcr.io/autamus/wget/1.21.1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### ghcr.io-autamus-wget-run:

```bash
$ singularity run <container>
```

#### ghcr.io-autamus-wget-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### ghcr.io-autamus-wget-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### ghcr.io-autamus-wget-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ghcr.io-autamus-wget-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### wget
       
```bash
$ singularity exec <container> /opt/view/bin/wget
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