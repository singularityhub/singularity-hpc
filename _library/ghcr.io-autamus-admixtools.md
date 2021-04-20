---
layout: container
name:  "ghcr.io/autamus/admixtools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/admixtools/container.yaml"
updated_at: "2021-04-20 03:15:58.035987"
container_url: ""
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

When you install this module, you'll be able to load it to make the following commands accessible:

#### ghcr.io-autamus-admixtools-run:

```bash
$ singularity run <container>
```

#### ghcr.io-autamus-admixtools-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### ghcr.io-autamus-admixtools-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### ghcr.io-autamus-admixtools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ghcr.io-autamus-admixtools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### convertf
       
```bash
$ singularity exec <container> /opt/view/bin/convertf
```


#### dowtjack
       
```bash
$ singularity exec <container> /opt/view/bin/dowtjack
```


#### expfit.sh
       
```bash
$ singularity exec <container> /opt/view/bin/expfit.sh
```


#### gcount
       
```bash
$ singularity exec <container> /opt/view/bin/gcount
```


#### grabpars
       
```bash
$ singularity exec <container> /opt/view/bin/grabpars
```


#### gsl-config
       
```bash
$ singularity exec <container> /opt/view/bin/gsl-config
```


#### gsl-histogram
       
```bash
$ singularity exec <container> /opt/view/bin/gsl-histogram
```


#### gsl-randist
       
```bash
$ singularity exec <container> /opt/view/bin/gsl-randist
```


#### jackdiff
       
```bash
$ singularity exec <container> /opt/view/bin/jackdiff
```


#### kimf
       
```bash
$ singularity exec <container> /opt/view/bin/kimf
```


#### mergeit
       
```bash
$ singularity exec <container> /opt/view/bin/mergeit
```


#### mkpretty
       
```bash
$ singularity exec <container> /opt/view/bin/mkpretty
```


#### qp3Pop
       
```bash
$ singularity exec <container> /opt/view/bin/qp3Pop
```


#### qp4diff
       
```bash
$ singularity exec <container> /opt/view/bin/qp4diff
```


#### qpAdm
       
```bash
$ singularity exec <container> /opt/view/bin/qpAdm
```


#### qpBound
       
```bash
$ singularity exec <container> /opt/view/bin/qpBound
```


#### qpDpart
       
```bash
$ singularity exec <container> /opt/view/bin/qpDpart
```


#### qpDstat
       
```bash
$ singularity exec <container> /opt/view/bin/qpDstat
```


#### qpF4ratio
       
```bash
$ singularity exec <container> /opt/view/bin/qpF4ratio
```


#### qpGraph
       
```bash
$ singularity exec <container> /opt/view/bin/qpGraph
```


#### qpWave
       
```bash
$ singularity exec <container> /opt/view/bin/qpWave
```


#### qpdslow
       
```bash
$ singularity exec <container> /opt/view/bin/qpdslow
```


#### qpff3base
       
```bash
$ singularity exec <container> /opt/view/bin/qpff3base
```


#### qpfmv
       
```bash
$ singularity exec <container> /opt/view/bin/qpfmv
```


#### qpfstats
       
```bash
$ singularity exec <container> /opt/view/bin/qpfstats
```


#### qpreroot
       
```bash
$ singularity exec <container> /opt/view/bin/qpreroot
```


#### rexpfit.r
       
```bash
$ singularity exec <container> /opt/view/bin/rexpfit.r
```


#### rolloff
       
```bash
$ singularity exec <container> /opt/view/bin/rolloff
```


#### rolloffp
       
```bash
$ singularity exec <container> /opt/view/bin/rolloffp
```


#### simpjack2
       
```bash
$ singularity exec <container> /opt/view/bin/simpjack2
```


#### twtable
       
```bash
$ singularity exec <container> /opt/view/bin/twtable
```


#### wtjack.pl
       
```bash
$ singularity exec <container> /opt/view/bin/wtjack.pl
```



In the above, the `<container>` directive will reference an actual container provided
by the module, for the version you have chosen to load. Note that although a container
might provide custom commands, every container exposes unique exec, shell, run, and
inspect aliases. For each of the above, you can export:

 - SINGULARITY_OPTS: to define custom options for singularity (e.g., --debug)
 - SINGULARITY_COMMAND_OPTS: to define custom options for the command (e.g., -b)

<br>
  
### Install

You can install shpc locally (for yourself or your user base) as follows:

```bash
$ git clone https://github.com/singularityhub/singularity-hpc
$ cd singularity-hpc
$ pip install -e .
```

Have any questions, or want to request a new module or version? [ask for help!](https://github.com/singularityhub/singularity-hpc/issues)