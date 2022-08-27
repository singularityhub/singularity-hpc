---
layout: container
name:  "mongo"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/mongo/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/mongo/container.yaml"
updated_at: "2022-08-27 02:53:53.706098"
latest: "5.0.6"
container_url: "https://hub.docker.com/r/_/mongo"
aliases:
 - "mongo"
 - "mongod"
 - "mongodump"
 - "mongoexport"
 - "mongofiles"
 - "mongoimport"
 - "mongos"
 - "mongostat"
 - "mongostore"
 - "mongotop"
versions:
 - "4.4.5-bionic"
 - "4.4.6-bionic"
 - "5.0.0-focal"
 - "5.0.0-rc1-focal"
 - "5.0.2"
 - "5.0.3"
 - "5.0.4"
 - "5.0.5"
 - "5.0.6"
 - "latest"
 - "5"
 - "5.0"
 - "4"
 - "4.9-rc"
 - "4.4"
description: "MongoDB is a free and open-source cross-platform document-oriented database program. Classified as a NoSQL database program, MongoDB uses JSON-like documents with schemata."
config: {"docker": "mongo", "url": "https://hub.docker.com/r/_/mongo", "maintainer": "@vsoch", "description": "MongoDB is a free and open-source cross-platform document-oriented database program. Classified as a NoSQL database program, MongoDB uses JSON-like documents with schemata.", "filter": ["^(?!.*nano).*$", "^(?!.*windows).*$"], "latest": {"5.0.6": "sha256:fed6248ae0bb0d54c0448eb786c87120737eedc522172ee1536ad47789782348"}, "tags": {"4.4.5-bionic": "sha256:cc8bb8711114fa726ca641f5644791d3d43bdd2c95dac541a5fa2c90a2e6e972", "4.4.6-bionic": "sha256:3d0e6df9fd5bc42cbf8ef8bc9e6c4e78f6f26c7157dbd7bdec72d202ab8ebe3a", "5.0.0-focal": "sha256:21aa30c16cf1f92c68890cefc612357bf856f94678cc4bfc0ef26bdeb7c34ad0", "5.0.0-rc1-focal": "sha256:238ca9b76e3034377a38be3dac927bd3920634c3af68053be000739c15106cec", "5.0.2": "sha256:58ea1bc09f269a9b85b7e1fae83b7505952aaa521afaaca4131f558955743842", "5.0.3": "sha256:4088649f737cf704deaf350ccd5ad8045552c5a0f8a5a2e81c1c23e280db2d80", "5.0.4": "sha256:cf9f5df5419319390cc3b5d9abfc2d0d0b149b3e04a6c9936990129e3e29b579", "5.0.5": "sha256:079089900e9511a782a59a4276046835189720eb668088869d147d1145cebe14", "5.0.6": "sha256:fed6248ae0bb0d54c0448eb786c87120737eedc522172ee1536ad47789782348", "latest": "sha256:37e84d3dd30cdfb5472ec42b8a6b4dc6ca7cacd91ebcfa0410a54528bbc5fa6d", "5": "sha256:37e84d3dd30cdfb5472ec42b8a6b4dc6ca7cacd91ebcfa0410a54528bbc5fa6d", "5.0": "sha256:37e84d3dd30cdfb5472ec42b8a6b4dc6ca7cacd91ebcfa0410a54528bbc5fa6d", "4": "sha256:8f77c137bf79d7022c96f17574a0efeaebc1ef8ceca171937661622e7e11e7df", "4.9-rc": "sha256:36b78340b10ff47a37428cae7481caf894db191bd2fdebe1834f3b0328d48320", "4.4": "sha256:8f77c137bf79d7022c96f17574a0efeaebc1ef8ceca171937661622e7e11e7df"}, "aliases": {"mongo": "/usr/bin/mongo", "mongod": "/usr/bin/mongod", "mongodump": "/usr/bin/mongodump", "mongoexport": "/usr/bin/mongoexport", "mongofiles": "/usr/bin/mongofiles", "mongoimport": "/usr/bin/mongoimport", "mongos": "/usr/bin/mongos", "mongostat": "/usr/bin/mongostat", "mongostore": "/usr/bin/mongorestore", "mongotop": "/usr/bin/mongotop"}}
---

This module is a singularity container wrapper for mongo.
MongoDB is a free and open-source cross-platform document-oriented database program. Classified as a NoSQL database program, MongoDB uses JSON-like documents with schemata.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install mongo
```

Or a specific version:

```bash
$ shpc install mongo:4.4.5-bionic
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load mongo/4.4.5-bionic
$ module help mongo/4.4.5-bionic
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mongo-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mongo-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mongo-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mongo-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mongo-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mongo-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### mongo
       
```bash
$ singularity exec <container> /usr/bin/mongo
$ podman run --it --rm --entrypoint /usr/bin/mongo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/mongo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mongod
       
```bash
$ singularity exec <container> /usr/bin/mongod
$ podman run --it --rm --entrypoint /usr/bin/mongod   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/mongod   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mongodump
       
```bash
$ singularity exec <container> /usr/bin/mongodump
$ podman run --it --rm --entrypoint /usr/bin/mongodump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/mongodump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mongoexport
       
```bash
$ singularity exec <container> /usr/bin/mongoexport
$ podman run --it --rm --entrypoint /usr/bin/mongoexport   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/mongoexport   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mongofiles
       
```bash
$ singularity exec <container> /usr/bin/mongofiles
$ podman run --it --rm --entrypoint /usr/bin/mongofiles   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/mongofiles   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mongoimport
       
```bash
$ singularity exec <container> /usr/bin/mongoimport
$ podman run --it --rm --entrypoint /usr/bin/mongoimport   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/mongoimport   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mongos
       
```bash
$ singularity exec <container> /usr/bin/mongos
$ podman run --it --rm --entrypoint /usr/bin/mongos   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/mongos   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mongostat
       
```bash
$ singularity exec <container> /usr/bin/mongostat
$ podman run --it --rm --entrypoint /usr/bin/mongostat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/mongostat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mongostore
       
```bash
$ singularity exec <container> /usr/bin/mongorestore
$ podman run --it --rm --entrypoint /usr/bin/mongorestore   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/mongorestore   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mongotop
       
```bash
$ singularity exec <container> /usr/bin/mongotop
$ podman run --it --rm --entrypoint /usr/bin/mongotop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/mongotop   -v ${PWD} -w ${PWD} <container> -c " $@"
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