---
layout: container
name:  "vault"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/vault/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/vault/container.yaml"
updated_at: "2022-08-27 01:37:46.995386"
latest: "1.11.0"
container_url: "https://hub.docker.com/_/vault"
aliases:
 - "vault"
versions:
 - "1.4.7"
 - "1.7.1"
 - "1.7.2"
 - "1.8.0-rc1"
 - "1.8.2"
 - "1.8.4"
 - "1.9.0"
 - "1.9.2"
 - "1.9.3"
 - "latest"
 - "1.10.0"
 - "1.9.4"
 - "1.8.9"
 - "1.7.10"
 - "1.6.7"
 - "1.10.2"
 - "1.9.6"
 - "1.8.11"
 - "1.10.3"
 - "1.11.0"
 - "1.10.4"
 - "1.9.7"
 - "1.8.12"
description: "Vault is a tool for securely accessing secrets via a unified interface and tight access control."
config: {"docker": "vault", "url": "https://hub.docker.com/_/vault", "maintainer": "@vsoch", "description": "Vault is a tool for securely accessing secrets via a unified interface and tight access control.", "latest": {"1.11.0": "sha256:d45ffca3b9bc5f15f665c0afb581de668bca935ff1fffa10049648183c80ef6f"}, "tags": {"1.4.7": "sha256:3929780d624754b7127293649a2c4af1fbc0e22742ea5414b647db3f5de71960", "1.7.1": "sha256:10f564c947706e021e60c84bd22b1e91559db133d6d3a57e930d32cd7e0cbf77", "1.7.2": "sha256:ee69b8ba4af9e85449b79f634ae4ddc2f100f466db2dcbb83f6b69c8581de3aa", "1.8.0-rc1": "sha256:cb63a678b0e692c98332e3d933ca8232ffaa741c5cfd47f1ef398283fcf3c023", "1.8.2": "sha256:1422cccf59c78e046576e84612202334d1f7d995091d33f0e00141c3b075d0db", "1.8.4": "sha256:a75b8996586ddaf57866c3e89fc1fadcecbb8c2b85dc6fb70e3613674d771161", "1.9.0": "sha256:b16dc6ba7319005d281b34013da19012eb1713b16400d45b62e15c8f06e70d44", "1.9.2": "sha256:cc7bca14ebe2e6f32401bf5e59c1b95081c387b75fb0c06c18c085670338a59b", "1.9.3": "sha256:cafdf67809db6efbbf3ea8662df002f0b5ba2d6cdddac64df1acb4d86c18b2c1", "latest": "sha256:d45ffca3b9bc5f15f665c0afb581de668bca935ff1fffa10049648183c80ef6f", "1.10.0": "sha256:5de5de4ae5635db5fcb6e97a459b4b8174a31d6d324b978a9861c20497c9977f", "1.9.4": "sha256:ce4781c0072c281c321eee474e25cfb233677431d788168599deda1d31b9467c", "1.8.9": "sha256:36a8654d66c092aa7f3670da74a94557762f8d3d3ea267700484af360cf990a5", "1.7.10": "sha256:7fbb3872c6f31b1b2c9d7b06d12baad36706de81ac4adca8c28176bb4a68412a", "1.6.7": "sha256:dcfe67d671880c5153f6ab135ec36a3ab98a3f412c890eb551b1443e5b18da9b", "1.10.2": "sha256:34fa80e67ccc4b7c78d7ed08bff7e2049ab9e5140d04d2223f72168fc05672dc", "1.9.6": "sha256:a52d4f755208e917d67999c02be8393306fc1d893631fd8fca9f2f307be04596", "1.8.11": "sha256:7dd615c5db44ba0ac9097ac43f2d641796d5564b8cf455213b261e00073b17ac", "1.10.3": "sha256:748f13ad4b437eb2ca78c5332aeeba5b8346c2022a244fa41e5d3ae889826629", "1.11.0": "sha256:d45ffca3b9bc5f15f665c0afb581de668bca935ff1fffa10049648183c80ef6f", "1.10.4": "sha256:1722d3a087c59230b8ad8e3b97da2188e19658ecd9ecc758770c6f1768bacbba", "1.9.7": "sha256:58f9b30808c98a809c451e58dba7c23a2c0f40c3cd46d79861bd7b6652027f46", "1.8.12": "sha256:afb63f1ff5c6f35e56931c1b98ac71957cec0aa5fffcd5e377358b94863a4b6b"}, "aliases": {"vault": "/bin/vault"}}
---

This module is a singularity container wrapper for vault.
Vault is a tool for securely accessing secrets via a unified interface and tight access control.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install vault
```

Or a specific version:

```bash
$ shpc install vault:1.4.7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load vault/1.4.7
$ module help vault/1.4.7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### vault-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### vault-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### vault-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### vault-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### vault-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### vault-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### vault
       
```bash
$ singularity exec <container> /bin/vault
$ podman run --it --rm --entrypoint /bin/vault   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /bin/vault   -v ${PWD} -w ${PWD} <container> -c " $@"
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