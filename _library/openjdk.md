---
layout: container
name:  "openjdk"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/openjdk/container.yaml"
updated_at: "2021-06-22 03:45:50.277034"
container_url: "https://hub.docker.com/_/openjdk"
aliases:
 - "jar"

 - "jarsigner"

 - "java"

 - "javac"

 - "javadoc"

 - "javap"

 - "jcmd"

 - "jconsole"

 - "jdb"

 - "jdeprscan"

 - "jdeps"

 - "jfr"

 - "jhsdb"

 - "jimage"

 - "jinfo"

 - "jlink"

 - "jmap"

 - "jmod"

 - "jobs"

 - "join"

 - "jpackage"

 - "jps"

 - "jrunscript"

 - "jshell"

 - "jstack"

 - "jstat"

 - "jstatd"

versions:
 - "16.0.1-buster"
 - "latest"
description: "OpenJDK is an open-source implementation of the Java Platform, Standard Edition."
---

This module is a singularity container wrapper for openjdk.
OpenJDK is an open-source implementation of the Java Platform, Standard Edition.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install openjdk
```

Or a specific version:

```bash
$ shpc install openjdk:16.0.1-buster
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load openjdk/16.0.1-buster
$ module help openjdk/16.0.1-buster
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### -run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### -shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### -exec:

```bash
$ singularity exec -s /bin/sh <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### -inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### -inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### -inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### jar
       
```bash
$ singularity exec <container> /usr/bin/jar
$ podman run --it --rm --entrypoint /usr/bin/jar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/jar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jarsigner
       
```bash
$ singularity exec <container> /usr/bin/jarsigner
$ podman run --it --rm --entrypoint /usr/bin/jarsigner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/jarsigner   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### java
       
```bash
$ singularity exec <container> /usr/bin/java
$ podman run --it --rm --entrypoint /usr/bin/java   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/java   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### javac
       
```bash
$ singularity exec <container> /usr/bin/javac
$ podman run --it --rm --entrypoint /usr/bin/javac   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/javac   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### javadoc
       
```bash
$ singularity exec <container> /usr/bin/javadoc
$ podman run --it --rm --entrypoint /usr/bin/javadoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/javadoc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### javap
       
```bash
$ singularity exec <container> /usr/bin/javap
$ podman run --it --rm --entrypoint /usr/bin/javap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/javap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jcmd
       
```bash
$ singularity exec <container> /usr/bin/jcmd
$ podman run --it --rm --entrypoint /usr/bin/jcmd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/jcmd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jconsole
       
```bash
$ singularity exec <container> /usr/bin/jconsole
$ podman run --it --rm --entrypoint /usr/bin/jconsole   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/jconsole   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jdb
       
```bash
$ singularity exec <container> /usr/bin/jdb
$ podman run --it --rm --entrypoint /usr/bin/jdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/jdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jdeprscan
       
```bash
$ singularity exec <container> /usr/bin/jdeprscan
$ podman run --it --rm --entrypoint /usr/bin/jdeprscan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/jdeprscan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jdeps
       
```bash
$ singularity exec <container> /usr/bin/jdeps
$ podman run --it --rm --entrypoint /usr/bin/jdeps   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/jdeps   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jfr
       
```bash
$ singularity exec <container> /usr/bin/jfr
$ podman run --it --rm --entrypoint /usr/bin/jfr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/jfr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jhsdb
       
```bash
$ singularity exec <container> /usr/bin/jhsdb
$ podman run --it --rm --entrypoint /usr/bin/jhsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/jhsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jimage
       
```bash
$ singularity exec <container> /usr/bin/jimage
$ podman run --it --rm --entrypoint /usr/bin/jimage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/jimage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jinfo
       
```bash
$ singularity exec <container> /usr/bin/jinfo
$ podman run --it --rm --entrypoint /usr/bin/jinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/jinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jlink
       
```bash
$ singularity exec <container> /usr/bin/jlink
$ podman run --it --rm --entrypoint /usr/bin/jlink   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/jlink   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jmap
       
```bash
$ singularity exec <container> /usr/bin/jmap
$ podman run --it --rm --entrypoint /usr/bin/jmap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/jmap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jmod
       
```bash
$ singularity exec <container> /usr/bin/jmod
$ podman run --it --rm --entrypoint /usr/bin/jmod   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/jmod   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jobs
       
```bash
$ singularity exec <container> /usr/bin/jobs
$ podman run --it --rm --entrypoint /usr/bin/jobs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/jobs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### join
       
```bash
$ singularity exec <container> /usr/bin/join
$ podman run --it --rm --entrypoint /usr/bin/join   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/join   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jpackage
       
```bash
$ singularity exec <container> /usr/bin/jpackage
$ podman run --it --rm --entrypoint /usr/bin/jpackage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/jpackage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jps
       
```bash
$ singularity exec <container> /usr/bin/jps
$ podman run --it --rm --entrypoint /usr/bin/jps   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/jps   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jrunscript
       
```bash
$ singularity exec <container> /usr/bin/jrunscript
$ podman run --it --rm --entrypoint /usr/bin/jrunscript   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/jrunscript   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jshell
       
```bash
$ singularity exec <container> /usr/bin/jshell
$ podman run --it --rm --entrypoint /usr/bin/jshell   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/jshell   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jstack
       
```bash
$ singularity exec <container> /usr/bin/jstack
$ podman run --it --rm --entrypoint /usr/bin/jstack   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/jstack   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jstat
       
```bash
$ singularity exec <container> /usr/bin/jstat
$ podman run --it --rm --entrypoint /usr/bin/jstat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/jstat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jstatd
       
```bash
$ singularity exec <container> /usr/bin/jstatd
$ podman run --it --rm --entrypoint /usr/bin/jstatd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/bin/jstatd   -v ${PWD} -w ${PWD} <container> -c " $@"
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