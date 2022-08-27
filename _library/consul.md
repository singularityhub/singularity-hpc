---
layout: container
name:  "consul"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/consul/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/consul/container.yaml"
updated_at: "2022-08-27 02:51:40.100037"
latest: "1.12"
container_url: "https://hub.docker.com/_/consul"
aliases:
 - "consul"
versions:
 - "1.7"
 - "1.7.14"
 - "1.10.0-beta"
 - "1.10.2"
 - "1.10.3"
 - "1.11.0-beta"
 - "1.11.1"
 - "1.11.2"
 - "1.11.3"
 - "latest"
 - "1.11"
 - "1.10"
 - "1.9"
 - "1.8"
 - "1.12"
description: "Consul is a datacenter runtime that provides service discovery, configuration, and orchestration."
config: {"docker": "consul", "url": "https://hub.docker.com/_/consul", "maintainer": "@vsoch", "description": "Consul is a datacenter runtime that provides service discovery, configuration, and orchestration.", "latest": {"1.12": "sha256:ee0735e34f80030c46002f71bc594f25e3f586202da8784b43b4050993ef2445"}, "tags": {"1.7": "sha256:fce4d3cbf7d610394f5c862356f0bddc652c0062c6fb078bc7a67a8831d55d97", "1.7.14": "sha256:fce4d3cbf7d610394f5c862356f0bddc652c0062c6fb078bc7a67a8831d55d97", "1.10.0-beta": "sha256:a3a7e4fca544b3d64a36a361e3bfe814eb052df2cd76f5dd48c5005124850338", "1.10.2": "sha256:5f59265e0ddcbfadee9f18038a02e5a465242fb4f514fc0b19fc445df49ef23b", "1.10.3": "sha256:483b592fa76d734882cf7336df94a5bf6f9e808a78b1a1ba17002a2aaf80da46", "1.11.0-beta": "sha256:b65caa85b885338a6a5ff8f11b5588ccc32f6534329b4ba39191f5d4292d2331", "1.11.1": "sha256:05d70d30639d5e0411f92fb75dd670ec1ef8fa4a918c6e57960db1710fd38125", "1.11.2": "sha256:43cc31d422649c88fec7f5c146110854149da68ee70c505f5bbd667c71bc698a", "1.11.3": "sha256:019e7f964280cd5719d60b8887fe20a349d1a0365acd06290ac1b055101d4e1c", "latest": "sha256:ee0735e34f80030c46002f71bc594f25e3f586202da8784b43b4050993ef2445", "1.11": "sha256:b046770864f58edfa6bb58640677396a66a29efb6e193c973d7f87e15ee6f6fe", "1.10": "sha256:644f8d0032fdb8af9f693892cb15bc734fff1f3ab821c709eb0cb432c07c4332", "1.9": "sha256:46ccd87fe5d42aa4d7d55522f64ab389dc2b4148f07011313d824e06d9f666ca", "1.8": "sha256:93cb9286a1ec5e084193fd2b625977df74003a81e8bc373f5adf900bb87318d4", "1.12": "sha256:ee0735e34f80030c46002f71bc594f25e3f586202da8784b43b4050993ef2445"}, "aliases": {"consul": "/bin/consul"}}
---

This module is a singularity container wrapper for consul.
Consul is a datacenter runtime that provides service discovery, configuration, and orchestration.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install consul
```

Or a specific version:

```bash
$ shpc install consul:1.7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load consul/1.7
$ module help consul/1.7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### consul-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### consul-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### consul-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### consul-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### consul-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### consul-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### consul
       
```bash
$ singularity exec <container> /bin/consul
$ podman run --it --rm --entrypoint /bin/consul   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /bin/consul   -v ${PWD} -w ${PWD} <container> -c " $@"
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