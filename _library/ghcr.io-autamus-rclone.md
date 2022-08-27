---
layout: container
name:  "ghcr.io/autamus/rclone"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/rclone/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/ghcr.io/autamus/rclone/container.yaml"
updated_at: "2022-08-27 01:36:40.330436"
latest: "1.57.0"
container_url: "https://github.com/orgs/autamus/packages/container/package/rclone"
aliases:
 - "rclone"
versions:
 - "1.55.0"
 - "1.55.1"
 - "1.56.0"
 - "1.56.2"
 - "1.57.0"
 - "latest"
description: "Rclone is a command line program to manage files on cloud storage."
config: {"docker": "ghcr.io/autamus/rclone", "url": "https://github.com/orgs/autamus/packages/container/package/rclone", "maintainer": "@vsoch", "description": "Rclone is a command line program to manage files on cloud storage.", "latest": {"1.57.0": "sha256:8e22eebdf6a5c0473b6c3010eeae66496a05ded4349d209278ddb4cd85f0a611"}, "tags": {"1.55.0": "sha256:8a8c07e1759f8ad45b34828b5adc6b43b811569f84093970d0366afd9f7b4b5f", "1.55.1": "sha256:e1020f643a5e613fb301f2b33c219e6f7430ff5bcaacf523655ad6d8e2e439c0", "1.56.0": "sha256:d95c8c617bef5259d583d9f994a93296bce22e67dc8fa193d3f30a33dc35326c", "1.56.2": "sha256:8fca8f455745ee5ff83b0bf31ec695766b02919b0babda81f97d96ba6bfe0113", "1.57.0": "sha256:8e22eebdf6a5c0473b6c3010eeae66496a05ded4349d209278ddb4cd85f0a611", "latest": "sha256:8e22eebdf6a5c0473b6c3010eeae66496a05ded4349d209278ddb4cd85f0a611"}, "aliases": {"rclone": "/opt/view/bin/rclone"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/rclone.
Rclone is a command line program to manage files on cloud storage.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/rclone
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/rclone:1.55.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/rclone/1.55.0
$ module help ghcr.io/autamus/rclone/1.55.0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rclone-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rclone-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rclone-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rclone-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rclone-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rclone-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### rclone
       
```bash
$ singularity exec <container> /opt/view/bin/rclone
$ podman run --it --rm --entrypoint /opt/view/bin/rclone   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/rclone   -v ${PWD} -w ${PWD} <container> -c " $@"
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