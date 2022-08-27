---
layout: container
name:  "ghcr.io/autamus/xz"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/xz/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/ghcr.io/autamus/xz/container.yaml"
updated_at: "2022-08-27 02:53:44.262466"
latest: "5.2.5"
container_url: "https://github.com/orgs/autamus/packages/container/package/xz"
aliases:
 - "xz"
 - "xzcat"
 - "xzcmp"
 - "xzdec"
 - "xzdiff"
 - "xzegrep"
 - "xzfgrep"
 - "xzgrep"
 - "xzless"
 - "xzmore"
versions:
 - "5.2.5"
 - "latest"
description: "XZ Utils is free general-purpose data compression software with a high compression ratio."
config: {"docker": "ghcr.io/autamus/xz", "url": "https://github.com/orgs/autamus/packages/container/package/xz", "maintainer": "@vsoch", "description": "XZ Utils is free general-purpose data compression software with a high compression ratio.", "latest": {"5.2.5": "sha256:c02609a24da48a0c328832099c95378e0ce43397b4aeda1e440245c52e833f6f"}, "tags": {"5.2.5": "sha256:c02609a24da48a0c328832099c95378e0ce43397b4aeda1e440245c52e833f6f", "latest": "sha256:c02609a24da48a0c328832099c95378e0ce43397b4aeda1e440245c52e833f6f"}, "aliases": {"xz": "/opt/view/bin/xz", "xzcat": "/opt/view/bin/xzcat", "xzcmp": "/opt/view/bin/xzcmp", "xzdec": "/opt/view/bin/xzdec", "xzdiff": "/opt/view/bin/xzdiff", "xzegrep": "/opt/view/bin/xzegrep", "xzfgrep": "/opt/view/bin/xzfgrep", "xzgrep": "/opt/view/bin/xzgrep", "xzless": "/opt/view/bin/xzless", "xzmore": "/opt/view/bin/xzmore"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/xz.
XZ Utils is free general-purpose data compression software with a high compression ratio.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/xz
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/xz:5.2.5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/xz/5.2.5
$ module help ghcr.io/autamus/xz/5.2.5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### xz-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### xz-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### xz-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### xz-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### xz-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### xz-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### xz
       
```bash
$ singularity exec <container> /opt/view/bin/xz
$ podman run --it --rm --entrypoint /opt/view/bin/xz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/xz   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xzcat
       
```bash
$ singularity exec <container> /opt/view/bin/xzcat
$ podman run --it --rm --entrypoint /opt/view/bin/xzcat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/xzcat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xzcmp
       
```bash
$ singularity exec <container> /opt/view/bin/xzcmp
$ podman run --it --rm --entrypoint /opt/view/bin/xzcmp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/xzcmp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xzdec
       
```bash
$ singularity exec <container> /opt/view/bin/xzdec
$ podman run --it --rm --entrypoint /opt/view/bin/xzdec   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/xzdec   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xzdiff
       
```bash
$ singularity exec <container> /opt/view/bin/xzdiff
$ podman run --it --rm --entrypoint /opt/view/bin/xzdiff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/xzdiff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xzegrep
       
```bash
$ singularity exec <container> /opt/view/bin/xzegrep
$ podman run --it --rm --entrypoint /opt/view/bin/xzegrep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/xzegrep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xzfgrep
       
```bash
$ singularity exec <container> /opt/view/bin/xzfgrep
$ podman run --it --rm --entrypoint /opt/view/bin/xzfgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/xzfgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xzgrep
       
```bash
$ singularity exec <container> /opt/view/bin/xzgrep
$ podman run --it --rm --entrypoint /opt/view/bin/xzgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/xzgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xzless
       
```bash
$ singularity exec <container> /opt/view/bin/xzless
$ podman run --it --rm --entrypoint /opt/view/bin/xzless   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/xzless   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xzmore
       
```bash
$ singularity exec <container> /opt/view/bin/xzmore
$ podman run --it --rm --entrypoint /opt/view/bin/xzmore   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/xzmore   -v ${PWD} -w ${PWD} <container> -c " $@"
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