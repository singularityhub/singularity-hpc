---
layout: container
name:  "ghcr.io/autamus/samtools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/samtools/container.yaml"
updated_at: "2021-05-01 15:22:15.648019"
container_url: ""
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

When you install this module, you'll be able to load it to make the following commands accessible:

#### ghcr.io-autamus-samtools-run:

```bash
$ singularity run <container>
```

#### ghcr.io-autamus-samtools-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### ghcr.io-autamus-samtools-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### ghcr.io-autamus-samtools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ghcr.io-autamus-samtools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### blast2sam.pl
       
```bash
$ singularity exec <container> /opt/view/bin/blast2sam.pl
```


#### bowtie2sam.pl
       
```bash
$ singularity exec <container> /opt/view/bin/bowtie2sam.pl
```


#### export2sam.pl
       
```bash
$ singularity exec <container> /opt/view/bin/export2sam.pl
```


#### fasta-sanitize.pl
       
```bash
$ singularity exec <container> /opt/view/bin/fasta-sanitize.pl
```


#### interpolate_sam.pl
       
```bash
$ singularity exec <container> /opt/view/bin/interpolate_sam.pl
```


#### novo2sam.pl
       
```bash
$ singularity exec <container> /opt/view/bin/novo2sam.pl
```


#### psl2sam.pl
       
```bash
$ singularity exec <container> /opt/view/bin/psl2sam.pl
```


#### sam2vcf.pl
       
```bash
$ singularity exec <container> /opt/view/bin/sam2vcf.pl
```


#### samtools
       
```bash
$ singularity exec <container> /opt/view/bin/samtools
```


#### samtools.pl
       
```bash
$ singularity exec <container> /opt/view/bin/samtools.pl
```


#### seq_cache_populate.pl
       
```bash
$ singularity exec <container> /opt/view/bin/seq_cache_populate.pl
```


#### soap2sam.pl
       
```bash
$ singularity exec <container> /opt/view/bin/soap2sam.pl
```


#### wgsim_eval.pl
       
```bash
$ singularity exec <container> /opt/view/bin/wgsim_eval.pl
```


#### zoom2sam.pl
       
```bash
$ singularity exec <container> /opt/view/bin/zoom2sam.pl
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