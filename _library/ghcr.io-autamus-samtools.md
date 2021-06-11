---
layout: container
name:  "ghcr.io/autamus/samtools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/samtools/container.yaml"
updated_at: "2021-06-11 05:46:45.563570"
container_url: "https://github.com/orgs/autamus/packages/container/package/samtools"
aliases:
 - "blast2sam.pl"

 - "bowtie2sam.pl"

 - "export2sam.pl"

 - "fasta-sanitize.pl"

 - "interpolate_sam.pl"

 - "novo2sam.pl"

 - "psl2sam.pl"

 - "sam2vcf.pl"

 - "samtools"

 - "samtools.pl"

 - "seq_cache_populate.pl"

 - "soap2sam.pl"

 - "wgsim_eval.pl"

 - "zoom2sam.pl"

versions:
 - "1.12"
 - "latest"
description: "Samtools is a suite of programs for interacting with high-throughput sequencing data."
---

This module is a singularity container wrapper for ghcr.io/autamus/samtools.
Samtools is a suite of programs for interacting with high-throughput sequencing data.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install ghcr.io/autamus/samtools
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/samtools:1.12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/samtools/1.12
$ module help ghcr.io/autamus/samtools/1.12
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


#### blast2sam.pl
       
```bash
$ singularity exec <container> /opt/view/bin/blast2sam.pl
$ podman run --it --rm --entrypoint /opt/view/bin/blast2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/blast2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2sam.pl
       
```bash
$ singularity exec <container> /opt/view/bin/bowtie2sam.pl
$ podman run --it --rm --entrypoint /opt/view/bin/bowtie2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/bowtie2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### export2sam.pl
       
```bash
$ singularity exec <container> /opt/view/bin/export2sam.pl
$ podman run --it --rm --entrypoint /opt/view/bin/export2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/export2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta-sanitize.pl
       
```bash
$ singularity exec <container> /opt/view/bin/fasta-sanitize.pl
$ podman run --it --rm --entrypoint /opt/view/bin/fasta-sanitize.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/fasta-sanitize.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### interpolate_sam.pl
       
```bash
$ singularity exec <container> /opt/view/bin/interpolate_sam.pl
$ podman run --it --rm --entrypoint /opt/view/bin/interpolate_sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/interpolate_sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### novo2sam.pl
       
```bash
$ singularity exec <container> /opt/view/bin/novo2sam.pl
$ podman run --it --rm --entrypoint /opt/view/bin/novo2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/novo2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### psl2sam.pl
       
```bash
$ singularity exec <container> /opt/view/bin/psl2sam.pl
$ podman run --it --rm --entrypoint /opt/view/bin/psl2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/psl2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sam2vcf.pl
       
```bash
$ singularity exec <container> /opt/view/bin/sam2vcf.pl
$ podman run --it --rm --entrypoint /opt/view/bin/sam2vcf.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/sam2vcf.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### samtools
       
```bash
$ singularity exec <container> /opt/view/bin/samtools
$ podman run --it --rm --entrypoint /opt/view/bin/samtools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/samtools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### samtools.pl
       
```bash
$ singularity exec <container> /opt/view/bin/samtools.pl
$ podman run --it --rm --entrypoint /opt/view/bin/samtools.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/samtools.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seq_cache_populate.pl
       
```bash
$ singularity exec <container> /opt/view/bin/seq_cache_populate.pl
$ podman run --it --rm --entrypoint /opt/view/bin/seq_cache_populate.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/seq_cache_populate.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### soap2sam.pl
       
```bash
$ singularity exec <container> /opt/view/bin/soap2sam.pl
$ podman run --it --rm --entrypoint /opt/view/bin/soap2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/soap2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wgsim_eval.pl
       
```bash
$ singularity exec <container> /opt/view/bin/wgsim_eval.pl
$ podman run --it --rm --entrypoint /opt/view/bin/wgsim_eval.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/wgsim_eval.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zoom2sam.pl
       
```bash
$ singularity exec <container> /opt/view/bin/zoom2sam.pl
$ podman run --it --rm --entrypoint /opt/view/bin/zoom2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/zoom2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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