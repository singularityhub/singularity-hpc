---
layout: container
name:  "ghcr.io/autamus/veloc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/veloc/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/ghcr.io/autamus/veloc/container.yaml"
updated_at: "2022-08-27 01:36:56.661642"
latest: "1.5"
container_url: "https://github.com/orgs/autamus/packages/container/package/veloc"
aliases:
 - "veloc-backend"
 - "veloc_check_node"
 - "veloc_env"
 - "veloc_glob_hosts"
 - "veloc_jsrun"
 - "veloc_list_down_nodes"
versions:
 - "1.4"
 - "1.5"
 - "latest"
description: "Very-Low Overhead Checkpointing System. VELOC is a multi-level checkpoint-restart runtime for HPC supercomputing infrastructures"
config: {"docker": "ghcr.io/autamus/veloc", "url": "https://github.com/orgs/autamus/packages/container/package/veloc", "maintainer": "@vsoch", "description": "Very-Low Overhead Checkpointing System. VELOC is a multi-level checkpoint-restart runtime for HPC supercomputing infrastructures", "latest": {"1.5": "sha256:98a4f6f292749587045821d0ab5e8c17dd1596fe523aa53252de543fc44fdeb3"}, "tags": {"1.4": "sha256:1cbebd19203bbcf3a9306683bb3f689c414c108ef18b15a4163c6e3529952914", "1.5": "sha256:98a4f6f292749587045821d0ab5e8c17dd1596fe523aa53252de543fc44fdeb3", "latest": "sha256:98a4f6f292749587045821d0ab5e8c17dd1596fe523aa53252de543fc44fdeb3"}, "aliases": {"veloc-backend": "/opt/view/bin/veloc-backend", "veloc_check_node": "/opt/view/bin/veloc_check_node", "veloc_env": "/opt/view/bin/veloc_env", "veloc_glob_hosts": "/opt/view/bin/veloc_glob_hosts", "veloc_jsrun": "/opt/view/bin/veloc_jsrun", "veloc_list_down_nodes": "/opt/view/bin/veloc_list_down_nodes"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/veloc.
Very-Low Overhead Checkpointing System. VELOC is a multi-level checkpoint-restart runtime for HPC supercomputing infrastructures
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/veloc
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/veloc:1.4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/veloc/1.4
$ module help ghcr.io/autamus/veloc/1.4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### veloc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### veloc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### veloc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### veloc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### veloc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### veloc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### veloc-backend
       
```bash
$ singularity exec <container> /opt/view/bin/veloc-backend
$ podman run --it --rm --entrypoint /opt/view/bin/veloc-backend   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/veloc-backend   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### veloc_check_node
       
```bash
$ singularity exec <container> /opt/view/bin/veloc_check_node
$ podman run --it --rm --entrypoint /opt/view/bin/veloc_check_node   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/veloc_check_node   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### veloc_env
       
```bash
$ singularity exec <container> /opt/view/bin/veloc_env
$ podman run --it --rm --entrypoint /opt/view/bin/veloc_env   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/veloc_env   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### veloc_glob_hosts
       
```bash
$ singularity exec <container> /opt/view/bin/veloc_glob_hosts
$ podman run --it --rm --entrypoint /opt/view/bin/veloc_glob_hosts   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/veloc_glob_hosts   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### veloc_jsrun
       
```bash
$ singularity exec <container> /opt/view/bin/veloc_jsrun
$ podman run --it --rm --entrypoint /opt/view/bin/veloc_jsrun   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/veloc_jsrun   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### veloc_list_down_nodes
       
```bash
$ singularity exec <container> /opt/view/bin/veloc_list_down_nodes
$ podman run --it --rm --entrypoint /opt/view/bin/veloc_list_down_nodes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/veloc_list_down_nodes   -v ${PWD} -w ${PWD} <container> -c " $@"
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