---
layout: container
name:  "ghcr.io/autamus/xz"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/xz/container.yaml"
updated_at: "2021-04-22 23:21:07.345958"
container_url: ""
aliases:
 - "xz"

 - "xzcat"

 - "xzcmp"

 - "xzdec"

 - "xzdiff"

 - "xzegrep"

 - "xzfgrep"

 - "xzgrep"

 - "xzless"

 - "xzmore"

versions:
 - "5.2.5"
 - "latest"
description: "XZ Utils is free general-purpose data compression software with a high compression ratio."
---

This module is a singularity container wrapper for ghcr.io/autamus/xz.
XZ Utils is free general-purpose data compression software with a high compression ratio.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install ghcr.io/autamus/xz
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/xz:5.2.5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/xz/5.2.5
$ module help ghcr.io/autamus/xz/5.2.5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### ghcr.io-autamus-xz-run:

```bash
$ singularity run <container>
```

#### ghcr.io-autamus-xz-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### ghcr.io-autamus-xz-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### ghcr.io-autamus-xz-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ghcr.io-autamus-xz-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### xz
       
```bash
$ singularity exec <container> /opt/view/bin/xz
```


#### xzcat
       
```bash
$ singularity exec <container> /opt/view/bin/xzcat
```


#### xzcmp
       
```bash
$ singularity exec <container> /opt/view/bin/xzcmp
```


#### xzdec
       
```bash
$ singularity exec <container> /opt/view/bin/xzdec
```


#### xzdiff
       
```bash
$ singularity exec <container> /opt/view/bin/xzdiff
```


#### xzegrep
       
```bash
$ singularity exec <container> /opt/view/bin/xzegrep
```


#### xzfgrep
       
```bash
$ singularity exec <container> /opt/view/bin/xzfgrep
```


#### xzgrep
       
```bash
$ singularity exec <container> /opt/view/bin/xzgrep
```


#### xzless
       
```bash
$ singularity exec <container> /opt/view/bin/xzless
```


#### xzmore
       
```bash
$ singularity exec <container> /opt/view/bin/xzmore
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