---
layout: container
name:  "bids/rshrf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/bids/rshrf/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/bids/rshrf/container.yaml"
updated_at: "2022-08-27 01:35:15.156617"
latest: "1.5.8"
container_url: "https://hub.docker.com/r/bids/rshrf"
aliases:
 - "rsHRF"
versions:
 - "latest"
 - "1.5.8"
 - "1.4.4"
 - "1.3.9"
 - "1.2.2"
 - "1.1.1"
description: "Resting state HRF estimation and deconvolution (https://github.com/BIDS-Apps/rsHRF)"
config: {"docker": "bids/rshrf", "url": "https://hub.docker.com/r/bids/rshrf", "maintainer": "@vsoch", "description": "Resting state HRF estimation and deconvolution (https://github.com/BIDS-Apps/rsHRF)", "latest": {"1.5.8": "sha256:7124aa5534b9fd9630450edb294c21263f62422c4a684b7aef921b47bf26ea32"}, "tags": {"latest": "sha256:7124aa5534b9fd9630450edb294c21263f62422c4a684b7aef921b47bf26ea32", "1.5.8": "sha256:7124aa5534b9fd9630450edb294c21263f62422c4a684b7aef921b47bf26ea32", "1.4.4": "sha256:0e7abbe256f66cdb2846b46830a74d846e02fc7344cb30f609e1b7c2f08a5052", "1.3.9": "sha256:68f1eb362cf4bd4812fdb6b8051757e731ae256490f94184c78a4eaf9258e458", "1.2.2": "sha256:3f29045ee611a0d8e98b47c7ef3d4907b221e85e4edca24ac4e3814ef789b7a8", "1.1.1": "sha256:53519ee4540668191150bb12b799bef186b30818d848002d93375429e315f72e"}, "filter": ["v*"], "aliases": {"rsHRF": "/usr/bin/rsHRF"}}
---

This module is a singularity container wrapper for bids/rshrf.
Resting state HRF estimation and deconvolution (https://github.com/BIDS-Apps/rsHRF)
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install bids/rshrf
```

Or a specific version:

```bash
$ shpc install bids/rshrf:latest
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load bids/rshrf/latest
$ module help bids/rshrf/latest
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rshrf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rshrf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rshrf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rshrf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rshrf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rshrf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### rsHRF
       
```bash
$ singularity exec <container> /usr/bin/rsHRF
$ podman run --it --rm --entrypoint /usr/bin/rsHRF   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/rsHRF   -v ${PWD} -w ${PWD} <container> -c " $@"
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