---
layout: container
name:  "mysql"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/mysql/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/mysql/container.yaml"
updated_at: "2022-08-27 02:53:54.368120"
latest: "8.0.28"
container_url: "https://hub.docker.com/r/_/mysql"
aliases:
 - "mysql"
 - "mysql_config_editor"
 - "mysql_secure_installation"
 - "mysql_ssl_rsa_setup"
 - "mysql_tzinfo_to_sql"
 - "mysql_upgrade"
 - "mysqladmin"
 - "mysqlbinlog"
 - "mysqlcheck"
 - "mysqld_multi"
 - "mysqld_safe"
 - "mysqldump"
 - "mysqldumpslow"
 - "mysqlimport"
 - "mysqlpump"
 - "mysqlshow"
 - "mysqlslap"
versions:
 - "8.0.25"
 - "8.0.26"
 - "8.0.27"
 - "8.0.28"
 - "latest"
 - "8"
 - "8.0"
description: "MySQL is the world's most popular open source database."
config: {"docker": "mysql", "url": "https://hub.docker.com/r/_/mysql", "maintainer": "@vsoch", "description": "MySQL is the world's most popular open source database.", "latest": {"8.0.28": "sha256:fc77d54cacef90ad3d75964837fad0f2a9a368b69e7d799665a3f4e90e600c2d"}, "tags": {"8.0.25": "sha256:52b8406e4c32b8cf0557f1b74517e14c5393aff5cf0384eff62d9e81f4985d4b", "8.0.26": "sha256:5d52dc010398db422949f079c76e98f6b62230e5b59c0bf7582409d2c85abacb", "8.0.27": "sha256:e9027fe4d91c0153429607251656806cc784e914937271037f7738bd5b8e7709", "8.0.28": "sha256:fc77d54cacef90ad3d75964837fad0f2a9a368b69e7d799665a3f4e90e600c2d", "latest": "sha256:a840244706a5fdc3c704b15a3700bfda39fdc069262d7753fa09de2d9faf5f83", "8": "sha256:a840244706a5fdc3c704b15a3700bfda39fdc069262d7753fa09de2d9faf5f83", "8.0": "sha256:a840244706a5fdc3c704b15a3700bfda39fdc069262d7753fa09de2d9faf5f83"}, "aliases": {"mysql": "/usr/bin/mysql", "mysql_config_editor": "/usr/bin/mysql_config_editor", "mysql_secure_installation": "/usr/bin/mysql_secure_installation", "mysql_ssl_rsa_setup": "/usr/bin/mysql_ssl_rsa_setup", "mysql_tzinfo_to_sql": "/usr/bin/mysql_tzinfo_to_sql", "mysql_upgrade": "/usr/bin/mysql_upgrade", "mysqladmin": "/usr/bin/mysqladmin", "mysqlbinlog": "/usr/bin/mysqlbinlog", "mysqlcheck": "/usr/bin/mysqlcheck", "mysqld_multi": "/usr/bin/mysqld_multi", "mysqld_safe": "/usr/bin/mysqld_safe", "mysqldump": "/usr/bin/mysqldump", "mysqldumpslow": "/usr/bin/mysqldumpslow", "mysqlimport": "/usr/bin/mysqlimport", "mysqlpump": "/usr/bin/mysqlpump", "mysqlshow": "/usr/bin/mysqlshow", "mysqlslap": "/usr/bin/mysqlslap"}}
---

This module is a singularity container wrapper for mysql.
MySQL is the world's most popular open source database.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install mysql
```

Or a specific version:

```bash
$ shpc install mysql:8.0.25
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load mysql/8.0.25
$ module help mysql/8.0.25
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mysql-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mysql-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mysql-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mysql-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
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
$ podman run --it --rm --entrypoint /usr/bin/mysql   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/mysql   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysql_config_editor
       
```bash
$ singularity exec <container> /usr/bin/mysql_config_editor
$ podman run --it --rm --entrypoint /usr/bin/mysql_config_editor   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/mysql_config_editor   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysql_secure_installation
       
```bash
$ singularity exec <container> /usr/bin/mysql_secure_installation
$ podman run --it --rm --entrypoint /usr/bin/mysql_secure_installation   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/mysql_secure_installation   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysql_ssl_rsa_setup
       
```bash
$ singularity exec <container> /usr/bin/mysql_ssl_rsa_setup
$ podman run --it --rm --entrypoint /usr/bin/mysql_ssl_rsa_setup   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/mysql_ssl_rsa_setup   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysql_tzinfo_to_sql
       
```bash
$ singularity exec <container> /usr/bin/mysql_tzinfo_to_sql
$ podman run --it --rm --entrypoint /usr/bin/mysql_tzinfo_to_sql   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/mysql_tzinfo_to_sql   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysql_upgrade
       
```bash
$ singularity exec <container> /usr/bin/mysql_upgrade
$ podman run --it --rm --entrypoint /usr/bin/mysql_upgrade   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/mysql_upgrade   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysqladmin
       
```bash
$ singularity exec <container> /usr/bin/mysqladmin
$ podman run --it --rm --entrypoint /usr/bin/mysqladmin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/mysqladmin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysqlbinlog
       
```bash
$ singularity exec <container> /usr/bin/mysqlbinlog
$ podman run --it --rm --entrypoint /usr/bin/mysqlbinlog   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/mysqlbinlog   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysqlcheck
       
```bash
$ singularity exec <container> /usr/bin/mysqlcheck
$ podman run --it --rm --entrypoint /usr/bin/mysqlcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/mysqlcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysqld_multi
       
```bash
$ singularity exec <container> /usr/bin/mysqld_multi
$ podman run --it --rm --entrypoint /usr/bin/mysqld_multi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/mysqld_multi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysqld_safe
       
```bash
$ singularity exec <container> /usr/bin/mysqld_safe
$ podman run --it --rm --entrypoint /usr/bin/mysqld_safe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/mysqld_safe   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysqldump
       
```bash
$ singularity exec <container> /usr/bin/mysqldump
$ podman run --it --rm --entrypoint /usr/bin/mysqldump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/mysqldump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysqldumpslow
       
```bash
$ singularity exec <container> /usr/bin/mysqldumpslow
$ podman run --it --rm --entrypoint /usr/bin/mysqldumpslow   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/mysqldumpslow   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysqlimport
       
```bash
$ singularity exec <container> /usr/bin/mysqlimport
$ podman run --it --rm --entrypoint /usr/bin/mysqlimport   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/mysqlimport   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysqlpump
       
```bash
$ singularity exec <container> /usr/bin/mysqlpump
$ podman run --it --rm --entrypoint /usr/bin/mysqlpump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/mysqlpump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysqlshow
       
```bash
$ singularity exec <container> /usr/bin/mysqlshow
$ podman run --it --rm --entrypoint /usr/bin/mysqlshow   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/mysqlshow   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysqlslap
       
```bash
$ singularity exec <container> /usr/bin/mysqlslap
$ podman run --it --rm --entrypoint /usr/bin/mysqlslap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/mysqlslap   -v ${PWD} -w ${PWD} <container> -c " $@"
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