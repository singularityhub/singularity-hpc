---
layout: container
name:  "ghcr.io/autamus/mothur"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/mothur/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/ghcr.io/autamus/mothur/container.yaml"
updated_at: "2022-08-27 01:36:19.823799"
latest: "1.46.1"
container_url: "https://github.com/orgs/autamus/packages/container/package/mothur"
aliases:
 - "mothur"
versions:
 - "1.45.1"
 - "1.45.3"
 - "1.46.0"
 - "1.46.1"
 - "latest"
description: "A single piece of open-source, expandable software to fill the bioinformatics needs of the microbial ecology community."
config: {"docker": "ghcr.io/autamus/mothur", "url": "https://github.com/orgs/autamus/packages/container/package/mothur", "maintainer": "@vsoch", "description": "A single piece of open-source, expandable software to fill the bioinformatics needs of the microbial ecology community.", "latest": {"1.46.1": "sha256:646ee790161ab827642175fb7131ddd3386f13df23133cb1aa66c51360ab1bfd"}, "tags": {"1.45.1": "sha256:af8905f940a15b823fab61acf3324630ae8e2b7240d1d28af54317c4e22af384", "1.45.3": "sha256:8fd2377dfeef70dad28b421d537ded4e57f20fc8fde781abebe93815a0346d87", "1.46.0": "sha256:99914cf54e72d6c2be85c7aaf7369497f94f56ac3823e410b41abdc1c4a1cab6", "1.46.1": "sha256:646ee790161ab827642175fb7131ddd3386f13df23133cb1aa66c51360ab1bfd", "latest": "sha256:646ee790161ab827642175fb7131ddd3386f13df23133cb1aa66c51360ab1bfd"}, "aliases": {"mothur": "/opt/view/bin/mothur"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/mothur.
A single piece of open-source, expandable software to fill the bioinformatics needs of the microbial ecology community.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/mothur
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/mothur:1.45.1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/mothur/1.45.1
$ module help ghcr.io/autamus/mothur/1.45.1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mothur-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mothur-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mothur-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mothur-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mothur-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mothur-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### mothur
       
```bash
$ singularity exec <container> /opt/view/bin/mothur
$ podman run --it --rm --entrypoint /opt/view/bin/mothur   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/mothur   -v ${PWD} -w ${PWD} <container> -c " $@"
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