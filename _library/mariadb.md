---
layout: container
name:  "mariadb"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/mariadb/container.yaml"
updated_at: "2021-04-20 02:20:05.693989"
container_url: ""
aliases:
 - "mariabackup"

 - "mariadb"

 - "mariadb-access"

 - "mariadb-admin"

 - "mariadb-analyze"

 - "mariadb-backup"

 - "mariadb-binlog"

 - "mariadb-check"

 - "mariadb-conv"

 - "mariadb-convert-table-format"

 - "mariadb-dump"

 - "mariadb-dumpslow"

 - "mariadb-find-rows"

 - "mariadb-fix-extensions"

 - "mariadb-hotcopy"

 - "mariadb-import"

 - "mariadb-install-db"

 - "mariadb-optimize"

 - "mariadb-plugin"

 - "mariadb-repair"

 - "mariadb-report"

 - "mariadb-secure-installation"

 - "mariadb-service-convert"

 - "mariadb-setpermission"

 - "mariadb-show"

 - "mariadb-slap"

 - "mariadb-tzinfo-to-sql"

 - "mariadb-upgrade"

 - "mariadb-waitpid"

 - "mariadbcheck"

 - "mariadbd-multi"

 - "mariadbd-safe"

 - "mariadbd-safe-helper"

versions:
 - "latest"
description: "MariaDB Server is one of the most popular database servers in the world. It’s made by the original developers of MySQL and guaranteed to stay open source. Notable users include Wikipedia, DBS Bank and ServiceNow."
---

This module is a singularity container wrapper for mariadb.
MariaDB Server is one of the most popular database servers in the world. It’s made by the original developers of MySQL and guaranteed to stay open source. Notable users include Wikipedia, DBS Bank and ServiceNow.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install mariadb
```

Or a specific version:

```bash
$ shpc install mariadb:latest
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load mariadb/latest
$ module help mariadb/latest
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### mariadb-run:

```bash
$ singularity run <container>
```

#### mariadb-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### mariadb-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### mariadb-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mariadb-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### mariabackup
       
```bash
$ singularity exec <container> /usr/bin/mariabackup
```


#### mariadb
       
```bash
$ singularity exec <container> /usr/bin/mariadb
```


#### mariadb-access
       
```bash
$ singularity exec <container> /usr/bin/mariadb-access
```


#### mariadb-admin
       
```bash
$ singularity exec <container> /usr/bin/mariadb-admin
```


#### mariadb-analyze
       
```bash
$ singularity exec <container> /usr/bin/mariadb-analyze
```


#### mariadb-backup
       
```bash
$ singularity exec <container> /usr/bin/mariadb-backup
```


#### mariadb-binlog
       
```bash
$ singularity exec <container> /usr/bin/mariadb-binlog
```


#### mariadb-check
       
```bash
$ singularity exec <container> /usr/bin/mariadb-check
```


#### mariadb-conv
       
```bash
$ singularity exec <container> /usr/bin/mariadb-conv
```


#### mariadb-convert-table-format
       
```bash
$ singularity exec <container> /usr/bin/mariadb-convert-table-format
```


#### mariadb-dump
       
```bash
$ singularity exec <container> /usr/bin/mariadb-dump
```


#### mariadb-dumpslow
       
```bash
$ singularity exec <container> /usr/bin/mariadb-dumpslow
```


#### mariadb-find-rows
       
```bash
$ singularity exec <container> /usr/bin/mariadb-find-rows
```


#### mariadb-fix-extensions
       
```bash
$ singularity exec <container> /usr/bin/mariadb-fix-extensions
```


#### mariadb-hotcopy
       
```bash
$ singularity exec <container> /usr/bin/mariadb-hotcopy
```


#### mariadb-import
       
```bash
$ singularity exec <container> /usr/bin/mariadb-import
```


#### mariadb-install-db
       
```bash
$ singularity exec <container> /usr/bin/mariadb-install-db
```


#### mariadb-optimize
       
```bash
$ singularity exec <container> /usr/bin/mariadb-optimize
```


#### mariadb-plugin
       
```bash
$ singularity exec <container> /usr/bin/mariadb-plugin
```


#### mariadb-repair
       
```bash
$ singularity exec <container> /usr/bin/mariadb-repair
```


#### mariadb-report
       
```bash
$ singularity exec <container> /usr/bin/mariadb-report
```


#### mariadb-secure-installation
       
```bash
$ singularity exec <container> /usr/bin/mariadb-secure-installation
```


#### mariadb-service-convert
       
```bash
$ singularity exec <container> /usr/bin/mariadb-service-convert
```


#### mariadb-setpermission
       
```bash
$ singularity exec <container> /usr/bin/mariadb-setpermission
```


#### mariadb-show
       
```bash
$ singularity exec <container> /usr/bin/mariadb-show
```


#### mariadb-slap
       
```bash
$ singularity exec <container> /usr/bin/mariadb-slap
```


#### mariadb-tzinfo-to-sql
       
```bash
$ singularity exec <container> /usr/bin/mariadb-tzinfo-to-sql
```


#### mariadb-upgrade
       
```bash
$ singularity exec <container> /usr/bin/mariadb-upgrade
```


#### mariadb-waitpid
       
```bash
$ singularity exec <container> /usr/bin/mariadb-waitpid
```


#### mariadbcheck
       
```bash
$ singularity exec <container> /usr/bin/mariadbcheck
```


#### mariadbd-multi
       
```bash
$ singularity exec <container> /usr/bin/mariadbd-multi
```


#### mariadbd-safe
       
```bash
$ singularity exec <container> /usr/bin/mariadbd-safe
```


#### mariadbd-safe-helper
       
```bash
$ singularity exec <container> /usr/bin/mariadbd-safe-helper
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