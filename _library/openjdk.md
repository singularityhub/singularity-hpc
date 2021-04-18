---
layout: container
name:  "openjdk"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/openjdk/container.yaml"
updated_at: "2021-04-18 08:29:27.691207"
container_url: ""
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
$ shpc install openjdk:latest
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load openjdk/latest
$ module help openjdk/latest
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### openjdk-run:

```bash
$ singularity run <container>
```

#### openjdk-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### openjdk-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
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
```


#### jarsigner
       
```bash
$ singularity exec <container> /usr/bin/jarsigner
```


#### java
       
```bash
$ singularity exec <container> /usr/bin/java
```


#### javac
       
```bash
$ singularity exec <container> /usr/bin/javac
```


#### javadoc
       
```bash
$ singularity exec <container> /usr/bin/javadoc
```


#### javap
       
```bash
$ singularity exec <container> /usr/bin/javap
```


#### jcmd
       
```bash
$ singularity exec <container> /usr/bin/jcmd
```


#### jconsole
       
```bash
$ singularity exec <container> /usr/bin/jconsole
```


#### jdb
       
```bash
$ singularity exec <container> /usr/bin/jdb
```


#### jdeprscan
       
```bash
$ singularity exec <container> /usr/bin/jdeprscan
```


#### jdeps
       
```bash
$ singularity exec <container> /usr/bin/jdeps
```


#### jfr
       
```bash
$ singularity exec <container> /usr/bin/jfr
```


#### jhsdb
       
```bash
$ singularity exec <container> /usr/bin/jhsdb
```


#### jimage
       
```bash
$ singularity exec <container> /usr/bin/jimage
```


#### jinfo
       
```bash
$ singularity exec <container> /usr/bin/jinfo
```


#### jlink
       
```bash
$ singularity exec <container> /usr/bin/jlink
```


#### jmap
       
```bash
$ singularity exec <container> /usr/bin/jmap
```


#### jmod
       
```bash
$ singularity exec <container> /usr/bin/jmod
```


#### jobs
       
```bash
$ singularity exec <container> /usr/bin/jobs
```


#### join
       
```bash
$ singularity exec <container> /usr/bin/join
```


#### jpackage
       
```bash
$ singularity exec <container> /usr/bin/jpackage
```


#### jps
       
```bash
$ singularity exec <container> /usr/bin/jps
```


#### jrunscript
       
```bash
$ singularity exec <container> /usr/bin/jrunscript
```


#### jshell
       
```bash
$ singularity exec <container> /usr/bin/jshell
```


#### jstack
       
```bash
$ singularity exec <container> /usr/bin/jstack
```


#### jstat
       
```bash
$ singularity exec <container> /usr/bin/jstat
```


#### jstatd
       
```bash
$ singularity exec <container> /usr/bin/jstatd
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