---
layout: container
name:  "openjdk"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/openjdk/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/openjdk/container.yaml"
updated_at: "2022-08-27 01:37:15.706849"
latest: "20"
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
 - "16.0.2"
 - "17.0.1"
 - "17.0.2"
 - "latest"
 - "19"
 - "19-alpine3.15"
 - "18"
 - "18-alpine3.15"
 - "17"
 - "18.0"
 - "19-alpine3.16"
 - "20"
description: "OpenJDK is an open-source implementation of the Java Platform, Standard Edition."
config: {"docker": "openjdk", "url": "https://hub.docker.com/_/openjdk", "maintainer": "@vsoch", "description": "OpenJDK is an open-source implementation of the Java Platform, Standard Edition.", "filter": ["^(?!.*ea).*$", "^(?!.*windows).*$", "^(?!.*nanoserver).*$", "^(?!.*oracle).*$"], "latest": {"20": "sha256:3a1dc196fbb30b56a7e02d41c8f2a229e7312660623177328a6696d022fea458"}, "tags": {"16.0.1-buster": "sha256:61f3786a28ed911028f8e7e3b65a57a8a9ed04067d137317d369c9b3bc11b289", "16.0.2": "sha256:bb68f084c2000c8532b1675ca7034f3922f4aa10e9c7126d29551c0ffd6dee8f", "17.0.1": "sha256:0da39ed69dec14f9603e2b916592691cc39341510abdf4255abb1c90b00eb3f4", "17.0.2": "sha256:528707081fdb9562eb819128a9f85ae7fe000e2fbaeaf9f87662e7b3f38cb7d8", "latest": "sha256:4ad8520b57104264bd155c787b2f6093b1fd3baa71763ab54792b3920f9e1956", "19": "sha256:fedc326a3e7be8d49380989386b97692c5982e4e63fe81923b811ec64262b453", "19-alpine3.15": "sha256:fd8c856fb7e3fc2d93815c4b9fa1d112c8d9f46d01f64c6ea858d33518555e5f", "18": "sha256:4ad8520b57104264bd155c787b2f6093b1fd3baa71763ab54792b3920f9e1956", "18-alpine3.15": "sha256:e5c5b35b831a4f655074a25604130ce53e33567b82c8a7204f0e5641b66d477e", "17": "sha256:528707081fdb9562eb819128a9f85ae7fe000e2fbaeaf9f87662e7b3f38cb7d8", "18.0": "sha256:4ad8520b57104264bd155c787b2f6093b1fd3baa71763ab54792b3920f9e1956", "19-alpine3.16": "sha256:f59fa1224f4af28299e484fd72c13549408b69b20ba4ad3b590a854df22dfd46", "20": "sha256:3a1dc196fbb30b56a7e02d41c8f2a229e7312660623177328a6696d022fea458"}, "aliases": {"jar": "/usr/bin/jar", "jarsigner": "/usr/bin/jarsigner", "java": "/usr/bin/java", "javac": "/usr/bin/javac", "javadoc": "/usr/bin/javadoc", "javap": "/usr/bin/javap", "jcmd": "/usr/bin/jcmd", "jconsole": "/usr/bin/jconsole", "jdb": "/usr/bin/jdb", "jdeprscan": "/usr/bin/jdeprscan", "jdeps": "/usr/bin/jdeps", "jfr": "/usr/bin/jfr", "jhsdb": "/usr/bin/jhsdb", "jimage": "/usr/bin/jimage", "jinfo": "/usr/bin/jinfo", "jlink": "/usr/bin/jlink", "jmap": "/usr/bin/jmap", "jmod": "/usr/bin/jmod", "jobs": "/usr/bin/jobs", "join": "/usr/bin/join", "jpackage": "/usr/bin/jpackage", "jps": "/usr/bin/jps", "jrunscript": "/usr/bin/jrunscript", "jshell": "/usr/bin/jshell", "jstack": "/usr/bin/jstack", "jstat": "/usr/bin/jstat", "jstatd": "/usr/bin/jstatd"}}
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

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### openjdk-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### openjdk-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### openjdk-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### openjdk-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### openjdk-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### openjdk-inspect-deffile:

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