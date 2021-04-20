---
layout: container
name:  "consul"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/consul/container.yaml"
updated_at: "2021-04-20 03:16:10.766774"
container_url: ""
aliases:
 - "consul"

versions:
 - "1.7.14"
 - "latest"
description: "Consul is a datacenter runtime that provides service discovery, configuration, and orchestration."
---

This module is a singularity container wrapper for consul.
Consul is a datacenter runtime that provides service discovery, configuration, and orchestration.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install consul
```

Or a specific version:

```bash
$ shpc install consul:1.7.14
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load consul/1.7.14
$ module help consul/1.7.14
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### consul-run:

```bash
$ singularity run <container>
```

#### consul-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### consul-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### consul-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### consul-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### consul
       
```bash
$ singularity exec <container> /bin/consul
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