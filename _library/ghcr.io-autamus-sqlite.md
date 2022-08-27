---
layout: container
name:  "ghcr.io/autamus/sqlite"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/sqlite/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/ghcr.io/autamus/sqlite/container.yaml"
updated_at: "2022-08-27 01:36:48.253758"
latest: "3.38.3"
container_url: "https://github.com/orgs/autamus/packages/container/package/sqlite"
aliases:
 - "sqlite3"
versions:
 - "3.35.4"
 - "3.35.5"
 - "3.36.0"
 - "3.37.1"
 - "latest"
 - "3.37.2"
 - "3.38.3"
description: "SQLite is a relational database management system contained in a C library. "
config: {"docker": "ghcr.io/autamus/sqlite", "url": "https://github.com/orgs/autamus/packages/container/package/sqlite", "maintainer": "@vsoch", "description": "SQLite is a relational database management system contained in a C library. ", "latest": {"3.38.3": "sha256:1d3a02d3733e5686ecff10a0fc33b5e3f75579b12c351d4559bcaa298c2a4164"}, "tags": {"3.35.4": "sha256:6fff31edcc2e88880c57b4ccf77bccfa3d89d626f289aa652103a906b8780880", "3.35.5": "sha256:5df8dfaf8a8273fa86bcbc6a172956285ba42b73e6893c0cd9f7c1989c522e14", "3.36.0": "sha256:d4d8fb1c2e40656247de3af3a0f8313d6cf7b2ecf979bb49cd1a577812525c0e", "3.37.1": "sha256:d94599a03df1134af1c2f2fec9244c5550551504209c7f0690aeaaecd2061f6a", "latest": "sha256:db9ddab38c750c462261b093c15f1520ae00b85bbd900080ac2d39d4f26fde47", "3.37.2": "sha256:76268c5e136035fdbbc6b4032910ffe19842766488b1ca015213f1a5bec718f6", "3.38.3": "sha256:1d3a02d3733e5686ecff10a0fc33b5e3f75579b12c351d4559bcaa298c2a4164"}, "aliases": {"sqlite3": "/opt/view/bin/sqlite3"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/sqlite.
SQLite is a relational database management system contained in a C library. 
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/sqlite
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/sqlite:3.35.4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/sqlite/3.35.4
$ module help ghcr.io/autamus/sqlite/3.35.4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sqlite-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sqlite-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sqlite-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sqlite-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sqlite-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sqlite-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### sqlite3
       
```bash
$ singularity exec <container> /opt/view/bin/sqlite3
$ podman run --it --rm --entrypoint /opt/view/bin/sqlite3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/sqlite3   -v ${PWD} -w ${PWD} <container> -c " $@"
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