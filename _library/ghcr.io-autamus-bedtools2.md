---
layout: container
name:  "ghcr.io/autamus/bedtools2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/bedtools2/container.yaml"
updated_at: "2021-06-06 20:44:15.828670"
container_url: "https://github.com/orgs/autamus/packages/container/package/bedtools2"
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


#### annotateBed
       
```bash
$ singularity exec <container> /opt/view/bin/annotateBed
$ podman run --it --rm --entrypoint /opt/view/bin/annotateBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/annotateBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamToBed
       
```bash
$ singularity exec <container> /opt/view/bin/bamToBed
$ podman run --it --rm --entrypoint /opt/view/bin/bamToBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/bamToBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bed12ToBed6
       
```bash
$ singularity exec <container> /opt/view/bin/bed12ToBed6
$ podman run --it --rm --entrypoint /opt/view/bin/bed12ToBed6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/bed12ToBed6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bedToBam
       
```bash
$ singularity exec <container> /opt/view/bin/bedToBam
$ podman run --it --rm --entrypoint /opt/view/bin/bedToBam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/bedToBam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bedToIgv
       
```bash
$ singularity exec <container> /opt/view/bin/bedToIgv
$ podman run --it --rm --entrypoint /opt/view/bin/bedToIgv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/bedToIgv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bedpeToBam
       
```bash
$ singularity exec <container> /opt/view/bin/bedpeToBam
$ podman run --it --rm --entrypoint /opt/view/bin/bedpeToBam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/bedpeToBam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bedtools
       
```bash
$ singularity exec <container> /opt/view/bin/bedtools
$ podman run --it --rm --entrypoint /opt/view/bin/bedtools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/bedtools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### closestBed
       
```bash
$ singularity exec <container> /opt/view/bin/closestBed
$ podman run --it --rm --entrypoint /opt/view/bin/closestBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/closestBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clusterBed
       
```bash
$ singularity exec <container> /opt/view/bin/clusterBed
$ podman run --it --rm --entrypoint /opt/view/bin/clusterBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/clusterBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### complementBed
       
```bash
$ singularity exec <container> /opt/view/bin/complementBed
$ podman run --it --rm --entrypoint /opt/view/bin/complementBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/complementBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### coverageBed
       
```bash
$ singularity exec <container> /opt/view/bin/coverageBed
$ podman run --it --rm --entrypoint /opt/view/bin/coverageBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/coverageBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastaFromBed
       
```bash
$ singularity exec <container> /opt/view/bin/fastaFromBed
$ podman run --it --rm --entrypoint /opt/view/bin/fastaFromBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/fastaFromBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flankBed
       
```bash
$ singularity exec <container> /opt/view/bin/flankBed
$ podman run --it --rm --entrypoint /opt/view/bin/flankBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/flankBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genomeCoverageBed
       
```bash
$ singularity exec <container> /opt/view/bin/genomeCoverageBed
$ podman run --it --rm --entrypoint /opt/view/bin/genomeCoverageBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/genomeCoverageBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### intersectBed
       
```bash
$ singularity exec <container> /opt/view/bin/intersectBed
$ podman run --it --rm --entrypoint /opt/view/bin/intersectBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/intersectBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### linksBed
       
```bash
$ singularity exec <container> /opt/view/bin/linksBed
$ podman run --it --rm --entrypoint /opt/view/bin/linksBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/linksBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mapBed
       
```bash
$ singularity exec <container> /opt/view/bin/mapBed
$ podman run --it --rm --entrypoint /opt/view/bin/mapBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/mapBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### maskFastaFromBed
       
```bash
$ singularity exec <container> /opt/view/bin/maskFastaFromBed
$ podman run --it --rm --entrypoint /opt/view/bin/maskFastaFromBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/maskFastaFromBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mergeBed
       
```bash
$ singularity exec <container> /opt/view/bin/mergeBed
$ podman run --it --rm --entrypoint /opt/view/bin/mergeBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/mergeBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### multiIntersectBed
       
```bash
$ singularity exec <container> /opt/view/bin/multiIntersectBed
$ podman run --it --rm --entrypoint /opt/view/bin/multiIntersectBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/multiIntersectBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nucBed
       
```bash
$ singularity exec <container> /opt/view/bin/nucBed
$ podman run --it --rm --entrypoint /opt/view/bin/nucBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/nucBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pairToBed
       
```bash
$ singularity exec <container> /opt/view/bin/pairToBed
$ podman run --it --rm --entrypoint /opt/view/bin/pairToBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/pairToBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### randomBed
       
```bash
$ singularity exec <container> /opt/view/bin/randomBed
$ podman run --it --rm --entrypoint /opt/view/bin/randomBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/randomBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shiftBed
       
```bash
$ singularity exec <container> /opt/view/bin/shiftBed
$ podman run --it --rm --entrypoint /opt/view/bin/shiftBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/shiftBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shuffleBed
       
```bash
$ singularity exec <container> /opt/view/bin/shuffleBed
$ podman run --it --rm --entrypoint /opt/view/bin/shuffleBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/shuffleBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### slopBed
       
```bash
$ singularity exec <container> /opt/view/bin/slopBed
$ podman run --it --rm --entrypoint /opt/view/bin/slopBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/slopBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sortBed
       
```bash
$ singularity exec <container> /opt/view/bin/sortBed
$ podman run --it --rm --entrypoint /opt/view/bin/sortBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/sortBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### subtractBed
       
```bash
$ singularity exec <container> /opt/view/bin/subtractBed
$ podman run --it --rm --entrypoint /opt/view/bin/subtractBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/subtractBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unionBedGraphs
       
```bash
$ singularity exec <container> /opt/view/bin/unionBedGraphs
$ podman run --it --rm --entrypoint /opt/view/bin/unionBedGraphs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/unionBedGraphs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### windowBed
       
```bash
$ singularity exec <container> /opt/view/bin/windowBed
$ podman run --it --rm --entrypoint /opt/view/bin/windowBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/windowBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```



In the above, the `<container>` directive will reference an actual container provided
by the module, for the version you have chosen to load. An environment file in the
module folder will also be bound. Note that although a container
might provide custom commands, every container exposes unique exec, shell, run, and
inspect aliases. For anycommands above, you can export:

 - SINGULARITY_OPTS: to define custom options for singularity (e.g., --debug)
 - SINGULARITY_COMMAND_OPTS: to define custom options for the command (e.g., -b)
 - DOCKER_OPTS: to define custom options for podman or docker
 - DOCKER_COMMAND_OPTS: to define custom options for the command

<br>
  
### Install

You can install shpc locally (for yourself or your user base) as follows:

```bash
$ git clone https://github.com/singularityhub/singularity-hpc
$ cd singularity-hpc
$ pip install -e .
```

Have any questions, or want to request a new module or version? [ask for help!](https://github.com/singularityhub/singularity-hpc/issues)