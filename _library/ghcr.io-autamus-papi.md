---
layout: container
name:  "ghcr.io/autamus/papi"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/singularity-hpc/blob/main/registry/ghcr.io/autamus/papi/container.yaml"
updated_at: "2021-04-20 02:17:26.462115"
container_url: ""
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
$ shpc install ghcr.io/autamus/papi:latest
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/papi/latest
$ module help ghcr.io/autamus/papi/latest
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### ghcr.io-autamus-papi-run:

```bash
$ singularity run <container>
```

#### ghcr.io-autamus-papi-shell:

```bash
$ singularity shell -s /bin/bash <container>
```

#### ghcr.io-autamus-papi-exec:

```bash
$ singularity exec -s /bin/bash <container> "$@"
```

#### ghcr.io-autamus-papi-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ghcr.io-autamus-papi-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### papi_avail
       
```bash
$ singularity exec <container> /opt/view/bin/papi_avail
```


#### papi_clockres
       
```bash
$ singularity exec <container> /opt/view/bin/papi_clockres
```


#### papi_command_line
       
```bash
$ singularity exec <container> /opt/view/bin/papi_command_line
```


#### papi_component_avail
       
```bash
$ singularity exec <container> /opt/view/bin/papi_component_avail
```


#### papi_cost
       
```bash
$ singularity exec <container> /opt/view/bin/papi_cost
```


#### papi_decode
       
```bash
$ singularity exec <container> /opt/view/bin/papi_decode
```


#### papi_error_codes
       
```bash
$ singularity exec <container> /opt/view/bin/papi_error_codes
```


#### papi_event_chooser
       
```bash
$ singularity exec <container> /opt/view/bin/papi_event_chooser
```


#### papi_hl_output_writer.py
       
```bash
$ singularity exec <container> /opt/view/bin/papi_hl_output_writer.py
```


#### papi_mem_info
       
```bash
$ singularity exec <container> /opt/view/bin/papi_mem_info
```


#### papi_multiplex_cost
       
```bash
$ singularity exec <container> /opt/view/bin/papi_multiplex_cost
```


#### papi_native_avail
       
```bash
$ singularity exec <container> /opt/view/bin/papi_native_avail
```


#### papi_version
       
```bash
$ singularity exec <container> /opt/view/bin/papi_version
```


#### papi_xml_event_info
       
```bash
$ singularity exec <container> /opt/view/bin/papi_xml_event_info
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