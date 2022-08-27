---
layout: container
name:  "ghcr.io/autamus/curl"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/curl/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/ghcr.io/autamus/curl/container.yaml"
updated_at: "2022-08-27 01:35:45.687390"
latest: "7.80.0"
container_url: "https://github.com/orgs/autamus/packages/container/package/curl"
aliases:
 - "c_rehash"
 - "curl"
 - "curl-config"
versions:
 - "7.76.1"
 - "7.78.0"
 - "7.79.0"
 - "7.80.0"
 - "latest"
description: "cURL is a computer software project providing a library and command-line tool for transferring data using various network protocols. The name stands for 'Client URL', which was first released in 1997."
config: {"docker": "ghcr.io/autamus/curl", "url": "https://github.com/orgs/autamus/packages/container/package/curl", "maintainer": "@vsoch", "description": "cURL is a computer software project providing a library and command-line tool for transferring data using various network protocols. The name stands for 'Client URL', which was first released in 1997.", "latest": {"7.80.0": "sha256:f23de2a51ddb4bdafcd39bcf902653bb54f5abbcf48571742907ed21036b8505"}, "tags": {"7.76.1": "sha256:997cf56439b4bfbc9d529b94b001bfc8d3e3ea8f74dbb6d18eff2dd6eb556109", "7.78.0": "sha256:20092460f849e09ff29c7227a682ef7edb8d23812532c0b2ff3ded099bd17e57", "7.79.0": "sha256:b69c6d7302e4753be9a8cb533ac3efc724d45a16139196744311d24f233cd100", "7.80.0": "sha256:f23de2a51ddb4bdafcd39bcf902653bb54f5abbcf48571742907ed21036b8505", "latest": "sha256:f23de2a51ddb4bdafcd39bcf902653bb54f5abbcf48571742907ed21036b8505"}, "aliases": {"c_rehash": "/opt/view/bin/c_rehash", "curl": "/opt/view/bin/curl", "curl-config": "/opt/view/bin/curl-config"}}
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

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### curl-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### curl-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### curl-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### curl-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### curl-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### curl-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### c_rehash
       
```bash
$ singularity exec <container> /opt/view/bin/c_rehash
$ podman run --it --rm --entrypoint /opt/view/bin/c_rehash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/c_rehash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### curl
       
```bash
$ singularity exec <container> /opt/view/bin/curl
$ podman run --it --rm --entrypoint /opt/view/bin/curl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/curl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### curl-config
       
```bash
$ singularity exec <container> /opt/view/bin/curl-config
$ podman run --it --rm --entrypoint /opt/view/bin/curl-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/curl-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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