---
layout: container
name:  "ghcr.io/autamus/gdal"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/gdal/container.yaml"
updated_at: "2021-04-20 02:48:44.401371"
container_url: ""
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
$ shpc install ghcr.io/autamus/gdal:latest
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/gdal/latest
$ module help ghcr.io/autamus/gdal/latest
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### ghcr.io-autamus-gdal-run:

```bash
$ singularity run <container>
```

#### ghcr.io-autamus-gdal-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### ghcr.io-autamus-gdal-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### ghcr.io-autamus-gdal-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ghcr.io-autamus-gdal-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gdal-config
       
```bash
$ singularity exec <container> /opt/view/bin/gdal-config
```


#### gdal_contour
       
```bash
$ singularity exec <container> /opt/view/bin/gdal_contour
```


#### gdal_create
       
```bash
$ singularity exec <container> /opt/view/bin/gdal_create
```


#### gdal_grid
       
```bash
$ singularity exec <container> /opt/view/bin/gdal_grid
```


#### gdal_rasterize
       
```bash
$ singularity exec <container> /opt/view/bin/gdal_rasterize
```


#### gdal_translate
       
```bash
$ singularity exec <container> /opt/view/bin/gdal_translate
```


#### gdal_viewshed
       
```bash
$ singularity exec <container> /opt/view/bin/gdal_viewshed
```


#### gdaladdo
       
```bash
$ singularity exec <container> /opt/view/bin/gdaladdo
```


#### gdalbuildvrt
       
```bash
$ singularity exec <container> /opt/view/bin/gdalbuildvrt
```


#### gdaldem
       
```bash
$ singularity exec <container> /opt/view/bin/gdaldem
```


#### gdalenhance
       
```bash
$ singularity exec <container> /opt/view/bin/gdalenhance
```


#### gdalinfo
       
```bash
$ singularity exec <container> /opt/view/bin/gdalinfo
```


#### gdallocationinfo
       
```bash
$ singularity exec <container> /opt/view/bin/gdallocationinfo
```


#### gdalmanage
       
```bash
$ singularity exec <container> /opt/view/bin/gdalmanage
```


#### gdalmdiminfo
       
```bash
$ singularity exec <container> /opt/view/bin/gdalmdiminfo
```


#### gdalmdimtranslate
       
```bash
$ singularity exec <container> /opt/view/bin/gdalmdimtranslate
```


#### gdalsrsinfo
       
```bash
$ singularity exec <container> /opt/view/bin/gdalsrsinfo
```


#### gdaltindex
       
```bash
$ singularity exec <container> /opt/view/bin/gdaltindex
```


#### gdaltransform
       
```bash
$ singularity exec <container> /opt/view/bin/gdaltransform
```


#### gdalwarp
       
```bash
$ singularity exec <container> /opt/view/bin/gdalwarp
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