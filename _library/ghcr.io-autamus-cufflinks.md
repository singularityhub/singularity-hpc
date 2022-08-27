---
layout: container
name:  "ghcr.io/autamus/cufflinks"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/cufflinks/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/ghcr.io/autamus/cufflinks/container.yaml"
updated_at: "2022-08-27 02:52:10.423443"
latest: "2.2.1"
container_url: "https://github.com/orgs/autamus/packages/container/package/cufflinks"
aliases:
 - "cuffcompare"
 - "cuffdiff"
 - "cufflinks"
 - "cuffmerge"
 - "cuffnorm"
 - "cuffquant"
versions:
 - "2.2.1"
 - "latest"
description: "Cufflinks assembles transcripts, estimates their abundances, and tests for differential expression and regulation in RNA-Seq samples."
config: {"docker": "ghcr.io/autamus/cufflinks", "url": "https://github.com/orgs/autamus/packages/container/package/cufflinks", "maintainer": "@vsoch", "description": "Cufflinks assembles transcripts, estimates their abundances, and tests for differential expression and regulation in RNA-Seq samples.", "latest": {"2.2.1": "sha256:6c39b07196632e49b7b5dcb770985dddc71e6e9518643b22adbd77d93d2c681c"}, "tags": {"2.2.1": "sha256:6c39b07196632e49b7b5dcb770985dddc71e6e9518643b22adbd77d93d2c681c", "latest": "sha256:6c39b07196632e49b7b5dcb770985dddc71e6e9518643b22adbd77d93d2c681c"}, "aliases": {"cuffcompare": "/opt/view/bin/cuffcompare", "cuffdiff": "/opt/view/bin/cuffdiff", "cufflinks": "/opt/view/bin/cufflinks", "cuffmerge": "/opt/view/bin/cuffmerge", "cuffnorm": "/opt/view/bin/cuffnorm", "cuffquant": "/opt/view/bin/cuffquant"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/cufflinks.
Cufflinks assembles transcripts, estimates their abundances, and tests for differential expression and regulation in RNA-Seq samples.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/cufflinks
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/cufflinks:2.2.1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/cufflinks/2.2.1
$ module help ghcr.io/autamus/cufflinks/2.2.1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cufflinks-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cufflinks-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cufflinks-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cufflinks-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cufflinks-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cufflinks-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cuffcompare
       
```bash
$ singularity exec <container> /opt/view/bin/cuffcompare
$ podman run --it --rm --entrypoint /opt/view/bin/cuffcompare   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/cuffcompare   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cuffdiff
       
```bash
$ singularity exec <container> /opt/view/bin/cuffdiff
$ podman run --it --rm --entrypoint /opt/view/bin/cuffdiff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/cuffdiff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cufflinks
       
```bash
$ singularity exec <container> /opt/view/bin/cufflinks
$ podman run --it --rm --entrypoint /opt/view/bin/cufflinks   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/cufflinks   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cuffmerge
       
```bash
$ singularity exec <container> /opt/view/bin/cuffmerge
$ podman run --it --rm --entrypoint /opt/view/bin/cuffmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/cuffmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cuffnorm
       
```bash
$ singularity exec <container> /opt/view/bin/cuffnorm
$ podman run --it --rm --entrypoint /opt/view/bin/cuffnorm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/cuffnorm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cuffquant
       
```bash
$ singularity exec <container> /opt/view/bin/cuffquant
$ podman run --it --rm --entrypoint /opt/view/bin/cuffquant   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/cuffquant   -v ${PWD} -w ${PWD} <container> -c " $@"
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