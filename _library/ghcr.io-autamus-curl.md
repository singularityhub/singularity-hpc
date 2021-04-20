---
layout: container
name:  "ghcr.io/autamus/curl"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/curl/container.yaml"
updated_at: "2021-04-20 03:17:32.747298"
container_url: ""
aliases:
 - "c_rehash"

 - "curl"

 - "curl-config"

versions:
 - "7.76.1"
 - "latest"
description: "cURL is a computer software project providing a library and command-line tool for transferring data using various network protocols. The name stands for 'Client URL', which was first released in 1997."
---

This module is a singularity container wrapper for ghcr.io/autamus/curl.
cURL is a computer software project providing a library and command-line tool for transferring data using various network protocols. The name stands for 'Client URL', which was first released in 1997.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install ghcr.io/autamus/curl
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/curl:7.76.1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/curl/7.76.1
$ module help ghcr.io/autamus/curl/7.76.1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### ghcr.io-autamus-curl-run:

```bash
$ singularity run <container>
```

#### ghcr.io-autamus-curl-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### ghcr.io-autamus-curl-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### ghcr.io-autamus-curl-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ghcr.io-autamus-curl-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### c_rehash
       
```bash
$ singularity exec <container> /opt/view/bin/c_rehash
```


#### curl
       
```bash
$ singularity exec <container> /opt/view/bin/curl
```


#### curl-config
       
```bash
$ singularity exec <container> /opt/view/bin/curl-config
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