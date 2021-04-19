---
layout: container
name:  "postgres"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/postgres/container.yaml"
updated_at: "2021-04-19 23:52:31.029567"
container_url: ""
aliases:
 - "clusterdb"

 - "createdb"

 - "createuser"

 - "dropdb"

 - "dropuser"

 - "initdb"

 - "oid2name"

 - "pg_archivecleanup"

 - "pg_basebackup"

 - "pg_checksums"

 - "pg_config"

 - "pg_controldata"

 - "pg_ctl"

 - "pg_dump"

 - "pg_dumpall"

 - "pg_isready"

 - "pg_receivewal"

 - "pg_recvlogical"

 - "pg_resetwal"

 - "pg_restore"

 - "pg_rewind"

 - "pg_standby"

 - "pg_test_fsync"

 - "pg_test_timing"

 - "pg_upgrade"

 - "pg_verifybackup"

 - "pg_waldump"

 - "pgbench"

 - "postgres"

 - "postmaster"

 - "psql"

 - "reindexdb"

 - "vacuumdb"

 - "vacuumlo"

versions:
 - "latest"
description: "PostgreSQL, often simply 'Postgres', is an object-relational database management system (ORDBMS) with an emphasis on extensibility and standards-compliance."
---

This module is a singularity container wrapper for postgres.
PostgreSQL, often simply 'Postgres', is an object-relational database management system (ORDBMS) with an emphasis on extensibility and standards-compliance.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install postgres
```

Or a specific version:

```bash
$ shpc install postgres:latest
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load postgres/latest
$ module help postgres/latest
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### postgres-run:

```bash
$ singularity run <container>
```

#### postgres-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### postgres-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### postgres-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### postgres-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### clusterdb
       
```bash
$ singularity exec <container> /usr/lib/postgresql/13/bin/clusterdb
```


#### createdb
       
```bash
$ singularity exec <container> /usr/lib/postgresql/13/bin/createdb
```


#### createuser
       
```bash
$ singularity exec <container> /usr/lib/postgresql/13/bin/createuser
```


#### dropdb
       
```bash
$ singularity exec <container> /usr/lib/postgresql/13/bin/dropdb
```


#### dropuser
       
```bash
$ singularity exec <container> /usr/lib/postgresql/13/bin/dropuser
```


#### initdb
       
```bash
$ singularity exec <container> /usr/lib/postgresql/13/bin/initdb
```


#### oid2name
       
```bash
$ singularity exec <container> /usr/lib/postgresql/13/bin/oid2name
```


#### pg_archivecleanup
       
```bash
$ singularity exec <container> /usr/lib/postgresql/13/bin/pg_archivecleanup
```


#### pg_basebackup
       
```bash
$ singularity exec <container> /usr/lib/postgresql/13/bin/pg_basebackup
```


#### pg_checksums
       
```bash
$ singularity exec <container> /usr/lib/postgresql/13/bin/pg_checksums
```


#### pg_config
       
```bash
$ singularity exec <container> /usr/lib/postgresql/13/bin/pg_config
```


#### pg_controldata
       
```bash
$ singularity exec <container> /usr/lib/postgresql/13/bin/pg_controldata
```


#### pg_ctl
       
```bash
$ singularity exec <container> /usr/lib/postgresql/13/bin/pg_ctl
```


#### pg_dump
       
```bash
$ singularity exec <container> /usr/lib/postgresql/13/bin/pg_dump
```


#### pg_dumpall
       
```bash
$ singularity exec <container> /usr/lib/postgresql/13/bin/pg_dumpall
```


#### pg_isready
       
```bash
$ singularity exec <container> /usr/lib/postgresql/13/bin/pg_isready
```


#### pg_receivewal
       
```bash
$ singularity exec <container> /usr/lib/postgresql/13/bin/pg_receivewal
```


#### pg_recvlogical
       
```bash
$ singularity exec <container> /usr/lib/postgresql/13/bin/pg_recvlogical
```


#### pg_resetwal
       
```bash
$ singularity exec <container> /usr/lib/postgresql/13/bin/pg_resetwal
```


#### pg_restore
       
```bash
$ singularity exec <container> /usr/lib/postgresql/13/bin/pg_restore
```


#### pg_rewind
       
```bash
$ singularity exec <container> /usr/lib/postgresql/13/bin/pg_rewind
```


#### pg_standby
       
```bash
$ singularity exec <container> /usr/lib/postgresql/13/bin/pg_standby
```


#### pg_test_fsync
       
```bash
$ singularity exec <container> /usr/lib/postgresql/13/bin/pg_test_fsync
```


#### pg_test_timing
       
```bash
$ singularity exec <container> /usr/lib/postgresql/13/bin/pg_test_timing
```


#### pg_upgrade
       
```bash
$ singularity exec <container> /usr/lib/postgresql/13/bin/pg_upgrade
```


#### pg_verifybackup
       
```bash
$ singularity exec <container> /usr/lib/postgresql/13/bin/pg_verifybackup
```


#### pg_waldump
       
```bash
$ singularity exec <container> /usr/lib/postgresql/13/bin/pg_waldump
```


#### pgbench
       
```bash
$ singularity exec <container> /usr/lib/postgresql/13/bin/pgbench
```


#### postgres
       
```bash
$ singularity exec <container> /usr/lib/postgresql/13/bin/postgres
```


#### postmaster
       
```bash
$ singularity exec <container> /usr/lib/postgresql/13/bin/postmaster
```


#### psql
       
```bash
$ singularity exec <container> /usr/lib/postgresql/13/bin/psql
```


#### reindexdb
       
```bash
$ singularity exec <container> /usr/lib/postgresql/13/bin/reindexdb
```


#### vacuumdb
       
```bash
$ singularity exec <container> /usr/lib/postgresql/13/bin/vacuumdb
```


#### vacuumlo
       
```bash
$ singularity exec <container> /usr/lib/postgresql/13/bin/vacuumlo
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