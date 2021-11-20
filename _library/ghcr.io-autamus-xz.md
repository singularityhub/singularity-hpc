---
layout: container
name:  "ghcr.io/autamus/xz"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/xz/container.yaml"
updated_at: "2021-11-20 06:11:15.056977"
container_url: "https://github.com/orgs/autamus/packages/container/package/xz"
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


#### xz
       
```bash
$ singularity exec <container> /opt/view/bin/xz
$ podman run --it --rm --entrypoint /opt/view/bin/xz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/xz   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xzcat
       
```bash
$ singularity exec <container> /opt/view/bin/xzcat
$ podman run --it --rm --entrypoint /opt/view/bin/xzcat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/xzcat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xzcmp
       
```bash
$ singularity exec <container> /opt/view/bin/xzcmp
$ podman run --it --rm --entrypoint /opt/view/bin/xzcmp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/xzcmp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xzdec
       
```bash
$ singularity exec <container> /opt/view/bin/xzdec
$ podman run --it --rm --entrypoint /opt/view/bin/xzdec   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/xzdec   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xzdiff
       
```bash
$ singularity exec <container> /opt/view/bin/xzdiff
$ podman run --it --rm --entrypoint /opt/view/bin/xzdiff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/xzdiff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xzegrep
       
```bash
$ singularity exec <container> /opt/view/bin/xzegrep
$ podman run --it --rm --entrypoint /opt/view/bin/xzegrep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/xzegrep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xzfgrep
       
```bash
$ singularity exec <container> /opt/view/bin/xzfgrep
$ podman run --it --rm --entrypoint /opt/view/bin/xzfgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/xzfgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xzgrep
       
```bash
$ singularity exec <container> /opt/view/bin/xzgrep
$ podman run --it --rm --entrypoint /opt/view/bin/xzgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/xzgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xzless
       
```bash
$ singularity exec <container> /opt/view/bin/xzless
$ podman run --it --rm --entrypoint /opt/view/bin/xzless   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/xzless   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xzmore
       
```bash
$ singularity exec <container> /opt/view/bin/xzmore
$ podman run --it --rm --entrypoint /opt/view/bin/xzmore   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/xzmore   -v ${PWD} -w ${PWD} <container> -c " $@"
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