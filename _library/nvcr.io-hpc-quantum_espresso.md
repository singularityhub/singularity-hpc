---
layout: container
name:  "nvcr.io/hpc/quantum_espresso"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/nvcr.io/hpc/quantum_espresso/container.yaml"
updated_at: "2021-04-20 03:18:25.854609"
container_url: ""

versions:
 - "v6.7"
description: "Quantum ESPRESSO is an integrated suite of Open-Source computer codes for electronic-structure calculations and materials modeling at the nanoscale based on density-functional theory, plane waves, and pseudopotentials."
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

When you install this module, you'll be able to load it to make the following commands accessible:

#### nvcr.io-hpc-quantum_espresso-run:

```bash
$ singularity run <container>
```

#### nvcr.io-hpc-quantum_espresso-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### nvcr.io-hpc-quantum_espresso-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### nvcr.io-hpc-quantum_espresso-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### nvcr.io-hpc-quantum_espresso-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### nvcr.io-hpc-quantum_espresso

```bash
$ singularity run <container>
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