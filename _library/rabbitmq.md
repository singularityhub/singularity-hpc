---
layout: container
name:  "rabbitmq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/rabbitmq/container.yaml"
updated_at: "2021-04-20 03:17:50.850319"
container_url: ""
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
$ shpc install rabbitmq:latest
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load rabbitmq/latest
$ module help rabbitmq/latest
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### rabbitmq-run:

```bash
$ singularity run <container>
```

#### rabbitmq-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### rabbitmq-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
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
```


#### rabbitmq-diagnostics
       
```bash
$ singularity exec <container> /opt/rabbitmq/sbin/rabbitmq-diagnostics
```


#### rabbitmq-env
       
```bash
$ singularity exec <container> /opt/rabbitmq/sbin/rabbitmq-env
```


#### rabbitmq-plugins
       
```bash
$ singularity exec <container> /opt/rabbitmq/sbin/rabbitmq-plugins
```


#### rabbitmq-queues
       
```bash
$ singularity exec <container> /opt/rabbitmq/sbin/rabbitmq-queues
```


#### rabbitmq-server
       
```bash
$ singularity exec <container> /opt/rabbitmq/sbin/rabbitmq-server
```


#### rabbitmq-upgrade
       
```bash
$ singularity exec <container> /opt/rabbitmq/sbin/rabbitmq-upgrade
```


#### rabbitmqctl
       
```bash
$ singularity exec <container> /opt/rabbitmq/sbin/rabbitmqctl
```



In the above, the `<container>` directive will reference an actual container provided
by the module, for the version you have chosen to load. Note that although a container
might provide custom commands, every container exposes unique exec, shell, run, and
inspect aliases. For each of the above, you can export:

 - SINGULARITY_OPTS: to define custom options for singularity (e.g., --debug)
 - SINGULARITY_COMMAND_OPTS: to define custom options for the command (e.g., -b)

<br>
  
### Install

You can install shpc locally (for yourself or your user base) as follows:

```bash
$ git clone https://github.com/singularityhub/singularity-hpc
$ cd singularity-hpc
$ pip install -e .
```

Have any questions, or want to request a new module or version? [ask for help!](https://github.com/singularityhub/singularity-hpc/issues)