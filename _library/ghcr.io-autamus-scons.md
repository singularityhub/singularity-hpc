---
layout: container
name:  "ghcr.io/autamus/scons"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/scons/container.yaml"
updated_at: "2021-05-23 12:56:47.606011"
container_url: "https://github.com/orgs/autamus/packages/container/package/scons"
aliases:
 - "scons"

 - "scons-3.1.2"

 - "scons-3.1.2.bat"

 - "scons-configure-cache"

 - "scons-configure-cache-3.1.2"

 - "scons-time"

 - "scons-time-3.1.2"

 - "scons.bat"

 - "sconsign"

 - "sconsign-3.1.2"

versions:
 - "3.1.2"
 - "latest"
description: "SCons is an Open Source software construction tool."
---

This module is a singularity container wrapper for ghcr.io/autamus/scons.
SCons is an Open Source software construction tool.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install ghcr.io/autamus/scons
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/scons:3.1.2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/scons/3.1.2
$ module help ghcr.io/autamus/scons/3.1.2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### ghcr.io-autamus-scons-run:

```bash
$ singularity run <container>
```

#### ghcr.io-autamus-scons-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### ghcr.io-autamus-scons-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### ghcr.io-autamus-scons-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ghcr.io-autamus-scons-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### scons
       
```bash
$ singularity exec <container> /opt/view/bin/scons
```


#### scons-3.1.2
       
```bash
$ singularity exec <container> /opt/view/bin/scons-3.1.2
```


#### scons-3.1.2.bat
       
```bash
$ singularity exec <container> /opt/view/bin/scons-3.1.2.bat
```


#### scons-configure-cache
       
```bash
$ singularity exec <container> /opt/view/bin/scons-configure-cache
```


#### scons-configure-cache-3.1.2
       
```bash
$ singularity exec <container> /opt/view/bin/scons-configure-cache-3.1.2
```


#### scons-time
       
```bash
$ singularity exec <container> /opt/view/bin/scons-time
```


#### scons-time-3.1.2
       
```bash
$ singularity exec <container> /opt/view/bin/scons-time-3.1.2
```


#### scons.bat
       
```bash
$ singularity exec <container> /opt/view/bin/scons.bat
```


#### sconsign
       
```bash
$ singularity exec <container> /opt/view/bin/sconsign
```


#### sconsign-3.1.2
       
```bash
$ singularity exec <container> /opt/view/bin/sconsign-3.1.2
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