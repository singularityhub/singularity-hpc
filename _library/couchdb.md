---
layout: container
name:  "couchdb"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/couchdb/container.yaml"
updated_at: "2021-05-05 15:43:25.878608"
container_url: ""
aliases:
 - "couchdb"

 - "couchdb.cmd"

 - "couchjs"

 - "remsh"

versions:
 - "2"
 - "3.1.1"
 - "latest"
description: "CouchDB is a database that uses JSON for documents, an HTTP API, & JavaScript/declarative indexing."
---

This module is a singularity container wrapper for couchdb.
CouchDB is a database that uses JSON for documents, an HTTP API, & JavaScript/declarative indexing.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install couchdb
```

Or a specific version:

```bash
$ shpc install couchdb:2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load couchdb/2
$ module help couchdb/2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### couchdb-run:

```bash
$ singularity run <container>
```

#### couchdb-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### couchdb-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### couchdb-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### couchdb-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### couchdb
       
```bash
$ singularity exec <container> /opt/couchdb/bin/couchdb
```


#### couchdb.cmd
       
```bash
$ singularity exec <container> /opt/couchdb/bin/couchdb.cmd
```


#### couchjs
       
```bash
$ singularity exec <container> /opt/couchdb/bin/couchjs
```


#### remsh
       
```bash
$ singularity exec <container> /opt/couchdb/bin/remsh
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