---
layout: container
name:  "ghcr.io/autamus/bismark"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/bismark/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/ghcr.io/autamus/bismark/container.yaml"
updated_at: "2022-08-27 01:35:35.099954"
latest: "0.23.1"
container_url: "https://github.com/orgs/autamus/packages/container/package/bismark"
aliases:
 - "bismark"
 - "bismark_genome_preparation"
 - "bismark_methylation_extractor"
 - "bismark2bedGraph"
 - "bismark2report"
 - "bismark2summary"
versions:
 - "0.23.0"
 - "0.23.1"
 - "latest"
description: "Bismark is a program to map bisulfite treated sequencing reads to a genome of interest and perform methylation calls in a single step."
config: {"docker": "ghcr.io/autamus/bismark", "url": "https://github.com/orgs/autamus/packages/container/package/bismark", "maintainer": "@vsoch", "description": "Bismark is a program to map bisulfite treated sequencing reads to a genome of interest and perform methylation calls in a single step.", "latest": {"0.23.1": "sha256:2442def08bb76e9a31575e950cb25f584b1b3b1945441f1a5aee15144fa9e2fb"}, "tags": {"0.23.0": "sha256:297e5839757a5ae3d7f383fd8716c8dad44ce8653f63a85df238a12f85875bee", "0.23.1": "sha256:2442def08bb76e9a31575e950cb25f584b1b3b1945441f1a5aee15144fa9e2fb", "latest": "sha256:2442def08bb76e9a31575e950cb25f584b1b3b1945441f1a5aee15144fa9e2fb"}, "aliases": {"bismark": "/opt/view/bin/bismark", "bismark_genome_preparation": "/opt/view/bin/bismark_genome_preparation", "bismark_methylation_extractor": "/opt/view/bin/bismark_methylation_extractor", "bismark2bedGraph": "/opt/view/bin/bismark2bedGraph", "bismark2report": "/opt/view/bin/bismark2report", "bismark2summary": "/opt/view/bin/bismark2summary"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/bismark.
Bismark is a program to map bisulfite treated sequencing reads to a genome of interest and perform methylation calls in a single step.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/bismark
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/bismark:0.23.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/bismark/0.23.0
$ module help ghcr.io/autamus/bismark/0.23.0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bismark-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bismark-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bismark-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bismark-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bismark-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bismark-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bismark
       
```bash
$ singularity exec <container> /opt/view/bin/bismark
$ podman run --it --rm --entrypoint /opt/view/bin/bismark   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/bismark   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bismark_genome_preparation
       
```bash
$ singularity exec <container> /opt/view/bin/bismark_genome_preparation
$ podman run --it --rm --entrypoint /opt/view/bin/bismark_genome_preparation   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/bismark_genome_preparation   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bismark_methylation_extractor
       
```bash
$ singularity exec <container> /opt/view/bin/bismark_methylation_extractor
$ podman run --it --rm --entrypoint /opt/view/bin/bismark_methylation_extractor   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/bismark_methylation_extractor   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bismark2bedGraph
       
```bash
$ singularity exec <container> /opt/view/bin/bismark2bedGraph
$ podman run --it --rm --entrypoint /opt/view/bin/bismark2bedGraph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/bismark2bedGraph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bismark2report
       
```bash
$ singularity exec <container> /opt/view/bin/bismark2report
$ podman run --it --rm --entrypoint /opt/view/bin/bismark2report   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/bismark2report   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bismark2summary
       
```bash
$ singularity exec <container> /opt/view/bin/bismark2summary
$ podman run --it --rm --entrypoint /opt/view/bin/bismark2summary   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/bismark2summary   -v ${PWD} -w ${PWD} <container> -c " $@"
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