---
layout: container
name:  "biocontainers/tpp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/biocontainers/tpp/container.yaml"
updated_at: "2021-04-20 03:14:48.435098"
container_url: ""
aliases:
 - "config_data"

 - "json_xs"

 - "lwp-download"

 - "lwp-dump"

 - "lwp-mirror"

 - "lwp-request"

versions:
 - "v5.2_cv1"
description: "The Trans-Proteomic Pipeline (TPP) is a collection of integrated tools for MS/MS proteomics, developed at the SPC."
---

This module is a singularity container wrapper for biocontainers/tpp.
The Trans-Proteomic Pipeline (TPP) is a collection of integrated tools for MS/MS proteomics, developed at the SPC.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install biocontainers/tpp
```

Or a specific version:

```bash
$ shpc install biocontainers/tpp:v5.2_cv1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load biocontainers/tpp/v5.2_cv1
$ module help biocontainers/tpp/v5.2_cv1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### biocontainers-tpp-run:

```bash
$ singularity run <container>
```

#### biocontainers-tpp-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### biocontainers-tpp-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### biocontainers-tpp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### biocontainers-tpp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### config_data
       
```bash
$ singularity exec <container> /usr/local/bin/config_data
```


#### json_xs
       
```bash
$ singularity exec <container> /usr/local/bin/json_xs
```


#### lwp-download
       
```bash
$ singularity exec <container> /usr/local/bin/lwp-download
```


#### lwp-dump
       
```bash
$ singularity exec <container> /usr/local/bin/lwp-dump
```


#### lwp-mirror
       
```bash
$ singularity exec <container> /usr/local/bin/lwp-mirror
```


#### lwp-request
       
```bash
$ singularity exec <container> /usr/local/bin/lwp-request
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