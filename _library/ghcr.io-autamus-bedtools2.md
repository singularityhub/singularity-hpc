---
layout: container
name:  "ghcr.io/autamus/bedtools2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/bedtools2/container.yaml"
updated_at: "2021-04-20 03:18:25.812082"
container_url: ""
aliases:
 - "annotateBed"

 - "bamToBed"

 - "bed12ToBed6"

 - "bedToBam"

 - "bedToIgv"

 - "bedpeToBam"

 - "bedtools"

 - "closestBed"

 - "clusterBed"

 - "complementBed"

 - "coverageBed"

 - "fastaFromBed"

 - "flankBed"

 - "genomeCoverageBed"

 - "intersectBed"

 - "linksBed"

 - "mapBed"

 - "maskFastaFromBed"

 - "mergeBed"

 - "multiIntersectBed"

 - "nucBed"

 - "pairToBed"

 - "randomBed"

 - "shiftBed"

 - "shuffleBed"

 - "slopBed"

 - "sortBed"

 - "subtractBed"

 - "unionBedGraphs"

 - "windowBed"

versions:
 - "2.30.0"
 - "latest"
description: "The swiss army knife for genome arithmetic"
---

This module is a singularity container wrapper for ghcr.io/autamus/bedtools2.
The swiss army knife for genome arithmetic
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install ghcr.io/autamus/bedtools2
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/bedtools2:2.30.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/bedtools2/2.30.0
$ module help ghcr.io/autamus/bedtools2/2.30.0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### ghcr.io-autamus-bedtools2-run:

```bash
$ singularity run <container>
```

#### ghcr.io-autamus-bedtools2-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### ghcr.io-autamus-bedtools2-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### ghcr.io-autamus-bedtools2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ghcr.io-autamus-bedtools2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### annotateBed
       
```bash
$ singularity exec <container> /opt/view/bin/annotateBed
```


#### bamToBed
       
```bash
$ singularity exec <container> /opt/view/bin/bamToBed
```


#### bed12ToBed6
       
```bash
$ singularity exec <container> /opt/view/bin/bed12ToBed6
```


#### bedToBam
       
```bash
$ singularity exec <container> /opt/view/bin/bedToBam
```


#### bedToIgv
       
```bash
$ singularity exec <container> /opt/view/bin/bedToIgv
```


#### bedpeToBam
       
```bash
$ singularity exec <container> /opt/view/bin/bedpeToBam
```


#### bedtools
       
```bash
$ singularity exec <container> /opt/view/bin/bedtools
```


#### closestBed
       
```bash
$ singularity exec <container> /opt/view/bin/closestBed
```


#### clusterBed
       
```bash
$ singularity exec <container> /opt/view/bin/clusterBed
```


#### complementBed
       
```bash
$ singularity exec <container> /opt/view/bin/complementBed
```


#### coverageBed
       
```bash
$ singularity exec <container> /opt/view/bin/coverageBed
```


#### fastaFromBed
       
```bash
$ singularity exec <container> /opt/view/bin/fastaFromBed
```


#### flankBed
       
```bash
$ singularity exec <container> /opt/view/bin/flankBed
```


#### genomeCoverageBed
       
```bash
$ singularity exec <container> /opt/view/bin/genomeCoverageBed
```


#### intersectBed
       
```bash
$ singularity exec <container> /opt/view/bin/intersectBed
```


#### linksBed
       
```bash
$ singularity exec <container> /opt/view/bin/linksBed
```


#### mapBed
       
```bash
$ singularity exec <container> /opt/view/bin/mapBed
```


#### maskFastaFromBed
       
```bash
$ singularity exec <container> /opt/view/bin/maskFastaFromBed
```


#### mergeBed
       
```bash
$ singularity exec <container> /opt/view/bin/mergeBed
```


#### multiIntersectBed
       
```bash
$ singularity exec <container> /opt/view/bin/multiIntersectBed
```


#### nucBed
       
```bash
$ singularity exec <container> /opt/view/bin/nucBed
```


#### pairToBed
       
```bash
$ singularity exec <container> /opt/view/bin/pairToBed
```


#### randomBed
       
```bash
$ singularity exec <container> /opt/view/bin/randomBed
```


#### shiftBed
       
```bash
$ singularity exec <container> /opt/view/bin/shiftBed
```


#### shuffleBed
       
```bash
$ singularity exec <container> /opt/view/bin/shuffleBed
```


#### slopBed
       
```bash
$ singularity exec <container> /opt/view/bin/slopBed
```


#### sortBed
       
```bash
$ singularity exec <container> /opt/view/bin/sortBed
```


#### subtractBed
       
```bash
$ singularity exec <container> /opt/view/bin/subtractBed
```


#### unionBedGraphs
       
```bash
$ singularity exec <container> /opt/view/bin/unionBedGraphs
```


#### windowBed
       
```bash
$ singularity exec <container> /opt/view/bin/windowBed
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