---
layout: container
name:  "ghcr.io/autamus/geant4"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/geant4/container.yaml"
updated_at: "2021-06-06 20:44:11.623485"
container_url: "https://github.com/orgs/autamus/packages/container/package/geant4"
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
 - "10.7.1"
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
$ shpc install ghcr.io/autamus/geant4:10.7.1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/geant4/10.7.1
$ module help ghcr.io/autamus/geant4/10.7.1
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


#### Cast-config
       
```bash
$ singularity exec <container> /opt/view/bin/Cast-config
$ podman run --it --rm --entrypoint /opt/view/bin/Cast-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/Cast-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CreateDOMDocument
       
```bash
$ singularity exec <container> /opt/view/bin/CreateDOMDocument
$ podman run --it --rm --entrypoint /opt/view/bin/CreateDOMDocument   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/CreateDOMDocument   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### DOMCount
       
```bash
$ singularity exec <container> /opt/view/bin/DOMCount
$ podman run --it --rm --entrypoint /opt/view/bin/DOMCount   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/DOMCount   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### DOMPrint
       
```bash
$ singularity exec <container> /opt/view/bin/DOMPrint
$ podman run --it --rm --entrypoint /opt/view/bin/DOMPrint   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/DOMPrint   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### EnumVal
       
```bash
$ singularity exec <container> /opt/view/bin/EnumVal
$ podman run --it --rm --entrypoint /opt/view/bin/EnumVal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/EnumVal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Evaluator-config
       
```bash
$ singularity exec <container> /opt/view/bin/Evaluator-config
$ podman run --it --rm --entrypoint /opt/view/bin/Evaluator-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/Evaluator-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Exceptions-config
       
```bash
$ singularity exec <container> /opt/view/bin/Exceptions-config
$ podman run --it --rm --entrypoint /opt/view/bin/Exceptions-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/Exceptions-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### GenericFunctions-config
       
```bash
$ singularity exec <container> /opt/view/bin/GenericFunctions-config
$ podman run --it --rm --entrypoint /opt/view/bin/GenericFunctions-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/GenericFunctions-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Geometry-config
       
```bash
$ singularity exec <container> /opt/view/bin/Geometry-config
$ podman run --it --rm --entrypoint /opt/view/bin/Geometry-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/Geometry-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Matrix-config
       
```bash
$ singularity exec <container> /opt/view/bin/Matrix-config
$ podman run --it --rm --entrypoint /opt/view/bin/Matrix-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/Matrix-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### MemParse
       
```bash
$ singularity exec <container> /opt/view/bin/MemParse
$ podman run --it --rm --entrypoint /opt/view/bin/MemParse   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/MemParse   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PParse
       
```bash
$ singularity exec <container> /opt/view/bin/PParse
$ podman run --it --rm --entrypoint /opt/view/bin/PParse   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/PParse   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PSVIWriter
       
```bash
$ singularity exec <container> /opt/view/bin/PSVIWriter
$ podman run --it --rm --entrypoint /opt/view/bin/PSVIWriter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/PSVIWriter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Random-config
       
```bash
$ singularity exec <container> /opt/view/bin/Random-config
$ podman run --it --rm --entrypoint /opt/view/bin/Random-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/Random-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RandomObjects-config
       
```bash
$ singularity exec <container> /opt/view/bin/RandomObjects-config
$ podman run --it --rm --entrypoint /opt/view/bin/RandomObjects-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/RandomObjects-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Redirect
       
```bash
$ singularity exec <container> /opt/view/bin/Redirect
$ podman run --it --rm --entrypoint /opt/view/bin/Redirect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/Redirect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RefCount-config
       
```bash
$ singularity exec <container> /opt/view/bin/RefCount-config
$ podman run --it --rm --entrypoint /opt/view/bin/RefCount-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/RefCount-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SAX2Count
       
```bash
$ singularity exec <container> /opt/view/bin/SAX2Count
$ podman run --it --rm --entrypoint /opt/view/bin/SAX2Count   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/SAX2Count   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SAX2Print
       
```bash
$ singularity exec <container> /opt/view/bin/SAX2Print
$ podman run --it --rm --entrypoint /opt/view/bin/SAX2Print   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/SAX2Print   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SAXCount
       
```bash
$ singularity exec <container> /opt/view/bin/SAXCount
$ podman run --it --rm --entrypoint /opt/view/bin/SAXCount   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/SAXCount   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SAXPrint
       
```bash
$ singularity exec <container> /opt/view/bin/SAXPrint
$ podman run --it --rm --entrypoint /opt/view/bin/SAXPrint   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/SAXPrint   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SCMPrint
       
```bash
$ singularity exec <container> /opt/view/bin/SCMPrint
$ podman run --it --rm --entrypoint /opt/view/bin/SCMPrint   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/SCMPrint   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SEnumVal
       
```bash
$ singularity exec <container> /opt/view/bin/SEnumVal
$ podman run --it --rm --entrypoint /opt/view/bin/SEnumVal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/SEnumVal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### StdInParse
       
```bash
$ singularity exec <container> /opt/view/bin/StdInParse
$ podman run --it --rm --entrypoint /opt/view/bin/StdInParse   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/StdInParse   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Units-config
       
```bash
$ singularity exec <container> /opt/view/bin/Units-config
$ podman run --it --rm --entrypoint /opt/view/bin/Units-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/Units-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Utility-config
       
```bash
$ singularity exec <container> /opt/view/bin/Utility-config
$ podman run --it --rm --entrypoint /opt/view/bin/Utility-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/Utility-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Vector-config
       
```bash
$ singularity exec <container> /opt/view/bin/Vector-config
$ podman run --it --rm --entrypoint /opt/view/bin/Vector-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/Vector-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### XInclude
       
```bash
$ singularity exec <container> /opt/view/bin/XInclude
$ podman run --it --rm --entrypoint /opt/view/bin/XInclude   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/XInclude   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### geant4-config
       
```bash
$ singularity exec <container> /opt/view/bin/geant4-config
$ podman run --it --rm --entrypoint /opt/view/bin/geant4-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/geant4-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### geant4.csh
       
```bash
$ singularity exec <container> /opt/view/bin/geant4.csh
$ podman run --it --rm --entrypoint /opt/view/bin/geant4.csh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/geant4.csh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### geant4.sh
       
```bash
$ singularity exec <container> /opt/view/bin/geant4.sh
$ podman run --it --rm --entrypoint /opt/view/bin/geant4.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/geant4.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
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