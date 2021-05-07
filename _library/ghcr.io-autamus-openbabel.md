---
layout: container
name:  "ghcr.io/autamus/openbabel"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/openbabel/container.yaml"
updated_at: "2021-05-07 08:59:03.262485"
container_url: ""
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

When you install this module, you'll be able to load it to make the following commands accessible:

#### ghcr.io-autamus-openbabel-run:

```bash
$ singularity run <container>
```

#### ghcr.io-autamus-openbabel-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### ghcr.io-autamus-openbabel-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### ghcr.io-autamus-openbabel-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ghcr.io-autamus-openbabel-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### obabel
       
```bash
$ singularity exec <container> /opt/view/bin/obabel
```


#### obconformer
       
```bash
$ singularity exec <container> /opt/view/bin/obconformer
```


#### obdistgen
       
```bash
$ singularity exec <container> /opt/view/bin/obdistgen
```


#### obenergy
       
```bash
$ singularity exec <container> /opt/view/bin/obenergy
```


#### obfit
       
```bash
$ singularity exec <container> /opt/view/bin/obfit
```


#### obfitall
       
```bash
$ singularity exec <container> /opt/view/bin/obfitall
```


#### obgen
       
```bash
$ singularity exec <container> /opt/view/bin/obgen
```


#### obgrep
       
```bash
$ singularity exec <container> /opt/view/bin/obgrep
```


#### obminimize
       
```bash
$ singularity exec <container> /opt/view/bin/obminimize
```


#### obmm
       
```bash
$ singularity exec <container> /opt/view/bin/obmm
```


#### obprobe
       
```bash
$ singularity exec <container> /opt/view/bin/obprobe
```


#### obprop
       
```bash
$ singularity exec <container> /opt/view/bin/obprop
```


#### obrms
       
```bash
$ singularity exec <container> /opt/view/bin/obrms
```


#### obrotamer
       
```bash
$ singularity exec <container> /opt/view/bin/obrotamer
```


#### obrotate
       
```bash
$ singularity exec <container> /opt/view/bin/obrotate
```


#### obspectrophore
       
```bash
$ singularity exec <container> /opt/view/bin/obspectrophore
```


#### obsym
       
```bash
$ singularity exec <container> /opt/view/bin/obsym
```


#### obtautomer
       
```bash
$ singularity exec <container> /opt/view/bin/obtautomer
```


#### obthermo
       
```bash
$ singularity exec <container> /opt/view/bin/obthermo
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