---
layout: container
name:  "ghcr.io/autamus/poppler"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/poppler/container.yaml"
updated_at: "2021-06-22 03:45:40.253567"
container_url: "https://github.com/orgs/autamus/packages/container/package/poppler"
aliases:
 - "pdfattach"

 - "pdfdetach"

 - "pdffonts"

 - "pdfimages"

 - "pdfinfo"

 - "pdfseparate"

 - "pdftohtml"

 - "pdftops"

 - "pdftotext"

 - "pdfunite"

 - "png-fix-itxt"

 - "pngfix"

versions:
 - "0.90.1"
 - "latest"
description: "Poppler is a free software utility library for rendering Portable Document Format (PDF) documents."
---

This module is a singularity container wrapper for ghcr.io/autamus/poppler.
Poppler is a free software utility library for rendering Portable Document Format (PDF) documents.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install ghcr.io/autamus/poppler
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/poppler:0.90.1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/poppler/0.90.1
$ module help ghcr.io/autamus/poppler/0.90.1
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


#### pdfattach
       
```bash
$ singularity exec <container> /opt/view/bin/pdfattach
$ podman run --it --rm --entrypoint /opt/view/bin/pdfattach   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/pdfattach   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pdfdetach
       
```bash
$ singularity exec <container> /opt/view/bin/pdfdetach
$ podman run --it --rm --entrypoint /opt/view/bin/pdfdetach   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/pdfdetach   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pdffonts
       
```bash
$ singularity exec <container> /opt/view/bin/pdffonts
$ podman run --it --rm --entrypoint /opt/view/bin/pdffonts   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/pdffonts   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pdfimages
       
```bash
$ singularity exec <container> /opt/view/bin/pdfimages
$ podman run --it --rm --entrypoint /opt/view/bin/pdfimages   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/pdfimages   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pdfinfo
       
```bash
$ singularity exec <container> /opt/view/bin/pdfinfo
$ podman run --it --rm --entrypoint /opt/view/bin/pdfinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/pdfinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pdfseparate
       
```bash
$ singularity exec <container> /opt/view/bin/pdfseparate
$ podman run --it --rm --entrypoint /opt/view/bin/pdfseparate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/pdfseparate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pdftohtml
       
```bash
$ singularity exec <container> /opt/view/bin/pdftohtml
$ podman run --it --rm --entrypoint /opt/view/bin/pdftohtml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/pdftohtml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pdftops
       
```bash
$ singularity exec <container> /opt/view/bin/pdftops
$ podman run --it --rm --entrypoint /opt/view/bin/pdftops   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/pdftops   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pdftotext
       
```bash
$ singularity exec <container> /opt/view/bin/pdftotext
$ podman run --it --rm --entrypoint /opt/view/bin/pdftotext   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/pdftotext   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pdfunite
       
```bash
$ singularity exec <container> /opt/view/bin/pdfunite
$ podman run --it --rm --entrypoint /opt/view/bin/pdfunite   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/pdfunite   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### png-fix-itxt
       
```bash
$ singularity exec <container> /opt/view/bin/png-fix-itxt
$ podman run --it --rm --entrypoint /opt/view/bin/png-fix-itxt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/png-fix-itxt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pngfix
       
```bash
$ singularity exec <container> /opt/view/bin/pngfix
$ podman run --it --rm --entrypoint /opt/view/bin/pngfix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/pngfix   -v ${PWD} -w ${PWD} <container> -c " $@"
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