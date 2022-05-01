---
layout: container
name:  "node"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/node/container.yaml"
updated_at: "2022-05-01 04:17:46.671749"
container_url: "https://hub.docker.com/r/_/node"
aliases:
 - "node"

 - "nodejs"

 - "npm"

 - "npx"

 - "yarn"

 - "yarnpkg"

versions:
 - "15.14.0-alpine"
 - "16.0.0-alpine"
 - "16.1.0-alpine"
 - "16.2.0-alpine"
 - "16.3.0-alpine"
 - "16.5.0-alpine"
 - "16.8.0"
 - "17.0.1"
 - "17.1.0"
 - "17.3.0"
 - "17.4.0"
 - "17.6.0"
 - "latest"
 - "17"
 - "17.8"
 - "17.7"
 - "17.6"
 - "17.5"
 - "18"
 - "18-alpine3.15"
 - "18.0"
 - "17.9"
description: "Node.js is a software platform for scalable server-side and networking applications."
---

This module is a singularity container wrapper for node.
Node.js is a software platform for scalable server-side and networking applications.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install node
```

Or a specific version:

```bash
$ shpc install node:15.14.0-alpine
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load node/15.14.0-alpine
$ module help node/15.14.0-alpine
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### node-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### node-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### node-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### node-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### node-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### node-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### node
       
```bash
$ singularity exec <container> /usr/local/bin/node
$ podman run --it --rm --entrypoint /usr/local/bin/node   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/node   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nodejs
       
```bash
$ singularity exec <container> /usr/local/bin/nodejs
$ podman run --it --rm --entrypoint /usr/local/bin/nodejs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nodejs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### npm
       
```bash
$ singularity exec <container> /usr/local/bin/npm
$ podman run --it --rm --entrypoint /usr/local/bin/npm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/npm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### npx
       
```bash
$ singularity exec <container> /usr/local/bin/npx
$ podman run --it --rm --entrypoint /usr/local/bin/npx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/npx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### yarn
       
```bash
$ singularity exec <container> /usr/local/bin/yarn
$ podman run --it --rm --entrypoint /usr/local/bin/yarn   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/yarn   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### yarnpkg
       
```bash
$ singularity exec <container> /usr/local/bin/yarnpkg
$ podman run --it --rm --entrypoint /usr/local/bin/yarnpkg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/yarnpkg   -v ${PWD} -w ${PWD} <container> -c " $@"
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