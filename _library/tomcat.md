---
layout: container
name:  "tomcat"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/tomcat/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/tomcat/container.yaml"
updated_at: "2022-08-27 02:54:43.710554"
latest: "10-jdk17"
container_url: "https://hub.docker.com/_/tomcat"

versions:
 - "10.0.5-jdk11-adoptopenjdk-hotspot"
 - "10.0.6-jdk11-adoptopenjdk-hotspot"
 - "10.0.7-jdk11-adoptopenjdk-hotspot"
 - "10.0.8-jdk11-adoptopenjdk-hotspot"
 - "10.1.0"
 - "latest"
 - "10"
 - "10-jdk17"
 - "10-jdk16"
 - "10-jdk15"
 - "10-jdk14"
description: "Apache Tomcat is an open source implementation of the Java Servlet and JavaServer Pages technologies"
config: {"docker": "tomcat", "url": "https://hub.docker.com/_/tomcat", "maintainer": "@vsoch", "description": "Apache Tomcat is an open source implementation of the Java Servlet and JavaServer Pages technologies", "filter": ["^(?!jdk1[1-7]).*$"], "latest": {"10-jdk17": "sha256:9edc5c51c2dec7794769eede1e88a60e77abe355b73a77e231c464a8384d3697"}, "tags": {"10.0.5-jdk11-adoptopenjdk-hotspot": "sha256:a7418f29d3dd7ad20bcf052b3b6dc2777d118344286c6374bc447fb217a97c08", "10.0.6-jdk11-adoptopenjdk-hotspot": "sha256:c0019c8254bc1017f64e6ffd1612e25b50abca78d98d25f9ff8023e8999f0384", "10.0.7-jdk11-adoptopenjdk-hotspot": "sha256:d75c50123194e5533dd8b397175fab79c9dff69ed5c0bada70be5dff6d8fcc6d", "10.0.8-jdk11-adoptopenjdk-hotspot": "sha256:98ae9e70b3bd2129c2ef83179c38bc902e613f433c6222c88b2c1a2f3bdfd1ec", "10.1.0": "sha256:835fce245528f2257a944eefc05810e2c3ed4e752cc13ce6f52c64abe9d6ae61", "latest": "sha256:9edc5c51c2dec7794769eede1e88a60e77abe355b73a77e231c464a8384d3697", "10": "sha256:9edc5c51c2dec7794769eede1e88a60e77abe355b73a77e231c464a8384d3697", "10-jdk17": "sha256:9edc5c51c2dec7794769eede1e88a60e77abe355b73a77e231c464a8384d3697", "10-jdk16": "sha256:06894e19b914a4e491580d54091ac248d53b0c4c474ff9e55e97e27d9adb45d5", "10-jdk15": "sha256:822bc61a43b972b5f784af5f8f40ce077399c06cfa724fc1cd60ea687f5d9828", "10-jdk14": "sha256:e97bde5b2bba850a96ba59b5500e9448216c989c0061a4e7e5c8d9d64185a36e"}}
---

This module is a singularity container wrapper for tomcat.
Apache Tomcat is an open source implementation of the Java Servlet and JavaServer Pages technologies
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install tomcat
```

Or a specific version:

```bash
$ shpc install tomcat:10.0.5-jdk11-adoptopenjdk-hotspot
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load tomcat/10.0.5-jdk11-adoptopenjdk-hotspot
$ module help tomcat/10.0.5-jdk11-adoptopenjdk-hotspot
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### tomcat-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### tomcat-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### tomcat-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### tomcat-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
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
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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