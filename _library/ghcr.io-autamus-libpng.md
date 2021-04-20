---
layout: container
name:  "ghcr.io/autamus/libpng"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/libpng/container.yaml"
updated_at: "2021-04-20 03:16:37.544837"
container_url: ""
aliases:
 - "libpng-config"

 - "libpng16-config"

 - "png-fix-itxt"

 - "pngfix"

versions:
 - "latest"
description: "libpng is the official PNG reference library."
---

This module is a singularity container wrapper for ghcr.io/autamus/libpng.
libpng is the official PNG reference library.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install ghcr.io/autamus/libpng
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/libpng:latest
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/libpng/latest
$ module help ghcr.io/autamus/libpng/latest
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### ghcr.io-autamus-libpng-run:

```bash
$ singularity run <container>
```

#### ghcr.io-autamus-libpng-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### ghcr.io-autamus-libpng-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### ghcr.io-autamus-libpng-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ghcr.io-autamus-libpng-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### libpng-config
       
```bash
$ singularity exec <container> /opt/view/bin/libpng-config
```


#### libpng16-config
       
```bash
$ singularity exec <container> /opt/view/bin/libpng16-config
```


#### png-fix-itxt
       
```bash
$ singularity exec <container> /opt/view/bin/png-fix-itxt
```


#### pngfix
       
```bash
$ singularity exec <container> /opt/view/bin/pngfix
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