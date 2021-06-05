---
layout: container
name:  "bids/tracula"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/bids/tracula/container.yaml"
updated_at: "2021-06-05 19:34:10.336792"
container_url: "https://hub.docker.com/r/bids/tracula"

versions:
 - "v6.0.0-5"
 - "latest"
description: "Implements Freesurfer's TRACULA (TRActs Constrained by UnderLying Anatomy) tool for cross-sectional as well as longitudinal (multi session) input data (https://github.com/BIDS-Apps/tracula)"
---

This module is a singularity container wrapper for bids/tracula.
Implements Freesurfer's TRACULA (TRActs Constrained by UnderLying Anatomy) tool for cross-sectional as well as longitudinal (multi session) input data (https://github.com/BIDS-Apps/tracula)
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install bids/tracula
```

Or a specific version:

```bash
$ shpc install bids/tracula:v6.0.0-5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load bids/tracula/v6.0.0-5
$ module help bids/tracula/v6.0.0-5
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



#### 

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
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