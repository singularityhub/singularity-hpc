---
layout: container
name:  "ghcr.io/autamus/geant4"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/geant4/container.yaml"
updated_at: "2021-04-20 02:22:48.699711"
container_url: ""
aliases:
 - "Cast-config"

 - "CreateDOMDocument"

 - "DOMCount"

 - "DOMPrint"

 - "EnumVal"

 - "Evaluator-config"

 - "Exceptions-config"

 - "GenericFunctions-config"

 - "Geometry-config"

 - "Matrix-config"

 - "MemParse"

 - "PParse"

 - "PSVIWriter"

 - "Random-config"

 - "RandomObjects-config"

 - "Redirect"

 - "RefCount-config"

 - "SAX2Count"

 - "SAX2Print"

 - "SAXCount"

 - "SAXPrint"

 - "SCMPrint"

 - "SEnumVal"

 - "StdInParse"

 - "Units-config"

 - "Utility-config"

 - "Vector-config"

 - "XInclude"

 - "geant4-config"

 - "geant4.csh"

 - "geant4.sh"

versions:
 - "latest"
description: "Geant4 is a platform for the simulation of the passage of particles through matter using Monte Carlo methods."
---

This module is a singularity container wrapper for ghcr.io/autamus/geant4.
Geant4 is a platform for the simulation of the passage of particles through matter using Monte Carlo methods.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install ghcr.io/autamus/geant4
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/geant4:latest
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/geant4/latest
$ module help ghcr.io/autamus/geant4/latest
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### ghcr.io-autamus-geant4-run:

```bash
$ singularity run <container>
```

#### ghcr.io-autamus-geant4-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### ghcr.io-autamus-geant4-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### ghcr.io-autamus-geant4-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ghcr.io-autamus-geant4-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Cast-config
       
```bash
$ singularity exec <container> /opt/view/bin/Cast-config
```


#### CreateDOMDocument
       
```bash
$ singularity exec <container> /opt/view/bin/CreateDOMDocument
```


#### DOMCount
       
```bash
$ singularity exec <container> /opt/view/bin/DOMCount
```


#### DOMPrint
       
```bash
$ singularity exec <container> /opt/view/bin/DOMPrint
```


#### EnumVal
       
```bash
$ singularity exec <container> /opt/view/bin/EnumVal
```


#### Evaluator-config
       
```bash
$ singularity exec <container> /opt/view/bin/Evaluator-config
```


#### Exceptions-config
       
```bash
$ singularity exec <container> /opt/view/bin/Exceptions-config
```


#### GenericFunctions-config
       
```bash
$ singularity exec <container> /opt/view/bin/GenericFunctions-config
```


#### Geometry-config
       
```bash
$ singularity exec <container> /opt/view/bin/Geometry-config
```


#### Matrix-config
       
```bash
$ singularity exec <container> /opt/view/bin/Matrix-config
```


#### MemParse
       
```bash
$ singularity exec <container> /opt/view/bin/MemParse
```


#### PParse
       
```bash
$ singularity exec <container> /opt/view/bin/PParse
```


#### PSVIWriter
       
```bash
$ singularity exec <container> /opt/view/bin/PSVIWriter
```


#### Random-config
       
```bash
$ singularity exec <container> /opt/view/bin/Random-config
```


#### RandomObjects-config
       
```bash
$ singularity exec <container> /opt/view/bin/RandomObjects-config
```


#### Redirect
       
```bash
$ singularity exec <container> /opt/view/bin/Redirect
```


#### RefCount-config
       
```bash
$ singularity exec <container> /opt/view/bin/RefCount-config
```


#### SAX2Count
       
```bash
$ singularity exec <container> /opt/view/bin/SAX2Count
```


#### SAX2Print
       
```bash
$ singularity exec <container> /opt/view/bin/SAX2Print
```


#### SAXCount
       
```bash
$ singularity exec <container> /opt/view/bin/SAXCount
```


#### SAXPrint
       
```bash
$ singularity exec <container> /opt/view/bin/SAXPrint
```


#### SCMPrint
       
```bash
$ singularity exec <container> /opt/view/bin/SCMPrint
```


#### SEnumVal
       
```bash
$ singularity exec <container> /opt/view/bin/SEnumVal
```


#### StdInParse
       
```bash
$ singularity exec <container> /opt/view/bin/StdInParse
```


#### Units-config
       
```bash
$ singularity exec <container> /opt/view/bin/Units-config
```


#### Utility-config
       
```bash
$ singularity exec <container> /opt/view/bin/Utility-config
```


#### Vector-config
       
```bash
$ singularity exec <container> /opt/view/bin/Vector-config
```


#### XInclude
       
```bash
$ singularity exec <container> /opt/view/bin/XInclude
```


#### geant4-config
       
```bash
$ singularity exec <container> /opt/view/bin/geant4-config
```


#### geant4.csh
       
```bash
$ singularity exec <container> /opt/view/bin/geant4.csh
```


#### geant4.sh
       
```bash
$ singularity exec <container> /opt/view/bin/geant4.sh
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