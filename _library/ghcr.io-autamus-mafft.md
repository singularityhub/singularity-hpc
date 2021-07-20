---
layout: container
name:  "ghcr.io/autamus/mafft"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/mafft/container.yaml"
updated_at: "2021-07-20 19:26:45.592897"
container_url: "https://github.com/orgs/autamus/packages/container/package/mafft"
aliases:
 - "mafft"

 - "mafft-distance"

 - "mafft-einsi"

 - "mafft-fftns"

 - "mafft-fftnsi"

 - "mafft-ginsi"

 - "mafft-linsi"

 - "mafft-nwns"

 - "mafft-nwnsi"

 - "mafft-profile"

 - "mafft-qinsi"

 - "mafft-xinsi"

versions:
 - "7.475"
 - "7.481"
 - "latest"
description: "MAFFT is a multiple sequence alignment program for unix-like operating systems."
---

This module is a singularity container wrapper for ghcr.io/autamus/mafft.
MAFFT is a multiple sequence alignment program for unix-like operating systems.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install ghcr.io/autamus/mafft
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/mafft:7.475
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/mafft/7.475
$ module help ghcr.io/autamus/mafft/7.475
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


#### mafft
       
```bash
$ singularity exec <container> /opt/view/bin/mafft
$ podman run --it --rm --entrypoint /opt/view/bin/mafft   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/mafft   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mafft-distance
       
```bash
$ singularity exec <container> /opt/view/bin/mafft-distance
$ podman run --it --rm --entrypoint /opt/view/bin/mafft-distance   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/mafft-distance   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mafft-einsi
       
```bash
$ singularity exec <container> /opt/view/bin/mafft-einsi
$ podman run --it --rm --entrypoint /opt/view/bin/mafft-einsi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/mafft-einsi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mafft-fftns
       
```bash
$ singularity exec <container> /opt/view/bin/mafft-fftns
$ podman run --it --rm --entrypoint /opt/view/bin/mafft-fftns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/mafft-fftns   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mafft-fftnsi
       
```bash
$ singularity exec <container> /opt/view/bin/mafft-fftnsi
$ podman run --it --rm --entrypoint /opt/view/bin/mafft-fftnsi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/mafft-fftnsi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mafft-ginsi
       
```bash
$ singularity exec <container> /opt/view/bin/mafft-ginsi
$ podman run --it --rm --entrypoint /opt/view/bin/mafft-ginsi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/mafft-ginsi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mafft-linsi
       
```bash
$ singularity exec <container> /opt/view/bin/mafft-linsi
$ podman run --it --rm --entrypoint /opt/view/bin/mafft-linsi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/mafft-linsi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mafft-nwns
       
```bash
$ singularity exec <container> /opt/view/bin/mafft-nwns
$ podman run --it --rm --entrypoint /opt/view/bin/mafft-nwns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/mafft-nwns   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mafft-nwnsi
       
```bash
$ singularity exec <container> /opt/view/bin/mafft-nwnsi
$ podman run --it --rm --entrypoint /opt/view/bin/mafft-nwnsi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/mafft-nwnsi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mafft-profile
       
```bash
$ singularity exec <container> /opt/view/bin/mafft-profile
$ podman run --it --rm --entrypoint /opt/view/bin/mafft-profile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/mafft-profile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mafft-qinsi
       
```bash
$ singularity exec <container> /opt/view/bin/mafft-qinsi
$ podman run --it --rm --entrypoint /opt/view/bin/mafft-qinsi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/mafft-qinsi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mafft-xinsi
       
```bash
$ singularity exec <container> /opt/view/bin/mafft-xinsi
$ podman run --it --rm --entrypoint /opt/view/bin/mafft-xinsi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/mafft-xinsi   -v ${PWD} -w ${PWD} <container> -c " $@"
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