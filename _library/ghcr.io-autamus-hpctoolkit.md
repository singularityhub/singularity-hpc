---
layout: container
name:  "ghcr.io/autamus/hpctoolkit"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/hpctoolkit/container.yaml"
updated_at: "2022-02-06 01:58:11.509296"
container_url: "https://github.com/orgs/autamus/packages/container/package/hpctoolkit"
aliases:
 - "hello"

 - "hpclink"

 - "hpcprof"

 - "hpcrun"

 - "hpcstruct"

 - "hpcviewer"

versions:
 - "2021.05.15"
 - "2021.10.15"
description: "HPCToolkit is an integrated suite of tools for measurement and analysis of program performance on computers ranging from multicore desktop systems to the nation's largest supercomputers."
---

This module is a singularity container wrapper for ghcr.io/autamus/hpctoolkit.
HPCToolkit is an integrated suite of tools for measurement and analysis of program performance on computers ranging from multicore desktop systems to the nation's largest supercomputers.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install ghcr.io/autamus/hpctoolkit
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/hpctoolkit:2021.05.15
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/hpctoolkit/2021.05.15
$ module help ghcr.io/autamus/hpctoolkit/2021.05.15
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


#### hello
       
```bash
$ singularity exec <container> /opt/view/bin/hello
$ podman run --it --rm --entrypoint /opt/view/bin/hello   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/hello   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hpclink
       
```bash
$ singularity exec <container> /opt/view/bin/hpclink
$ podman run --it --rm --entrypoint /opt/view/bin/hpclink   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/hpclink   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hpcprof
       
```bash
$ singularity exec <container> /opt/view/bin/hpcprof
$ podman run --it --rm --entrypoint /opt/view/bin/hpcprof   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/hpcprof   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hpcrun
       
```bash
$ singularity exec <container> /opt/view/bin/hpcrun
$ podman run --it --rm --entrypoint /opt/view/bin/hpcrun   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/hpcrun   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hpcstruct
       
```bash
$ singularity exec <container> /opt/view/bin/hpcstruct
$ podman run --it --rm --entrypoint /opt/view/bin/hpcstruct   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/hpcstruct   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hpcviewer
       
```bash
$ singularity exec <container> /opt/view/bin/hpcviewer
$ podman run --it --rm --entrypoint /opt/view/bin/hpcviewer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/hpcviewer   -v ${PWD} -w ${PWD} <container> -c " $@"
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