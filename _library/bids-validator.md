---
layout: container
name:  "bids/validator"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/bids/validator/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/bids/validator/container.yaml"
updated_at: "2022-08-27 01:35:16.739217"
latest: "v1.9.2"
container_url: "https://hub.docker.com/r/bids/validator"
aliases:
 - "bids-validator"
versions:
 - "latest"
 - "v1.7.0"
 - "v1.7.1"
 - "v1.7.3-dev.0"
 - "v1.7.4-dev.0"
 - "v1.8.1-dev.0"
 - "v1.8.5"
 - "v1.8.9"
 - "v1.9.2"
description: "A validator for BIDS (Brain Imaging Data Structure) datasets."
config: {"docker": "bids/validator", "url": "https://hub.docker.com/r/bids/validator", "maintainer": "@vsoch", "description": "A validator for BIDS (Brain Imaging Data Structure) datasets.", "latest": {"v1.9.2": "sha256:0c15cecae3919db5a14d43495cb2f2663b04c7f6cb049b7fdcfec3102284fe36"}, "tags": {"latest": "sha256:1af76bd57cd6eab2752f9f5887290ad44e30b0430859489ade6efa389f1d561e", "v1.7.0": "sha256:51c9481b357448cc2138909e03dfa8e053d424d5e776e94dbec929aeb96f9563", "v1.7.1": "sha256:d07b847f26e77e842abfd5b964f8553eb458ca796f4f0f5d1ca8d9290552ac2c", "v1.7.3-dev.0": "sha256:48d468d43b72ebb67014b33927171742d299c54c3e1c1db263a161b8917ca077", "v1.7.4-dev.0": "sha256:ab01a4d1105dd71d336d045e5787994299d66c927f2a42e231dde510c9c48a9a", "v1.8.1-dev.0": "sha256:8940256846cf4a98645760c6a03e5ee9686bdadfbbabfa8ed5f4a3e47fb0c910", "v1.8.5": "sha256:a2b52f99dd4571079bbe7547acaba3f6689b074de90e25fb85175568d2026705", "v1.8.9": "sha256:ee3d031f5096ace592fedfe87a095b4b634edcc5a8f464783034168257db90c0", "v1.9.2": "sha256:0c15cecae3919db5a14d43495cb2f2663b04c7f6cb049b7fdcfec3102284fe36"}, "filter": ["v*"], "aliases": {"bids-validator": "/usr/local/bin/bids-validator"}}
---

This module is a singularity container wrapper for bids/validator.
A validator for BIDS (Brain Imaging Data Structure) datasets.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install bids/validator
```

Or a specific version:

```bash
$ shpc install bids/validator:latest
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load bids/validator/latest
$ module help bids/validator/latest
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### validator-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### validator-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### validator-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### validator-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### validator-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### validator-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bids-validator
       
```bash
$ singularity exec <container> /usr/local/bin/bids-validator
$ podman run --it --rm --entrypoint /usr/local/bin/bids-validator   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bids-validator   -v ${PWD} -w ${PWD} <container> -c " $@"
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