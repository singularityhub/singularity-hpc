---
layout: container
name:  "quay.io/biocontainers/bracken"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/quay.io/biocontainers/bracken/container.yaml"
updated_at: "2022-02-04 13:17:06.804987"
container_url: "https://quay.io/repository/biocontainers/bracken"
aliases:
 - "bracken"

 - "bracken-build"

 - "combine_bracken_outputs.py"

 - "est_abundance.py"

 - "generate_kmer_distribution.py"

 - "kmer2read_distr"

versions:
 - "2.6.1--py27h2bce143_0"
 - "2.6.1--py39h7cff6ad_2"
description: "A highly accurate statistical method that computes the abundance of species in DNA sequences from a metagenomics sample."
---

This module is a singularity container wrapper for quay.io/biocontainers/bracken.
A highly accurate statistical method that computes the abundance of species in DNA sequences from a metagenomics sample.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install quay.io/biocontainers/bracken
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bracken:2.6.1--py27h2bce143_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bracken/2.6.1--py27h2bce143_0
$ module help quay.io/biocontainers/bracken/2.6.1--py27h2bce143_0
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


#### bracken
       
```bash
$ singularity exec <container> /usr/local/bin/bracken
$ podman run --it --rm --entrypoint /usr/local/bin/bracken   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bracken   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bracken-build
       
```bash
$ singularity exec <container> /usr/local/bin/bracken-build
$ podman run --it --rm --entrypoint /usr/local/bin/bracken-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bracken-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### combine_bracken_outputs.py
       
```bash
$ singularity exec <container> /usr/local/bin/combine_bracken_outputs.py
$ podman run --it --rm --entrypoint /usr/local/bin/combine_bracken_outputs.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/combine_bracken_outputs.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### est_abundance.py
       
```bash
$ singularity exec <container> /usr/local/bin/est_abundance.py
$ podman run --it --rm --entrypoint /usr/local/bin/est_abundance.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/est_abundance.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### generate_kmer_distribution.py
       
```bash
$ singularity exec <container> /usr/local/bin/generate_kmer_distribution.py
$ podman run --it --rm --entrypoint /usr/local/bin/generate_kmer_distribution.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/generate_kmer_distribution.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kmer2read_distr
       
```bash
$ singularity exec <container> /usr/local/bin/kmer2read_distr
$ podman run --it --rm --entrypoint /usr/local/bin/kmer2read_distr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kmer2read_distr   -v ${PWD} -w ${PWD} <container> -c " $@"
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