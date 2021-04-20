---
layout: container
name:  "ghcr.io/autamus/addrwatch"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/addrwatch/container.yaml"
updated_at: "2021-04-20 03:14:17.395545"
container_url: ""
aliases:
 - "addrwatch"

 - "addrwatch_stdout"

 - "addrwatch_syslog"

versions:
 - "1.0.2"
 - "latest"
description: "addrwatch is a similar software to arpwatch. It main purpose is to monitor network and log ethernet/ip pairings."
---

This module is a singularity container wrapper for ghcr.io/autamus/addrwatch.
addrwatch is a similar software to arpwatch. It main purpose is to monitor network and log ethernet/ip pairings.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install ghcr.io/autamus/addrwatch
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/addrwatch:1.0.2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/addrwatch/1.0.2
$ module help ghcr.io/autamus/addrwatch/1.0.2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### ghcr.io-autamus-addrwatch-run:

```bash
$ singularity run <container>
```

#### ghcr.io-autamus-addrwatch-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### ghcr.io-autamus-addrwatch-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### ghcr.io-autamus-addrwatch-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ghcr.io-autamus-addrwatch-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### addrwatch
       
```bash
$ singularity exec <container> /opt/view/bin/addrwatch
```


#### addrwatch_stdout
       
```bash
$ singularity exec <container> /opt/view/bin/addrwatch_stdout
```


#### addrwatch_syslog
       
```bash
$ singularity exec <container> /opt/view/bin/addrwatch_syslog
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