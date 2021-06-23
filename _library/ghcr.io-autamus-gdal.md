---
layout: container
name:  "ghcr.io/autamus/gdal"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/gdal/container.yaml"
updated_at: "2021-06-23 01:49:32.101176"
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
 - "latest"
description: "GDAL is a translator library for raster and vector geospatial data formats that is released under an X/MIT style Open Source License by the Open Source Geospatial Foundation. "
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