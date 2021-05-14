---
layout: container
name:  "ghcr.io/autamus/openjdk"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/openjdk/container.yaml"
updated_at: "2021-05-14 14:52:59.531447"
container_url: "https://github.com/orgs/autamus/packages/container/package/openjdk"
aliases:
 - "jaotc"

 - "javadoc"

 - "jinfo"

 - "jps"

 - "jstatd"

 - "jar"

 - "javap"

 - "jdeps"

 - "jjs"

 - "jrunscript"

 - "jarsigner"

 - "jcmd"

 - "jfr"

 - "jlink"

 - "jshell"

 - "java"

 - "jconsole"

 - "jhsdb"

 - "jmap"

 - "jstack"

 - "javac"

 - "jdb"

 - "jimage"

 - "jmod"

 - "jstat"

versions:
 - "latest"
description: "Open Java Development Kit"
---

This module is a singularity container wrapper for ghcr.io/autamus/openjdk.
Open Java Development Kit
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install ghcr.io/autamus/openjdk
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/openjdk:latest
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/openjdk/latest
$ module help ghcr.io/autamus/openjdk/latest
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### ghcr.io-autamus-openjdk-run:

```bash
$ singularity run <container>
```

#### ghcr.io-autamus-openjdk-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### ghcr.io-autamus-openjdk-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### ghcr.io-autamus-openjdk-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ghcr.io-autamus-openjdk-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### jaotc
       
```bash
$ singularity exec <container> /opt/view/bin/jaotc
```


#### javadoc
       
```bash
$ singularity exec <container> /opt/view/bin/javadoc
```


#### jinfo
       
```bash
$ singularity exec <container> /opt/view/bin/jinfo
```


#### jps
       
```bash
$ singularity exec <container> /opt/view/bin/jps
```


#### jstatd
       
```bash
$ singularity exec <container> /opt/view/bin/jstatd
```


#### jar
       
```bash
$ singularity exec <container> /opt/view/bin/jar
```


#### javap
       
```bash
$ singularity exec <container> /opt/view/bin/javap
```


#### jdeps
       
```bash
$ singularity exec <container> /opt/view/bin/jdeps
```


#### jjs
       
```bash
$ singularity exec <container> /opt/view/bin/jjs
```


#### jrunscript
       
```bash
$ singularity exec <container> /opt/view/bin/jrunscript
```


#### jarsigner
       
```bash
$ singularity exec <container> /opt/view/bin/jarsigner
```


#### jcmd
       
```bash
$ singularity exec <container> /opt/view/bin/jcmd
```


#### jfr
       
```bash
$ singularity exec <container> /opt/view/bin/jfr
```


#### jlink
       
```bash
$ singularity exec <container> /opt/view/bin/jlink
```


#### jshell
       
```bash
$ singularity exec <container> /opt/view/bin/jshell
```


#### java
       
```bash
$ singularity exec <container> /opt/view/bin/java
```


#### jconsole
       
```bash
$ singularity exec <container> /opt/view/bin/jconsole
```


#### jhsdb
       
```bash
$ singularity exec <container> /opt/view/bin/jhsdb
```


#### jmap
       
```bash
$ singularity exec <container> /opt/view/bin/jmap
```


#### jstack
       
```bash
$ singularity exec <container> /opt/view/bin/jstack
```


#### javac
       
```bash
$ singularity exec <container> /opt/view/bin/javac
```


#### jdb
       
```bash
$ singularity exec <container> /opt/view/bin/jdb
```


#### jimage
       
```bash
$ singularity exec <container> /opt/view/bin/jimage
```


#### jmod
       
```bash
$ singularity exec <container> /opt/view/bin/jmod
```


#### jstat
       
```bash
$ singularity exec <container> /opt/view/bin/jstat
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