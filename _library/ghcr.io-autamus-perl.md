---
layout: container
name:  "ghcr.io/autamus/perl"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/perl/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/ghcr.io/autamus/perl/container.yaml"
updated_at: "2022-08-27 02:53:07.423201"
latest: "5.35.0"
container_url: "https://github.com/orgs/autamus/packages/container/package/perl"
aliases:
 - "perl"
 - "perlbug"
 - "perldoc"
 - "perlivp"
 - "perlthanks"
versions:
 - "5.33.3"
 - "5.35.0"
 - "latest"
description: "The Perl programming language."
config: {"docker": "ghcr.io/autamus/perl", "url": "https://github.com/orgs/autamus/packages/container/package/perl", "maintainer": "@vsoch", "description": "The Perl programming language.", "latest": {"5.35.0": "sha256:52533a12008858c35d966a9d3f6743f01e75b206cb16760d367f80206f071e4d"}, "tags": {"5.33.3": "sha256:ddbe04d704c8883aed0959dbd88bd8410cf5e1a6775a2f46264af306723b6459", "5.35.0": "sha256:52533a12008858c35d966a9d3f6743f01e75b206cb16760d367f80206f071e4d", "latest": "sha256:52533a12008858c35d966a9d3f6743f01e75b206cb16760d367f80206f071e4d"}, "aliases": {"perl": "/opt/view/bin/perl", "perlbug": "/opt/view/bin/perlbug", "perldoc": "/opt/view/bin/perldoc", "perlivp": "/opt/view/bin/perlivp", "perlthanks": "/opt/view/bin/perlthanks"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/perl.
The Perl programming language.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/perl
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/perl:5.33.3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/perl/5.33.3
$ module help ghcr.io/autamus/perl/5.33.3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### perl
       
```bash
$ singularity exec <container> /opt/view/bin/perl
$ podman run --it --rm --entrypoint /opt/view/bin/perl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/perl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perlbug
       
```bash
$ singularity exec <container> /opt/view/bin/perlbug
$ podman run --it --rm --entrypoint /opt/view/bin/perlbug   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/perlbug   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perldoc
       
```bash
$ singularity exec <container> /opt/view/bin/perldoc
$ podman run --it --rm --entrypoint /opt/view/bin/perldoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/perldoc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perlivp
       
```bash
$ singularity exec <container> /opt/view/bin/perlivp
$ podman run --it --rm --entrypoint /opt/view/bin/perlivp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/perlivp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perlthanks
       
```bash
$ singularity exec <container> /opt/view/bin/perlthanks
$ podman run --it --rm --entrypoint /opt/view/bin/perlthanks   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/perlthanks   -v ${PWD} -w ${PWD} <container> -c " $@"
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