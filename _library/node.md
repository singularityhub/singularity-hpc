---
layout: container
name:  "node"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/node/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/node/container.yaml"
updated_at: "2022-08-27 01:37:08.310582"
latest: "18.4"
container_url: "https://hub.docker.com/r/_/node"
aliases:
 - "node"
 - "nodejs"
 - "npm"
 - "npx"
 - "yarn"
 - "yarnpkg"
versions:
 - "15.14.0-alpine"
 - "16.0.0-alpine"
 - "16.1.0-alpine"
 - "16.2.0-alpine"
 - "16.3.0-alpine"
 - "16.5.0-alpine"
 - "16.8.0"
 - "17.0.1"
 - "17.1.0"
 - "17.3.0"
 - "17.4.0"
 - "17.6.0"
 - "latest"
 - "17"
 - "17.8"
 - "17.7"
 - "17.6"
 - "17.5"
 - "18"
 - "18-alpine3.15"
 - "18.0"
 - "17.9"
 - "18.2"
 - "18.1"
 - "18-alpine3.16"
 - "18.4"
description: "Node.js is a software platform for scalable server-side and networking applications."
config: {"docker": "node", "url": "https://hub.docker.com/r/_/node", "maintainer": "@vsoch", "description": "Node.js is a software platform for scalable server-side and networking applications.", "latest": {"18.4": "sha256:5244663c5cc6392808aa1c4a78f90369e75c3d9e9a27589cffed0ae73d1f0815"}, "tags": {"15.14.0-alpine": "sha256:6edd37368174c15d4cc59395ca2643be8e2a1c9846714bc92c5f5c5a92fb8929", "16.0.0-alpine": "sha256:fabc6adac6dba5e150130e10acfc11a81447be93f4bf384076abdb63dbd34033", "16.1.0-alpine": "sha256:8704247878fe10eddfcb5c26540112b15e50d21ce8e5c7a7f6caf5cf857de219", "16.2.0-alpine": "sha256:e5615005591e2450e782fa82b10bf31e4c3a90b00f4f47f3691bcb4c03c5b1a2", "16.3.0-alpine": "sha256:2eee2f439d3b3509bbe40faff6584bd31b5745b4c137e93e2d795899a2927762", "16.5.0-alpine": "sha256:50b33102c307e04f73817dad87cdae145b14782875495ddd950b5a48e4937c70", "16.8.0": "sha256:ba82c1fd24e2b735ca0e980f1d227e48b2debb641315c3e9ad72d220a5a534e4", "17.0.1": "sha256:a562ce5da0b5e43107b4acbc5d8845129370f11bcb81c795601dc3d6004d6158", "17.1.0": "sha256:22f1866405ad50bb1d141739596ba803aed073d618ab2ae6d5e66aedcf9261b5", "17.3.0": "sha256:36aca218a5eb57cb23bc790a030591382c7664c15a384e2ddc2075761ac7e701", "17.4.0": "sha256:88becea956ea5ec0262b8aac011a234f95310e5cacc38cc9d2468a836d67ffc9", "17.6.0": "sha256:08e37ce0636ad9796900a180f2539f3110648e4f2c1b541bc0d4d3039e6b3251", "latest": "sha256:5244663c5cc6392808aa1c4a78f90369e75c3d9e9a27589cffed0ae73d1f0815", "17": "sha256:1845a99ada85e286535bbf12e1261ea688b28b7e8bcf6521590edbbea9f41cf9", "17.8": "sha256:0b553d28086d90b9b3be3339beb97401f8c0a83c17230a37ad99ff88fdad3b3f", "17.7": "sha256:720d77136dc06bbdac28ef5cd13c385e40a2f1bfaaf7340180fc66820cc184e3", "17.6": "sha256:08e37ce0636ad9796900a180f2539f3110648e4f2c1b541bc0d4d3039e6b3251", "17.5": "sha256:a0590a265b222387d756ba357c4a9875778f1a7638ac011f3fb4942d3b7ae5c0", "18": "sha256:5244663c5cc6392808aa1c4a78f90369e75c3d9e9a27589cffed0ae73d1f0815", "18-alpine3.15": "sha256:f55132b48261c7ca0394d71c204eb419db0a0209be341762390693434e4bdd92", "18.0": "sha256:e5b7b349d517159246070bf14242027a9e220ffa8bd98a67ba1495d969c06c01", "17.9": "sha256:1845a99ada85e286535bbf12e1261ea688b28b7e8bcf6521590edbbea9f41cf9", "18.2": "sha256:52bda4c171f379c1dcba5411d18ed83ae6e99c3751cad67a450684efb9491f6b", "18.1": "sha256:82f9e078898dce32c7bf3232049715f1b8fbf0d62d5f3091bca20fcaede50bf0", "18-alpine3.16": "sha256:7ae41699c38d8e50f5bf592867cf661368d71ff922e07f6f66f36dca2ff0c590", "18.4": "sha256:5244663c5cc6392808aa1c4a78f90369e75c3d9e9a27589cffed0ae73d1f0815"}, "aliases": {"node": "/usr/local/bin/node", "nodejs": "/usr/local/bin/nodejs", "npm": "/usr/local/bin/npm", "npx": "/usr/local/bin/npx", "yarn": "/usr/local/bin/yarn", "yarnpkg": "/usr/local/bin/yarnpkg"}}
---

This module is a singularity container wrapper for node.
Node.js is a software platform for scalable server-side and networking applications.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install node
```

Or a specific version:

```bash
$ shpc install node:15.14.0-alpine
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load node/15.14.0-alpine
$ module help node/15.14.0-alpine
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### node-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### node-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### node-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### node-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### node-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### node-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### node
       
```bash
$ singularity exec <container> /usr/local/bin/node
$ podman run --it --rm --entrypoint /usr/local/bin/node   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/node   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nodejs
       
```bash
$ singularity exec <container> /usr/local/bin/nodejs
$ podman run --it --rm --entrypoint /usr/local/bin/nodejs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nodejs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### npm
       
```bash
$ singularity exec <container> /usr/local/bin/npm
$ podman run --it --rm --entrypoint /usr/local/bin/npm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/npm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### npx
       
```bash
$ singularity exec <container> /usr/local/bin/npx
$ podman run --it --rm --entrypoint /usr/local/bin/npx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/npx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### yarn
       
```bash
$ singularity exec <container> /usr/local/bin/yarn
$ podman run --it --rm --entrypoint /usr/local/bin/yarn   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/yarn   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### yarnpkg
       
```bash
$ singularity exec <container> /usr/local/bin/yarnpkg
$ podman run --it --rm --entrypoint /usr/local/bin/yarnpkg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/yarnpkg   -v ${PWD} -w ${PWD} <container> -c " $@"
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