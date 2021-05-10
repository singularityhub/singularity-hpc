---
layout: container
name:  "kibana"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/kibana/container.yaml"
updated_at: "2021-05-10 15:19:43.073597"
container_url: "https://hub.docker.com/_/kibana"
aliases:
 - "kibana"

 - "kibana-encryption-keys"

 - "kibana-keystore"

 - "kibana-plugin"

versions:
 - "7.12.0"
 - "7.12.1"
description: "Kibana gives shape to any kind of data — structured and unstructured — indexed in Elasticsearch."
---

This module is a singularity container wrapper for kibana.
Kibana gives shape to any kind of data — structured and unstructured — indexed in Elasticsearch.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install kibana
```

Or a specific version:

```bash
$ shpc install kibana:7.12.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load kibana/7.12.0
$ module help kibana/7.12.0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### kibana-run:

```bash
$ singularity run <container>
```

#### kibana-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### kibana-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### kibana-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### kibana-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### kibana
       
```bash
$ singularity exec <container> /usr/share/kibana/bin/kibana
```


#### kibana-encryption-keys
       
```bash
$ singularity exec <container> /usr/share/kibana/bin/kibana-encryption-keys
```


#### kibana-keystore
       
```bash
$ singularity exec <container> /usr/share/kibana/bin/kibana-keystore
```


#### kibana-plugin
       
```bash
$ singularity exec <container> /usr/share/kibana/bin/kibana-plugin
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