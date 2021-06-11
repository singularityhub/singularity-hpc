---
layout: container
name:  "ghcr.io/autamus/ruby"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/ruby/container.yaml"
updated_at: "2021-06-11 05:58:06.734051"
container_url: "https://github.com/orgs/autamus/packages/container/package/ruby"
aliases:
 - "bundle"

 - "bundler"

 - "erb"

 - "gem"

 - "irb"

 - "racc"

 - "rake"

 - "rbs"

 - "rdoc"

 - "ri"

 - "ruby"

versions:
 - "3.0.0"
 - "latest"
description: "An interpreted, high-level, general-purpose programming language."
---

This module is a singularity container wrapper for ghcr.io/autamus/ruby.
An interpreted, high-level, general-purpose programming language.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install ghcr.io/autamus/ruby
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/ruby:3.0.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/ruby/3.0.0
$ module help ghcr.io/autamus/ruby/3.0.0
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


#### bundle
       
```bash
$ singularity exec <container> /opt/view/bin/bundle
$ podman run --it --rm --entrypoint /opt/view/bin/bundle   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/bundle   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bundler
       
```bash
$ singularity exec <container> /opt/view/bin/bundler
$ podman run --it --rm --entrypoint /opt/view/bin/bundler   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/bundler   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### erb
       
```bash
$ singularity exec <container> /opt/view/bin/erb
$ podman run --it --rm --entrypoint /opt/view/bin/erb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/erb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gem
       
```bash
$ singularity exec <container> /opt/view/bin/gem
$ podman run --it --rm --entrypoint /opt/view/bin/gem   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/gem   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### irb
       
```bash
$ singularity exec <container> /opt/view/bin/irb
$ podman run --it --rm --entrypoint /opt/view/bin/irb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/irb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### racc
       
```bash
$ singularity exec <container> /opt/view/bin/racc
$ podman run --it --rm --entrypoint /opt/view/bin/racc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/racc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rake
       
```bash
$ singularity exec <container> /opt/view/bin/rake
$ podman run --it --rm --entrypoint /opt/view/bin/rake   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/rake   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rbs
       
```bash
$ singularity exec <container> /opt/view/bin/rbs
$ podman run --it --rm --entrypoint /opt/view/bin/rbs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/rbs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rdoc
       
```bash
$ singularity exec <container> /opt/view/bin/rdoc
$ podman run --it --rm --entrypoint /opt/view/bin/rdoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/rdoc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ri
       
```bash
$ singularity exec <container> /opt/view/bin/ri
$ podman run --it --rm --entrypoint /opt/view/bin/ri   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/ri   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ruby
       
```bash
$ singularity exec <container> /opt/view/bin/ruby
$ podman run --it --rm --entrypoint /opt/view/bin/ruby   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/ruby   -v ${PWD} -w ${PWD} <container> -c " $@"
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