---
layout: container
name:  "ghcr.io/autamus/openbabel"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/openbabel/container.yaml"
updated_at: "2022-03-27 05:30:08.024722"
container_url: "https://github.com/orgs/autamus/packages/container/package/openbabel"
aliases:
 - "obabel"

 - "obconformer"

 - "obdistgen"

 - "obenergy"

 - "obfit"

 - "obfitall"

 - "obgen"

 - "obgrep"

 - "obminimize"

 - "obmm"

 - "obprobe"

 - "obprop"

 - "obrms"

 - "obrotamer"

 - "obrotate"

 - "obspectrophore"

 - "obsym"

 - "obtautomer"

 - "obthermo"

versions:
 - "3.1.1"
 - "latest"
description: "Open Babel is a chemical toolbox designed to speak the many languages of chemical data. It's an open, collaborative project allowing anyone to search, convert, analyze, or store data from molecular modeling, chemistry, solid-state materials, biochemistry, or related areas."
---

This module is a singularity container wrapper for ghcr.io/autamus/openbabel.
Open Babel is a chemical toolbox designed to speak the many languages of chemical data. It's an open, collaborative project allowing anyone to search, convert, analyze, or store data from molecular modeling, chemistry, solid-state materials, biochemistry, or related areas.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/openbabel
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/openbabel:3.1.1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/openbabel/3.1.1
$ module help ghcr.io/autamus/openbabel/3.1.1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### openbabel-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### openbabel-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### openbabel-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### openbabel-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### openbabel-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### openbabel-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### obabel
       
```bash
$ singularity exec <container> /opt/view/bin/obabel
$ podman run --it --rm --entrypoint /opt/view/bin/obabel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/obabel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obconformer
       
```bash
$ singularity exec <container> /opt/view/bin/obconformer
$ podman run --it --rm --entrypoint /opt/view/bin/obconformer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/obconformer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obdistgen
       
```bash
$ singularity exec <container> /opt/view/bin/obdistgen
$ podman run --it --rm --entrypoint /opt/view/bin/obdistgen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/obdistgen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obenergy
       
```bash
$ singularity exec <container> /opt/view/bin/obenergy
$ podman run --it --rm --entrypoint /opt/view/bin/obenergy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/obenergy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obfit
       
```bash
$ singularity exec <container> /opt/view/bin/obfit
$ podman run --it --rm --entrypoint /opt/view/bin/obfit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/obfit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obfitall
       
```bash
$ singularity exec <container> /opt/view/bin/obfitall
$ podman run --it --rm --entrypoint /opt/view/bin/obfitall   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/obfitall   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obgen
       
```bash
$ singularity exec <container> /opt/view/bin/obgen
$ podman run --it --rm --entrypoint /opt/view/bin/obgen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/obgen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obgrep
       
```bash
$ singularity exec <container> /opt/view/bin/obgrep
$ podman run --it --rm --entrypoint /opt/view/bin/obgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/obgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obminimize
       
```bash
$ singularity exec <container> /opt/view/bin/obminimize
$ podman run --it --rm --entrypoint /opt/view/bin/obminimize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/obminimize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obmm
       
```bash
$ singularity exec <container> /opt/view/bin/obmm
$ podman run --it --rm --entrypoint /opt/view/bin/obmm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/obmm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obprobe
       
```bash
$ singularity exec <container> /opt/view/bin/obprobe
$ podman run --it --rm --entrypoint /opt/view/bin/obprobe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/obprobe   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obprop
       
```bash
$ singularity exec <container> /opt/view/bin/obprop
$ podman run --it --rm --entrypoint /opt/view/bin/obprop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/obprop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obrms
       
```bash
$ singularity exec <container> /opt/view/bin/obrms
$ podman run --it --rm --entrypoint /opt/view/bin/obrms   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/obrms   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obrotamer
       
```bash
$ singularity exec <container> /opt/view/bin/obrotamer
$ podman run --it --rm --entrypoint /opt/view/bin/obrotamer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/obrotamer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obrotate
       
```bash
$ singularity exec <container> /opt/view/bin/obrotate
$ podman run --it --rm --entrypoint /opt/view/bin/obrotate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/obrotate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obspectrophore
       
```bash
$ singularity exec <container> /opt/view/bin/obspectrophore
$ podman run --it --rm --entrypoint /opt/view/bin/obspectrophore   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/obspectrophore   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obsym
       
```bash
$ singularity exec <container> /opt/view/bin/obsym
$ podman run --it --rm --entrypoint /opt/view/bin/obsym   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/obsym   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obtautomer
       
```bash
$ singularity exec <container> /opt/view/bin/obtautomer
$ podman run --it --rm --entrypoint /opt/view/bin/obtautomer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/obtautomer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### obthermo
       
```bash
$ singularity exec <container> /opt/view/bin/obthermo
$ podman run --it --rm --entrypoint /opt/view/bin/obthermo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/obthermo   -v ${PWD} -w ${PWD} <container> -c " $@"
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