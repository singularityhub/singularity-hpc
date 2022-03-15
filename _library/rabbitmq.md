---
layout: container
name:  "rabbitmq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/rabbitmq/container.yaml"
updated_at: "2022-03-15 13:30:30.951735"
container_url: "https://hub.docker.com/r/_/rabbitmq"
aliases:
 - "rabbitmq-defaults"

 - "rabbitmq-diagnostics"

 - "rabbitmq-env"

 - "rabbitmq-plugins"

 - "rabbitmq-queues"

 - "rabbitmq-server"

 - "rabbitmq-upgrade"

 - "rabbitmqctl"

versions:
 - "3.8.15-rc.2-alpine"
 - "3.8.16-alpine"
 - "3.8.17-alpine"
 - "3.8.17-rc.1-alpine"
 - "3.8.18-beta.1-alpine"
 - "3.9.0-beta.2-alpine"
 - "3.9.5"
 - "3.9.8"
 - "3.9.10"
 - "3.9.11"
 - "3.9.13"
 - "latest"
description: "RabbitMQ is an open source multi-protocol messaging broker."
---

This module is a singularity container wrapper for rabbitmq.
RabbitMQ is an open source multi-protocol messaging broker.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install rabbitmq
```

Or a specific version:

```bash
$ shpc install rabbitmq:3.8.15-rc.2-alpine
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load rabbitmq/3.8.15-rc.2-alpine
$ module help rabbitmq/3.8.15-rc.2-alpine
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rabbitmq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rabbitmq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rabbitmq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rabbitmq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rabbitmq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rabbitmq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### rabbitmq-defaults
       
```bash
$ singularity exec <container> /opt/rabbitmq/sbin/rabbitmq-defaults
$ podman run --it --rm --entrypoint /opt/rabbitmq/sbin/rabbitmq-defaults   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/rabbitmq/sbin/rabbitmq-defaults   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rabbitmq-diagnostics
       
```bash
$ singularity exec <container> /opt/rabbitmq/sbin/rabbitmq-diagnostics
$ podman run --it --rm --entrypoint /opt/rabbitmq/sbin/rabbitmq-diagnostics   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/rabbitmq/sbin/rabbitmq-diagnostics   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rabbitmq-env
       
```bash
$ singularity exec <container> /opt/rabbitmq/sbin/rabbitmq-env
$ podman run --it --rm --entrypoint /opt/rabbitmq/sbin/rabbitmq-env   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/rabbitmq/sbin/rabbitmq-env   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rabbitmq-plugins
       
```bash
$ singularity exec <container> /opt/rabbitmq/sbin/rabbitmq-plugins
$ podman run --it --rm --entrypoint /opt/rabbitmq/sbin/rabbitmq-plugins   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/rabbitmq/sbin/rabbitmq-plugins   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rabbitmq-queues
       
```bash
$ singularity exec <container> /opt/rabbitmq/sbin/rabbitmq-queues
$ podman run --it --rm --entrypoint /opt/rabbitmq/sbin/rabbitmq-queues   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/rabbitmq/sbin/rabbitmq-queues   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rabbitmq-server
       
```bash
$ singularity exec <container> /opt/rabbitmq/sbin/rabbitmq-server
$ podman run --it --rm --entrypoint /opt/rabbitmq/sbin/rabbitmq-server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/rabbitmq/sbin/rabbitmq-server   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rabbitmq-upgrade
       
```bash
$ singularity exec <container> /opt/rabbitmq/sbin/rabbitmq-upgrade
$ podman run --it --rm --entrypoint /opt/rabbitmq/sbin/rabbitmq-upgrade   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/rabbitmq/sbin/rabbitmq-upgrade   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rabbitmqctl
       
```bash
$ singularity exec <container> /opt/rabbitmq/sbin/rabbitmqctl
$ podman run --it --rm --entrypoint /opt/rabbitmq/sbin/rabbitmqctl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/rabbitmq/sbin/rabbitmqctl   -v ${PWD} -w ${PWD} <container> -c " $@"
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