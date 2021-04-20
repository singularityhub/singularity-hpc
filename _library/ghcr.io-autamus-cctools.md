---
layout: container
name:  "ghcr.io/autamus/cctools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/cctools/container.yaml"
updated_at: "2021-04-20 03:16:17.441479"
container_url: ""
aliases:
 - "c_rehash"

 - "captoinfo"

 - "catalog_query"

 - "catalog_server"

 - "catalog_update"

 - "ccache-swig"

 - "cctools_gpu_autodetect"

 - "chirp"

 - "chirp_audit_cluster"

 - "chirp_benchmark"

 - "chirp_distribute"

 - "chirp_fuse"

 - "chirp_get"

 - "chirp_put"

 - "chirp_server"

 - "chirp_server_hdfs"

 - "chirp_status"

 - "chirp_stream_files"

 - "chroot_package_run"

 - "clear"

 - "condor_submit_makeflow"

 - "condor_submit_workers"

 - "confuga_adm"

 - "corelist"

 - "cpan"

 - "cpanm"

versions:
 - "7.2.4"
 - "latest"
description: "The Cooperative Computing Tools (CCTools) are a collection of programs that enable large scale distributed computing on systems such as clusters, clouds, and grids."
---

This module is a singularity container wrapper for ghcr.io/autamus/cctools.
The Cooperative Computing Tools (CCTools) are a collection of programs that enable large scale distributed computing on systems such as clusters, clouds, and grids.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install ghcr.io/autamus/cctools
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/cctools:7.2.4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/cctools/7.2.4
$ module help ghcr.io/autamus/cctools/7.2.4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### ghcr.io-autamus-cctools-run:

```bash
$ singularity run <container>
```

#### ghcr.io-autamus-cctools-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### ghcr.io-autamus-cctools-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### ghcr.io-autamus-cctools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ghcr.io-autamus-cctools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### c_rehash
       
```bash
$ singularity exec <container> /opt/view/bin/c_rehash
```


#### captoinfo
       
```bash
$ singularity exec <container> /opt/view/bin/captoinfo
```


#### catalog_query
       
```bash
$ singularity exec <container> /opt/view/bin/catalog_query
```


#### catalog_server
       
```bash
$ singularity exec <container> /opt/view/bin/catalog_server
```


#### catalog_update
       
```bash
$ singularity exec <container> /opt/view/bin/catalog_update
```


#### ccache-swig
       
```bash
$ singularity exec <container> /opt/view/bin/ccache-swig
```


#### cctools_gpu_autodetect
       
```bash
$ singularity exec <container> /opt/view/bin/cctools_gpu_autodetect
```


#### chirp
       
```bash
$ singularity exec <container> /opt/view/bin/chirp
```


#### chirp_audit_cluster
       
```bash
$ singularity exec <container> /opt/view/bin/chirp_audit_cluster
```


#### chirp_benchmark
       
```bash
$ singularity exec <container> /opt/view/bin/chirp_benchmark
```


#### chirp_distribute
       
```bash
$ singularity exec <container> /opt/view/bin/chirp_distribute
```


#### chirp_fuse
       
```bash
$ singularity exec <container> /opt/view/bin/chirp_fuse
```


#### chirp_get
       
```bash
$ singularity exec <container> /opt/view/bin/chirp_get
```


#### chirp_put
       
```bash
$ singularity exec <container> /opt/view/bin/chirp_put
```


#### chirp_server
       
```bash
$ singularity exec <container> /opt/view/bin/chirp_server
```


#### chirp_server_hdfs
       
```bash
$ singularity exec <container> /opt/view/bin/chirp_server_hdfs
```


#### chirp_status
       
```bash
$ singularity exec <container> /opt/view/bin/chirp_status
```


#### chirp_stream_files
       
```bash
$ singularity exec <container> /opt/view/bin/chirp_stream_files
```


#### chroot_package_run
       
```bash
$ singularity exec <container> /opt/view/bin/chroot_package_run
```


#### clear
       
```bash
$ singularity exec <container> /opt/view/bin/clear
```


#### condor_submit_makeflow
       
```bash
$ singularity exec <container> /opt/view/bin/condor_submit_makeflow
```


#### condor_submit_workers
       
```bash
$ singularity exec <container> /opt/view/bin/condor_submit_workers
```


#### confuga_adm
       
```bash
$ singularity exec <container> /opt/view/bin/confuga_adm
```


#### corelist
       
```bash
$ singularity exec <container> /opt/view/bin/corelist
```


#### cpan
       
```bash
$ singularity exec <container> /opt/view/bin/cpan
```


#### cpanm
       
```bash
$ singularity exec <container> /opt/view/bin/cpanm
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