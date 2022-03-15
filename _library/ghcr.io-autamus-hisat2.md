---
layout: container
name:  "ghcr.io/autamus/hisat2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/hisat2/container.yaml"
updated_at: "2022-03-15 23:21:49.004038"
container_url: "https://github.com/orgs/autamus/packages/container/package/hisat2"
aliases:
 - "hisat2"

 - "hisat2-align-l"

 - "hisat2-align-s"

 - "hisat2-build"

 - "hisat2-build-l"

 - "hisat2-build-s"

 - "hisat2-inspect"

 - "hisat2-inspect-l"

 - "hisat2-inspect-s"

 - "hisat2_extract_exons.py"

 - "hisat2_extract_snps_haplotypes_UCSC.py"

 - "hisat2_extract_snps_haplotypes_VCF.py"

 - "hisat2_extract_splice_sites.py"

 - "hisat2_read_statistics.py"

 - "hisat2_simulate_reads.py"

 - "hisatgenotype.py"

 - "hisatgenotype_build_genome.py"

 - "hisatgenotype_extract_reads.py"

 - "hisatgenotype_extract_vars.py"

 - "hisatgenotype_hla_cyp.py"

 - "hisatgenotype_locus.py"

versions:
 - "2.2.0"
 - "latest"
description: "HISAT2 is a fast and sensitive alignment program for mapping next-generation sequencing reads (both DNA and RNA) to a population of human genomes as well as to a single reference genome."
---

This module is a singularity container wrapper for ghcr.io/autamus/hisat2.
HISAT2 is a fast and sensitive alignment program for mapping next-generation sequencing reads (both DNA and RNA) to a population of human genomes as well as to a single reference genome.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/hisat2
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/hisat2:2.2.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/hisat2/2.2.0
$ module help ghcr.io/autamus/hisat2/2.2.0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### hisat2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### hisat2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### hisat2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### hisat2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### hisat2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### hisat2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### hisat2
       
```bash
$ singularity exec <container> /opt/view/bin/hisat2
$ podman run --it --rm --entrypoint /opt/view/bin/hisat2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/hisat2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hisat2-align-l
       
```bash
$ singularity exec <container> /opt/view/bin/hisat2-align-l
$ podman run --it --rm --entrypoint /opt/view/bin/hisat2-align-l   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/hisat2-align-l   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hisat2-align-s
       
```bash
$ singularity exec <container> /opt/view/bin/hisat2-align-s
$ podman run --it --rm --entrypoint /opt/view/bin/hisat2-align-s   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/hisat2-align-s   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hisat2-build
       
```bash
$ singularity exec <container> /opt/view/bin/hisat2-build
$ podman run --it --rm --entrypoint /opt/view/bin/hisat2-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/hisat2-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hisat2-build-l
       
```bash
$ singularity exec <container> /opt/view/bin/hisat2-build-l
$ podman run --it --rm --entrypoint /opt/view/bin/hisat2-build-l   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/hisat2-build-l   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hisat2-build-s
       
```bash
$ singularity exec <container> /opt/view/bin/hisat2-build-s
$ podman run --it --rm --entrypoint /opt/view/bin/hisat2-build-s   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/hisat2-build-s   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hisat2-inspect
       
```bash
$ singularity exec <container> /opt/view/bin/hisat2-inspect
$ podman run --it --rm --entrypoint /opt/view/bin/hisat2-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/hisat2-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hisat2-inspect-l
       
```bash
$ singularity exec <container> /opt/view/bin/hisat2-inspect-l
$ podman run --it --rm --entrypoint /opt/view/bin/hisat2-inspect-l   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/hisat2-inspect-l   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hisat2-inspect-s
       
```bash
$ singularity exec <container> /opt/view/bin/hisat2-inspect-s
$ podman run --it --rm --entrypoint /opt/view/bin/hisat2-inspect-s   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/hisat2-inspect-s   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hisat2_extract_exons.py
       
```bash
$ singularity exec <container> /opt/view/bin/hisat2_extract_exons.py
$ podman run --it --rm --entrypoint /opt/view/bin/hisat2_extract_exons.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/hisat2_extract_exons.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hisat2_extract_snps_haplotypes_UCSC.py
       
```bash
$ singularity exec <container> /opt/view/bin/hisat2_extract_snps_haplotypes_UCSC.py
$ podman run --it --rm --entrypoint /opt/view/bin/hisat2_extract_snps_haplotypes_UCSC.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/hisat2_extract_snps_haplotypes_UCSC.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hisat2_extract_snps_haplotypes_VCF.py
       
```bash
$ singularity exec <container> /opt/view/bin/hisat2_extract_snps_haplotypes_VCF.py
$ podman run --it --rm --entrypoint /opt/view/bin/hisat2_extract_snps_haplotypes_VCF.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/hisat2_extract_snps_haplotypes_VCF.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hisat2_extract_splice_sites.py
       
```bash
$ singularity exec <container> /opt/view/bin/hisat2_extract_splice_sites.py
$ podman run --it --rm --entrypoint /opt/view/bin/hisat2_extract_splice_sites.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/hisat2_extract_splice_sites.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hisat2_read_statistics.py
       
```bash
$ singularity exec <container> /opt/view/bin/hisat2_read_statistics.py
$ podman run --it --rm --entrypoint /opt/view/bin/hisat2_read_statistics.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/hisat2_read_statistics.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hisat2_simulate_reads.py
       
```bash
$ singularity exec <container> /opt/view/bin/hisat2_simulate_reads.py
$ podman run --it --rm --entrypoint /opt/view/bin/hisat2_simulate_reads.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/hisat2_simulate_reads.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hisatgenotype.py
       
```bash
$ singularity exec <container> /opt/view/bin/hisatgenotype.py
$ podman run --it --rm --entrypoint /opt/view/bin/hisatgenotype.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/hisatgenotype.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hisatgenotype_build_genome.py
       
```bash
$ singularity exec <container> /opt/view/bin/hisatgenotype_build_genome.py
$ podman run --it --rm --entrypoint /opt/view/bin/hisatgenotype_build_genome.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/hisatgenotype_build_genome.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hisatgenotype_extract_reads.py
       
```bash
$ singularity exec <container> /opt/view/bin/hisatgenotype_extract_reads.py
$ podman run --it --rm --entrypoint /opt/view/bin/hisatgenotype_extract_reads.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/hisatgenotype_extract_reads.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hisatgenotype_extract_vars.py
       
```bash
$ singularity exec <container> /opt/view/bin/hisatgenotype_extract_vars.py
$ podman run --it --rm --entrypoint /opt/view/bin/hisatgenotype_extract_vars.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/hisatgenotype_extract_vars.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hisatgenotype_hla_cyp.py
       
```bash
$ singularity exec <container> /opt/view/bin/hisatgenotype_hla_cyp.py
$ podman run --it --rm --entrypoint /opt/view/bin/hisatgenotype_hla_cyp.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/hisatgenotype_hla_cyp.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hisatgenotype_locus.py
       
```bash
$ singularity exec <container> /opt/view/bin/hisatgenotype_locus.py
$ podman run --it --rm --entrypoint /opt/view/bin/hisatgenotype_locus.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/hisatgenotype_locus.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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