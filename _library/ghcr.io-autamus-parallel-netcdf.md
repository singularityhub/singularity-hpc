---
layout: container
name:  "ghcr.io/autamus/parallel-netcdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/parallel-netcdf/container.yaml"
updated_at: "2022-03-16 20:17:03.930022"
container_url: "https://github.com/orgs/autamus/packages/container/package/parallel-netcdf"
aliases:
 - "pnetcdf-config"

 - "pnetcdf_version"

versions:
 - "1.12.2"
description: "PnetCDF (Parallel netCDF) is a high-performance parallel I/O library for accessing files in format compatibility with Unidata's NetCDF, specifically the formats of CDF-1, 2, and 5."
---

This module is a singularity container wrapper for ghcr.io/autamus/parallel-netcdf.
PnetCDF (Parallel netCDF) is a high-performance parallel I/O library for accessing files in format compatibility with Unidata's NetCDF, specifically the formats of CDF-1, 2, and 5.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/parallel-netcdf
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/parallel-netcdf:1.12.2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/parallel-netcdf/1.12.2
$ module help ghcr.io/autamus/parallel-netcdf/1.12.2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### parallel-netcdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### parallel-netcdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### parallel-netcdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### parallel-netcdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### parallel-netcdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### parallel-netcdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pnetcdf-config
       
```bash
$ singularity exec <container> /opt/view/bin/pnetcdf-config
$ podman run --it --rm --entrypoint /opt/view/bin/pnetcdf-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/pnetcdf-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pnetcdf_version
       
```bash
$ singularity exec <container> /opt/view/bin/pnetcdf_version
$ podman run --it --rm --entrypoint /opt/view/bin/pnetcdf_version   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/pnetcdf_version   -v ${PWD} -w ${PWD} <container> -c " $@"
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