---
layout: container
name:  "golang"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/golang/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/golang/container.yaml"
updated_at: "2022-08-27 02:53:46.951783"
latest: "1.19-rc"
container_url: "https://hub.docker.com/r/_/golang"
aliases:
 - "go"
 - "gofmt"
versions:
 - "1.16.4-alpine"
 - "1.16.5-alpine"
 - "1.17-rc-alpine"
 - "1.17.0"
 - "1.17.2"
 - "1.17.3"
 - "1.18-rc"
 - "latest"
 - "1"
 - "1.18"
 - "1.17rc2"
 - "1.17rc2-buster"
 - "1.19-rc"
 - "1.18-rc-buster"
description: "Go (a.k.a., Golang) is a programming language first developed at Google."
config: {"docker": "golang", "url": "https://hub.docker.com/r/_/golang", "maintainer": "@vsoch", "description": "Go (a.k.a., Golang) is a programming language first developed at Google.", "latest": {"1.19-rc": "sha256:d7bcbe801bdeaae4087c59a7519b7a82171f082478d86307a5ecd3e32aea7c18"}, "filter": ["^(?!nano).*$", "^(?!windows).*$"], "tags": {"1.16.4-alpine": "sha256:0dc62c5cc2d97657c17ff3bc0224214e10226e245c94317e352ee8a2c54368b4", "1.16.5-alpine": "sha256:45f32e963bb3cc408cfcd01a8e76b2872fb238f602ec5481cd75393da29369c0", "1.17-rc-alpine": "sha256:787111a3069abdb2c4d8c0b27dff2a29cef8b147f8e7a431f5a464ea84ebfa41", "1.17.0": "sha256:7dbfeb9d51c049e8bfe36cf1a4217c7b1ba304bf0eb72d57d0c04f405589f122", "1.17.2": "sha256:124966f5d54a41317ee81ccfe5f849d4f0deef4ed3c5c32c20be855c51c15027", "1.17.3": "sha256:199102125d11c943c927a8a33911ef960ca72c4879e307c7c2e40ceaa72201e3", "1.18-rc": "sha256:2da497bcc0c9ff09d4185907068c6f137d14e8848059971072f2e9cc936aae70", "latest": "sha256:a452d6273ad03a47c2f29b898d6bb57630e77baf839651ef77d03e4e049c5bf3", "1": "sha256:a452d6273ad03a47c2f29b898d6bb57630e77baf839651ef77d03e4e049c5bf3", "1.18": "sha256:a452d6273ad03a47c2f29b898d6bb57630e77baf839651ef77d03e4e049c5bf3", "1.17rc2": "sha256:c5b50f8381dcc9223b63dbb3e9f558eea0650310232bbc2dde8c3b861c60d1b2", "1.17rc2-buster": "sha256:824267ad82d38a31225b61038ac8735b791396d7df2a6c58f761756964ab4d2d", "1.19-rc": "sha256:d7bcbe801bdeaae4087c59a7519b7a82171f082478d86307a5ecd3e32aea7c18", "1.18-rc-buster": "sha256:9acf37d060418071d7dbad182979fedc8289eaff0105806a0de2d1a389716fa6"}, "aliases": {"go": "/usr/local/go/bin/go", "gofmt": "/usr/local/go/bin/gofmt"}}
---

This module is a singularity container wrapper for golang.
Go (a.k.a., Golang) is a programming language first developed at Google.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install golang
```

Or a specific version:

```bash
$ shpc install golang:1.16.4-alpine
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load golang/1.16.4-alpine
$ module help golang/1.16.4-alpine
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### golang-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### golang-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### golang-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### golang-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### golang-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### golang-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### go
       
```bash
$ singularity exec <container> /usr/local/go/bin/go
$ podman run --it --rm --entrypoint /usr/local/go/bin/go   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/go/bin/go   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gofmt
       
```bash
$ singularity exec <container> /usr/local/go/bin/gofmt
$ podman run --it --rm --entrypoint /usr/local/go/bin/gofmt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/go/bin/gofmt   -v ${PWD} -w ${PWD} <container> -c " $@"
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