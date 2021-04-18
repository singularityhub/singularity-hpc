---
layout: container
name:  "tomcat"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/tomcat/container.yaml"
updated_at: "2021-04-18 08:27:34.082770"
container_url: ""

versions:
 - "latest"
description: "Apache Tomcat is an open source implementation of the Java Servlet and JavaServer Pages technologies"
---

This module is a singularity container wrapper for tomcat.
Apache Tomcat is an open source implementation of the Java Servlet and JavaServer Pages technologies
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install tomcat
```

Or a specific version:

```bash
$ shpc install tomcat:latest
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load tomcat/latest
$ module help tomcat/latest
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### tomcat-run:

```bash
$ singularity run <container>
```

#### tomcat-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### tomcat-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### tomcat-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### tomcat-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### tomcat

```bash
$ singularity run <container>
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