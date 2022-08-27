---
layout: container
name:  "ghcr.io/autamus/gdal"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/gdal/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/ghcr.io/autamus/gdal/container.yaml"
updated_at: "2022-08-27 02:52:22.476800"
latest: "3.4.1"
container_url: "https://github.com/orgs/autamus/packages/container/package/gdal"
aliases:
 - "gdal-config"
 - "gdal_contour"
 - "gdal_create"
 - "gdal_grid"
 - "gdal_rasterize"
 - "gdal_translate"
 - "gdal_viewshed"
 - "gdaladdo"
 - "gdalbuildvrt"
 - "gdaldem"
 - "gdalenhance"
 - "gdalinfo"
 - "gdallocationinfo"
 - "gdalmanage"
 - "gdalmdiminfo"
 - "gdalmdimtranslate"
 - "gdalsrsinfo"
 - "gdaltindex"
 - "gdaltransform"
 - "gdalwarp"
versions:
 - "3.3.0"
 - "3.3.1"
 - "3.3.3"
 - "3.4.0"
 - "3.4.1"
 - "latest"
description: "GDAL is a translator library for raster and vector geospatial data formats that is released under an X/MIT style Open Source License by the Open Source Geospatial Foundation. "
config: {"docker": "ghcr.io/autamus/gdal", "url": "https://github.com/orgs/autamus/packages/container/package/gdal", "maintainer": "@vsoch", "description": "GDAL is a translator library for raster and vector geospatial data formats that is released under an X/MIT style Open Source License by the Open Source Geospatial Foundation. ", "latest": {"3.4.1": "sha256:457c38a20f0e219741a47d5bafac37e34134b303129040f771cae6ad9ca99163"}, "tags": {"3.3.0": "sha256:6a82c83a2970ccea4cc28f9bb5c356f36ba26bde14c485437413724bfad28a8a", "3.3.1": "sha256:58d19784ff309c2314928bdfae5243d57a746339e82c2b99b18eafe0d75697bf", "3.3.3": "sha256:1a7c2b70d6d930929c283d1d62ddae1a0f37f87630160833269af6bfb6473eee", "3.4.0": "sha256:bfe8bdf52ddeb00b3584b1a6353e2d94e6dcd0b7c76766c6162bb5d7a7ccb8be", "3.4.1": "sha256:457c38a20f0e219741a47d5bafac37e34134b303129040f771cae6ad9ca99163", "latest": "sha256:457c38a20f0e219741a47d5bafac37e34134b303129040f771cae6ad9ca99163"}, "aliases": {"gdal-config": "/opt/view/bin/gdal-config", "gdal_contour": "/opt/view/bin/gdal_contour", "gdal_create": "/opt/view/bin/gdal_create", "gdal_grid": "/opt/view/bin/gdal_grid", "gdal_rasterize": "/opt/view/bin/gdal_rasterize", "gdal_translate": "/opt/view/bin/gdal_translate", "gdal_viewshed": "/opt/view/bin/gdal_viewshed", "gdaladdo": "/opt/view/bin/gdaladdo", "gdalbuildvrt": "/opt/view/bin/gdalbuildvrt", "gdaldem": "/opt/view/bin/gdaldem", "gdalenhance": "/opt/view/bin/gdalenhance", "gdalinfo": "/opt/view/bin/gdalinfo", "gdallocationinfo": "/opt/view/bin/gdallocationinfo", "gdalmanage": "/opt/view/bin/gdalmanage", "gdalmdiminfo": "/opt/view/bin/gdalmdiminfo", "gdalmdimtranslate": "/opt/view/bin/gdalmdimtranslate", "gdalsrsinfo": "/opt/view/bin/gdalsrsinfo", "gdaltindex": "/opt/view/bin/gdaltindex", "gdaltransform": "/opt/view/bin/gdaltransform", "gdalwarp": "/opt/view/bin/gdalwarp"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/gdal.
GDAL is a translator library for raster and vector geospatial data formats that is released under an X/MIT style Open Source License by the Open Source Geospatial Foundation. 
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/gdal
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/gdal:3.3.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/gdal/3.3.0
$ module help ghcr.io/autamus/gdal/3.3.0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gdal-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gdal-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gdal-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gdal-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gdal-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gdal-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gdal-config
       
```bash
$ singularity exec <container> /opt/view/bin/gdal-config
$ podman run --it --rm --entrypoint /opt/view/bin/gdal-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/gdal-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdal_contour
       
```bash
$ singularity exec <container> /opt/view/bin/gdal_contour
$ podman run --it --rm --entrypoint /opt/view/bin/gdal_contour   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/gdal_contour   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdal_create
       
```bash
$ singularity exec <container> /opt/view/bin/gdal_create
$ podman run --it --rm --entrypoint /opt/view/bin/gdal_create   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/gdal_create   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdal_grid
       
```bash
$ singularity exec <container> /opt/view/bin/gdal_grid
$ podman run --it --rm --entrypoint /opt/view/bin/gdal_grid   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/gdal_grid   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdal_rasterize
       
```bash
$ singularity exec <container> /opt/view/bin/gdal_rasterize
$ podman run --it --rm --entrypoint /opt/view/bin/gdal_rasterize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/gdal_rasterize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdal_translate
       
```bash
$ singularity exec <container> /opt/view/bin/gdal_translate
$ podman run --it --rm --entrypoint /opt/view/bin/gdal_translate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/gdal_translate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdal_viewshed
       
```bash
$ singularity exec <container> /opt/view/bin/gdal_viewshed
$ podman run --it --rm --entrypoint /opt/view/bin/gdal_viewshed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/gdal_viewshed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdaladdo
       
```bash
$ singularity exec <container> /opt/view/bin/gdaladdo
$ podman run --it --rm --entrypoint /opt/view/bin/gdaladdo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/gdaladdo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdalbuildvrt
       
```bash
$ singularity exec <container> /opt/view/bin/gdalbuildvrt
$ podman run --it --rm --entrypoint /opt/view/bin/gdalbuildvrt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/gdalbuildvrt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdaldem
       
```bash
$ singularity exec <container> /opt/view/bin/gdaldem
$ podman run --it --rm --entrypoint /opt/view/bin/gdaldem   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/gdaldem   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdalenhance
       
```bash
$ singularity exec <container> /opt/view/bin/gdalenhance
$ podman run --it --rm --entrypoint /opt/view/bin/gdalenhance   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/gdalenhance   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdalinfo
       
```bash
$ singularity exec <container> /opt/view/bin/gdalinfo
$ podman run --it --rm --entrypoint /opt/view/bin/gdalinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/gdalinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdallocationinfo
       
```bash
$ singularity exec <container> /opt/view/bin/gdallocationinfo
$ podman run --it --rm --entrypoint /opt/view/bin/gdallocationinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/gdallocationinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdalmanage
       
```bash
$ singularity exec <container> /opt/view/bin/gdalmanage
$ podman run --it --rm --entrypoint /opt/view/bin/gdalmanage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/gdalmanage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdalmdiminfo
       
```bash
$ singularity exec <container> /opt/view/bin/gdalmdiminfo
$ podman run --it --rm --entrypoint /opt/view/bin/gdalmdiminfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/gdalmdiminfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdalmdimtranslate
       
```bash
$ singularity exec <container> /opt/view/bin/gdalmdimtranslate
$ podman run --it --rm --entrypoint /opt/view/bin/gdalmdimtranslate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/gdalmdimtranslate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdalsrsinfo
       
```bash
$ singularity exec <container> /opt/view/bin/gdalsrsinfo
$ podman run --it --rm --entrypoint /opt/view/bin/gdalsrsinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/gdalsrsinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdaltindex
       
```bash
$ singularity exec <container> /opt/view/bin/gdaltindex
$ podman run --it --rm --entrypoint /opt/view/bin/gdaltindex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/gdaltindex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdaltransform
       
```bash
$ singularity exec <container> /opt/view/bin/gdaltransform
$ podman run --it --rm --entrypoint /opt/view/bin/gdaltransform   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/gdaltransform   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdalwarp
       
```bash
$ singularity exec <container> /opt/view/bin/gdalwarp
$ podman run --it --rm --entrypoint /opt/view/bin/gdalwarp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/gdalwarp   -v ${PWD} -w ${PWD} <container> -c " $@"
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