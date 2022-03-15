---
layout: container
name:  "ghcr.io/autamus/papi"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/papi/container.yaml"
updated_at: "2022-03-15 13:29:59.169796"
container_url: "https://github.com/orgs/autamus/packages/container/package/papi"
aliases:
 - "papi_avail"

 - "papi_clockres"

 - "papi_command_line"

 - "papi_component_avail"

 - "papi_cost"

 - "papi_decode"

 - "papi_error_codes"

 - "papi_event_chooser"

 - "papi_hl_output_writer.py"

 - "papi_mem_info"

 - "papi_multiplex_cost"

 - "papi_native_avail"

 - "papi_version"

 - "papi_xml_event_info"

versions:
 - "6.0.0.1"
 - "latest"
description: "Performance Application Programming Interface."
---

This module is a singularity container wrapper for ghcr.io/autamus/papi.
Performance Application Programming Interface.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/papi
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/papi:6.0.0.1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/papi/6.0.0.1
$ module help ghcr.io/autamus/papi/6.0.0.1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### papi-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### papi-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### papi-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### papi-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### papi-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### papi-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### papi_avail
       
```bash
$ singularity exec <container> /opt/view/bin/papi_avail
$ podman run --it --rm --entrypoint /opt/view/bin/papi_avail   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/papi_avail   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### papi_clockres
       
```bash
$ singularity exec <container> /opt/view/bin/papi_clockres
$ podman run --it --rm --entrypoint /opt/view/bin/papi_clockres   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/papi_clockres   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### papi_command_line
       
```bash
$ singularity exec <container> /opt/view/bin/papi_command_line
$ podman run --it --rm --entrypoint /opt/view/bin/papi_command_line   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/papi_command_line   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### papi_component_avail
       
```bash
$ singularity exec <container> /opt/view/bin/papi_component_avail
$ podman run --it --rm --entrypoint /opt/view/bin/papi_component_avail   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/papi_component_avail   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### papi_cost
       
```bash
$ singularity exec <container> /opt/view/bin/papi_cost
$ podman run --it --rm --entrypoint /opt/view/bin/papi_cost   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/papi_cost   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### papi_decode
       
```bash
$ singularity exec <container> /opt/view/bin/papi_decode
$ podman run --it --rm --entrypoint /opt/view/bin/papi_decode   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/papi_decode   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### papi_error_codes
       
```bash
$ singularity exec <container> /opt/view/bin/papi_error_codes
$ podman run --it --rm --entrypoint /opt/view/bin/papi_error_codes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/papi_error_codes   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### papi_event_chooser
       
```bash
$ singularity exec <container> /opt/view/bin/papi_event_chooser
$ podman run --it --rm --entrypoint /opt/view/bin/papi_event_chooser   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/papi_event_chooser   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### papi_hl_output_writer.py
       
```bash
$ singularity exec <container> /opt/view/bin/papi_hl_output_writer.py
$ podman run --it --rm --entrypoint /opt/view/bin/papi_hl_output_writer.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/papi_hl_output_writer.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### papi_mem_info
       
```bash
$ singularity exec <container> /opt/view/bin/papi_mem_info
$ podman run --it --rm --entrypoint /opt/view/bin/papi_mem_info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/papi_mem_info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### papi_multiplex_cost
       
```bash
$ singularity exec <container> /opt/view/bin/papi_multiplex_cost
$ podman run --it --rm --entrypoint /opt/view/bin/papi_multiplex_cost   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/papi_multiplex_cost   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### papi_native_avail
       
```bash
$ singularity exec <container> /opt/view/bin/papi_native_avail
$ podman run --it --rm --entrypoint /opt/view/bin/papi_native_avail   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/papi_native_avail   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### papi_version
       
```bash
$ singularity exec <container> /opt/view/bin/papi_version
$ podman run --it --rm --entrypoint /opt/view/bin/papi_version   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/papi_version   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### papi_xml_event_info
       
```bash
$ singularity exec <container> /opt/view/bin/papi_xml_event_info
$ podman run --it --rm --entrypoint /opt/view/bin/papi_xml_event_info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/papi_xml_event_info   -v ${PWD} -w ${PWD} <container> -c " $@"
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