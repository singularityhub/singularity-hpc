---
layout: container
name:  "nvcr.io/hpc/namd"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/nvcr.io/hpc/namd/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/nvcr.io/hpc/namd/container.yaml"
updated_at: "2022-08-27 01:37:10.431636"
latest: "3.0-alpha11"
container_url: "https://ngc.nvidia.com/catalog/containers/hpc:lammps/tags"
aliases:
 - "charmrun"
 - "flipbinpdb"
 - "flipdcd"
 - "namd3"
 - "psfgen"
 - "sortreplicas"
 - "vmd"
versions:
 - "3.0-alpha3-singlenode"
 - "3.0-alpha3-singlenode-arm64"
 - "3.0-alpha3-singlenode-x86_64"
 - "3.0-alpha9-singlenode"
 - "3.0-alpha11"
description: "NAMD is a parallel molecular dynamics code designed for high-performance simulation of large biomolecular systems. NAMD uses the popular molecular graphics program VMD for simulation setup and trajectory analysis, but is also file-comp atible with AMBER, CHARMM, and X-PLOR."
config: {"docker": "nvcr.io/hpc/namd", "url": "https://ngc.nvidia.com/catalog/containers/hpc:lammps/tags", "maintainer": "@vsoch", "description": "NAMD is a parallel molecular dynamics code designed for high-performance simulation of large biomolecular systems. NAMD uses the popular molecular graphics program VMD for simulation setup and trajectory analysis, but is also file-comp atible with AMBER, CHARMM, and X-PLOR.", "latest": {"3.0-alpha11": "sha256:f0bbd27b2a5d28f2e39418c6b2b5cad8f7895dad51d8bb040442a3776431b128"}, "tags": {"3.0-alpha3-singlenode": "sha256:9db0e23f0f53dd200568cc57f3618971378173555d30d3158ec41c6df8aee15e", "3.0-alpha3-singlenode-arm64": "sha256:3743f24e1bd353296adef6c14127ae418716ef686f75c790d497f90150785d39", "3.0-alpha3-singlenode-x86_64": "sha256:040e38a36f467f6a2e61dd343f480e4c7c7a571b6072607922851214070a627e", "3.0-alpha9-singlenode": "sha256:05e7c1eeb167b9d4250f6d75aab5e1d23597b922cf9aed4eaadfd3c24068287d", "3.0-alpha11": "sha256:f0bbd27b2a5d28f2e39418c6b2b5cad8f7895dad51d8bb040442a3776431b128"}, "filter": ["^((?!arm).)*$"], "aliases": {"charmrun": "/usr/local/bin/charmrun", "flipbinpdb": "/usr/local/bin/flipbinpdb", "flipdcd": "/usr/local/bin/flipdcd", "namd3": "/usr/local/bin/namd3", "psfgen": "/usr/local/bin/psfgen", "sortreplicas": "/usr/local/bin/sortreplicas", "vmd": "/usr/local/bin/vmd"}, "features": {"gpu": true}}
---

This module is a singularity container wrapper for nvcr.io/hpc/namd.
NAMD is a parallel molecular dynamics code designed for high-performance simulation of large biomolecular systems. NAMD uses the popular molecular graphics program VMD for simulation setup and trajectory analysis, but is also file-comp atible with AMBER, CHARMM, and X-PLOR.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install nvcr.io/hpc/namd
```

Or a specific version:

```bash
$ shpc install nvcr.io/hpc/namd:3.0-alpha3-singlenode
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load nvcr.io/hpc/namd/3.0-alpha3-singlenode
$ module help nvcr.io/hpc/namd/3.0-alpha3-singlenode
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### namd-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### namd-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### namd-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### namd-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### namd-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### namd-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### charmrun
       
```bash
$ singularity exec <container> /usr/local/bin/charmrun
$ podman run --it --rm --entrypoint /usr/local/bin/charmrun   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/charmrun   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flipbinpdb
       
```bash
$ singularity exec <container> /usr/local/bin/flipbinpdb
$ podman run --it --rm --entrypoint /usr/local/bin/flipbinpdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flipbinpdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flipdcd
       
```bash
$ singularity exec <container> /usr/local/bin/flipdcd
$ podman run --it --rm --entrypoint /usr/local/bin/flipdcd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flipdcd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### namd3
       
```bash
$ singularity exec <container> /usr/local/bin/namd3
$ podman run --it --rm --entrypoint /usr/local/bin/namd3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/namd3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### psfgen
       
```bash
$ singularity exec <container> /usr/local/bin/psfgen
$ podman run --it --rm --entrypoint /usr/local/bin/psfgen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/psfgen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sortreplicas
       
```bash
$ singularity exec <container> /usr/local/bin/sortreplicas
$ podman run --it --rm --entrypoint /usr/local/bin/sortreplicas   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sortreplicas   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vmd
       
```bash
$ singularity exec <container> /usr/local/bin/vmd
$ podman run --it --rm --entrypoint /usr/local/bin/vmd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vmd   -v ${PWD} -w ${PWD} <container> -c " $@"
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