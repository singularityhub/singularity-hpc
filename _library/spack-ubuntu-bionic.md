---
layout: container
name:  "spack/ubuntu-bionic"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/spack/ubuntu-bionic/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/spack/ubuntu-bionic/container.yaml"
updated_at: "2022-08-27 02:54:42.361226"
latest: "v0.18.0"
container_url: "https://hub.docker.com/r/spack/ubuntu-bionic"
aliases:
 - "sbang"
 - "spack"
 - "spack-python"
versions:
 - "0.16.1"
 - "0.16.2"
 - "0.16.3"
 - "latest"
 - "0.16"
 - "prerelease"
 - "v0.17.2"
 - "v0.18.0"
description: "Ubuntu 18.04 with Spack preinstalled."
config: {"docker": "spack/ubuntu-bionic", "url": "https://hub.docker.com/r/spack/ubuntu-bionic", "maintainer": "@vsoch", "description": "Ubuntu 18.04 with Spack preinstalled.", "latest": {"v0.18.0": "sha256:585efe3455c4ecd1781f7cb711e5b072a3fbc18acc200550d9264f1124de51f1"}, "tags": {"0.16.1": "sha256:8261977ff63fe420446c349f0e3bd4e09a6417ebb1008ab472861041f1edd11b", "0.16.2": "sha256:698899684998df4a49f02bce1cffca9aa59644477f94b1909fc26b2adf4c4be4", "0.16.3": "sha256:fd9bfae1b8133bfb1c8636434f5ec24b2deae94e6b21d533cf6ee6df19af0772", "latest": "sha256:1ce08be957c1c4b86801a81583c8b2a664cde7c6e1e0a69c5f0c3ada0ebb4c02", "0.16": "sha256:5c6e3f016333b48bc85fa3e42634bb77d8af318c28c69b575e279cd875a93fe0", "prerelease": "sha256:e8565c944612471f06df71364e2ae390a9483837d116b208e7b476086b05ba4a", "v0.17.2": "sha256:29730dee9527826dfb3de157f46daefa68cedb611b2b393d06f4cb074c3223c5", "v0.18.0": "sha256:585efe3455c4ecd1781f7cb711e5b072a3fbc18acc200550d9264f1124de51f1"}, "aliases": {"sbang": "/opt/spack/bin/sbang", "spack": "/opt/spack/bin/spack", "spack-python": "/opt/spack/bin/spack-python"}}
---

This module is a singularity container wrapper for spack/ubuntu-bionic.
Ubuntu 18.04 with Spack preinstalled.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install spack/ubuntu-bionic
```

Or a specific version:

```bash
$ shpc install spack/ubuntu-bionic:0.16.1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load spack/ubuntu-bionic/0.16.1
$ module help spack/ubuntu-bionic/0.16.1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ubuntu-bionic-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ubuntu-bionic-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ubuntu-bionic-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ubuntu-bionic-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ubuntu-bionic-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ubuntu-bionic-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### sbang
       
```bash
$ singularity exec <container> /opt/spack/bin/sbang
$ podman run --it --rm --entrypoint /opt/spack/bin/sbang   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/spack/bin/sbang   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spack
       
```bash
$ singularity exec <container> /opt/spack/bin/spack
$ podman run --it --rm --entrypoint /opt/spack/bin/spack   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/spack/bin/spack   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spack-python
       
```bash
$ singularity exec <container> /opt/spack/bin/spack-python
$ podman run --it --rm --entrypoint /opt/spack/bin/spack-python   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/spack/bin/spack-python   -v ${PWD} -w ${PWD} <container> -c " $@"
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