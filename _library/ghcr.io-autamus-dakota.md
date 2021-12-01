---
layout: container
name:  "ghcr.io/autamus/dakota"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/dakota/container.yaml"
updated_at: "2021-12-01 01:35:02.116548"
container_url: "https://github.com/orgs/autamus/packages/container/package/dakota"
aliases:
 - "dakota"

 - "dakota_library_mode"

 - "dakota_library_split"

 - "dakota_order_input"

 - "dakota_restart_util"

versions:
 - "6.12"
 - "latest"
description: "The Dakota project delivers both state-of-the-art research and robust, usable software for optimization and UQ. Broadly, the Dakota software's advanced parametric analyses enable design exploration, model calibration, risk analysis, and quantification of margins and uncertainty with computational models."
---

This module is a singularity container wrapper for ghcr.io/autamus/dakota.
The Dakota project delivers both state-of-the-art research and robust, usable software for optimization and UQ. Broadly, the Dakota software's advanced parametric analyses enable design exploration, model calibration, risk analysis, and quantification of margins and uncertainty with computational models.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install ghcr.io/autamus/dakota
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/dakota:6.12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/dakota/6.12
$ module help ghcr.io/autamus/dakota/6.12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### -run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### -shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### -exec:

```bash
$ singularity exec -s /bin/sh <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### -inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### -inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### -inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dakota
       
```bash
$ singularity exec <container> /opt/view/bin/dakota
$ podman run --it --rm --entrypoint /opt/view/bin/dakota   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/dakota   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dakota_library_mode
       
```bash
$ singularity exec <container> /opt/view/bin/dakota_library_mode
$ podman run --it --rm --entrypoint /opt/view/bin/dakota_library_mode   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/dakota_library_mode   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dakota_library_split
       
```bash
$ singularity exec <container> /opt/view/bin/dakota_library_split
$ podman run --it --rm --entrypoint /opt/view/bin/dakota_library_split   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/dakota_library_split   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dakota_order_input
       
```bash
$ singularity exec <container> /opt/view/bin/dakota_order_input
$ podman run --it --rm --entrypoint /opt/view/bin/dakota_order_input   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/dakota_order_input   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dakota_restart_util
       
```bash
$ singularity exec <container> /opt/view/bin/dakota_restart_util
$ podman run --it --rm --entrypoint /opt/view/bin/dakota_restart_util   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/dakota_restart_util   -v ${PWD} -w ${PWD} <container> -c " $@"
```



In the above, the `<container>` directive will reference an actual container provided
by the module, for the version you have chosen to load. An environment file in the
module folder will also be bound. Note that although a container
might provide custom commands, every container exposes unique exec, shell, run, and
inspect aliases. For anycommands above, you can export:

 - SINGULARITY_OPTS: to define custom options for singularity (e.g., --debug)
 - SINGULARITY_COMMAND_OPTS: to define custom options for the command (e.g., -b)
 - PODMAN_OPTS: to define custom options for podman or docker
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