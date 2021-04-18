---
layout: container
name:  "ghcr.io/autamus/hdf5"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/hdf5/container.yaml"
updated_at: "2021-04-18 07:12:27.703098"
container_url: ""
aliases:
 - "h5clear"

 - "h5copy"

 - "h5debug"

 - "h5diff"

 - "h5dump"

 - "h5format_convert"

 - "h5import"

 - "h5jam"

 - "h5ls"

 - "h5mkgrp"

 - "h5pcc"

 - "h5perf"

 - "h5perf_serial"

 - "h5redeploy"

 - "h5repack"

 - "h5repart"

 - "h5stat"

 - "h5unjam"

versions:
 - "latest"
description: "HDF5 is a unique technology suite that makes possible the management of extremely large and complex data collections."
---

This module is a singularity container wrapper for ghcr.io/autamus/hdf5.
HDF5 is a unique technology suite that makes possible the management of extremely large and complex data collections.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install ghcr.io/autamus/hdf5
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/hdf5:latest
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/hdf5/latest
$ module help ghcr.io/autamus/hdf5/latest
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### ghcr.io-autamus-hdf5-run:

```bash
$ singularity run <container>
```

#### ghcr.io-autamus-hdf5-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### ghcr.io-autamus-hdf5-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### ghcr.io-autamus-hdf5-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ghcr.io-autamus-hdf5-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### h5clear
       
```bash
$ singularity exec <container> /opt/view/bin/h5clear
```


#### h5copy
       
```bash
$ singularity exec <container> /opt/view/bin/h5copy
```


#### h5debug
       
```bash
$ singularity exec <container> /opt/view/bin/h5debug
```


#### h5diff
       
```bash
$ singularity exec <container> /opt/view/bin/h5diff
```


#### h5dump
       
```bash
$ singularity exec <container> /opt/view/bin/h5dump
```


#### h5format_convert
       
```bash
$ singularity exec <container> /opt/view/bin/h5format_convert
```


#### h5import
       
```bash
$ singularity exec <container> /opt/view/bin/h5import
```


#### h5jam
       
```bash
$ singularity exec <container> /opt/view/bin/h5jam
```


#### h5ls
       
```bash
$ singularity exec <container> /opt/view/bin/h5ls
```


#### h5mkgrp
       
```bash
$ singularity exec <container> /opt/view/bin/h5mkgrp
```


#### h5pcc
       
```bash
$ singularity exec <container> /opt/view/bin/h5pcc
```


#### h5perf
       
```bash
$ singularity exec <container> /opt/view/bin/h5perf
```


#### h5perf_serial
       
```bash
$ singularity exec <container> /opt/view/bin/h5perf_serial
```


#### h5redeploy
       
```bash
$ singularity exec <container> /opt/view/bin/h5redeploy
```


#### h5repack
       
```bash
$ singularity exec <container> /opt/view/bin/h5repack
```


#### h5repart
       
```bash
$ singularity exec <container> /opt/view/bin/h5repart
```


#### h5stat
       
```bash
$ singularity exec <container> /opt/view/bin/h5stat
```


#### h5unjam
       
```bash
$ singularity exec <container> /opt/view/bin/h5unjam
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