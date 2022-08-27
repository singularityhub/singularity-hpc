---
layout: container
name:  "quay.io/biocontainers/sambamba"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sambamba/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/sambamba/container.yaml"
updated_at: "2022-08-27 02:54:24.610905"
latest: "0.8.2--h98b6b92_2"
container_url: "https://quay.io/repository/biocontainers/sambamba"
aliases:
 - "sambamba"
versions:
 - "0.6.9--h89e63da_0"
 - "0.7.1--h984e79f_3"
 - "0.8.0--h984e79f_0"
 - "0.8.1--h41abebc_0"
 - "0.8.2--h98b6b92_2"
description: "Sambamba is a high performance highly parallel robust and fast tool (and library), written in the D programming language, for working with SAM and BAM files."
config: {"docker": "quay.io/biocontainers/sambamba", "url": "https://quay.io/repository/biocontainers/sambamba", "maintainer": "@audreystott", "description": "Sambamba is a high performance highly parallel robust and fast tool (and library), written in the D programming language, for working with SAM and BAM files.", "latest": {"0.8.2--h98b6b92_2": "sha256:7eef9b8c037f526a3ecb71cc05604c77eda72d90a50ca29c0af42a6e94580073"}, "tags": {"0.6.9--h89e63da_0": "sha256:b7852eccc079fff9e1ff6c4fb6e59883624373e2489588174da9f99db83b431b", "0.7.1--h984e79f_3": "sha256:9ec72d3d0991c4209830e4ff17937986808c64c430780071559e7072e8317ab3", "0.8.0--h984e79f_0": "sha256:ae92faef4c53a632b2120dfffa7b6dcfe5366a0647e61bbbd6188aedc89da4e8", "0.8.1--h41abebc_0": "sha256:69c2510f3f5bafe3e14aee763ef437f2e70805f1b18d07e97fec7e61ef52375d", "0.8.2--h98b6b92_2": "sha256:7eef9b8c037f526a3ecb71cc05604c77eda72d90a50ca29c0af42a6e94580073"}, "aliases": {"sambamba": "/usr/local/bin/sambamba"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/sambamba.
Sambamba is a high performance highly parallel robust and fast tool (and library), written in the D programming language, for working with SAM and BAM files.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sambamba
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sambamba:0.6.9--h89e63da_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sambamba/0.6.9--h89e63da_0
$ module help quay.io/biocontainers/sambamba/0.6.9--h89e63da_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sambamba-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sambamba-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sambamba-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sambamba-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sambamba-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sambamba-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### sambamba
       
```bash
$ singularity exec <container> /usr/local/bin/sambamba
$ podman run --it --rm --entrypoint /usr/local/bin/sambamba   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sambamba   -v ${PWD} -w ${PWD} <container> -c " $@"
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