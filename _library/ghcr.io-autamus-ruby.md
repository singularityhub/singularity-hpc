---
layout: container
name:  "ghcr.io/autamus/ruby"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/ruby/container.yaml"
updated_at: "2021-04-20 01:49:04.998281"
container_url: ""
aliases:
 - "ruby"

 - "bundle"

 - "bundler"

 - "erb"

 - "irb"

 - "gem"

 - "rake"

 - "rdoc"

 - "rbs"

 - "racc"

 - "ri"

versions:
 - "latest"
description: "An interpreted, high-level, general-purpose programming language."
---

This module is a singularity container wrapper for ghcr.io/autamus/ruby.
An interpreted, high-level, general-purpose programming language.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install ghcr.io/autamus/ruby
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/ruby:latest
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/ruby/latest
$ module help ghcr.io/autamus/ruby/latest
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### ghcr.io-autamus-ruby-run:

```bash
$ singularity run <container>
```

#### ghcr.io-autamus-ruby-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### ghcr.io-autamus-ruby-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### ghcr.io-autamus-ruby-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ghcr.io-autamus-ruby-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ruby
       
```bash
$ singularity exec <container> /opt/view/bin/ruby
```


#### bundle
       
```bash
$ singularity exec <container> /opt/view/bin/bundle
```


#### bundler
       
```bash
$ singularity exec <container> /opt/view/bin/bundler
```


#### erb
       
```bash
$ singularity exec <container> /opt/view/bin/erb
```


#### irb
       
```bash
$ singularity exec <container> /opt/view/bin/irb
```


#### gem
       
```bash
$ singularity exec <container> /opt/view/bin/gem
```


#### rake
       
```bash
$ singularity exec <container> /opt/view/bin/rake
```


#### rdoc
       
```bash
$ singularity exec <container> /opt/view/bin/rdoc
```


#### rbs
       
```bash
$ singularity exec <container> /opt/view/bin/rbs
```


#### racc
       
```bash
$ singularity exec <container> /opt/view/bin/racc
```


#### ri
       
```bash
$ singularity exec <container> /opt/view/bin/ri
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