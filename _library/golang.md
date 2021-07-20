---
layout: container
name:  "golang"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/golang/container.yaml"
updated_at: "2021-07-20 19:27:34.480181"
container_url: "https://hub.docker.com/r/_/golang"
aliases:
 - "go"

 - "gofmt"

versions:
 - "1.16.4-alpine"
 - "1.16.5-alpine"
 - "1.17-rc-alpine"
 - "latest"
description: "Go (a.k.a., Golang) is a programming language first developed at Google."
---

This module is a singularity container wrapper for golang.
Go (a.k.a., Golang) is a programming language first developed at Google.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install golang
```

Or a specific version:

```bash
$ shpc install golang:1.16.4-alpine
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load golang/1.16.4-alpine
$ module help golang/1.16.4-alpine
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


#### go
       
```bash
$ singularity exec <container> /usr/local/go/bin/go
$ podman run --it --rm --entrypoint /usr/local/go/bin/go   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/go/bin/go   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gofmt
       
```bash
$ singularity exec <container> /usr/local/go/bin/gofmt
$ podman run --it --rm --entrypoint /usr/local/go/bin/gofmt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/go/bin/gofmt   -v ${PWD} -w ${PWD} <container> -c " $@"
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