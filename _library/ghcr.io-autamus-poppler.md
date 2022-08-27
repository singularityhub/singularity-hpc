---
layout: container
name:  "ghcr.io/autamus/poppler"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/poppler/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/ghcr.io/autamus/poppler/container.yaml"
updated_at: "2022-08-27 02:53:11.362529"
latest: "21.11.0"
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
 - "21.07.0"
 - "21.08.0"
 - "21.10.0"
 - "21.11.0"
 - "latest"
 - "21.09.0"
description: "Poppler is a free software utility library for rendering Portable Document Format (PDF) documents."
config: {"docker": "ghcr.io/autamus/poppler", "url": "https://github.com/orgs/autamus/packages/container/package/poppler", "maintainer": "@vsoch", "description": "Poppler is a free software utility library for rendering Portable Document Format (PDF) documents.", "latest": {"21.11.0": "sha256:fc8e899c6b81f8ed02b0adf09eda55b724c5575f03e06c3dca107399be7a0bd1"}, "tags": {"0.90.1": "sha256:972979693c1d915c879f9c2a6d23f566d3727f5a3a909355915a003b1abd3504", "21.07.0": "sha256:a119cd1f5da78fcda917793990b4ce1915891df317cf6bb261013278a1c239b7", "21.08.0": "sha256:d6b967aca449063448f0bd6fc5f0f31c429fd6ac797dd9fdf0937254216ece18", "21.10.0": "sha256:c6b76b31a5566664896e1d055df8a186eee31c8a6ce3e168303367b8e12b2c3e", "21.11.0": "sha256:fc8e899c6b81f8ed02b0adf09eda55b724c5575f03e06c3dca107399be7a0bd1", "latest": "sha256:fc8e899c6b81f8ed02b0adf09eda55b724c5575f03e06c3dca107399be7a0bd1", "21.09.0": "sha256:3a85adb7afb5a060e9eeaf35eeb5a648b8e682c953d2f7e1db5d9fa7c906b903"}, "aliases": {"pdfattach": "/opt/view/bin/pdfattach", "pdfdetach": "/opt/view/bin/pdfdetach", "pdffonts": "/opt/view/bin/pdffonts", "pdfimages": "/opt/view/bin/pdfimages", "pdfinfo": "/opt/view/bin/pdfinfo", "pdfseparate": "/opt/view/bin/pdfseparate", "pdftohtml": "/opt/view/bin/pdftohtml", "pdftops": "/opt/view/bin/pdftops", "pdftotext": "/opt/view/bin/pdftotext", "pdfunite": "/opt/view/bin/pdfunite", "png-fix-itxt": "/opt/view/bin/png-fix-itxt", "pngfix": "/opt/view/bin/pngfix"}}
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

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### poppler-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### poppler-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### poppler-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### poppler-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### poppler-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### poppler-inspect-deffile:

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