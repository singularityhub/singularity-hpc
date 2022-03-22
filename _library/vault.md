---
layout: container
name:  "vault"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/vault/container.yaml"
updated_at: "2022-03-22 13:22:19.452178"
container_url: "https://hub.docker.com/_/vault"
aliases:
 - "vault"

versions:
 - "1.4.7"
 - "1.7.1"
 - "1.7.2"
 - "1.8.0-rc1"
 - "1.8.2"
 - "1.8.4"
 - "1.9.0"
 - "1.9.2"
 - "1.9.3"
 - "latest"
description: "Vault is a tool for securely accessing secrets via a unified interface and tight access control."
---

This module is a singularity container wrapper for vault.
Vault is a tool for securely accessing secrets via a unified interface and tight access control.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install vault
```

Or a specific version:

```bash
$ shpc install vault:1.4.7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load vault/1.4.7
$ module help vault/1.4.7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### vault-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### vault-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### vault-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### vault-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### vault-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### vault-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### vault
       
```bash
$ singularity exec <container> /bin/vault
$ podman run --it --rm --entrypoint /bin/vault   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /bin/vault   -v ${PWD} -w ${PWD} <container> -c " $@"
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