---
layout: container
name:  "ghcr.io/autamus/gcc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/gcc/container.yaml"
updated_at: "2021-04-18 07:59:40.093926"
container_url: ""
aliases:
 - "c++"

 - "cpp"

 - "g++"

 - "gcc"

 - "gcc-ar"

 - "gcc-nm"

 - "gcc-ranlib"

 - "gcov"

 - "gcov-dump"

 - "gcov-tool"

 - "gfortran"

 - "zstd"

versions:
 - "latest"
description: "The GNU Compiler Collection"
---

This module is a singularity container wrapper for ghcr.io/autamus/gcc.
The GNU Compiler Collection
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install ghcr.io/autamus/gcc
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/gcc:latest
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/gcc/latest
$ module help ghcr.io/autamus/gcc/latest
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### ghcr.io-autamus-gcc-run:

```bash
$ singularity run <container>
```

#### ghcr.io-autamus-gcc-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### ghcr.io-autamus-gcc-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### ghcr.io-autamus-gcc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ghcr.io-autamus-gcc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### c++
       
```bash
$ singularity exec <container> /opt/view/bin/c++
```


#### cpp
       
```bash
$ singularity exec <container> /opt/view/bin/cpp
```


#### g++
       
```bash
$ singularity exec <container> /opt/view/bin/g++
```


#### gcc
       
```bash
$ singularity exec <container> /opt/view/bin/gcc
```


#### gcc-ar
       
```bash
$ singularity exec <container> /opt/view/bin/gcc-ar
```


#### gcc-nm
       
```bash
$ singularity exec <container> /opt/view/bin/gcc-nm
```


#### gcc-ranlib
       
```bash
$ singularity exec <container> /opt/view/bin/gcc-ranlib
```


#### gcov
       
```bash
$ singularity exec <container> /opt/view/bin/gcov
```


#### gcov-dump
       
```bash
$ singularity exec <container> /opt/view/bin/gcov-dump
```


#### gcov-tool
       
```bash
$ singularity exec <container> /opt/view/bin/gcov-tool
```


#### gfortran
       
```bash
$ singularity exec <container> /opt/view/bin/gfortran
```


#### zstd
       
```bash
$ singularity exec <container> /opt/view/bin/zstd
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