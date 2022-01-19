---
layout: container
name:  "ghcr.io/autamus/nco"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/nco/container.yaml"
updated_at: "2022-01-19 11:06:30.833926"
container_url: "https://github.com/orgs/autamus/packages/container/package/nco"
aliases:
 - "nc-config"

 - "ncap2"

 - "ncatted"

 - "ncbo"

 - "ncclimo"

 - "nccopy"

 - "ncdiff"

 - "ncdump"

 - "ncea"

 - "ncecat"

 - "nces"

 - "ncflint"

 - "ncgen"

 - "ncgen3"

 - "ncks"

 - "ncpdq"

 - "ncra"

 - "ncrcat"

 - "ncremap"

 - "ncrename"

 - "ncurses6-config"

 - "ncursesw6-config"

 - "ncwa"

versions:
 - "4.9.8"
 - "4.9.9"
 - "5.0.0"
 - "5.0.1"
 - "5.0.3"
 - "latest"

---

This module is a singularity container wrapper for ghcr.io/autamus/nco.

After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install ghcr.io/autamus/nco
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/nco:4.9.8
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/nco/4.9.8
$ module help ghcr.io/autamus/nco/4.9.8
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


#### nc-config
       
```bash
$ singularity exec <container> /opt/view/bin/nc-config
$ podman run --it --rm --entrypoint /opt/view/bin/nc-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/nc-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncap2
       
```bash
$ singularity exec <container> /opt/view/bin/ncap2
$ podman run --it --rm --entrypoint /opt/view/bin/ncap2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/ncap2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncatted
       
```bash
$ singularity exec <container> /opt/view/bin/ncatted
$ podman run --it --rm --entrypoint /opt/view/bin/ncatted   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/ncatted   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncbo
       
```bash
$ singularity exec <container> /opt/view/bin/ncbo
$ podman run --it --rm --entrypoint /opt/view/bin/ncbo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/ncbo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncclimo
       
```bash
$ singularity exec <container> /opt/view/bin/ncclimo
$ podman run --it --rm --entrypoint /opt/view/bin/ncclimo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/ncclimo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nccopy
       
```bash
$ singularity exec <container> /opt/view/bin/nccopy
$ podman run --it --rm --entrypoint /opt/view/bin/nccopy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/nccopy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncdiff
       
```bash
$ singularity exec <container> /opt/view/bin/ncdiff
$ podman run --it --rm --entrypoint /opt/view/bin/ncdiff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/ncdiff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncdump
       
```bash
$ singularity exec <container> /opt/view/bin/ncdump
$ podman run --it --rm --entrypoint /opt/view/bin/ncdump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/ncdump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncea
       
```bash
$ singularity exec <container> /opt/view/bin/ncea
$ podman run --it --rm --entrypoint /opt/view/bin/ncea   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/ncea   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncecat
       
```bash
$ singularity exec <container> /opt/view/bin/ncecat
$ podman run --it --rm --entrypoint /opt/view/bin/ncecat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/ncecat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nces
       
```bash
$ singularity exec <container> /opt/view/bin/nces
$ podman run --it --rm --entrypoint /opt/view/bin/nces   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/nces   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncflint
       
```bash
$ singularity exec <container> /opt/view/bin/ncflint
$ podman run --it --rm --entrypoint /opt/view/bin/ncflint   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/ncflint   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncgen
       
```bash
$ singularity exec <container> /opt/view/bin/ncgen
$ podman run --it --rm --entrypoint /opt/view/bin/ncgen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/ncgen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncgen3
       
```bash
$ singularity exec <container> /opt/view/bin/ncgen3
$ podman run --it --rm --entrypoint /opt/view/bin/ncgen3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/ncgen3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncks
       
```bash
$ singularity exec <container> /opt/view/bin/ncks
$ podman run --it --rm --entrypoint /opt/view/bin/ncks   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/ncks   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncpdq
       
```bash
$ singularity exec <container> /opt/view/bin/ncpdq
$ podman run --it --rm --entrypoint /opt/view/bin/ncpdq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/ncpdq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncra
       
```bash
$ singularity exec <container> /opt/view/bin/ncra
$ podman run --it --rm --entrypoint /opt/view/bin/ncra   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/ncra   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncrcat
       
```bash
$ singularity exec <container> /opt/view/bin/ncrcat
$ podman run --it --rm --entrypoint /opt/view/bin/ncrcat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/ncrcat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncremap
       
```bash
$ singularity exec <container> /opt/view/bin/ncremap
$ podman run --it --rm --entrypoint /opt/view/bin/ncremap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/ncremap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncrename
       
```bash
$ singularity exec <container> /opt/view/bin/ncrename
$ podman run --it --rm --entrypoint /opt/view/bin/ncrename   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/ncrename   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncurses6-config
       
```bash
$ singularity exec <container> /opt/view/bin/ncurses6-config
$ podman run --it --rm --entrypoint /opt/view/bin/ncurses6-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/ncurses6-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncursesw6-config
       
```bash
$ singularity exec <container> /opt/view/bin/ncursesw6-config
$ podman run --it --rm --entrypoint /opt/view/bin/ncursesw6-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/ncursesw6-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncwa
       
```bash
$ singularity exec <container> /opt/view/bin/ncwa
$ podman run --it --rm --entrypoint /opt/view/bin/ncwa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/ncwa   -v ${PWD} -w ${PWD} <container> -c " $@"
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