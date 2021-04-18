---
layout: container
name:  "spack/ubuntu-bionic"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/spack/ubuntu-bionic/container.yaml"
updated_at: "2021-04-18 21:08:37.332084"
container_url: ""
aliases:
 - "sbang"

 - "spack"

 - "spack-python"

versions:
 - "latest"
description: "Ubuntu 18.04 with Spack preinstalled."
---

This module is a singularity container wrapper for spack/ubuntu-bionic.
Ubuntu 18.04 with Spack preinstalled.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install spack/ubuntu-bionic
```

Or a specific version:

```bash
$ shpc install spack/ubuntu-bionic:latest
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load spack/ubuntu-bionic/latest
$ module help spack/ubuntu-bionic/latest
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### spack-ubuntu-bionic-run:

```bash
$ singularity run <container>
```

#### spack-ubuntu-bionic-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### spack-ubuntu-bionic-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### spack-ubuntu-bionic-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### spack-ubuntu-bionic-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### sbang
       
```bash
$ singularity exec <container> /opt/spack/bin/sbang
```


#### spack
       
```bash
$ singularity exec <container> /opt/spack/bin/spack
```


#### spack-python
       
```bash
$ singularity exec <container> /opt/spack/bin/spack-python
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