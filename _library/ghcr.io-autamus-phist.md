---
layout: container
name:  "ghcr.io/autamus/phist"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/phist/container.yaml"
updated_at: "2021-07-20 19:37:08.636023"
container_url: "https://github.com/orgs/autamus/packages/container/package/phist"
aliases:
 - "phist_Danasazi_krylov_schur"

 - "phist_Danasazi_lobpcg"

 - "phist_Dbelos_bgmres"

 - "phist_Dbelos_bpcg"

 - "phist_Dblockedbicgstab"

 - "phist_Dblockedgmres"

 - "phist_Dblockedpcg"

 - "phist_Dsimple_lanczos"

 - "phist_Dsubspacejada"

 - "phist_carp_cg"

versions:
 - "1.9.4"
description: "The Pipelined, Hybrid-parallel Iterative Solver Toolkit provides implementations of and interfaces to block iterative solvers for sparse linear and eigenvalue problems."
---

This module is a singularity container wrapper for ghcr.io/autamus/phist.
The Pipelined, Hybrid-parallel Iterative Solver Toolkit provides implementations of and interfaces to block iterative solvers for sparse linear and eigenvalue problems.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install ghcr.io/autamus/phist
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/phist:1.9.4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/phist/1.9.4
$ module help ghcr.io/autamus/phist/1.9.4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### -run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### -shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### -exec:

```bash
$ singularity exec -s /bin/sh <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### -inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### -inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### -inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### phist_Danasazi_krylov_schur
       
```bash
$ singularity exec <container> /opt/view/bin/phist_Danasazi_krylov_schur
$ podman run --it --rm --entrypoint /opt/view/bin/phist_Danasazi_krylov_schur   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/phist_Danasazi_krylov_schur   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phist_Danasazi_lobpcg
       
```bash
$ singularity exec <container> /opt/view/bin/phist_Danasazi_lobpcg
$ podman run --it --rm --entrypoint /opt/view/bin/phist_Danasazi_lobpcg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/phist_Danasazi_lobpcg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phist_Dbelos_bgmres
       
```bash
$ singularity exec <container> /opt/view/bin/phist_Dbelos_bgmres
$ podman run --it --rm --entrypoint /opt/view/bin/phist_Dbelos_bgmres   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/phist_Dbelos_bgmres   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phist_Dbelos_bpcg
       
```bash
$ singularity exec <container> /opt/view/bin/phist_Dbelos_bpcg
$ podman run --it --rm --entrypoint /opt/view/bin/phist_Dbelos_bpcg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/phist_Dbelos_bpcg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phist_Dblockedbicgstab
       
```bash
$ singularity exec <container> /opt/view/bin/phist_Dblockedbicgstab
$ podman run --it --rm --entrypoint /opt/view/bin/phist_Dblockedbicgstab   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/phist_Dblockedbicgstab   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phist_Dblockedgmres
       
```bash
$ singularity exec <container> /opt/view/bin/phist_Dblockedgmres
$ podman run --it --rm --entrypoint /opt/view/bin/phist_Dblockedgmres   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/phist_Dblockedgmres   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phist_Dblockedpcg
       
```bash
$ singularity exec <container> /opt/view/bin/phist_Dblockedpcg
$ podman run --it --rm --entrypoint /opt/view/bin/phist_Dblockedpcg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/phist_Dblockedpcg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phist_Dsimple_lanczos
       
```bash
$ singularity exec <container> /opt/view/bin/phist_Dsimple_lanczos
$ podman run --it --rm --entrypoint /opt/view/bin/phist_Dsimple_lanczos   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/phist_Dsimple_lanczos   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phist_Dsubspacejada
       
```bash
$ singularity exec <container> /opt/view/bin/phist_Dsubspacejada
$ podman run --it --rm --entrypoint /opt/view/bin/phist_Dsubspacejada   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/phist_Dsubspacejada   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phist_carp_cg
       
```bash
$ singularity exec <container> /opt/view/bin/phist_carp_cg
$ podman run --it --rm --entrypoint /opt/view/bin/phist_carp_cg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/phist_carp_cg   -v ${PWD} -w ${PWD} <container> -c " $@"
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