---
layout: container
name:  "mongo"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/mongo/container.yaml"
updated_at: "2021-04-18 06:43:55.034668"
container_url: ""
aliases:
 - "mongo"

 - "mongodump"

 - "mongofiles"

 - "mongostore"

 - "mongostat"

 - "mongod"

 - "mongoexport"

 - "mongoimport"

 - "mongos"

 - "mongotop"

versions:
 - "latest"
description: "MongoDB is a free and open-source cross-platform document-oriented database program. Classified as a NoSQL database program, MongoDB uses JSON-like documents with schemata."
---

This module is a singularity container wrapper for mongo.
MongoDB is a free and open-source cross-platform document-oriented database program. Classified as a NoSQL database program, MongoDB uses JSON-like documents with schemata.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install mongo
```

Or a specific version:

```bash
$ shpc install mongo:latest
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load mongo/latest
$ module help mongo/latest
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### mongo-run:

```bash
$ singularity run <container>
```

#### mongo-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### mongo-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
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
```


#### mongodump
       
```bash
$ singularity exec <container> /usr/bin/mongodump
```


#### mongofiles
       
```bash
$ singularity exec <container> /usr/bin/mongofiles
```


#### mongostore
       
```bash
$ singularity exec <container> /usr/bin/mongorestore
```


#### mongostat
       
```bash
$ singularity exec <container> /usr/bin/mongostat
```


#### mongod
       
```bash
$ singularity exec <container> /usr/bin/mongod
```


#### mongoexport
       
```bash
$ singularity exec <container> /usr/bin/mongoexport
```


#### mongoimport
       
```bash
$ singularity exec <container> /usr/bin/mongoimport
```


#### mongos
       
```bash
$ singularity exec <container> /usr/bin/mongos
```


#### mongotop
       
```bash
$ singularity exec <container> /usr/bin/mongotop
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