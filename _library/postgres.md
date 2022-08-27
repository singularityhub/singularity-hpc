---
layout: container
name:  "postgres"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/postgres/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/postgres/container.yaml"
updated_at: "2022-08-27 02:54:07.801798"
latest: "15beta1"
container_url: "https://hub.docker.com/r/_/postgres"
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
 - "13.2-alpine"
 - "13.3-alpine"
 - "13.4"
 - "14.0"
 - "14.1"
 - "14.2"
 - "latest"
 - "14"
 - "14-alpine3.15"
 - "15beta1"
 - "14-alpine3.16"
 - "14.4"
description: "PostgreSQL, often simply 'Postgres', is an object-relational database management system (ORDBMS) with an emphasis on extensibility and standards-compliance."
config: {"docker": "postgres", "url": "https://hub.docker.com/r/_/postgres", "maintainer": "@vsoch", "description": "PostgreSQL, often simply 'Postgres', is an object-relational database management system (ORDBMS) with an emphasis on extensibility and standards-compliance.", "latest": {"15beta1": "sha256:f920673ef9784586b0494d9c8bfffcc289ed75ee533bb5edf98cba10a8995f35"}, "tags": {"13.2-alpine": "sha256:c4c7a1585974706b5f72b8ab595e47399b23b2e03d93bbf75c1b0904be1803dc", "13.3-alpine": "sha256:e98a69a836391fe94d889a6ccfbb21257b93f47b2794da114a82ef23e342342f", "13.4": "sha256:1adb50e5c24f550a9e68457a2ce60e9e4103dfc43c3b36e98310168165b443a1", "14.0": "sha256:db927beee892dd02fbe963559f29a7867708747934812a80f83bff406a0d54fd", "14.1": "sha256:3162a6ead070474b27289f09eac4c865e75f93847a2d7098f718ee5a721637c4", "14.2": "sha256:2c954f8c5d03da58f8b82645b783b56c1135df17e650b186b296fa1bb71f9cfd", "latest": "sha256:4ba3b78788bb284687376b9c1e0565b245375ddee0fe14cef25e315b6bd88b1a", "14": "sha256:4ba3b78788bb284687376b9c1e0565b245375ddee0fe14cef25e315b6bd88b1a", "14-alpine3.15": "sha256:a00af33e23643f497a42bc24d2f6f28cc67f3f48b076135c5626b2e07945ff9c", "15beta1": "sha256:f920673ef9784586b0494d9c8bfffcc289ed75ee533bb5edf98cba10a8995f35", "14-alpine3.16": "sha256:3eab206b57cf9acb206359d14eb2d00cdd2c396ddd7cb246690788b22ed858c4", "14.4": "sha256:4ba3b78788bb284687376b9c1e0565b245375ddee0fe14cef25e315b6bd88b1a"}, "aliases": {"clusterdb": "/usr/lib/postgresql/13/bin/clusterdb", "createdb": "/usr/lib/postgresql/13/bin/createdb", "createuser": "/usr/lib/postgresql/13/bin/createuser", "dropdb": "/usr/lib/postgresql/13/bin/dropdb", "dropuser": "/usr/lib/postgresql/13/bin/dropuser", "initdb": "/usr/lib/postgresql/13/bin/initdb", "oid2name": "/usr/lib/postgresql/13/bin/oid2name", "pg_archivecleanup": "/usr/lib/postgresql/13/bin/pg_archivecleanup", "pg_basebackup": "/usr/lib/postgresql/13/bin/pg_basebackup", "pg_checksums": "/usr/lib/postgresql/13/bin/pg_checksums", "pg_config": "/usr/lib/postgresql/13/bin/pg_config", "pg_controldata": "/usr/lib/postgresql/13/bin/pg_controldata", "pg_ctl": "/usr/lib/postgresql/13/bin/pg_ctl", "pg_dump": "/usr/lib/postgresql/13/bin/pg_dump", "pg_dumpall": "/usr/lib/postgresql/13/bin/pg_dumpall", "pg_isready": "/usr/lib/postgresql/13/bin/pg_isready", "pg_receivewal": "/usr/lib/postgresql/13/bin/pg_receivewal", "pg_recvlogical": "/usr/lib/postgresql/13/bin/pg_recvlogical", "pg_resetwal": "/usr/lib/postgresql/13/bin/pg_resetwal", "pg_restore": "/usr/lib/postgresql/13/bin/pg_restore", "pg_rewind": "/usr/lib/postgresql/13/bin/pg_rewind", "pg_standby": "/usr/lib/postgresql/13/bin/pg_standby", "pg_test_fsync": "/usr/lib/postgresql/13/bin/pg_test_fsync", "pg_test_timing": "/usr/lib/postgresql/13/bin/pg_test_timing", "pg_upgrade": "/usr/lib/postgresql/13/bin/pg_upgrade", "pg_verifybackup": "/usr/lib/postgresql/13/bin/pg_verifybackup", "pg_waldump": "/usr/lib/postgresql/13/bin/pg_waldump", "pgbench": "/usr/lib/postgresql/13/bin/pgbench", "postgres": "/usr/lib/postgresql/13/bin/postgres", "postmaster": "/usr/lib/postgresql/13/bin/postmaster", "psql": "/usr/lib/postgresql/13/bin/psql", "reindexdb": "/usr/lib/postgresql/13/bin/reindexdb", "vacuumdb": "/usr/lib/postgresql/13/bin/vacuumdb", "vacuumlo": "/usr/lib/postgresql/13/bin/vacuumlo"}}
---

This module is a singularity container wrapper for postgres.
PostgreSQL, often simply 'Postgres', is an object-relational database management system (ORDBMS) with an emphasis on extensibility and standards-compliance.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install postgres
```

Or a specific version:

```bash
$ shpc install postgres:13.2-alpine
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load postgres/13.2-alpine
$ module help postgres/13.2-alpine
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### postgres-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### postgres-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### postgres-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### postgres-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
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
$ podman run --it --rm --entrypoint /usr/lib/postgresql/13/bin/clusterdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/lib/postgresql/13/bin/clusterdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### createdb
       
```bash
$ singularity exec <container> /usr/lib/postgresql/13/bin/createdb
$ podman run --it --rm --entrypoint /usr/lib/postgresql/13/bin/createdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/lib/postgresql/13/bin/createdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### createuser
       
```bash
$ singularity exec <container> /usr/lib/postgresql/13/bin/createuser
$ podman run --it --rm --entrypoint /usr/lib/postgresql/13/bin/createuser   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/lib/postgresql/13/bin/createuser   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dropdb
       
```bash
$ singularity exec <container> /usr/lib/postgresql/13/bin/dropdb
$ podman run --it --rm --entrypoint /usr/lib/postgresql/13/bin/dropdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/lib/postgresql/13/bin/dropdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dropuser
       
```bash
$ singularity exec <container> /usr/lib/postgresql/13/bin/dropuser
$ podman run --it --rm --entrypoint /usr/lib/postgresql/13/bin/dropuser   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/lib/postgresql/13/bin/dropuser   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### initdb
       
```bash
$ singularity exec <container> /usr/lib/postgresql/13/bin/initdb
$ podman run --it --rm --entrypoint /usr/lib/postgresql/13/bin/initdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/lib/postgresql/13/bin/initdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### oid2name
       
```bash
$ singularity exec <container> /usr/lib/postgresql/13/bin/oid2name
$ podman run --it --rm --entrypoint /usr/lib/postgresql/13/bin/oid2name   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/lib/postgresql/13/bin/oid2name   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pg_archivecleanup
       
```bash
$ singularity exec <container> /usr/lib/postgresql/13/bin/pg_archivecleanup
$ podman run --it --rm --entrypoint /usr/lib/postgresql/13/bin/pg_archivecleanup   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/lib/postgresql/13/bin/pg_archivecleanup   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pg_basebackup
       
```bash
$ singularity exec <container> /usr/lib/postgresql/13/bin/pg_basebackup
$ podman run --it --rm --entrypoint /usr/lib/postgresql/13/bin/pg_basebackup   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/lib/postgresql/13/bin/pg_basebackup   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pg_checksums
       
```bash
$ singularity exec <container> /usr/lib/postgresql/13/bin/pg_checksums
$ podman run --it --rm --entrypoint /usr/lib/postgresql/13/bin/pg_checksums   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/lib/postgresql/13/bin/pg_checksums   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pg_config
       
```bash
$ singularity exec <container> /usr/lib/postgresql/13/bin/pg_config
$ podman run --it --rm --entrypoint /usr/lib/postgresql/13/bin/pg_config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/lib/postgresql/13/bin/pg_config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pg_controldata
       
```bash
$ singularity exec <container> /usr/lib/postgresql/13/bin/pg_controldata
$ podman run --it --rm --entrypoint /usr/lib/postgresql/13/bin/pg_controldata   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/lib/postgresql/13/bin/pg_controldata   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pg_ctl
       
```bash
$ singularity exec <container> /usr/lib/postgresql/13/bin/pg_ctl
$ podman run --it --rm --entrypoint /usr/lib/postgresql/13/bin/pg_ctl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/lib/postgresql/13/bin/pg_ctl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pg_dump
       
```bash
$ singularity exec <container> /usr/lib/postgresql/13/bin/pg_dump
$ podman run --it --rm --entrypoint /usr/lib/postgresql/13/bin/pg_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/lib/postgresql/13/bin/pg_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pg_dumpall
       
```bash
$ singularity exec <container> /usr/lib/postgresql/13/bin/pg_dumpall
$ podman run --it --rm --entrypoint /usr/lib/postgresql/13/bin/pg_dumpall   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/lib/postgresql/13/bin/pg_dumpall   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pg_isready
       
```bash
$ singularity exec <container> /usr/lib/postgresql/13/bin/pg_isready
$ podman run --it --rm --entrypoint /usr/lib/postgresql/13/bin/pg_isready   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/lib/postgresql/13/bin/pg_isready   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pg_receivewal
       
```bash
$ singularity exec <container> /usr/lib/postgresql/13/bin/pg_receivewal
$ podman run --it --rm --entrypoint /usr/lib/postgresql/13/bin/pg_receivewal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/lib/postgresql/13/bin/pg_receivewal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pg_recvlogical
       
```bash
$ singularity exec <container> /usr/lib/postgresql/13/bin/pg_recvlogical
$ podman run --it --rm --entrypoint /usr/lib/postgresql/13/bin/pg_recvlogical   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/lib/postgresql/13/bin/pg_recvlogical   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pg_resetwal
       
```bash
$ singularity exec <container> /usr/lib/postgresql/13/bin/pg_resetwal
$ podman run --it --rm --entrypoint /usr/lib/postgresql/13/bin/pg_resetwal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/lib/postgresql/13/bin/pg_resetwal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pg_restore
       
```bash
$ singularity exec <container> /usr/lib/postgresql/13/bin/pg_restore
$ podman run --it --rm --entrypoint /usr/lib/postgresql/13/bin/pg_restore   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/lib/postgresql/13/bin/pg_restore   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pg_rewind
       
```bash
$ singularity exec <container> /usr/lib/postgresql/13/bin/pg_rewind
$ podman run --it --rm --entrypoint /usr/lib/postgresql/13/bin/pg_rewind   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/lib/postgresql/13/bin/pg_rewind   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pg_standby
       
```bash
$ singularity exec <container> /usr/lib/postgresql/13/bin/pg_standby
$ podman run --it --rm --entrypoint /usr/lib/postgresql/13/bin/pg_standby   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/lib/postgresql/13/bin/pg_standby   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pg_test_fsync
       
```bash
$ singularity exec <container> /usr/lib/postgresql/13/bin/pg_test_fsync
$ podman run --it --rm --entrypoint /usr/lib/postgresql/13/bin/pg_test_fsync   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/lib/postgresql/13/bin/pg_test_fsync   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pg_test_timing
       
```bash
$ singularity exec <container> /usr/lib/postgresql/13/bin/pg_test_timing
$ podman run --it --rm --entrypoint /usr/lib/postgresql/13/bin/pg_test_timing   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/lib/postgresql/13/bin/pg_test_timing   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pg_upgrade
       
```bash
$ singularity exec <container> /usr/lib/postgresql/13/bin/pg_upgrade
$ podman run --it --rm --entrypoint /usr/lib/postgresql/13/bin/pg_upgrade   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/lib/postgresql/13/bin/pg_upgrade   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pg_verifybackup
       
```bash
$ singularity exec <container> /usr/lib/postgresql/13/bin/pg_verifybackup
$ podman run --it --rm --entrypoint /usr/lib/postgresql/13/bin/pg_verifybackup   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/lib/postgresql/13/bin/pg_verifybackup   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pg_waldump
       
```bash
$ singularity exec <container> /usr/lib/postgresql/13/bin/pg_waldump
$ podman run --it --rm --entrypoint /usr/lib/postgresql/13/bin/pg_waldump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/lib/postgresql/13/bin/pg_waldump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pgbench
       
```bash
$ singularity exec <container> /usr/lib/postgresql/13/bin/pgbench
$ podman run --it --rm --entrypoint /usr/lib/postgresql/13/bin/pgbench   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/lib/postgresql/13/bin/pgbench   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### postgres
       
```bash
$ singularity exec <container> /usr/lib/postgresql/13/bin/postgres
$ podman run --it --rm --entrypoint /usr/lib/postgresql/13/bin/postgres   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/lib/postgresql/13/bin/postgres   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### postmaster
       
```bash
$ singularity exec <container> /usr/lib/postgresql/13/bin/postmaster
$ podman run --it --rm --entrypoint /usr/lib/postgresql/13/bin/postmaster   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/lib/postgresql/13/bin/postmaster   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### psql
       
```bash
$ singularity exec <container> /usr/lib/postgresql/13/bin/psql
$ podman run --it --rm --entrypoint /usr/lib/postgresql/13/bin/psql   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/lib/postgresql/13/bin/psql   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### reindexdb
       
```bash
$ singularity exec <container> /usr/lib/postgresql/13/bin/reindexdb
$ podman run --it --rm --entrypoint /usr/lib/postgresql/13/bin/reindexdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/lib/postgresql/13/bin/reindexdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vacuumdb
       
```bash
$ singularity exec <container> /usr/lib/postgresql/13/bin/vacuumdb
$ podman run --it --rm --entrypoint /usr/lib/postgresql/13/bin/vacuumdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/lib/postgresql/13/bin/vacuumdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vacuumlo
       
```bash
$ singularity exec <container> /usr/lib/postgresql/13/bin/vacuumlo
$ podman run --it --rm --entrypoint /usr/lib/postgresql/13/bin/vacuumlo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/lib/postgresql/13/bin/vacuumlo   -v ${PWD} -w ${PWD} <container> -c " $@"
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