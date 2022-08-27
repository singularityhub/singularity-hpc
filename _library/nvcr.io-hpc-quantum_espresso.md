---
layout: container
name:  "nvcr.io/hpc/quantum_espresso"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/nvcr.io/hpc/quantum_espresso/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/nvcr.io/hpc/quantum_espresso/container.yaml"
updated_at: "2022-08-27 02:54:00.420342"
latest: "qe-7.0"
container_url: "https://ngc.nvidia.com/catalog/containers/hpc:quantum_espresso/tags"

versions:
 - "v6.7"
 - "qe-6.8"
 - "qe-7.0"
description: "Quantum ESPRESSO is an integrated suite of Open-Source computer codes for electronic-structure calculations and materials modeling at the nanoscale based on density-functional theory, plane waves, and pseudopotentials."
config: {"docker": "nvcr.io/hpc/quantum_espresso", "url": "https://ngc.nvidia.com/catalog/containers/hpc:quantum_espresso/tags", "maintainer": "@vsoch", "description": "Quantum ESPRESSO is an integrated suite of Open-Source computer codes for electronic-structure calculations and materials modeling at the nanoscale based on density-functional theory, plane waves, and pseudopotentials.", "latest": {"qe-7.0": "sha256:e117f9df9868b7d7908fabc951719d8bf4a450ef7a9a01cf2e0ed5ab3f2b9651"}, "tags": {"v6.7": "sha256:fdcea13eec98f48af813f172be42a40adf4e856d07cfb4ee1fc584d5c4a8f0f9", "qe-6.8": "sha256:1db6a3eae9baa8cbb6c72f227c14d48fd8a8b2548f021c10764608a321525de8", "qe-7.0": "sha256:e117f9df9868b7d7908fabc951719d8bf4a450ef7a9a01cf2e0ed5ab3f2b9651"}, "filter": ["v*"], "features": {"gpu": true}}
---

This module is a singularity container wrapper for nvcr.io/hpc/quantum_espresso.
Quantum ESPRESSO is an integrated suite of Open-Source computer codes for electronic-structure calculations and materials modeling at the nanoscale based on density-functional theory, plane waves, and pseudopotentials.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install nvcr.io/hpc/quantum_espresso
```

Or a specific version:

```bash
$ shpc install nvcr.io/hpc/quantum_espresso:v6.7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load nvcr.io/hpc/quantum_espresso/v6.7
$ module help nvcr.io/hpc/quantum_espresso/v6.7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### quantum_espresso-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### quantum_espresso-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### quantum_espresso-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### quantum_espresso-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### quantum_espresso-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### quantum_espresso-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### quantum_espresso

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