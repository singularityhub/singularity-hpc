---
layout: container
name:  "ghcr.io/autamus/rust"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/rust/container.yaml"
updated_at: "2021-04-18 18:21:19.614631"
container_url: ""
aliases:
 - "rust"

 - "rustc"

 - "rustdoc"

 - "rustfmt"

 - "rust-gdb"

 - "rust-gdbgui"

 - "rust-lldb"

 - "cargo"

 - "cargo-fmt"

 - "cargo-clippy"

 - "clippy-driver"

versions:
 - "latest"
description: "Rust is a multi-paradigm programming language designed for performance and safety, especially safe concurrency."
---

This module is a singularity container wrapper for ghcr.io/autamus/rust.
Rust is a multi-paradigm programming language designed for performance and safety, especially safe concurrency.
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install ghcr.io/autamus/rust
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/rust:latest
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/rust/latest
$ module help ghcr.io/autamus/rust/latest
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### ghcr.io-autamus-rust-run:

```bash
$ singularity run <container>
```

#### ghcr.io-autamus-rust-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### ghcr.io-autamus-rust-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### ghcr.io-autamus-rust-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ghcr.io-autamus-rust-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### rust
       
```bash
$ singularity exec <container> /opt/view/bin/rust
```


#### rustc
       
```bash
$ singularity exec <container> /opt/view/bin/rustc
```


#### rustdoc
       
```bash
$ singularity exec <container> /opt/view/bin/rustdoc
```


#### rustfmt
       
```bash
$ singularity exec <container> /opt/view/bin/rustfmt
```


#### rust-gdb
       
```bash
$ singularity exec <container> /opt/view/bin/rust-gdb
```


#### rust-gdbgui
       
```bash
$ singularity exec <container> /opt/view/bin/rust-gdbgui
```


#### rust-lldb
       
```bash
$ singularity exec <container> /opt/view/bin/rust-lldb
```


#### cargo
       
```bash
$ singularity exec <container> /opt/view/bin/cargo
```


#### cargo-fmt
       
```bash
$ singularity exec <container> /opt/view/bin/cargo-fmt
```


#### cargo-clippy
       
```bash
$ singularity exec <container> /opt/view/bin/cargo-clippy
```


#### clippy-driver
       
```bash
$ singularity exec <container> /opt/view/bin/clippy-driver
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