---
layout: container
name:  "mysql"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/mysql/container.yaml"
updated_at: "2021-04-18 20:17:58.246036"
container_url: ""
aliases:
 - "mysql"

 - "mysql_ssl_rsa_setup"

 - "mysqldump"

 - "mysql_tzinfo_to_sql"

 - "mysqldumpslow"

 - "mysql_upgrade"

 - "mysqlimport"

 - "mysqladmin"

 - "mysqlpump"

 - "mysqlbinlog"

 - "mysqlshow"

 - "mysqlcheck"

 - "mysqlslap"

 - "mysql_config_editor"

 - "mysqld_multi"

 - "mysql_secure_installation"

 - "mysqld_safe"

versions:
 - "latest"
description: "MySQL is the world's most popular open source database."
---

This module is a singularity container wrapper for mysql.
MySQL is the world's most popular open source database.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install mysql
```

Or a specific version:

```bash
$ shpc install mysql:latest
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load mysql/latest
$ module help mysql/latest
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### mysql-run:

```bash
$ singularity run <container>
```

#### mysql-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### mysql-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### mysql-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mysql-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### mysql
       
```bash
$ singularity exec <container> /usr/bin/mysql
```


#### mysql_ssl_rsa_setup
       
```bash
$ singularity exec <container> /usr/bin/mysql_ssl_rsa_setup
```


#### mysqldump
       
```bash
$ singularity exec <container> /usr/bin/mysqldump
```


#### mysql_tzinfo_to_sql
       
```bash
$ singularity exec <container> /usr/bin/mysql_tzinfo_to_sql
```


#### mysqldumpslow
       
```bash
$ singularity exec <container> /usr/bin/mysqldumpslow
```


#### mysql_upgrade
       
```bash
$ singularity exec <container> /usr/bin/mysql_upgrade
```


#### mysqlimport
       
```bash
$ singularity exec <container> /usr/bin/mysqlimport
```


#### mysqladmin
       
```bash
$ singularity exec <container> /usr/bin/mysqladmin
```


#### mysqlpump
       
```bash
$ singularity exec <container> /usr/bin/mysqlpump
```


#### mysqlbinlog
       
```bash
$ singularity exec <container> /usr/bin/mysqlbinlog
```


#### mysqlshow
       
```bash
$ singularity exec <container> /usr/bin/mysqlshow
```


#### mysqlcheck
       
```bash
$ singularity exec <container> /usr/bin/mysqlcheck
```


#### mysqlslap
       
```bash
$ singularity exec <container> /usr/bin/mysqlslap
```


#### mysql_config_editor
       
```bash
$ singularity exec <container> /usr/bin/mysql_config_editor
```


#### mysqld_multi
       
```bash
$ singularity exec <container> /usr/bin/mysqld_multi
```


#### mysql_secure_installation
       
```bash
$ singularity exec <container> /usr/bin/mysql_secure_installation
```


#### mysqld_safe
       
```bash
$ singularity exec <container> /usr/bin/mysqld_safe
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