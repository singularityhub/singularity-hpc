---
layout: container
name:  "ghcr.io/autamus/admixtools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/admixtools/container.yaml"
updated_at: "2022-03-15 23:21:39.861008"
container_url: "https://github.com/orgs/autamus/packages/container/package/admixtools"
aliases:
 - "convertf"

 - "dowtjack"

 - "expfit.sh"

 - "gcount"

 - "grabpars"

 - "gsl-config"

 - "gsl-histogram"

 - "gsl-randist"

 - "jackdiff"

 - "kimf"

 - "mergeit"

 - "mkpretty"

 - "qp3Pop"

 - "qp4diff"

 - "qpAdm"

 - "qpBound"

 - "qpDpart"

 - "qpDstat"

 - "qpF4ratio"

 - "qpGraph"

 - "qpWave"

 - "qpdslow"

 - "qpff3base"

 - "qpfmv"

 - "qpfstats"

 - "qpreroot"

 - "rexpfit.r"

 - "rolloff"

 - "rolloffp"

 - "simpjack2"

 - "twtable"

 - "wtjack.pl"

versions:
 - "7.0.1"
 - "7.0.2"
 - "latest"
description: "ADMIXTOOLS is a collection of programs which use genetic data to infer how populations are related to one another."
---

This module is a singularity container wrapper for ghcr.io/autamus/admixtools.
ADMIXTOOLS is a collection of programs which use genetic data to infer how populations are related to one another.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/admixtools
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/admixtools:7.0.1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/admixtools/7.0.1
$ module help ghcr.io/autamus/admixtools/7.0.1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### admixtools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### admixtools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### admixtools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### admixtools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### admixtools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### admixtools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### convertf
       
```bash
$ singularity exec <container> /opt/view/bin/convertf
$ podman run --it --rm --entrypoint /opt/view/bin/convertf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/convertf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dowtjack
       
```bash
$ singularity exec <container> /opt/view/bin/dowtjack
$ podman run --it --rm --entrypoint /opt/view/bin/dowtjack   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/dowtjack   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### expfit.sh
       
```bash
$ singularity exec <container> /opt/view/bin/expfit.sh
$ podman run --it --rm --entrypoint /opt/view/bin/expfit.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/expfit.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gcount
       
```bash
$ singularity exec <container> /opt/view/bin/gcount
$ podman run --it --rm --entrypoint /opt/view/bin/gcount   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/gcount   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grabpars
       
```bash
$ singularity exec <container> /opt/view/bin/grabpars
$ podman run --it --rm --entrypoint /opt/view/bin/grabpars   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/grabpars   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gsl-config
       
```bash
$ singularity exec <container> /opt/view/bin/gsl-config
$ podman run --it --rm --entrypoint /opt/view/bin/gsl-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/gsl-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gsl-histogram
       
```bash
$ singularity exec <container> /opt/view/bin/gsl-histogram
$ podman run --it --rm --entrypoint /opt/view/bin/gsl-histogram   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/gsl-histogram   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gsl-randist
       
```bash
$ singularity exec <container> /opt/view/bin/gsl-randist
$ podman run --it --rm --entrypoint /opt/view/bin/gsl-randist   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/gsl-randist   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jackdiff
       
```bash
$ singularity exec <container> /opt/view/bin/jackdiff
$ podman run --it --rm --entrypoint /opt/view/bin/jackdiff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/jackdiff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kimf
       
```bash
$ singularity exec <container> /opt/view/bin/kimf
$ podman run --it --rm --entrypoint /opt/view/bin/kimf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/kimf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mergeit
       
```bash
$ singularity exec <container> /opt/view/bin/mergeit
$ podman run --it --rm --entrypoint /opt/view/bin/mergeit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/mergeit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mkpretty
       
```bash
$ singularity exec <container> /opt/view/bin/mkpretty
$ podman run --it --rm --entrypoint /opt/view/bin/mkpretty   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/mkpretty   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qp3Pop
       
```bash
$ singularity exec <container> /opt/view/bin/qp3Pop
$ podman run --it --rm --entrypoint /opt/view/bin/qp3Pop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/qp3Pop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qp4diff
       
```bash
$ singularity exec <container> /opt/view/bin/qp4diff
$ podman run --it --rm --entrypoint /opt/view/bin/qp4diff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/qp4diff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qpAdm
       
```bash
$ singularity exec <container> /opt/view/bin/qpAdm
$ podman run --it --rm --entrypoint /opt/view/bin/qpAdm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/qpAdm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qpBound
       
```bash
$ singularity exec <container> /opt/view/bin/qpBound
$ podman run --it --rm --entrypoint /opt/view/bin/qpBound   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/qpBound   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qpDpart
       
```bash
$ singularity exec <container> /opt/view/bin/qpDpart
$ podman run --it --rm --entrypoint /opt/view/bin/qpDpart   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/qpDpart   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qpDstat
       
```bash
$ singularity exec <container> /opt/view/bin/qpDstat
$ podman run --it --rm --entrypoint /opt/view/bin/qpDstat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/qpDstat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qpF4ratio
       
```bash
$ singularity exec <container> /opt/view/bin/qpF4ratio
$ podman run --it --rm --entrypoint /opt/view/bin/qpF4ratio   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/qpF4ratio   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qpGraph
       
```bash
$ singularity exec <container> /opt/view/bin/qpGraph
$ podman run --it --rm --entrypoint /opt/view/bin/qpGraph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/qpGraph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qpWave
       
```bash
$ singularity exec <container> /opt/view/bin/qpWave
$ podman run --it --rm --entrypoint /opt/view/bin/qpWave   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/qpWave   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qpdslow
       
```bash
$ singularity exec <container> /opt/view/bin/qpdslow
$ podman run --it --rm --entrypoint /opt/view/bin/qpdslow   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/qpdslow   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qpff3base
       
```bash
$ singularity exec <container> /opt/view/bin/qpff3base
$ podman run --it --rm --entrypoint /opt/view/bin/qpff3base   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/qpff3base   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qpfmv
       
```bash
$ singularity exec <container> /opt/view/bin/qpfmv
$ podman run --it --rm --entrypoint /opt/view/bin/qpfmv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/qpfmv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qpfstats
       
```bash
$ singularity exec <container> /opt/view/bin/qpfstats
$ podman run --it --rm --entrypoint /opt/view/bin/qpfstats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/qpfstats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qpreroot
       
```bash
$ singularity exec <container> /opt/view/bin/qpreroot
$ podman run --it --rm --entrypoint /opt/view/bin/qpreroot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/qpreroot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rexpfit.r
       
```bash
$ singularity exec <container> /opt/view/bin/rexpfit.r
$ podman run --it --rm --entrypoint /opt/view/bin/rexpfit.r   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/rexpfit.r   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rolloff
       
```bash
$ singularity exec <container> /opt/view/bin/rolloff
$ podman run --it --rm --entrypoint /opt/view/bin/rolloff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/rolloff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rolloffp
       
```bash
$ singularity exec <container> /opt/view/bin/rolloffp
$ podman run --it --rm --entrypoint /opt/view/bin/rolloffp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/rolloffp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### simpjack2
       
```bash
$ singularity exec <container> /opt/view/bin/simpjack2
$ podman run --it --rm --entrypoint /opt/view/bin/simpjack2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/simpjack2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### twtable
       
```bash
$ singularity exec <container> /opt/view/bin/twtable
$ podman run --it --rm --entrypoint /opt/view/bin/twtable   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/twtable   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wtjack.pl
       
```bash
$ singularity exec <container> /opt/view/bin/wtjack.pl
$ podman run --it --rm --entrypoint /opt/view/bin/wtjack.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/wtjack.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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