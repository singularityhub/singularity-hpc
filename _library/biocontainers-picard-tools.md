---
layout: container
name:  "biocontainers/picard-tools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/biocontainers/picard-tools/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/biocontainers/picard-tools/container.yaml"
updated_at: "2022-08-27 01:35:18.320066"
latest: "v2.18.25dfsg-2-deb_cv1"
container_url: "https://hub.docker.com/r/biocontainers/picard-tools/tags"

versions:
 - "v2.18.25dfsg-2-deb_cv1"
description: "The Picard command-line tools are packaged as executable jar files."
config: {"docker": "biocontainers/picard-tools", "latest": {"v2.18.25dfsg-2-deb_cv1": "sha256:55513f9b0bda5403e31dec41142447045650e28a2accf3d0dd7e548b301c3a88"}, "tags": {"v2.18.25dfsg-2-deb_cv1": "sha256:55513f9b0bda5403e31dec41142447045650e28a2accf3d0dd7e548b301c3a88"}, "filter": ["v*"], "maintainer": "@vsoch", "description": "The Picard command-line tools are packaged as executable jar files.", "url": "https://hub.docker.com/r/biocontainers/picard-tools/tags"}
---

This module is a singularity container wrapper for biocontainers/picard-tools.
The Picard command-line tools are packaged as executable jar files.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install biocontainers/picard-tools
```

Or a specific version:

```bash
$ shpc install biocontainers/picard-tools:v2.18.25dfsg-2-deb_cv1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load biocontainers/picard-tools/v2.18.25dfsg-2-deb_cv1
$ module help biocontainers/picard-tools/v2.18.25dfsg-2-deb_cv1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### picard-tools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### picard-tools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### picard-tools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### picard-tools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### picard-tools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### picard-tools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### picard-tools

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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