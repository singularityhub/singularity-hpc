---
layout: container
name:  "ghcr.io/autamus/octave"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/octave/container.yaml"
updated_at: "2021-04-20 02:21:38.864281"
container_url: ""
aliases:
 - "octave"

 - "octave-6.2.0"

 - "octave-cli"

 - "octave-cli-6.2.0"

 - "octave-config"

 - "octave-config-6.2.0"

versions:
 - "latest"
description: "GNU Octave is a high-level interpreted language, primarily intended for numerical computations (like an open source Matlab)"
---

This module is a singularity container wrapper for ghcr.io/autamus/octave.
GNU Octave is a high-level interpreted language, primarily intended for numerical computations (like an open source Matlab)
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install ghcr.io/autamus/octave
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/octave:latest
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/octave/latest
$ module help ghcr.io/autamus/octave/latest
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### ghcr.io-autamus-octave-run:

```bash
$ singularity run <container>
```

#### ghcr.io-autamus-octave-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### ghcr.io-autamus-octave-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### ghcr.io-autamus-octave-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ghcr.io-autamus-octave-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### octave
       
```bash
$ singularity exec <container> /opt/view/bin/octave
```


#### octave-6.2.0
       
```bash
$ singularity exec <container> /opt/view/bin/octave-6.2.0
```


#### octave-cli
       
```bash
$ singularity exec <container> /opt/view/bin/octave-cli
```


#### octave-cli-6.2.0
       
```bash
$ singularity exec <container> /opt/view/bin/octave-cli-6.2.0
```


#### octave-config
       
```bash
$ singularity exec <container> /opt/view/bin/octave-config
```


#### octave-config-6.2.0
       
```bash
$ singularity exec <container> /opt/view/bin/octave-config-6.2.0
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