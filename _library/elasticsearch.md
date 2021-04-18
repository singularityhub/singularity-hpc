---
layout: container
name:  "elasticsearch"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/elasticsearch/container.yaml"
updated_at: "2021-04-18 11:25:25.806141"
container_url: ""
aliases:
 - "elasticsearch"

 - "elasticsearch-certgen"

 - "elasticsearch-certutil"

 - "elasticsearch-cli"

 - "elasticsearch-croneval"

 - "elasticsearch-env"

 - "elasticsearch-env-from-file"

 - "elasticsearch-keystore"

 - "elasticsearch-migrate"

 - "elasticsearch-node"

 - "elasticsearch-plugin"

 - "elasticsearch-saml-metadata"

 - "elasticsearch-setup-passwords"

 - "elasticsearch-shard"

 - "elasticsearch-sql-cli"

 - "elasticsearch-sql-cli-7.12.0.jar"

 - "elasticsearch-syskeygen"

 - "elasticsearch-users"

versions:
 - "7.12.0"
description: "Elasticsearch is a powerful open source search and analytics engine that makes data easy to explore."
---

This module is a singularity container wrapper for elasticsearch.
Elasticsearch is a powerful open source search and analytics engine that makes data easy to explore.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install elasticsearch
```

Or a specific version:

```bash
$ shpc install elasticsearch:7.12.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load elasticsearch/7.12.0
$ module help elasticsearch/7.12.0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### elasticsearch-run:

```bash
$ singularity run <container>
```

#### elasticsearch-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### elasticsearch-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### elasticsearch-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### elasticsearch-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### elasticsearch
       
```bash
$ singularity exec <container> /usr/share/elasticsearch/bin/elasticsearch
```


#### elasticsearch-certgen
       
```bash
$ singularity exec <container> /usr/share/elasticsearch/bin/elasticsearch-certgen
```


#### elasticsearch-certutil
       
```bash
$ singularity exec <container> /usr/share/elasticsearch/bin/elasticsearch-certutil
```


#### elasticsearch-cli
       
```bash
$ singularity exec <container> /usr/share/elasticsearch/bin/elasticsearch-cli
```


#### elasticsearch-croneval
       
```bash
$ singularity exec <container> /usr/share/elasticsearch/bin/elasticsearch-croneval
```


#### elasticsearch-env
       
```bash
$ singularity exec <container> /usr/share/elasticsearch/bin/elasticsearch-env
```


#### elasticsearch-env-from-file
       
```bash
$ singularity exec <container> /usr/share/elasticsearch/bin/elasticsearch-env-from-file
```


#### elasticsearch-keystore
       
```bash
$ singularity exec <container> /usr/share/elasticsearch/bin/elasticsearch-keystore
```


#### elasticsearch-migrate
       
```bash
$ singularity exec <container> /usr/share/elasticsearch/bin/elasticsearch-migrate
```


#### elasticsearch-node
       
```bash
$ singularity exec <container> /usr/share/elasticsearch/bin/elasticsearch-node
```


#### elasticsearch-plugin
       
```bash
$ singularity exec <container> /usr/share/elasticsearch/bin/elasticsearch-plugin
```


#### elasticsearch-saml-metadata
       
```bash
$ singularity exec <container> /usr/share/elasticsearch/bin/elasticsearch-saml-metadata
```


#### elasticsearch-setup-passwords
       
```bash
$ singularity exec <container> /usr/share/elasticsearch/bin/elasticsearch-setup-passwords
```


#### elasticsearch-shard
       
```bash
$ singularity exec <container> /usr/share/elasticsearch/bin/elasticsearch-shard
```


#### elasticsearch-sql-cli
       
```bash
$ singularity exec <container> /usr/share/elasticsearch/bin/elasticsearch-sql-cli
```


#### elasticsearch-sql-cli-7.12.0.jar
       
```bash
$ singularity exec <container> java jar /usr/share/elasticsearch/bin/elasticsearch-sql-cli-7.12.0.jar
```


#### elasticsearch-syskeygen
       
```bash
$ singularity exec <container> /usr/share/elasticsearch/bin/elasticsearch-syskeygen
```


#### elasticsearch-users
       
```bash
$ singularity exec <container> /usr/share/elasticsearch/bin/elasticsearch-users
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