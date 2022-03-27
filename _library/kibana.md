---
layout: container
name:  "kibana"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/kibana/container.yaml"
updated_at: "2022-03-27 18:04:43.268058"
container_url: "https://hub.docker.com/_/kibana"
aliases:
 - "kibana"

 - "kibana-encryption-keys"

 - "kibana-keystore"

 - "kibana-plugin"

versions:
 - "7.12.0"
 - "7.12.1"
 - "7.13.1"
 - "7.13.2"
 - "7.13.3"
 - "7.14.0"
 - "7.14.2"
 - "7.16.2"
 - "7.16.3"
 - "8.0.0"
description: "Kibana gives shape to any kind of data — structured and unstructured — indexed in Elasticsearch."
---

This module is a singularity container wrapper for kibana.
Kibana gives shape to any kind of data — structured and unstructured — indexed in Elasticsearch.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install kibana
```

Or a specific version:

```bash
$ shpc install kibana:7.12.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load kibana/7.12.0
$ module help kibana/7.12.0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### kibana-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### kibana-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### kibana-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### kibana-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### kibana-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### kibana-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### kibana
       
```bash
$ singularity exec <container> /usr/share/kibana/bin/kibana
$ podman run --it --rm --entrypoint /usr/share/kibana/bin/kibana   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/share/kibana/bin/kibana   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kibana-encryption-keys
       
```bash
$ singularity exec <container> /usr/share/kibana/bin/kibana-encryption-keys
$ podman run --it --rm --entrypoint /usr/share/kibana/bin/kibana-encryption-keys   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/share/kibana/bin/kibana-encryption-keys   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kibana-keystore
       
```bash
$ singularity exec <container> /usr/share/kibana/bin/kibana-keystore
$ podman run --it --rm --entrypoint /usr/share/kibana/bin/kibana-keystore   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/share/kibana/bin/kibana-keystore   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kibana-plugin
       
```bash
$ singularity exec <container> /usr/share/kibana/bin/kibana-plugin
$ podman run --it --rm --entrypoint /usr/share/kibana/bin/kibana-plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/share/kibana/bin/kibana-plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
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