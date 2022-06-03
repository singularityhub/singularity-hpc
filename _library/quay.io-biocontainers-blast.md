---
layout: container
name:  "quay.io/biocontainers/blast"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/quay.io/biocontainers/blast/container.yaml"
updated_at: "2022-06-03 04:17:29.159837"
container_url: "https://quay.io/repository/biocontainers/blast"
aliases:
 - "blast_formatter"

 - "blastdb_aliastool"

 - "blastdbcheck"

 - "blastdbcmd"

 - "blastn"

 - "blastp"

 - "blastx"

 - "cleanup-blastdb-volumes.py"

 - "convert2blastmask"

 - "deltablast"

 - "eblast"

 - "makeblastdb"

 - "psiblast"

 - "rpsblast"

 - "rpstblastn"

 - "tblastn"

 - "tblastx"

 - "update_blastdb.pl"

versions:
 - "2.10.1--pl526he19e7b1_3"
 - "2.11.0--pl5262h3289130_1"
 - "2.12.0--pl5262h3289130_0"
 - "2.12.0--hf3cf87c_4"
description: "BLAST finds regions of similarity between biological sequences."
---

This module is a singularity container wrapper for quay.io/biocontainers/blast.
BLAST finds regions of similarity between biological sequences.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/blast
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/blast:2.10.1--pl526he19e7b1_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/blast/2.10.1--pl526he19e7b1_3
$ module help quay.io/biocontainers/blast/2.10.1--pl526he19e7b1_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### blast-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### blast-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### blast-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### blast-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### blast-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### blast-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### blast_formatter
       
```bash
$ singularity exec <container> /usr/local/bin/blast_formatter
$ podman run --it --rm --entrypoint /usr/local/bin/blast_formatter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blast_formatter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastdb_aliastool
       
```bash
$ singularity exec <container> /usr/local/bin/blastdb_aliastool
$ podman run --it --rm --entrypoint /usr/local/bin/blastdb_aliastool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastdb_aliastool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastdbcheck
       
```bash
$ singularity exec <container> /usr/local/bin/blastdbcheck
$ podman run --it --rm --entrypoint /usr/local/bin/blastdbcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastdbcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastdbcmd
       
```bash
$ singularity exec <container> /usr/local/bin/blastdbcmd
$ podman run --it --rm --entrypoint /usr/local/bin/blastdbcmd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastdbcmd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastn
       
```bash
$ singularity exec <container> /usr/local/bin/blastn
$ podman run --it --rm --entrypoint /usr/local/bin/blastn   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastn   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastp
       
```bash
$ singularity exec <container> /usr/local/bin/blastp
$ podman run --it --rm --entrypoint /usr/local/bin/blastp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastx
       
```bash
$ singularity exec <container> /usr/local/bin/blastx
$ podman run --it --rm --entrypoint /usr/local/bin/blastx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cleanup-blastdb-volumes.py
       
```bash
$ singularity exec <container> /usr/local/bin/cleanup-blastdb-volumes.py
$ podman run --it --rm --entrypoint /usr/local/bin/cleanup-blastdb-volumes.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cleanup-blastdb-volumes.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### convert2blastmask
       
```bash
$ singularity exec <container> /usr/local/bin/convert2blastmask
$ podman run --it --rm --entrypoint /usr/local/bin/convert2blastmask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convert2blastmask   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### deltablast
       
```bash
$ singularity exec <container> /usr/local/bin/deltablast
$ podman run --it --rm --entrypoint /usr/local/bin/deltablast   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/deltablast   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eblast
       
```bash
$ singularity exec <container> /usr/local/bin/eblast
$ podman run --it --rm --entrypoint /usr/local/bin/eblast   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eblast   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### makeblastdb
       
```bash
$ singularity exec <container> /usr/local/bin/makeblastdb
$ podman run --it --rm --entrypoint /usr/local/bin/makeblastdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/makeblastdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### psiblast
       
```bash
$ singularity exec <container> /usr/local/bin/psiblast
$ podman run --it --rm --entrypoint /usr/local/bin/psiblast   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/psiblast   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rpsblast
       
```bash
$ singularity exec <container> /usr/local/bin/rpsblast
$ podman run --it --rm --entrypoint /usr/local/bin/rpsblast   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rpsblast   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rpstblastn
       
```bash
$ singularity exec <container> /usr/local/bin/rpstblastn
$ podman run --it --rm --entrypoint /usr/local/bin/rpstblastn   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rpstblastn   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tblastn
       
```bash
$ singularity exec <container> /usr/local/bin/tblastn
$ podman run --it --rm --entrypoint /usr/local/bin/tblastn   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tblastn   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tblastx
       
```bash
$ singularity exec <container> /usr/local/bin/tblastx
$ podman run --it --rm --entrypoint /usr/local/bin/tblastx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tblastx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### update_blastdb.pl
       
```bash
$ singularity exec <container> /usr/local/bin/update_blastdb.pl
$ podman run --it --rm --entrypoint /usr/local/bin/update_blastdb.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/update_blastdb.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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