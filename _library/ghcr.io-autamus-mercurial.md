---
layout: container
name:  "ghcr.io/autamus/mercurial"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/mercurial/container.yaml"
updated_at: "2021-05-13 14:46:35.167427"
container_url: "https://github.com/orgs/autamus/packages/container/package/mercurial"
aliases:
 - "hg"

versions:
 - "5.7.1"
 - "latest"
description: "Mercurial is a distributed revision control tool for software developers."
---

This module is a singularity container wrapper for ghcr.io/autamus/mercurial.
Mercurial is a distributed revision control tool for software developers.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install ghcr.io/autamus/mercurial
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/mercurial:5.7.1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/mercurial/5.7.1
$ module help ghcr.io/autamus/mercurial/5.7.1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### ghcr.io-autamus-mercurial-run:

```bash
$ singularity run <container>
```

#### ghcr.io-autamus-mercurial-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### ghcr.io-autamus-mercurial-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### ghcr.io-autamus-mercurial-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ghcr.io-autamus-mercurial-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### hg
       
```bash
$ singularity exec <container> /opt/view/bin/hg
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