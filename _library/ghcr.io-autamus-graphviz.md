---
layout: container
name:  "ghcr.io/autamus/graphviz"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/graphviz/container.yaml"
updated_at: "2022-08-01 18:20:17.891913"
container_url: "https://github.com/orgs/autamus/packages/container/package/graphviz"
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
 - "2.47.1"
 - "2.47.2"
 - "2.47.3"
 - "2.49.0"
 - "2.49.3"
 - "latest"
 - "2.49.2"
 - "2.48.0"
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
$ shpc install ghcr.io/autamus/graphviz:2.47.1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/graphviz/2.47.1
$ module help ghcr.io/autamus/graphviz/2.47.1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### graphviz-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### graphviz-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### graphviz-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### graphviz-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### graphviz-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### graphviz-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gc
       
```bash
$ singularity exec <container> /opt/view/bin/gc
$ podman run --it --rm --entrypoint /opt/view/bin/gc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/gc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gml2gv
       
```bash
$ singularity exec <container> /opt/view/bin/gml2gv
$ podman run --it --rm --entrypoint /opt/view/bin/gml2gv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/gml2gv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### graphml2gv
       
```bash
$ singularity exec <container> /opt/view/bin/graphml2gv
$ podman run --it --rm --entrypoint /opt/view/bin/graphml2gv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/graphml2gv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gv2gml
       
```bash
$ singularity exec <container> /opt/view/bin/gv2gml
$ podman run --it --rm --entrypoint /opt/view/bin/gv2gml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/gv2gml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gv2gxl
       
```bash
$ singularity exec <container> /opt/view/bin/gv2gxl
$ podman run --it --rm --entrypoint /opt/view/bin/gv2gxl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/gv2gxl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gvcolor
       
```bash
$ singularity exec <container> /opt/view/bin/gvcolor
$ podman run --it --rm --entrypoint /opt/view/bin/gvcolor   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/gvcolor   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gvgen
       
```bash
$ singularity exec <container> /opt/view/bin/gvgen
$ podman run --it --rm --entrypoint /opt/view/bin/gvgen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/gvgen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gvmap
       
```bash
$ singularity exec <container> /opt/view/bin/gvmap
$ podman run --it --rm --entrypoint /opt/view/bin/gvmap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/gvmap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gvmap.sh
       
```bash
$ singularity exec <container> /opt/view/bin/gvmap.sh
$ podman run --it --rm --entrypoint /opt/view/bin/gvmap.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/gvmap.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gvpack
       
```bash
$ singularity exec <container> /opt/view/bin/gvpack
$ podman run --it --rm --entrypoint /opt/view/bin/gvpack   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/gvpack   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gvpr
       
```bash
$ singularity exec <container> /opt/view/bin/gvpr
$ podman run --it --rm --entrypoint /opt/view/bin/gvpr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/gvpr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gxl2dot
       
```bash
$ singularity exec <container> /opt/view/bin/gxl2dot
$ podman run --it --rm --entrypoint /opt/view/bin/gxl2dot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/gxl2dot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gxl2gv
       
```bash
$ singularity exec <container> /opt/view/bin/gxl2gv
$ podman run --it --rm --entrypoint /opt/view/bin/gxl2gv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/gxl2gv   -v ${PWD} -w ${PWD} <container> -c " $@"
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