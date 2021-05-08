---
layout: container
name:  "ghcr.io/autamus/nco"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/nco/container.yaml"
updated_at: "2021-05-08 17:36:16.574712"
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

When you install this module, you'll be able to load it to make the following commands accessible:

#### ghcr.io-autamus-nco-run:

```bash
$ singularity run <container>
```

#### ghcr.io-autamus-nco-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### ghcr.io-autamus-nco-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### ghcr.io-autamus-nco-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ghcr.io-autamus-nco-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### nc-config
       
```bash
$ singularity exec <container> /opt/view/bin/nc-config
```


#### ncap2
       
```bash
$ singularity exec <container> /opt/view/bin/ncap2
```


#### ncatted
       
```bash
$ singularity exec <container> /opt/view/bin/ncatted
```


#### ncbo
       
```bash
$ singularity exec <container> /opt/view/bin/ncbo
```


#### ncclimo
       
```bash
$ singularity exec <container> /opt/view/bin/ncclimo
```


#### nccopy
       
```bash
$ singularity exec <container> /opt/view/bin/nccopy
```


#### ncdiff
       
```bash
$ singularity exec <container> /opt/view/bin/ncdiff
```


#### ncdump
       
```bash
$ singularity exec <container> /opt/view/bin/ncdump
```


#### ncea
       
```bash
$ singularity exec <container> /opt/view/bin/ncea
```


#### ncecat
       
```bash
$ singularity exec <container> /opt/view/bin/ncecat
```


#### nces
       
```bash
$ singularity exec <container> /opt/view/bin/nces
```


#### ncflint
       
```bash
$ singularity exec <container> /opt/view/bin/ncflint
```


#### ncgen
       
```bash
$ singularity exec <container> /opt/view/bin/ncgen
```


#### ncgen3
       
```bash
$ singularity exec <container> /opt/view/bin/ncgen3
```


#### ncks
       
```bash
$ singularity exec <container> /opt/view/bin/ncks
```


#### ncpdq
       
```bash
$ singularity exec <container> /opt/view/bin/ncpdq
```


#### ncra
       
```bash
$ singularity exec <container> /opt/view/bin/ncra
```


#### ncrcat
       
```bash
$ singularity exec <container> /opt/view/bin/ncrcat
```


#### ncremap
       
```bash
$ singularity exec <container> /opt/view/bin/ncremap
```


#### ncrename
       
```bash
$ singularity exec <container> /opt/view/bin/ncrename
```


#### ncurses6-config
       
```bash
$ singularity exec <container> /opt/view/bin/ncurses6-config
```


#### ncursesw6-config
       
```bash
$ singularity exec <container> /opt/view/bin/ncursesw6-config
```


#### ncwa
       
```bash
$ singularity exec <container> /opt/view/bin/ncwa
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