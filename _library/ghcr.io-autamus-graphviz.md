---
layout: container
name:  "ghcr.io/autamus/graphviz"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/graphviz/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/ghcr.io/autamus/graphviz/container.yaml"
updated_at: "2022-08-27 02:52:28.476972"
latest: "2.49.3"
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
config: {"docker": "ghcr.io/autamus/graphviz", "url": "https://github.com/orgs/autamus/packages/container/package/graphviz", "maintainer": "@vsoch", "description": "Graphviz is open source graph visualization software.", "latest": {"2.49.3": "sha256:9f201c64a3e1290b429a15bd18670a7da0133e3eca8a56f2793f153bfd036ba9"}, "tags": {"2.47.1": "sha256:a9ec69fd28145200959c397ea8712bdab28184cc36859a5588391c6fa35940b9", "2.47.2": "sha256:68e91383955d89014501b70522a5d7a5f3d8abd9e43c6bb33b2f6bb0b0076118", "2.47.3": "sha256:c7156c353904ff244535472315d0e14b3b15f5fd9f4ee646d42be677f73308f1", "2.49.0": "sha256:ec1ca7f59ced4325267b8a8834a63ac114724b9b61de2004857e53fb6267e7e6", "2.49.3": "sha256:9f201c64a3e1290b429a15bd18670a7da0133e3eca8a56f2793f153bfd036ba9", "latest": "sha256:9f201c64a3e1290b429a15bd18670a7da0133e3eca8a56f2793f153bfd036ba9", "2.49.2": "sha256:6cd5099df746975bdcdc722daa01cf80d2e2c40c93cd77246d866e325edc8a7e", "2.48.0": "sha256:71ac73e010dd7395bf9260437de6bf9b4fa0f4ea3447049d5fa8e3c21dc36729"}, "aliases": {"gc": "/opt/view/bin/gc", "gml2gv": "/opt/view/bin/gml2gv", "graphml2gv": "/opt/view/bin/graphml2gv", "gv2gml": "/opt/view/bin/gv2gml", "gv2gxl": "/opt/view/bin/gv2gxl", "gvcolor": "/opt/view/bin/gvcolor", "gvgen": "/opt/view/bin/gvgen", "gvmap": "/opt/view/bin/gvmap", "gvmap.sh": "/opt/view/bin/gvmap.sh", "gvpack": "/opt/view/bin/gvpack", "gvpr": "/opt/view/bin/gvpr", "gxl2dot": "/opt/view/bin/gxl2dot", "gxl2gv": "/opt/view/bin/gxl2gv"}}
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