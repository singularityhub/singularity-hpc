---
layout: container
name:  "nvcr.io/hpc/lammps"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/nvcr.io/hpc/lammps/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/nvcr.io/hpc/lammps/container.yaml"
updated_at: "2022-08-27 01:37:09.892705"
latest: "29Sep2021"
container_url: "https://ngc.nvidia.com/catalog/containers/hpc:lammps/tags"

versions:
 - "29Oct2020"
 - "29Sep2021"
description: "Large-scale Atomic/Molecular Massively Parallel Simulator (LAMMPS) is a software application designed for molecular dynamics simulations. It has the potentials for solid-state materials (metals, semiconductor), soft matter (biomolecules, polymers), and coarse-grained or mesoscopic systems. The main use-case is atom scale particle modeling or, more generically, as a parallel particle simulator at the atomic, meson, or continuum scale. LAMMPS runs on single processors or in parallel using message-passing techniques and a spatial-decomposition of the simulation domain. Read more on the LAMMPS website https://lammps.sandia.gov/."
config: {"docker": "nvcr.io/hpc/lammps", "url": "https://ngc.nvidia.com/catalog/containers/hpc:lammps/tags", "maintainer": "@vsoch", "description": "Large-scale Atomic/Molecular Massively Parallel Simulator (LAMMPS) is a software application designed for molecular dynamics simulations. It has the potentials for solid-state materials (metals, semiconductor), soft matter (biomolecules, polymers), and coarse-grained or mesoscopic systems. The main use-case is atom scale particle modeling or, more generically, as a parallel particle simulator at the atomic, meson, or continuum scale. LAMMPS runs on single processors or in parallel using message-passing techniques and a spatial-decomposition of the simulation domain. Read more on the LAMMPS website https://lammps.sandia.gov/.", "latest": {"29Sep2021": "sha256:6c40caaa7c2aadd0e49748ddef584a7d88235651479e416919ced889e2156596"}, "tags": {"29Oct2020": "sha256:c6cf2371ad7eb491925e58cc28ee0ef9f0bd84a15634bb0e7f818c7d07e8877e", "29Sep2021": "sha256:6c40caaa7c2aadd0e49748ddef584a7d88235651479e416919ced889e2156596"}, "filter": ["2021"], "features": {"gpu": true}}
---

This module is a singularity container wrapper for nvcr.io/hpc/lammps.
Large-scale Atomic/Molecular Massively Parallel Simulator (LAMMPS) is a software application designed for molecular dynamics simulations. It has the potentials for solid-state materials (metals, semiconductor), soft matter (biomolecules, polymers), and coarse-grained or mesoscopic systems. The main use-case is atom scale particle modeling or, more generically, as a parallel particle simulator at the atomic, meson, or continuum scale. LAMMPS runs on single processors or in parallel using message-passing techniques and a spatial-decomposition of the simulation domain. Read more on the LAMMPS website https://lammps.sandia.gov/.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install nvcr.io/hpc/lammps
```

Or a specific version:

```bash
$ shpc install nvcr.io/hpc/lammps:29Oct2020
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load nvcr.io/hpc/lammps/29Oct2020
$ module help nvcr.io/hpc/lammps/29Oct2020
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### lammps-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### lammps-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### lammps-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### lammps-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### lammps-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### lammps-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### lammps

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