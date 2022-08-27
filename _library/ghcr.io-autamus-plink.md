---
layout: container
name:  "ghcr.io/autamus/plink"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/plink/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/ghcr.io/autamus/plink/container.yaml"
updated_at: "2022-08-27 02:53:10.714110"
latest: "1.9.beta.6.10"
container_url: "https://github.com/orgs/autamus/packages/container/package/plink"
aliases:
 - "plink"
versions:
 - "1.9.beta.6.10"
 - "latest"
description: "PLINK is a free, open-source whole genome association analysis toolset, designed to perform a range of basic, large-scale analyses in a computationally efficient manner."
config: {"docker": "ghcr.io/autamus/plink", "url": "https://github.com/orgs/autamus/packages/container/package/plink", "maintainer": "@vsoch", "description": "PLINK is a free, open-source whole genome association analysis toolset, designed to perform a range of basic, large-scale analyses in a computationally efficient manner.", "latest": {"1.9.beta.6.10": "sha256:561d3a6d0e34bae0880daa39d4f150048ff4be15fb27bc027d64f0e5c1ca4a23"}, "tags": {"1.9.beta.6.10": "sha256:561d3a6d0e34bae0880daa39d4f150048ff4be15fb27bc027d64f0e5c1ca4a23", "latest": "sha256:561d3a6d0e34bae0880daa39d4f150048ff4be15fb27bc027d64f0e5c1ca4a23"}, "aliases": {"plink": "/opt/view/bin/plink"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/plink.
PLINK is a free, open-source whole genome association analysis toolset, designed to perform a range of basic, large-scale analyses in a computationally efficient manner.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/plink
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/plink:1.9.beta.6.10
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/plink/1.9.beta.6.10
$ module help ghcr.io/autamus/plink/1.9.beta.6.10
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### plink-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### plink-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### plink-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### plink-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### plink-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### plink-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### plink
       
```bash
$ singularity exec <container> /opt/view/bin/plink
$ podman run --it --rm --entrypoint /opt/view/bin/plink   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/plink   -v ${PWD} -w ${PWD} <container> -c " $@"
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