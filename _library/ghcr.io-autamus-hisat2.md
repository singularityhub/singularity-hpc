---
layout: container
name:  "ghcr.io/autamus/hisat2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/hisat2/container.yaml"
updated_at: "2021-04-20 02:19:47.300461"
container_url: ""
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
$ shpc install ghcr.io/autamus/hisat2:latest
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/hisat2/latest
$ module help ghcr.io/autamus/hisat2/latest
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### ghcr.io-autamus-hisat2-run:

```bash
$ singularity run <container>
```

#### ghcr.io-autamus-hisat2-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### ghcr.io-autamus-hisat2-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### ghcr.io-autamus-hisat2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ghcr.io-autamus-hisat2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### hisat2
       
```bash
$ singularity exec <container> /opt/view/bin/hisat2
```


#### hisat2-align-l
       
```bash
$ singularity exec <container> /opt/view/bin/hisat2-align-l
```


#### hisat2-align-s
       
```bash
$ singularity exec <container> /opt/view/bin/hisat2-align-s
```


#### hisat2-build
       
```bash
$ singularity exec <container> /opt/view/bin/hisat2-build
```


#### hisat2-build-l
       
```bash
$ singularity exec <container> /opt/view/bin/hisat2-build-l
```


#### hisat2-build-s
       
```bash
$ singularity exec <container> /opt/view/bin/hisat2-build-s
```


#### hisat2-inspect
       
```bash
$ singularity exec <container> /opt/view/bin/hisat2-inspect
```


#### hisat2-inspect-l
       
```bash
$ singularity exec <container> /opt/view/bin/hisat2-inspect-l
```


#### hisat2-inspect-s
       
```bash
$ singularity exec <container> /opt/view/bin/hisat2-inspect-s
```


#### hisat2_extract_exons.py
       
```bash
$ singularity exec <container> /opt/view/bin/hisat2_extract_exons.py
```


#### hisat2_extract_snps_haplotypes_UCSC.py
       
```bash
$ singularity exec <container> /opt/view/bin/hisat2_extract_snps_haplotypes_UCSC.py
```


#### hisat2_extract_snps_haplotypes_VCF.py
       
```bash
$ singularity exec <container> /opt/view/bin/hisat2_extract_snps_haplotypes_VCF.py
```


#### hisat2_extract_splice_sites.py
       
```bash
$ singularity exec <container> /opt/view/bin/hisat2_extract_splice_sites.py
```


#### hisat2_read_statistics.py
       
```bash
$ singularity exec <container> /opt/view/bin/hisat2_read_statistics.py
```


#### hisat2_simulate_reads.py
       
```bash
$ singularity exec <container> /opt/view/bin/hisat2_simulate_reads.py
```


#### hisatgenotype.py
       
```bash
$ singularity exec <container> /opt/view/bin/hisatgenotype.py
```


#### hisatgenotype_build_genome.py
       
```bash
$ singularity exec <container> /opt/view/bin/hisatgenotype_build_genome.py
```


#### hisatgenotype_extract_reads.py
       
```bash
$ singularity exec <container> /opt/view/bin/hisatgenotype_extract_reads.py
```


#### hisatgenotype_extract_vars.py
       
```bash
$ singularity exec <container> /opt/view/bin/hisatgenotype_extract_vars.py
```


#### hisatgenotype_hla_cyp.py
       
```bash
$ singularity exec <container> /opt/view/bin/hisatgenotype_hla_cyp.py
```


#### hisatgenotype_locus.py
       
```bash
$ singularity exec <container> /opt/view/bin/hisatgenotype_locus.py
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