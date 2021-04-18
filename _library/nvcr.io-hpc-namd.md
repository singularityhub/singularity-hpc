---
layout: container
name:  "nvcr.io/hpc/namd"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/nvcr.io/hpc/namd/container.yaml"
updated_at: "2021-04-18 21:11:49.331490"
container_url: ""
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
description: "NAMD is a parallel molecular dynamics code designed for high-performance simulation of large biomolecular systems. NAMD uses the popular molecular graphics program VMD for simulation setup and trajectory analysis, but is also file-comp atible with AMBER, CHARMM, and X-PLOR."
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

When you install this module, you'll be able to load it to make the following commands accessible:

#### nvcr.io-hpc-namd-run:

```bash
$ singularity run <container>
```

#### nvcr.io-hpc-namd-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### nvcr.io-hpc-namd-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### nvcr.io-hpc-namd-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### nvcr.io-hpc-namd-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### charmrun
       
```bash
$ singularity exec <container> /usr/local/bin/charmrun
```


#### flipbinpdb
       
```bash
$ singularity exec <container> /usr/local/bin/flipbinpdb
```


#### flipdcd
       
```bash
$ singularity exec <container> /usr/local/bin/flipdcd
```


#### namd3
       
```bash
$ singularity exec <container> /usr/local/bin/namd3
```


#### psfgen
       
```bash
$ singularity exec <container> /usr/local/bin/psfgen
```


#### sortreplicas
       
```bash
$ singularity exec <container> /usr/local/bin/sortreplicas
```


#### vmd
       
```bash
$ singularity exec <container> /usr/local/bin/vmd
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