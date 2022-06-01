---
layout: container
name:  "ghcr.io/autamus/adios"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/adios/container.yaml"
updated_at: "2022-06-01 02:29:00.097140"
container_url: "https://github.com/orgs/autamus/packages/container/package/adios"
aliases:
 - "adios_config"

 - "adios_lint"

 - "adios_list_methods"

 - "adios_list_methods_nompi"

 - "adios_list_methods_readonly"

 - "adios_list_methods_readonly_nompi"

versions:
 - "1.13.1"
 - "latest"
description: "The Adaptable IO System (ADIOS) provides a simple, flexible way for scientists to describe the data in their code that may need to be written, read, or processed outside of the running simulation."
---

This module is a singularity container wrapper for ghcr.io/autamus/adios.
The Adaptable IO System (ADIOS) provides a simple, flexible way for scientists to describe the data in their code that may need to be written, read, or processed outside of the running simulation.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/adios
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/adios:1.13.1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/adios/1.13.1
$ module help ghcr.io/autamus/adios/1.13.1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### adios-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### adios-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### adios-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### adios-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### adios-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### adios-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### adios_config
       
```bash
$ singularity exec <container> /opt/view/bin/adios_config
$ podman run --it --rm --entrypoint /opt/view/bin/adios_config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/adios_config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### adios_lint
       
```bash
$ singularity exec <container> /opt/view/bin/adios_lint
$ podman run --it --rm --entrypoint /opt/view/bin/adios_lint   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/adios_lint   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### adios_list_methods
       
```bash
$ singularity exec <container> /opt/view/bin/adios_list_methods
$ podman run --it --rm --entrypoint /opt/view/bin/adios_list_methods   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/adios_list_methods   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### adios_list_methods_nompi
       
```bash
$ singularity exec <container> /opt/view/bin/adios_list_methods_nompi
$ podman run --it --rm --entrypoint /opt/view/bin/adios_list_methods_nompi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/adios_list_methods_nompi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### adios_list_methods_readonly
       
```bash
$ singularity exec <container> /opt/view/bin/adios_list_methods_readonly
$ podman run --it --rm --entrypoint /opt/view/bin/adios_list_methods_readonly   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/adios_list_methods_readonly   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### adios_list_methods_readonly_nompi
       
```bash
$ singularity exec <container> /opt/view/bin/adios_list_methods_readonly_nompi
$ podman run --it --rm --entrypoint /opt/view/bin/adios_list_methods_readonly_nompi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/adios_list_methods_readonly_nompi   -v ${PWD} -w ${PWD} <container> -c " $@"
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