---
layout: container
name:  "gradle"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/gradle/container.yaml"
updated_at: "2022-07-11 07:56:41.249638"
container_url: "https://hub.docker.com/_/gradle"
aliases:
 - "gradle"

versions:
 - "7.0.0-hotspot"
 - "7.0.1-hotspot"
 - "7.0.2-hotspot"
 - "7.1.0-hotspot"
 - "7.1.1-hotspot"
 - "7.2.0"
 - "7.3.0"
 - "7.3.3"
 - "7.4.0"
 - "latest"
 - "7"
 - "7-jdk17"
 - "7-jdk16"
 - "7-jdk11"
 - "7-jdk-openj9"
 - "7-jdk18"
description: "Gradle is a build tool with a focus on build automation and support for multi-language development."
---

This module is a singularity container wrapper for gradle.
Gradle is a build tool with a focus on build automation and support for multi-language development.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install gradle
```

Or a specific version:

```bash
$ shpc install gradle:7.0.0-hotspot
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load gradle/7.0.0-hotspot
$ module help gradle/7.0.0-hotspot
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gradle-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gradle-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gradle-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gradle-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gradle-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gradle-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gradle
       
```bash
$ singularity exec <container> /usr/bin/gradle
$ podman run --it --rm --entrypoint /usr/bin/gradle   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/gradle   -v ${PWD} -w ${PWD} <container> -c " $@"
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