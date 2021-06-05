---
layout: container
name:  "ghcr.io/autamus/octave"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/octave/container.yaml"
updated_at: "2021-06-05 19:34:02.126259"
container_url: "https://github.com/orgs/autamus/packages/container/package/octave"
aliases:
 - "octave"

 - "octave-6.2.0"

 - "octave-cli"

 - "octave-cli-6.2.0"

 - "octave-config"

 - "octave-config-6.2.0"

versions:
 - "6.2.0"
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
$ shpc install ghcr.io/autamus/octave:6.2.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/octave/6.2.0
$ module help ghcr.io/autamus/octave/6.2.0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible.
Examples for both Singularity and Podman (container technologies supported) are included.

#### -run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
```

#### -shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### -exec:

```bash
$ singularity exec -s /bin/sh <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### -inspect:

Podman only has one inspect type.

```bash
$ podman inspect <container>
```

#### -inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### -inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### octave
       
```bash
$ singularity exec <container> /opt/view/bin/octave
$ podman run --it --rm --entrypoint /opt/view/bin/octave   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### octave-6.2.0
       
```bash
$ singularity exec <container> /opt/view/bin/octave-6.2.0
$ podman run --it --rm --entrypoint /opt/view/bin/octave-6.2.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### octave-cli
       
```bash
$ singularity exec <container> /opt/view/bin/octave-cli
$ podman run --it --rm --entrypoint /opt/view/bin/octave-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### octave-cli-6.2.0
       
```bash
$ singularity exec <container> /opt/view/bin/octave-cli-6.2.0
$ podman run --it --rm --entrypoint /opt/view/bin/octave-cli-6.2.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### octave-config
       
```bash
$ singularity exec <container> /opt/view/bin/octave-config
$ podman run --it --rm --entrypoint /opt/view/bin/octave-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### octave-config-6.2.0
       
```bash
$ singularity exec <container> /opt/view/bin/octave-config-6.2.0
$ podman run --it --rm --entrypoint /opt/view/bin/octave-config-6.2.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```



In the above, the `<container>` directive will reference an actual container provided
by the module, for the version you have chosen to load. An environment file in the
module folder will also be bound. Note that although a container
might provide custom commands, every container exposes unique exec, shell, run, and
inspect aliases. For anycommands above, you can export:

 - SINGULARITY_OPTS: to define custom options for singularity (e.g., --debug)
 - SINGULARITY_COMMAND_OPTS: to define custom options for the command (e.g., -b)
 - PODMAN_OPTS: to define custom options for podman
 - PODMAN_COMMAND_OPTS: to define custom options for the command

<br>
  
### Install

You can install shpc locally (for yourself or your user base) as follows:

```bash
$ git clone https://github.com/singularityhub/singularity-hpc
$ cd singularity-hpc
$ pip install -e .
```

Have any questions, or want to request a new module or version? [ask for help!](https://github.com/singularityhub/singularity-hpc/issues)