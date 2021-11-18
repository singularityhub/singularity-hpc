---
layout: container
name:  "ghcr.io/autamus/cctools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/cctools/container.yaml"
updated_at: "2021-11-18 17:37:09.206528"
container_url: "https://github.com/orgs/autamus/packages/container/package/cctools"
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
 - "7.2.10"
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


#### c_rehash
       
```bash
$ singularity exec <container> /opt/view/bin/c_rehash
$ podman run --it --rm --entrypoint /opt/view/bin/c_rehash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/c_rehash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### captoinfo
       
```bash
$ singularity exec <container> /opt/view/bin/captoinfo
$ podman run --it --rm --entrypoint /opt/view/bin/captoinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/captoinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### catalog_query
       
```bash
$ singularity exec <container> /opt/view/bin/catalog_query
$ podman run --it --rm --entrypoint /opt/view/bin/catalog_query   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/catalog_query   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### catalog_server
       
```bash
$ singularity exec <container> /opt/view/bin/catalog_server
$ podman run --it --rm --entrypoint /opt/view/bin/catalog_server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/catalog_server   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### catalog_update
       
```bash
$ singularity exec <container> /opt/view/bin/catalog_update
$ podman run --it --rm --entrypoint /opt/view/bin/catalog_update   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/catalog_update   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ccache-swig
       
```bash
$ singularity exec <container> /opt/view/bin/ccache-swig
$ podman run --it --rm --entrypoint /opt/view/bin/ccache-swig   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/ccache-swig   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cctools_gpu_autodetect
       
```bash
$ singularity exec <container> /opt/view/bin/cctools_gpu_autodetect
$ podman run --it --rm --entrypoint /opt/view/bin/cctools_gpu_autodetect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/cctools_gpu_autodetect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chirp
       
```bash
$ singularity exec <container> /opt/view/bin/chirp
$ podman run --it --rm --entrypoint /opt/view/bin/chirp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/chirp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chirp_audit_cluster
       
```bash
$ singularity exec <container> /opt/view/bin/chirp_audit_cluster
$ podman run --it --rm --entrypoint /opt/view/bin/chirp_audit_cluster   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/chirp_audit_cluster   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chirp_benchmark
       
```bash
$ singularity exec <container> /opt/view/bin/chirp_benchmark
$ podman run --it --rm --entrypoint /opt/view/bin/chirp_benchmark   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/chirp_benchmark   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chirp_distribute
       
```bash
$ singularity exec <container> /opt/view/bin/chirp_distribute
$ podman run --it --rm --entrypoint /opt/view/bin/chirp_distribute   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/chirp_distribute   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chirp_fuse
       
```bash
$ singularity exec <container> /opt/view/bin/chirp_fuse
$ podman run --it --rm --entrypoint /opt/view/bin/chirp_fuse   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/chirp_fuse   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chirp_get
       
```bash
$ singularity exec <container> /opt/view/bin/chirp_get
$ podman run --it --rm --entrypoint /opt/view/bin/chirp_get   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/chirp_get   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chirp_put
       
```bash
$ singularity exec <container> /opt/view/bin/chirp_put
$ podman run --it --rm --entrypoint /opt/view/bin/chirp_put   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/chirp_put   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chirp_server
       
```bash
$ singularity exec <container> /opt/view/bin/chirp_server
$ podman run --it --rm --entrypoint /opt/view/bin/chirp_server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/chirp_server   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chirp_server_hdfs
       
```bash
$ singularity exec <container> /opt/view/bin/chirp_server_hdfs
$ podman run --it --rm --entrypoint /opt/view/bin/chirp_server_hdfs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/chirp_server_hdfs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chirp_status
       
```bash
$ singularity exec <container> /opt/view/bin/chirp_status
$ podman run --it --rm --entrypoint /opt/view/bin/chirp_status   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/chirp_status   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chirp_stream_files
       
```bash
$ singularity exec <container> /opt/view/bin/chirp_stream_files
$ podman run --it --rm --entrypoint /opt/view/bin/chirp_stream_files   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/chirp_stream_files   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chroot_package_run
       
```bash
$ singularity exec <container> /opt/view/bin/chroot_package_run
$ podman run --it --rm --entrypoint /opt/view/bin/chroot_package_run   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/chroot_package_run   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clear
       
```bash
$ singularity exec <container> /opt/view/bin/clear
$ podman run --it --rm --entrypoint /opt/view/bin/clear   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/clear   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### condor_submit_makeflow
       
```bash
$ singularity exec <container> /opt/view/bin/condor_submit_makeflow
$ podman run --it --rm --entrypoint /opt/view/bin/condor_submit_makeflow   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/condor_submit_makeflow   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### condor_submit_workers
       
```bash
$ singularity exec <container> /opt/view/bin/condor_submit_workers
$ podman run --it --rm --entrypoint /opt/view/bin/condor_submit_workers   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/condor_submit_workers   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### confuga_adm
       
```bash
$ singularity exec <container> /opt/view/bin/confuga_adm
$ podman run --it --rm --entrypoint /opt/view/bin/confuga_adm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/confuga_adm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### corelist
       
```bash
$ singularity exec <container> /opt/view/bin/corelist
$ podman run --it --rm --entrypoint /opt/view/bin/corelist   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/corelist   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cpan
       
```bash
$ singularity exec <container> /opt/view/bin/cpan
$ podman run --it --rm --entrypoint /opt/view/bin/cpan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/cpan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cpanm
       
```bash
$ singularity exec <container> /opt/view/bin/cpanm
$ podman run --it --rm --entrypoint /opt/view/bin/cpanm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/cpanm   -v ${PWD} -w ${PWD} <container> -c " $@"
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