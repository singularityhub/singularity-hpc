---
layout: container
name:  "ghcr.io/autamus/xrootd"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/xrootd/container.yaml"
updated_at: "2021-05-09 15:35:02.414289"
container_url: "https://github.com/orgs/autamus/packages/container/package/xrootd"
aliases:
 - "xrdacctest"

 - "xrdadler32"

 - "xrdcopy"

 - "xrdcp"

 - "xrdfs"

 - "xrdgsiproxy"

 - "xrdgsitest"

 - "xrdmapc"

 - "xrdpfc_print"

 - "xrdpinls"

 - "xrdpwdadmin"

 - "xrdsssadmin"

 - "xrootd"

 - "xrootd-config"

versions:
 - "5.1.0"
 - "latest"
description: "XRootD software framework is a fully generic suite for fast, low latency and scalable data access, which can serve natively any kind of data, organized as a hierarchical filesystem-like namespace, based on the concept of directory."
---

This module is a singularity container wrapper for ghcr.io/autamus/xrootd.
XRootD software framework is a fully generic suite for fast, low latency and scalable data access, which can serve natively any kind of data, organized as a hierarchical filesystem-like namespace, based on the concept of directory.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install ghcr.io/autamus/xrootd
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/xrootd:5.1.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/xrootd/5.1.0
$ module help ghcr.io/autamus/xrootd/5.1.0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### ghcr.io-autamus-xrootd-run:

```bash
$ singularity run <container>
```

#### ghcr.io-autamus-xrootd-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### ghcr.io-autamus-xrootd-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### ghcr.io-autamus-xrootd-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ghcr.io-autamus-xrootd-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### xrdacctest
       
```bash
$ singularity exec <container> /opt/view/bin/xrdacctest
```


#### xrdadler32
       
```bash
$ singularity exec <container> /opt/view/bin/xrdadler32
```


#### xrdcopy
       
```bash
$ singularity exec <container> /opt/view/bin/xrdcopy
```


#### xrdcp
       
```bash
$ singularity exec <container> /opt/view/bin/xrdcp
```


#### xrdfs
       
```bash
$ singularity exec <container> /opt/view/bin/xrdfs
```


#### xrdgsiproxy
       
```bash
$ singularity exec <container> /opt/view/bin/xrdgsiproxy
```


#### xrdgsitest
       
```bash
$ singularity exec <container> /opt/view/bin/xrdgsitest
```


#### xrdmapc
       
```bash
$ singularity exec <container> /opt/view/bin/xrdmapc
```


#### xrdpfc_print
       
```bash
$ singularity exec <container> /opt/view/bin/xrdpfc_print
```


#### xrdpinls
       
```bash
$ singularity exec <container> /opt/view/bin/xrdpinls
```


#### xrdpwdadmin
       
```bash
$ singularity exec <container> /opt/view/bin/xrdpwdadmin
```


#### xrdsssadmin
       
```bash
$ singularity exec <container> /opt/view/bin/xrdsssadmin
```


#### xrootd
       
```bash
$ singularity exec <container> /opt/view/bin/xrootd
```


#### xrootd-config
       
```bash
$ singularity exec <container> /opt/view/bin/xrootd-config
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