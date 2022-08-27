---
layout: container
name:  "quay.io/biocontainers/samtools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/samtools/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/samtools/container.yaml"
updated_at: "2022-08-27 01:37:31.107955"
latest: "1.15--h3843a85_0"
container_url: "https://quay.io/repository/biocontainers/samtools"
aliases:
 - "ace2sam"
 - "bgzip"
 - "blast2sam.pl"
 - "bowtie2sam.pl"
 - "export2sam.pl"
 - "fasta-sanitize.pl"
 - "htsfile"
 - "interpolate_sam.pl"
 - "libdeflate-gunzip"
 - "libdeflate-gzip"
 - "maq2sam-long"
 - "maq2sam-short"
 - "md5fa"
 - "md5sum-lite"
 - "novo2sam.pl"
 - "plot-ampliconstats"
 - "plot-bamstats"
 - "psl2sam.pl"
 - "sam2vcf.pl"
 - "samtools"
 - "samtools.pl"
 - "seq_cache_populate.pl"
 - "soap2sam.pl"
 - "tabix"
 - "wgsim"
 - "wgsim_eval.pl"
 - "zoom2sam.pl"
versions:
 - "1.10--h2e538c0_3"
 - "1.11--h6270b1f_0"
 - "1.12--h9aed4be_1"
 - "1.13--h8c37831_0"
 - "1.14--hb421002_0"
 - "1.15--h3843a85_0"
description: "Tools for reading/writing/editing/indexing/viewing SAM/BAM/CRAM format."
config: {"docker": "quay.io/biocontainers/samtools", "url": "https://quay.io/repository/biocontainers/samtools", "maintainer": "@audreystott", "description": "Tools for reading/writing/editing/indexing/viewing SAM/BAM/CRAM format.", "latest": {"1.15--h3843a85_0": "sha256:d68e1b5f504dc60eb9f2a02eecbac44a63f144e7d455b3fb1a25323c667ca4c4"}, "tags": {"1.10--h2e538c0_3": "sha256:84a8d0c0acec87448a47cefa60c4f4a545887239fcd7984a58b48e7a6ac86390", "1.11--h6270b1f_0": "sha256:141120f19f849b79e05ae2fac981383988445c373b8b5db7f3dd221179af382b", "1.12--h9aed4be_1": "sha256:5fd5f0937adf8a24b5bf7655110e501df78ae51588547c8617f17c3291a723e1", "1.13--h8c37831_0": "sha256:04da5297386dfae2458a93613a8c60216d158ee7cb9f96188dad71c1952f7f72", "1.14--hb421002_0": "sha256:88632c41eba8b94b7a2a1013f422aecf478a0cb278740bcc3a38058c903d61ad", "1.15--h3843a85_0": "sha256:d68e1b5f504dc60eb9f2a02eecbac44a63f144e7d455b3fb1a25323c667ca4c4"}, "aliases": {"ace2sam": "/usr/local/bin/ace2sam", "bgzip": "/usr/local/bin/bgzip", "blast2sam.pl": "/usr/local/bin/blast2sam.pl", "bowtie2sam.pl": "/usr/local/bin/bowtie2sam.pl", "export2sam.pl": "/usr/local/bin/export2sam.pl", "fasta-sanitize.pl": "/usr/local/bin/fasta-sanitize.pl", "htsfile": "/usr/local/bin/htsfile", "interpolate_sam.pl": "/usr/local/bin/interpolate_sam.pl", "libdeflate-gunzip": "/usr/local/bin/libdeflate-gunzip", "libdeflate-gzip": "/usr/local/bin/libdeflate-gzip", "maq2sam-long": "/usr/local/bin/maq2sam-long", "maq2sam-short": "/usr/local/bin/maq2sam-short", "md5fa": "/usr/local/bin/md5fa", "md5sum-lite": "/usr/local/bin/md5sum-lite", "novo2sam.pl": "/usr/local/bin/novo2sam.pl", "plot-ampliconstats": "/usr/local/bin/plot-ampliconstats", "plot-bamstats": "/usr/local/bin/plot-bamstats", "psl2sam.pl": "/usr/local/bin/psl2sam.pl", "sam2vcf.pl": "/usr/local/bin/sam2vcf.pl", "samtools": "/usr/local/bin/samtools", "samtools.pl": "/usr/local/bin/samtools.pl", "seq_cache_populate.pl": "/usr/local/bin/seq_cache_populate.pl", "soap2sam.pl": "/usr/local/bin/soap2sam.pl", "tabix": "/usr/local/bin/tabix", "wgsim": "/usr/local/bin/wgsim", "wgsim_eval.pl": "/usr/local/bin/wgsim_eval.pl", "zoom2sam.pl": "/usr/local/bin/zoom2sam.pl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/samtools.
Tools for reading/writing/editing/indexing/viewing SAM/BAM/CRAM format.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/samtools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/samtools:1.10--h2e538c0_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/samtools/1.10--h2e538c0_3
$ module help quay.io/biocontainers/samtools/1.10--h2e538c0_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### samtools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### samtools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### samtools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### samtools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### samtools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### samtools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ace2sam
       
```bash
$ singularity exec <container> /usr/local/bin/ace2sam
$ podman run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bgzip
       
```bash
$ singularity exec <container> /usr/local/bin/bgzip
$ podman run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blast2sam.pl
       
```bash
$ singularity exec <container> /usr/local/bin/blast2sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/blast2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blast2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2sam.pl
       
```bash
$ singularity exec <container> /usr/local/bin/bowtie2sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### export2sam.pl
       
```bash
$ singularity exec <container> /usr/local/bin/export2sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/export2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/export2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta-sanitize.pl
       
```bash
$ singularity exec <container> /usr/local/bin/fasta-sanitize.pl
$ podman run --it --rm --entrypoint /usr/local/bin/fasta-sanitize.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta-sanitize.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### htsfile
       
```bash
$ singularity exec <container> /usr/local/bin/htsfile
$ podman run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### interpolate_sam.pl
       
```bash
$ singularity exec <container> /usr/local/bin/interpolate_sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/interpolate_sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/interpolate_sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### libdeflate-gunzip
       
```bash
$ singularity exec <container> /usr/local/bin/libdeflate-gunzip
$ podman run --it --rm --entrypoint /usr/local/bin/libdeflate-gunzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/libdeflate-gunzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### libdeflate-gzip
       
```bash
$ singularity exec <container> /usr/local/bin/libdeflate-gzip
$ podman run --it --rm --entrypoint /usr/local/bin/libdeflate-gzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/libdeflate-gzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### maq2sam-long
       
```bash
$ singularity exec <container> /usr/local/bin/maq2sam-long
$ podman run --it --rm --entrypoint /usr/local/bin/maq2sam-long   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/maq2sam-long   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### maq2sam-short
       
```bash
$ singularity exec <container> /usr/local/bin/maq2sam-short
$ podman run --it --rm --entrypoint /usr/local/bin/maq2sam-short   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/maq2sam-short   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### md5fa
       
```bash
$ singularity exec <container> /usr/local/bin/md5fa
$ podman run --it --rm --entrypoint /usr/local/bin/md5fa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/md5fa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### md5sum-lite
       
```bash
$ singularity exec <container> /usr/local/bin/md5sum-lite
$ podman run --it --rm --entrypoint /usr/local/bin/md5sum-lite   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/md5sum-lite   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### novo2sam.pl
       
```bash
$ singularity exec <container> /usr/local/bin/novo2sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/novo2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/novo2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot-ampliconstats
       
```bash
$ singularity exec <container> /usr/local/bin/plot-ampliconstats
$ podman run --it --rm --entrypoint /usr/local/bin/plot-ampliconstats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot-ampliconstats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot-bamstats
       
```bash
$ singularity exec <container> /usr/local/bin/plot-bamstats
$ podman run --it --rm --entrypoint /usr/local/bin/plot-bamstats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot-bamstats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### psl2sam.pl
       
```bash
$ singularity exec <container> /usr/local/bin/psl2sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/psl2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/psl2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sam2vcf.pl
       
```bash
$ singularity exec <container> /usr/local/bin/sam2vcf.pl
$ podman run --it --rm --entrypoint /usr/local/bin/sam2vcf.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sam2vcf.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### samtools
       
```bash
$ singularity exec <container> /usr/local/bin/samtools
$ podman run --it --rm --entrypoint /usr/local/bin/samtools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/samtools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### samtools.pl
       
```bash
$ singularity exec <container> /usr/local/bin/samtools.pl
$ podman run --it --rm --entrypoint /usr/local/bin/samtools.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/samtools.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seq_cache_populate.pl
       
```bash
$ singularity exec <container> /usr/local/bin/seq_cache_populate.pl
$ podman run --it --rm --entrypoint /usr/local/bin/seq_cache_populate.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seq_cache_populate.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### soap2sam.pl
       
```bash
$ singularity exec <container> /usr/local/bin/soap2sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/soap2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/soap2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tabix
       
```bash
$ singularity exec <container> /usr/local/bin/tabix
$ podman run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wgsim
       
```bash
$ singularity exec <container> /usr/local/bin/wgsim
$ podman run --it --rm --entrypoint /usr/local/bin/wgsim   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wgsim   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wgsim_eval.pl
       
```bash
$ singularity exec <container> /usr/local/bin/wgsim_eval.pl
$ podman run --it --rm --entrypoint /usr/local/bin/wgsim_eval.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wgsim_eval.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zoom2sam.pl
       
```bash
$ singularity exec <container> /usr/local/bin/zoom2sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/zoom2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zoom2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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