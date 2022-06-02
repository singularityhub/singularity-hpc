---
layout: container
name:  "biocontainers/emboss"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/biocontainers/emboss/container.yaml"
updated_at: "2022-06-02 03:40:06.011201"
container_url: "https://hub.docker.com/r/biocontainers/emboss"
aliases:
 - "embossdata"

 - "embossupdate"

 - "embossversion"

 - "emma"

 - "emowse"

 - "em_pscan"

 - "em_cons"

versions:
 - "v6.6.0dfsg-7b1-deb_cv1"
description: "Free Open Source software analysis package which covers several molecular biology tools."
---

This module is a singularity container wrapper for biocontainers/emboss.
Free Open Source software analysis package which covers several molecular biology tools.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install biocontainers/emboss
```

Or a specific version:

```bash
$ shpc install biocontainers/emboss:v6.6.0dfsg-7b1-deb_cv1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load biocontainers/emboss/v6.6.0dfsg-7b1-deb_cv1
$ module help biocontainers/emboss/v6.6.0dfsg-7b1-deb_cv1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### emboss-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### emboss-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### emboss-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### emboss-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### emboss-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### emboss-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### embossdata
       
```bash
$ singularity exec <container> /usr/bin/embossdata
$ podman run --it --rm --entrypoint /usr/bin/embossdata   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/embossdata   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### embossupdate
       
```bash
$ singularity exec <container> /usr/bin/embossupdate
$ podman run --it --rm --entrypoint /usr/bin/embossupdate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/embossupdate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### embossversion
       
```bash
$ singularity exec <container> /usr/bin/embossversion
$ podman run --it --rm --entrypoint /usr/bin/embossversion   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/embossversion   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### emma
       
```bash
$ singularity exec <container> /usr/bin/emma
$ podman run --it --rm --entrypoint /usr/bin/emma   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/emma   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### emowse
       
```bash
$ singularity exec <container> /usr/bin/emouse
$ podman run --it --rm --entrypoint /usr/bin/emouse   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/emouse   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### em_pscan
       
```bash
$ singularity exec <container> /usr/bin/em_pscan
$ podman run --it --rm --entrypoint /usr/bin/em_pscan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/em_pscan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### em_cons
       
```bash
$ singularity exec <container> /usr/bin/em_cons
$ podman run --it --rm --entrypoint /usr/bin/em_cons   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/em_cons   -v ${PWD} -w ${PWD} <container> -c " $@"
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