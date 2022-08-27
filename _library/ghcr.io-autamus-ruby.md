---
layout: container
name:  "ghcr.io/autamus/ruby"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/ruby/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/ghcr.io/autamus/ruby/container.yaml"
updated_at: "2022-08-27 01:36:41.907388"
latest: "3.1.0"
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
 - "3.0.2"
 - "3.1.0"
 - "latest"
description: "An interpreted, high-level, general-purpose programming language."
config: {"docker": "ghcr.io/autamus/ruby", "url": "https://github.com/orgs/autamus/packages/container/package/ruby", "maintainer": "@vsoch", "description": "An interpreted, high-level, general-purpose programming language.", "latest": {"3.1.0": "sha256:2090e247c5efcff49e18b1d80f37091251376e6f8321c97e9b886b9fb442e859"}, "tags": {"3.0.0": "sha256:13449cbf4d0edc53e79bb7d8080b8a3ce34b2ff26219ea1318c7122d1f497208", "3.0.2": "sha256:8c9057626f354e76b6550c7081b628f434b27951058bdd64b76d4f7b24463e8a", "3.1.0": "sha256:2090e247c5efcff49e18b1d80f37091251376e6f8321c97e9b886b9fb442e859", "latest": "sha256:2090e247c5efcff49e18b1d80f37091251376e6f8321c97e9b886b9fb442e859"}, "aliases": {"bundle": "/opt/view/bin/bundle", "bundler": "/opt/view/bin/bundler", "erb": "/opt/view/bin/erb", "gem": "/opt/view/bin/gem", "irb": "/opt/view/bin/irb", "racc": "/opt/view/bin/racc", "rake": "/opt/view/bin/rake", "rbs": "/opt/view/bin/rbs", "rdoc": "/opt/view/bin/rdoc", "ri": "/opt/view/bin/ri", "ruby": "/opt/view/bin/ruby"}}
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

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ruby-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ruby-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ruby-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ruby-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ruby-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ruby-inspect-deffile:

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