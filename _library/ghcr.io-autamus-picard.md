---
layout: container
name:  "ghcr.io/autamus/picard"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/picard/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/ghcr.io/autamus/picard/container.yaml"
updated_at: "2022-08-27 01:36:31.408512"
latest: "2.26.5"
container_url: "https://github.com/orgs/autamus/packages/container/package/picard"
aliases:
 - "picard"
 - "picard.jar"
versions:
 - "2.25.2"
 - "2.25.3"
 - "2.25.4"
 - "2.25.5"
 - "2.25.6"
 - "2.26.0"
 - "2.26.4"
 - "2.26.5"
 - "latest"
 - "2.25.7"
description: "A set of command line tools (in Java) for manipulating high-throughput sequencing (HTS) data and formats such as SAM/BAM/CRAM and VCF."
config: {"docker": "ghcr.io/autamus/picard", "url": "https://github.com/orgs/autamus/packages/container/package/picard", "maintainer": "@vsoch", "description": "A set of command line tools (in Java) for manipulating high-throughput sequencing (HTS) data and formats such as SAM/BAM/CRAM and VCF.", "latest": {"2.26.5": "sha256:4bdde83c5a64bfd9be18631eb4ad5fe8b5b5bef6f11345fc70299c2bc370ac70"}, "tags": {"2.25.2": "sha256:59d36498e8678f471aa46e0f1de0c1f0de953feb826ce76c48bd56ba5d57f35e", "2.25.3": "sha256:5ad0c904339aedf7f6e2feb20706bbe594ecff5226b5df947bccc817f25bc882", "2.25.4": "sha256:f9e420ca9ee6587356f413a079d587ad0e2f94c326b2433b70fa0265f17d963a", "2.25.5": "sha256:0361840e9c70fbf9c701aecda3e488d399a6dc7f00c306fdfec14b8755f7a633", "2.25.6": "sha256:a0604d204911e8e8ad17a47b1eebef02b590e811c02ecadccc2a33cdfa336fe4", "2.26.0": "sha256:accd314b904bb0a3d97597d7496b5bf6f0ea8b7e1a784c89546c7ead1e5a6068", "2.26.4": "sha256:d5e54eb6f2dee5e94b3cca0110b3528a52a30361b2bbd38ad6c265d6acff88c8", "2.26.5": "sha256:4bdde83c5a64bfd9be18631eb4ad5fe8b5b5bef6f11345fc70299c2bc370ac70", "latest": "sha256:4bdde83c5a64bfd9be18631eb4ad5fe8b5b5bef6f11345fc70299c2bc370ac70", "2.25.7": "sha256:31bdbd379c8059d344cbbf5b31dafc54a17f30a164846f104001f5f3438b2075"}, "aliases": {"picard": "/opt/view/bin/picard", "picard.jar": "/opt/view/bin/java -jar /opt/view/bin/picard.jar"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/picard.
A set of command line tools (in Java) for manipulating high-throughput sequencing (HTS) data and formats such as SAM/BAM/CRAM and VCF.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/picard
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/picard:2.25.2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/picard/2.25.2
$ module help ghcr.io/autamus/picard/2.25.2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### picard-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### picard-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### picard-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### picard-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### picard-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### picard-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### picard
       
```bash
$ singularity exec <container> /opt/view/bin/picard
$ podman run --it --rm --entrypoint /opt/view/bin/picard   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/picard   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### picard.jar
       
```bash
$ singularity exec <container> /opt/view/bin/java -jar /opt/view/bin/picard.jar
$ podman run --it --rm --entrypoint /opt/view/bin/java   -v ${PWD} -w ${PWD} <container> -c "-jar /opt/view/bin/picard.jar $@"
$ docker run --it --rm --entrypoint /opt/view/bin/java   -v ${PWD} -w ${PWD} <container> -c "-jar /opt/view/bin/picard.jar $@"
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