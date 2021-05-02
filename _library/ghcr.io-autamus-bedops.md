---
layout: container
name:  "ghcr.io/autamus/bedops"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/bedops/container.yaml"
updated_at: "2021-05-02 16:04:34.712445"
container_url: ""
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

When you install this module, you'll be able to load it to make the following commands accessible:

#### ghcr.io-autamus-bedops-run:

```bash
$ singularity run <container>
```

#### ghcr.io-autamus-bedops-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### ghcr.io-autamus-bedops-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### ghcr.io-autamus-bedops-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ghcr.io-autamus-bedops-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bam2bed
       
```bash
$ singularity exec <container> /opt/view/bin/bam2bed
```


#### bam2bed_gnuParallel
       
```bash
$ singularity exec <container> /opt/view/bin/bam2bed_gnuParallel
```


#### bam2bed_sge
       
```bash
$ singularity exec <container> /opt/view/bin/bam2bed_sge
```


#### bam2bed_slurm
       
```bash
$ singularity exec <container> /opt/view/bin/bam2bed_slurm
```


#### bam2starch
       
```bash
$ singularity exec <container> /opt/view/bin/bam2starch
```


#### bam2starch_gnuParallel
       
```bash
$ singularity exec <container> /opt/view/bin/bam2starch_gnuParallel
```


#### bam2starch_sge
       
```bash
$ singularity exec <container> /opt/view/bin/bam2starch_sge
```


#### bam2starch_slurm
       
```bash
$ singularity exec <container> /opt/view/bin/bam2starch_slurm
```


#### bedextract
       
```bash
$ singularity exec <container> /opt/view/bin/bedextract
```


#### bedmap
       
```bash
$ singularity exec <container> /opt/view/bin/bedmap
```


#### bedops
       
```bash
$ singularity exec <container> /opt/view/bin/bedops
```


#### closest-features
       
```bash
$ singularity exec <container> /opt/view/bin/closest-features
```


#### convert2bed
       
```bash
$ singularity exec <container> /opt/view/bin/convert2bed
```


#### gff2bed
       
```bash
$ singularity exec <container> /opt/view/bin/gff2bed
```


#### gff2starch
       
```bash
$ singularity exec <container> /opt/view/bin/gff2starch
```


#### gtf2bed
       
```bash
$ singularity exec <container> /opt/view/bin/gtf2bed
```


#### gtf2starch
       
```bash
$ singularity exec <container> /opt/view/bin/gtf2starch
```


#### gvf2bed
       
```bash
$ singularity exec <container> /opt/view/bin/gvf2bed
```


#### gvf2starch
       
```bash
$ singularity exec <container> /opt/view/bin/gvf2starch
```


#### psl2bed
       
```bash
$ singularity exec <container> /opt/view/bin/psl2bed
```


#### psl2starch
       
```bash
$ singularity exec <container> /opt/view/bin/psl2starch
```


#### rmsk2bed
       
```bash
$ singularity exec <container> /opt/view/bin/rmsk2bed
```


#### rmsk2starch
       
```bash
$ singularity exec <container> /opt/view/bin/rmsk2starch
```


#### sam2bed
       
```bash
$ singularity exec <container> /opt/view/bin/sam2bed
```


#### sam2starch
       
```bash
$ singularity exec <container> /opt/view/bin/sam2starch
```


#### sort-bed
       
```bash
$ singularity exec <container> /opt/view/bin/sort-bed
```


#### starch
       
```bash
$ singularity exec <container> /opt/view/bin/starch
```


#### starch-diff
       
```bash
$ singularity exec <container> /opt/view/bin/starch-diff
```


#### starchcat
       
```bash
$ singularity exec <container> /opt/view/bin/starchcat
```


#### starchcluster_gnuParallel
       
```bash
$ singularity exec <container> /opt/view/bin/starchcluster_gnuParallel
```


#### starchcluster_sge
       
```bash
$ singularity exec <container> /opt/view/bin/starchcluster_sge
```


#### starchcluster_slurm
       
```bash
$ singularity exec <container> /opt/view/bin/starchcluster_slurm
```


#### starchstrip
       
```bash
$ singularity exec <container> /opt/view/bin/starchstrip
```


#### unstarch
       
```bash
$ singularity exec <container> /opt/view/bin/unstarch
```


#### update-sort-bed-migrate-candidates
       
```bash
$ singularity exec <container> /opt/view/bin/update-sort-bed-migrate-candidates
```


#### update-sort-bed-slurm
       
```bash
$ singularity exec <container> /opt/view/bin/update-sort-bed-slurm
```


#### update-sort-bed-starch-slurm
       
```bash
$ singularity exec <container> /opt/view/bin/update-sort-bed-starch-slurm
```


#### vcf2bed
       
```bash
$ singularity exec <container> /opt/view/bin/vcf2bed
```


#### vcf2starch
       
```bash
$ singularity exec <container> /opt/view/bin/vcf2starch
```


#### wig2bed
       
```bash
$ singularity exec <container> /opt/view/bin/wig2bed
```


#### wig2starch
       
```bash
$ singularity exec <container> /opt/view/bin/wig2starch
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