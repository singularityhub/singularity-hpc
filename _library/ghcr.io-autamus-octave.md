---
layout: container
name:  "ghcr.io/autamus/octave"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/octave/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/ghcr.io/autamus/octave/container.yaml"
updated_at: "2022-08-27 01:36:24.029925"
latest: "7.1.0"
container_url: "https://github.com/orgs/autamus/packages/container/package/octave"
aliases:
 - "octave"
 - "octave-6.2.0"
 - "octave-cli"
 - "octave-cli-6.2.0"
 - "octave-config"
 - "octave-config-6.2.0"
versions:
 - "6.2.0"
 - "6.3.0"
 - "6.4.0"
 - "latest"
 - "7.1.0"
description: "GNU Octave is a high-level interpreted language, primarily intended for numerical computations (like an open source Matlab)"
config: {"docker": "ghcr.io/autamus/octave", "url": "https://github.com/orgs/autamus/packages/container/package/octave", "maintainer": "@vsoch", "description": "GNU Octave is a high-level interpreted language, primarily intended for numerical computations (like an open source Matlab)", "latest": {"7.1.0": "sha256:66e8b796cc8299ac4339023dcdab9cb3cac2e330b7b1975fa8c854f7a16ac656"}, "tags": {"6.2.0": "sha256:26a7d5c22a201b4acaa3e4c4d7d9c1aac0009fae4ea71cd73282762b46f39184", "6.3.0": "sha256:e345d6806ab132db208e84885b5c1fdc5cbc2ba20c41e3b6e9daf839c86090b6", "6.4.0": "sha256:b89c9561a24aa412e90560cb32f4affa68b78a626ba1636f9fa289add05846ba", "latest": "sha256:66e8b796cc8299ac4339023dcdab9cb3cac2e330b7b1975fa8c854f7a16ac656", "7.1.0": "sha256:66e8b796cc8299ac4339023dcdab9cb3cac2e330b7b1975fa8c854f7a16ac656"}, "aliases": {"octave": "/opt/view/bin/octave", "octave-6.2.0": "/opt/view/bin/octave-6.2.0", "octave-cli": "/opt/view/bin/octave-cli", "octave-cli-6.2.0": "/opt/view/bin/octave-cli-6.2.0", "octave-config": "/opt/view/bin/octave-config", "octave-config-6.2.0": "/opt/view/bin/octave-config-6.2.0"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/octave.
GNU Octave is a high-level interpreted language, primarily intended for numerical computations (like an open source Matlab)
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/octave
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/octave:6.2.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/octave/6.2.0
$ module help ghcr.io/autamus/octave/6.2.0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### octave-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### octave-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### octave-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### octave-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### octave-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### octave-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### octave
       
```bash
$ singularity exec <container> /opt/view/bin/octave
$ podman run --it --rm --entrypoint /opt/view/bin/octave   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/octave   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### octave-6.2.0
       
```bash
$ singularity exec <container> /opt/view/bin/octave-6.2.0
$ podman run --it --rm --entrypoint /opt/view/bin/octave-6.2.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/octave-6.2.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### octave-cli
       
```bash
$ singularity exec <container> /opt/view/bin/octave-cli
$ podman run --it --rm --entrypoint /opt/view/bin/octave-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/octave-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### octave-cli-6.2.0
       
```bash
$ singularity exec <container> /opt/view/bin/octave-cli-6.2.0
$ podman run --it --rm --entrypoint /opt/view/bin/octave-cli-6.2.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/octave-cli-6.2.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### octave-config
       
```bash
$ singularity exec <container> /opt/view/bin/octave-config
$ podman run --it --rm --entrypoint /opt/view/bin/octave-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/octave-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### octave-config-6.2.0
       
```bash
$ singularity exec <container> /opt/view/bin/octave-config-6.2.0
$ podman run --it --rm --entrypoint /opt/view/bin/octave-config-6.2.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/octave-config-6.2.0   -v ${PWD} -w ${PWD} <container> -c " $@"
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