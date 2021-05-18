---
layout: container
name:  "ghcr.io/autamus/clhep"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/clhep/container.yaml"
updated_at: "2021-05-18 14:04:16.911498"
container_url: "https://github.com/orgs/autamus/packages/container/package/clhep"
aliases:
 - "Cast-config"

 - "Evaluator-config"

 - "Exceptions-config"

 - "GenericFunctions-config"

 - "Geometry-config"

 - "Matrix-config"

 - "Random-config"

 - "RandomObjects-config"

 - "RefCount-config"

 - "Units-config"

 - "Utility-config"

 - "Vector-config"

 - "clhep-config"

versions:
 - "2.4.4.0"
 - "latest"
description: "CLHEP is a C++ library that provides utility classes for general numerical programming, vector arithmetic, geometry, pseudorandom number generation, and linear algebra, specifically targeted for high energy physics simulation and analysis software."
---

This module is a singularity container wrapper for ghcr.io/autamus/clhep.
CLHEP is a C++ library that provides utility classes for general numerical programming, vector arithmetic, geometry, pseudorandom number generation, and linear algebra, specifically targeted for high energy physics simulation and analysis software.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install ghcr.io/autamus/clhep
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/clhep:2.4.4.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/clhep/2.4.4.0
$ module help ghcr.io/autamus/clhep/2.4.4.0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### ghcr.io-autamus-clhep-run:

```bash
$ singularity run <container>
```

#### ghcr.io-autamus-clhep-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### ghcr.io-autamus-clhep-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### ghcr.io-autamus-clhep-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ghcr.io-autamus-clhep-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Cast-config
       
```bash
$ singularity exec <container> /opt/view/bin/Cast-config
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


#### Random-config
       
```bash
$ singularity exec <container> /opt/view/bin/Random-config
```


#### RandomObjects-config
       
```bash
$ singularity exec <container> /opt/view/bin/RandomObjects-config
```


#### RefCount-config
       
```bash
$ singularity exec <container> /opt/view/bin/RefCount-config
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


#### clhep-config
       
```bash
$ singularity exec <container> /opt/view/bin/clhep-config
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