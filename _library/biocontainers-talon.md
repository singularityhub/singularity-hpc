---
layout: container
name:  "biocontainers/talon"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/biocontainers/talon/container.yaml"
updated_at: "2022-07-08 12:10:12.850359"
container_url: "https://hub.docker.com/r/biocontainers/talon"
aliases:
 - "talon"

 - "talon_create_GTF"

 - "talon_fetch_reads"

 - "talon_filter_transcripts"

 - "talon_generate_report"

 - "talon_initialize_database"

 - "talon_get_sjs"

 - "talon_label_reads"

 - "talon_reformat_gtf"

 - "talon_summarize"

 - "talon_abundance"

versions:
 - "v5.0_cv1"
description: "Mailgun library to extract message quotations and signatures."
---

This module is a singularity container wrapper for biocontainers/talon.
Mailgun library to extract message quotations and signatures.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install biocontainers/talon
```

Or a specific version:

```bash
$ shpc install biocontainers/talon:v5.0_cv1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load biocontainers/talon/v5.0_cv1
$ module help biocontainers/talon/v5.0_cv1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### talon-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### talon-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### talon-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### talon-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### talon-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### talon-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### talon
       
```bash
$ singularity exec <container> /usr/local/bin/talon
$ podman run --it --rm --entrypoint /usr/local/bin/talon   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/talon   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### talon_create_GTF
       
```bash
$ singularity exec <container> /usr/local/bin/talon_create_GTF
$ podman run --it --rm --entrypoint /usr/local/bin/talon_create_GTF   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/talon_create_GTF   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### talon_fetch_reads
       
```bash
$ singularity exec <container> /usr/local/bin/talon_fetch_reads
$ podman run --it --rm --entrypoint /usr/local/bin/talon_fetch_reads   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/talon_fetch_reads   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### talon_filter_transcripts
       
```bash
$ singularity exec <container> /usr/local/bin/talon_filter_transcripts
$ podman run --it --rm --entrypoint /usr/local/bin/talon_filter_transcripts   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/talon_filter_transcripts   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### talon_generate_report
       
```bash
$ singularity exec <container> /usr/local/bin/talon_generate_report
$ podman run --it --rm --entrypoint /usr/local/bin/talon_generate_report   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/talon_generate_report   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### talon_initialize_database
       
```bash
$ singularity exec <container> /usr/local/bin/talon_initialize_database
$ podman run --it --rm --entrypoint /usr/local/bin/talon_initialize_database   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/talon_initialize_database   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### talon_get_sjs
       
```bash
$ singularity exec <container> /usr/local/bin/talon_get_sjs
$ podman run --it --rm --entrypoint /usr/local/bin/talon_get_sjs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/talon_get_sjs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### talon_label_reads
       
```bash
$ singularity exec <container> /usr/local/bin/talon_label_reads
$ podman run --it --rm --entrypoint /usr/local/bin/talon_label_reads   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/talon_label_reads   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### talon_reformat_gtf
       
```bash
$ singularity exec <container> /usr/local/bin/talon_reformat_gtf
$ podman run --it --rm --entrypoint /usr/local/bin/talon_reformat_gtf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/talon_reformat_gtf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### talon_summarize
       
```bash
$ singularity exec <container> /usr/local/bin/talon_summarize
$ podman run --it --rm --entrypoint /usr/local/bin/talon_summarize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/talon_summarize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### talon_abundance
       
```bash
$ singularity exec <container> /usr/local/bin/talon_abundance
$ podman run --it --rm --entrypoint /usr/local/bin/talon_abundance   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/talon_abundance   -v ${PWD} -w ${PWD} <container> -c " $@"
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