---
layout: container
name:  "nginx"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/nginx/container.yaml"
updated_at: "2021-04-20 02:18:15.275281"
container_url: ""
aliases:
 - "nginx"

 - "nginx-debug"

versions:
 - "latest"
description: "Nginx (pronounced 'engine-x') is an open source reverse proxy server for HTTP, HTTPS, SMTP, POP3, and IMAP protocols, as well as a load balancer, HTTP cache, and a web server (origin server)."
---

This module is a singularity container wrapper for nginx.
Nginx (pronounced 'engine-x') is an open source reverse proxy server for HTTP, HTTPS, SMTP, POP3, and IMAP protocols, as well as a load balancer, HTTP cache, and a web server (origin server).
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install nginx
```

Or a specific version:

```bash
$ shpc install nginx:latest
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load nginx/latest
$ module help nginx/latest
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### nginx-run:

```bash
$ singularity run <container>
```

#### nginx-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### nginx-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### nginx-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### nginx-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### nginx
       
```bash
$ singularity exec <container> /usr/sbin/nginx
```


#### nginx-debug
       
```bash
$ singularity exec <container> /usr/sbin/nginx-debug
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