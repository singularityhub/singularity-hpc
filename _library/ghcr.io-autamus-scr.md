---
layout: container
name:  "ghcr.io/autamus/scr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/scr/container.yaml"
updated_at: "2022-04-08 03:04:27.178566"
container_url: "https://github.com/orgs/autamus/packages/container/package/scr"
aliases:
 - "scancel"

 - "scontrol"

 - "scp"

 - "scr_check_node"

 - "scr_ckpt_interval.py"

 - "scr_copy"

 - "scr_crc32"

 - "scr_env"

 - "scr_flush_file"

 - "scr_get_jobstep_id"

 - "scr_glob_hosts"

 - "scr_halt"

 - "scr_halt_cntl"

 - "scr_index"

 - "scr_inspect"

 - "scr_kill_jobstep"

 - "scr_list_dir"

 - "scr_list_down_nodes"

 - "scr_log_event"

 - "scr_log_transfer"

 - "scr_nodes_file"

 - "scr_postrun"

 - "scr_prefix"

 - "scr_prerun"

 - "scr_print"

 - "scr_rebuild_partner"

 - "scr_rebuild_rs"

 - "scr_rebuild_xor"

 - "scr_retries_halt"

 - "scr_run"

 - "scr_scavenge"

 - "scr_srun"

 - "scr_test_datemanip"

 - "scr_test_runtime"

 - "scr_watchdog"

 - "scrlog.py"

 - "scrontab"

versions:
 - "3.0.rc.1"
 - "latest"
description: "SCR caches checkpoint data in storage on the compute nodes of a Linux cluster to provide a fast, scalable checkpoint/restart capability for MPI codes."
---

This module is a singularity container wrapper for ghcr.io/autamus/scr.
SCR caches checkpoint data in storage on the compute nodes of a Linux cluster to provide a fast, scalable checkpoint/restart capability for MPI codes.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/scr
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/scr:3.0.rc.1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/scr/3.0.rc.1
$ module help ghcr.io/autamus/scr/3.0.rc.1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### scr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### scr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### scr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### scr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### scr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### scr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### scancel
       
```bash
$ singularity exec <container> /opt/view/bin/scancel
$ podman run --it --rm --entrypoint /opt/view/bin/scancel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/scancel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scontrol
       
```bash
$ singularity exec <container> /opt/view/bin/scontrol
$ podman run --it --rm --entrypoint /opt/view/bin/scontrol   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/scontrol   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scp
       
```bash
$ singularity exec <container> /opt/view/bin/scp
$ podman run --it --rm --entrypoint /opt/view/bin/scp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/scp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scr_check_node
       
```bash
$ singularity exec <container> /opt/view/bin/scr_check_node
$ podman run --it --rm --entrypoint /opt/view/bin/scr_check_node   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/scr_check_node   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scr_ckpt_interval.py
       
```bash
$ singularity exec <container> /opt/view/bin/scr_ckpt_interval.py
$ podman run --it --rm --entrypoint /opt/view/bin/scr_ckpt_interval.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/scr_ckpt_interval.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scr_copy
       
```bash
$ singularity exec <container> /opt/view/bin/scr_copy
$ podman run --it --rm --entrypoint /opt/view/bin/scr_copy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/scr_copy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scr_crc32
       
```bash
$ singularity exec <container> /opt/view/bin/scr_crc32
$ podman run --it --rm --entrypoint /opt/view/bin/scr_crc32   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/scr_crc32   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scr_env
       
```bash
$ singularity exec <container> /opt/view/bin/scr_env
$ podman run --it --rm --entrypoint /opt/view/bin/scr_env   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/scr_env   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scr_flush_file
       
```bash
$ singularity exec <container> /opt/view/bin/scr_flush_file
$ podman run --it --rm --entrypoint /opt/view/bin/scr_flush_file   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/scr_flush_file   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scr_get_jobstep_id
       
```bash
$ singularity exec <container> /opt/view/bin/scr_get_jobstep_id
$ podman run --it --rm --entrypoint /opt/view/bin/scr_get_jobstep_id   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/scr_get_jobstep_id   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scr_glob_hosts
       
```bash
$ singularity exec <container> /opt/view/bin/scr_glob_hosts
$ podman run --it --rm --entrypoint /opt/view/bin/scr_glob_hosts   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/scr_glob_hosts   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scr_halt
       
```bash
$ singularity exec <container> /opt/view/bin/scr_halt
$ podman run --it --rm --entrypoint /opt/view/bin/scr_halt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/scr_halt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scr_halt_cntl
       
```bash
$ singularity exec <container> /opt/view/bin/scr_halt_cntl
$ podman run --it --rm --entrypoint /opt/view/bin/scr_halt_cntl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/scr_halt_cntl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scr_index
       
```bash
$ singularity exec <container> /opt/view/bin/scr_index
$ podman run --it --rm --entrypoint /opt/view/bin/scr_index   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/scr_index   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scr_inspect
       
```bash
$ singularity exec <container> /opt/view/bin/scr_inspect
$ podman run --it --rm --entrypoint /opt/view/bin/scr_inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/scr_inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scr_kill_jobstep
       
```bash
$ singularity exec <container> /opt/view/bin/scr_kill_jobstep
$ podman run --it --rm --entrypoint /opt/view/bin/scr_kill_jobstep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/scr_kill_jobstep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scr_list_dir
       
```bash
$ singularity exec <container> /opt/view/bin/scr_list_dir
$ podman run --it --rm --entrypoint /opt/view/bin/scr_list_dir   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/scr_list_dir   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scr_list_down_nodes
       
```bash
$ singularity exec <container> /opt/view/bin/scr_list_down_nodes
$ podman run --it --rm --entrypoint /opt/view/bin/scr_list_down_nodes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/scr_list_down_nodes   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scr_log_event
       
```bash
$ singularity exec <container> /opt/view/bin/scr_log_event
$ podman run --it --rm --entrypoint /opt/view/bin/scr_log_event   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/scr_log_event   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scr_log_transfer
       
```bash
$ singularity exec <container> /opt/view/bin/scr_log_transfer
$ podman run --it --rm --entrypoint /opt/view/bin/scr_log_transfer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/scr_log_transfer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scr_nodes_file
       
```bash
$ singularity exec <container> /opt/view/bin/scr_nodes_file
$ podman run --it --rm --entrypoint /opt/view/bin/scr_nodes_file   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/scr_nodes_file   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scr_postrun
       
```bash
$ singularity exec <container> /opt/view/bin/scr_postrun
$ podman run --it --rm --entrypoint /opt/view/bin/scr_postrun   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/scr_postrun   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scr_prefix
       
```bash
$ singularity exec <container> /opt/view/bin/scr_prefix
$ podman run --it --rm --entrypoint /opt/view/bin/scr_prefix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/scr_prefix   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scr_prerun
       
```bash
$ singularity exec <container> /opt/view/bin/scr_prerun
$ podman run --it --rm --entrypoint /opt/view/bin/scr_prerun   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/scr_prerun   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scr_print
       
```bash
$ singularity exec <container> /opt/view/bin/scr_print
$ podman run --it --rm --entrypoint /opt/view/bin/scr_print   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/scr_print   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scr_rebuild_partner
       
```bash
$ singularity exec <container> /opt/view/bin/scr_rebuild_partner
$ podman run --it --rm --entrypoint /opt/view/bin/scr_rebuild_partner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/scr_rebuild_partner   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scr_rebuild_rs
       
```bash
$ singularity exec <container> /opt/view/bin/scr_rebuild_rs
$ podman run --it --rm --entrypoint /opt/view/bin/scr_rebuild_rs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/scr_rebuild_rs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scr_rebuild_xor
       
```bash
$ singularity exec <container> /opt/view/bin/scr_rebuild_xor
$ podman run --it --rm --entrypoint /opt/view/bin/scr_rebuild_xor   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/scr_rebuild_xor   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scr_retries_halt
       
```bash
$ singularity exec <container> /opt/view/bin/scr_retries_halt
$ podman run --it --rm --entrypoint /opt/view/bin/scr_retries_halt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/scr_retries_halt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scr_run
       
```bash
$ singularity exec <container> /opt/view/bin/scr_run
$ podman run --it --rm --entrypoint /opt/view/bin/scr_run   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/scr_run   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scr_scavenge
       
```bash
$ singularity exec <container> /opt/view/bin/scr_scavenge
$ podman run --it --rm --entrypoint /opt/view/bin/scr_scavenge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/scr_scavenge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scr_srun
       
```bash
$ singularity exec <container> /opt/view/bin/scr_srun
$ podman run --it --rm --entrypoint /opt/view/bin/scr_srun   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/scr_srun   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scr_test_datemanip
       
```bash
$ singularity exec <container> /opt/view/bin/scr_test_datemanip
$ podman run --it --rm --entrypoint /opt/view/bin/scr_test_datemanip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/scr_test_datemanip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scr_test_runtime
       
```bash
$ singularity exec <container> /opt/view/bin/scr_test_runtime
$ podman run --it --rm --entrypoint /opt/view/bin/scr_test_runtime   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/scr_test_runtime   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scr_watchdog
       
```bash
$ singularity exec <container> /opt/view/bin/scr_watchdog
$ podman run --it --rm --entrypoint /opt/view/bin/scr_watchdog   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/scr_watchdog   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scrlog.py
       
```bash
$ singularity exec <container> /opt/view/bin/scrlog.py
$ podman run --it --rm --entrypoint /opt/view/bin/scrlog.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/scrlog.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scrontab
       
```bash
$ singularity exec <container> /opt/view/bin/scrontab
$ podman run --it --rm --entrypoint /opt/view/bin/scrontab   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/scrontab   -v ${PWD} -w ${PWD} <container> -c " $@"
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