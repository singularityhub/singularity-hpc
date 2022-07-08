---
layout: container
name:  "ghcr.io/autamus/addrwatch"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/addrwatch/container.yaml"
updated_at: "2022-07-08 12:09:20.818107"
container_url: "https://github.com/orgs/autamus/packages/container/package/addrwatch"
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

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### addrwatch-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### addrwatch-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### addrwatch-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### addrwatch-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### addrwatch-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### addrwatch-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### addrwatch
       
```bash
$ singularity exec <container> /opt/view/bin/addrwatch
$ podman run --it --rm --entrypoint /opt/view/bin/addrwatch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/addrwatch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### addrwatch_stdout
       
```bash
$ singularity exec <container> /opt/view/bin/addrwatch_stdout
$ podman run --it --rm --entrypoint /opt/view/bin/addrwatch_stdout   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/addrwatch_stdout   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### addrwatch_syslog
       
```bash
$ singularity exec <container> /opt/view/bin/addrwatch_syslog
$ podman run --it --rm --entrypoint /opt/view/bin/addrwatch_syslog   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/addrwatch_syslog   -v ${PWD} -w ${PWD} <container> -c " $@"
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