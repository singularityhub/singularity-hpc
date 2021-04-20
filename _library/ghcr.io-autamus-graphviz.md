---
layout: container
name:  "ghcr.io/autamus/graphviz"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/graphviz/container.yaml"
updated_at: "2021-04-20 03:15:06.054616"
container_url: ""
aliases:
 - "gc"

 - "gml2gv"

 - "graphml2gv"

 - "gv2gml"

 - "gv2gxl"

 - "gvcolor"

 - "gvgen"

 - "gvmap"

 - "gvmap.sh"

 - "gvpack"

 - "gvpr"

 - "gxl2dot"

 - "gxl2gv"

versions:
 - "latest"
description: "Graphviz is open source graph visualization software."
---

This module is a singularity container wrapper for ghcr.io/autamus/graphviz.
Graphviz is open source graph visualization software.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install ghcr.io/autamus/graphviz
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/graphviz:latest
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/graphviz/latest
$ module help ghcr.io/autamus/graphviz/latest
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### ghcr.io-autamus-graphviz-run:

```bash
$ singularity run <container>
```

#### ghcr.io-autamus-graphviz-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### ghcr.io-autamus-graphviz-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### ghcr.io-autamus-graphviz-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ghcr.io-autamus-graphviz-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gc
       
```bash
$ singularity exec <container> /opt/view/bin/gc
```


#### gml2gv
       
```bash
$ singularity exec <container> /opt/view/bin/gml2gv
```


#### graphml2gv
       
```bash
$ singularity exec <container> /opt/view/bin/graphml2gv
```


#### gv2gml
       
```bash
$ singularity exec <container> /opt/view/bin/gv2gml
```


#### gv2gxl
       
```bash
$ singularity exec <container> /opt/view/bin/gv2gxl
```


#### gvcolor
       
```bash
$ singularity exec <container> /opt/view/bin/gvcolor
```


#### gvgen
       
```bash
$ singularity exec <container> /opt/view/bin/gvgen
```


#### gvmap
       
```bash
$ singularity exec <container> /opt/view/bin/gvmap
```


#### gvmap.sh
       
```bash
$ singularity exec <container> /opt/view/bin/gvmap.sh
```


#### gvpack
       
```bash
$ singularity exec <container> /opt/view/bin/gvpack
```


#### gvpr
       
```bash
$ singularity exec <container> /opt/view/bin/gvpr
```


#### gxl2dot
       
```bash
$ singularity exec <container> /opt/view/bin/gxl2dot
```


#### gxl2gv
       
```bash
$ singularity exec <container> /opt/view/bin/gxl2gv
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