---
layout: container
name:  "ghcr.io/autamus/libtiff"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/libtiff/container.yaml"
updated_at: "2021-04-20 03:16:10.749331"
container_url: ""
aliases:
 - "fax2tiff"

 - "ppm2tiff"

 - "raw2tiff"

 - "tiff2bw"

 - "tiff2pdf"

 - "tiff2ps"

 - "tiff2rgba"

 - "tiffcmp"

 - "tiffcp"

 - "tiffcrop"

 - "tiffdither"

 - "tiffdump"

 - "tiffinfo"

 - "tiffmedian"

 - "tiffset"

 - "tiffsplit"

versions:
 - "latest"
description: "Libtiff is a library for reading and writing Tagged Image File Format (abbreviated TIFF) files."
---

This module is a singularity container wrapper for ghcr.io/autamus/libtiff.
Libtiff is a library for reading and writing Tagged Image File Format (abbreviated TIFF) files.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install ghcr.io/autamus/libtiff
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/libtiff:latest
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/libtiff/latest
$ module help ghcr.io/autamus/libtiff/latest
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### ghcr.io-autamus-libtiff-run:

```bash
$ singularity run <container>
```

#### ghcr.io-autamus-libtiff-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### ghcr.io-autamus-libtiff-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### ghcr.io-autamus-libtiff-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ghcr.io-autamus-libtiff-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fax2tiff
       
```bash
$ singularity exec <container> /opt/view/bin/fax2tiff
```


#### ppm2tiff
       
```bash
$ singularity exec <container> /opt/view/bin/ppm2tiff
```


#### raw2tiff
       
```bash
$ singularity exec <container> /opt/view/bin/raw2tiff
```


#### tiff2bw
       
```bash
$ singularity exec <container> /opt/view/bin/tiff2bw
```


#### tiff2pdf
       
```bash
$ singularity exec <container> /opt/view/bin/tiff2pdf
```


#### tiff2ps
       
```bash
$ singularity exec <container> /opt/view/bin/tiff2ps
```


#### tiff2rgba
       
```bash
$ singularity exec <container> /opt/view/bin/tiff2rgba
```


#### tiffcmp
       
```bash
$ singularity exec <container> /opt/view/bin/tiffcmp
```


#### tiffcp
       
```bash
$ singularity exec <container> /opt/view/bin/tiffcp
```


#### tiffcrop
       
```bash
$ singularity exec <container> /opt/view/bin/tiffcrop
```


#### tiffdither
       
```bash
$ singularity exec <container> /opt/view/bin/tiffdither
```


#### tiffdump
       
```bash
$ singularity exec <container> /opt/view/bin/tiffdump
```


#### tiffinfo
       
```bash
$ singularity exec <container> /opt/view/bin/tiffinfo
```


#### tiffmedian
       
```bash
$ singularity exec <container> /opt/view/bin/tiffmedian
```


#### tiffset
       
```bash
$ singularity exec <container> /opt/view/bin/tiffset
```


#### tiffsplit
       
```bash
$ singularity exec <container> /opt/view/bin/tiffsplit
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