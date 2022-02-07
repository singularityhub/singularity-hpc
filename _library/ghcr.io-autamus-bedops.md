---
layout: container
name:  "ghcr.io/autamus/bedops"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/bedops/container.yaml"
updated_at: "2022-02-07 11:14:35.864104"
container_url: "https://github.com/orgs/autamus/packages/container/package/bedops"
aliases:
 - "bam2bed"

 - "bam2bed_gnuParallel"

 - "bam2bed_sge"

 - "bam2bed_slurm"

 - "bam2starch"

 - "bam2starch_gnuParallel"

 - "bam2starch_sge"

 - "bam2starch_slurm"

 - "bedextract"

 - "bedmap"

 - "bedops"

 - "closest-features"

 - "convert2bed"

 - "gff2bed"

 - "gff2starch"

 - "gtf2bed"

 - "gtf2starch"

 - "gvf2bed"

 - "gvf2starch"

 - "psl2bed"

 - "psl2starch"

 - "rmsk2bed"

 - "rmsk2starch"

 - "sam2bed"

 - "sam2starch"

 - "sort-bed"

 - "starch"

 - "starch-diff"

 - "starchcat"

 - "starchcluster_gnuParallel"

 - "starchcluster_sge"

 - "starchcluster_slurm"

 - "starchstrip"

 - "unstarch"

 - "update-sort-bed-migrate-candidates"

 - "update-sort-bed-slurm"

 - "update-sort-bed-starch-slurm"

 - "vcf2bed"

 - "vcf2starch"

 - "wig2bed"

 - "wig2starch"

versions:
 - "2.4.39"
 - "2.4.40"
 - "latest"
description: "BEDOPS is an open-source command-line toolkit that performs highly efficient and scalable Boolean and other set operations, statistical calculations, archiving, conversion and other management of genomic data of arbitrary scale."
---

This module is a singularity container wrapper for ghcr.io/autamus/bedops.
BEDOPS is an open-source command-line toolkit that performs highly efficient and scalable Boolean and other set operations, statistical calculations, archiving, conversion and other management of genomic data of arbitrary scale.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install ghcr.io/autamus/bedops
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/bedops:2.4.39
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/bedops/2.4.39
$ module help ghcr.io/autamus/bedops/2.4.39
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


#### bam2bed
       
```bash
$ singularity exec <container> /opt/view/bin/bam2bed
$ podman run --it --rm --entrypoint /opt/view/bin/bam2bed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/bam2bed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2bed_gnuParallel
       
```bash
$ singularity exec <container> /opt/view/bin/bam2bed_gnuParallel
$ podman run --it --rm --entrypoint /opt/view/bin/bam2bed_gnuParallel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/bam2bed_gnuParallel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2bed_sge
       
```bash
$ singularity exec <container> /opt/view/bin/bam2bed_sge
$ podman run --it --rm --entrypoint /opt/view/bin/bam2bed_sge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/bam2bed_sge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2bed_slurm
       
```bash
$ singularity exec <container> /opt/view/bin/bam2bed_slurm
$ podman run --it --rm --entrypoint /opt/view/bin/bam2bed_slurm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/bam2bed_slurm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2starch
       
```bash
$ singularity exec <container> /opt/view/bin/bam2starch
$ podman run --it --rm --entrypoint /opt/view/bin/bam2starch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/bam2starch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2starch_gnuParallel
       
```bash
$ singularity exec <container> /opt/view/bin/bam2starch_gnuParallel
$ podman run --it --rm --entrypoint /opt/view/bin/bam2starch_gnuParallel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/bam2starch_gnuParallel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2starch_sge
       
```bash
$ singularity exec <container> /opt/view/bin/bam2starch_sge
$ podman run --it --rm --entrypoint /opt/view/bin/bam2starch_sge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/bam2starch_sge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2starch_slurm
       
```bash
$ singularity exec <container> /opt/view/bin/bam2starch_slurm
$ podman run --it --rm --entrypoint /opt/view/bin/bam2starch_slurm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/bam2starch_slurm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bedextract
       
```bash
$ singularity exec <container> /opt/view/bin/bedextract
$ podman run --it --rm --entrypoint /opt/view/bin/bedextract   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/bedextract   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bedmap
       
```bash
$ singularity exec <container> /opt/view/bin/bedmap
$ podman run --it --rm --entrypoint /opt/view/bin/bedmap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/bedmap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bedops
       
```bash
$ singularity exec <container> /opt/view/bin/bedops
$ podman run --it --rm --entrypoint /opt/view/bin/bedops   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/bedops   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### closest-features
       
```bash
$ singularity exec <container> /opt/view/bin/closest-features
$ podman run --it --rm --entrypoint /opt/view/bin/closest-features   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/closest-features   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### convert2bed
       
```bash
$ singularity exec <container> /opt/view/bin/convert2bed
$ podman run --it --rm --entrypoint /opt/view/bin/convert2bed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/convert2bed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gff2bed
       
```bash
$ singularity exec <container> /opt/view/bin/gff2bed
$ podman run --it --rm --entrypoint /opt/view/bin/gff2bed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/gff2bed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gff2starch
       
```bash
$ singularity exec <container> /opt/view/bin/gff2starch
$ podman run --it --rm --entrypoint /opt/view/bin/gff2starch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/gff2starch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtf2bed
       
```bash
$ singularity exec <container> /opt/view/bin/gtf2bed
$ podman run --it --rm --entrypoint /opt/view/bin/gtf2bed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/gtf2bed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtf2starch
       
```bash
$ singularity exec <container> /opt/view/bin/gtf2starch
$ podman run --it --rm --entrypoint /opt/view/bin/gtf2starch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/gtf2starch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gvf2bed
       
```bash
$ singularity exec <container> /opt/view/bin/gvf2bed
$ podman run --it --rm --entrypoint /opt/view/bin/gvf2bed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/gvf2bed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gvf2starch
       
```bash
$ singularity exec <container> /opt/view/bin/gvf2starch
$ podman run --it --rm --entrypoint /opt/view/bin/gvf2starch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/gvf2starch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### psl2bed
       
```bash
$ singularity exec <container> /opt/view/bin/psl2bed
$ podman run --it --rm --entrypoint /opt/view/bin/psl2bed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/psl2bed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### psl2starch
       
```bash
$ singularity exec <container> /opt/view/bin/psl2starch
$ podman run --it --rm --entrypoint /opt/view/bin/psl2starch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/psl2starch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rmsk2bed
       
```bash
$ singularity exec <container> /opt/view/bin/rmsk2bed
$ podman run --it --rm --entrypoint /opt/view/bin/rmsk2bed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/rmsk2bed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rmsk2starch
       
```bash
$ singularity exec <container> /opt/view/bin/rmsk2starch
$ podman run --it --rm --entrypoint /opt/view/bin/rmsk2starch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/rmsk2starch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sam2bed
       
```bash
$ singularity exec <container> /opt/view/bin/sam2bed
$ podman run --it --rm --entrypoint /opt/view/bin/sam2bed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/sam2bed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sam2starch
       
```bash
$ singularity exec <container> /opt/view/bin/sam2starch
$ podman run --it --rm --entrypoint /opt/view/bin/sam2starch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/sam2starch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sort-bed
       
```bash
$ singularity exec <container> /opt/view/bin/sort-bed
$ podman run --it --rm --entrypoint /opt/view/bin/sort-bed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/sort-bed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### starch
       
```bash
$ singularity exec <container> /opt/view/bin/starch
$ podman run --it --rm --entrypoint /opt/view/bin/starch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/starch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### starch-diff
       
```bash
$ singularity exec <container> /opt/view/bin/starch-diff
$ podman run --it --rm --entrypoint /opt/view/bin/starch-diff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/starch-diff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### starchcat
       
```bash
$ singularity exec <container> /opt/view/bin/starchcat
$ podman run --it --rm --entrypoint /opt/view/bin/starchcat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/starchcat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### starchcluster_gnuParallel
       
```bash
$ singularity exec <container> /opt/view/bin/starchcluster_gnuParallel
$ podman run --it --rm --entrypoint /opt/view/bin/starchcluster_gnuParallel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/starchcluster_gnuParallel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### starchcluster_sge
       
```bash
$ singularity exec <container> /opt/view/bin/starchcluster_sge
$ podman run --it --rm --entrypoint /opt/view/bin/starchcluster_sge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/starchcluster_sge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### starchcluster_slurm
       
```bash
$ singularity exec <container> /opt/view/bin/starchcluster_slurm
$ podman run --it --rm --entrypoint /opt/view/bin/starchcluster_slurm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/starchcluster_slurm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### starchstrip
       
```bash
$ singularity exec <container> /opt/view/bin/starchstrip
$ podman run --it --rm --entrypoint /opt/view/bin/starchstrip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/starchstrip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unstarch
       
```bash
$ singularity exec <container> /opt/view/bin/unstarch
$ podman run --it --rm --entrypoint /opt/view/bin/unstarch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/unstarch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### update-sort-bed-migrate-candidates
       
```bash
$ singularity exec <container> /opt/view/bin/update-sort-bed-migrate-candidates
$ podman run --it --rm --entrypoint /opt/view/bin/update-sort-bed-migrate-candidates   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/update-sort-bed-migrate-candidates   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### update-sort-bed-slurm
       
```bash
$ singularity exec <container> /opt/view/bin/update-sort-bed-slurm
$ podman run --it --rm --entrypoint /opt/view/bin/update-sort-bed-slurm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/update-sort-bed-slurm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### update-sort-bed-starch-slurm
       
```bash
$ singularity exec <container> /opt/view/bin/update-sort-bed-starch-slurm
$ podman run --it --rm --entrypoint /opt/view/bin/update-sort-bed-starch-slurm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/update-sort-bed-starch-slurm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf2bed
       
```bash
$ singularity exec <container> /opt/view/bin/vcf2bed
$ podman run --it --rm --entrypoint /opt/view/bin/vcf2bed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/vcf2bed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf2starch
       
```bash
$ singularity exec <container> /opt/view/bin/vcf2starch
$ podman run --it --rm --entrypoint /opt/view/bin/vcf2starch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/vcf2starch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wig2bed
       
```bash
$ singularity exec <container> /opt/view/bin/wig2bed
$ podman run --it --rm --entrypoint /opt/view/bin/wig2bed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/wig2bed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wig2starch
       
```bash
$ singularity exec <container> /opt/view/bin/wig2starch
$ podman run --it --rm --entrypoint /opt/view/bin/wig2starch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/wig2starch   -v ${PWD} -w ${PWD} <container> -c " $@"
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