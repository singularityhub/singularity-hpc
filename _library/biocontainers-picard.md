---
layout: container
name:  "biocontainers/picard"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/biocontainers/picard/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/biocontainers/picard/container.yaml"
updated_at: "2022-08-27 01:35:18.840775"
latest: "2.3.0"
container_url: "https://hub.docker.com/r/biocontainers/picard"
aliases:
 - "picard"
versions:
 - "v1.139_cv3"
 - "2.3.0"
 - "1.141"
 - "1.139"
description: "Java CLI tools for manipulating HTS data and formats"
config: {"docker": "biocontainers/picard", "latest": {"2.3.0": "sha256:5e1bc7788a3aa1329e59821e3f89b5bb209372926a67ed1a95f7b9a71350e2be"}, "tags": {"v1.139_cv3": "sha256:05a6dd401d47c930191fa8c017b2cf60c099c4da236f134586a2f3610e426229", "2.3.0": "sha256:5e1bc7788a3aa1329e59821e3f89b5bb209372926a67ed1a95f7b9a71350e2be", "1.141": "sha256:675128282859c9edf1c8679478c828a48d980a4e73b95abba6a087d315d01cfc", "1.139": "sha256:4ef7e76d7cae7ffe804a304377adba870de777b81e90c1e6f5c822280e0243ca"}, "filter": ["v*"], "maintainer": "@vsoch", "url": "https://hub.docker.com/r/biocontainers/picard", "description": "Java CLI tools for manipulating HTS data and formats", "aliases": {"picard": "java -jar /opt/conda/bin/picard.jar"}}
---

This module is a singularity container wrapper for biocontainers/picard.
Java CLI tools for manipulating HTS data and formats
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install biocontainers/picard
```

Or a specific version:

```bash
$ shpc install biocontainers/picard:v1.139_cv3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load biocontainers/picard/v1.139_cv3
$ module help biocontainers/picard/v1.139_cv3
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
$ singularity exec <container> java -jar /opt/conda/bin/picard.jar
$ podman run --it --rm --entrypoint java   -v ${PWD} -w ${PWD} <container> -c "-jar /opt/conda/bin/picard.jar $@"
$ docker run --it --rm --entrypoint java   -v ${PWD} -w ${PWD} <container> -c "-jar /opt/conda/bin/picard.jar $@"
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