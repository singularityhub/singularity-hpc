---
layout: container
name:  "ghcr.io/autamus/git"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/git/container.yaml"
updated_at: "2021-04-20 03:22:29.898731"
container_url: ""
aliases:
 - "git"

 - "git-cvsserver"

 - "git-receive-pack"

 - "git-shell"

 - "git-upload-archive"

 - "git-upload-pack"

versions:
 - "latest"
description: "Git is software for tracking changes in any set of files, usually used for coordinating work among programmers collaboratively developing source code during software development. Its goals include speed, data integrity, and support for distributed, non-linear workflows."
---

This module is a singularity container wrapper for ghcr.io/autamus/git.
Git is software for tracking changes in any set of files, usually used for coordinating work among programmers collaboratively developing source code during software development. Its goals include speed, data integrity, and support for distributed, non-linear workflows.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install ghcr.io/autamus/git
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/git:latest
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/git/latest
$ module help ghcr.io/autamus/git/latest
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### ghcr.io-autamus-git-run:

```bash
$ singularity run <container>
```

#### ghcr.io-autamus-git-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### ghcr.io-autamus-git-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### ghcr.io-autamus-git-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ghcr.io-autamus-git-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### git
       
```bash
$ singularity exec <container> /opt/view/bin/git
```


#### git-cvsserver
       
```bash
$ singularity exec <container> /opt/view/bin/git-cvsserver
```


#### git-receive-pack
       
```bash
$ singularity exec <container> /opt/view/bin/git-receive-pack
```


#### git-shell
       
```bash
$ singularity exec <container> /opt/view/bin/git-shell
```


#### git-upload-archive
       
```bash
$ singularity exec <container> /opt/view/bin/git-upload-archive
```


#### git-upload-pack
       
```bash
$ singularity exec <container> /opt/view/bin/git-upload-pack
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