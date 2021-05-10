---
layout: container
name:  "biocontainers/emboss"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/biocontainers/emboss/container.yaml"
updated_at: "2021-05-10 15:19:42.621605"
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

When you install this module, you'll be able to load it to make the following commands accessible:

#### biocontainers-emboss-run:

```bash
$ singularity run <container>
```

#### biocontainers-emboss-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### biocontainers-emboss-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### biocontainers-emboss-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### biocontainers-emboss-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### embossdata
       
```bash
$ singularity exec <container> /usr/bin/embossdata
```


#### embossupdate
       
```bash
$ singularity exec <container> /usr/bin/embossupdate
```


#### embossversion
       
```bash
$ singularity exec <container> /usr/bin/embossversion
```


#### emma
       
```bash
$ singularity exec <container> /usr/bin/emma
```


#### emowse
       
```bash
$ singularity exec <container> /usr/bin/emouse
```


#### em_pscan
       
```bash
$ singularity exec <container> /usr/bin/em_pscan
```


#### em_cons
       
```bash
$ singularity exec <container> /usr/bin/em_cons
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