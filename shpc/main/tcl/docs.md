---
layout: container
name:  "{{ name }}"
maintainer: "@vsoch"
github: "{{ github_url }}"
updated_at: "{{ creation_date }}"
container_url: "{{ container_url }}"
{% if aliases %}aliases:{% for alias in aliases %}
 - "{{ alias.name }}"
{% endfor %}{% endif %}
versions:{% for version in versions %}
 - "{{ version }}"{% endfor %}
{% if description %}description: "{{ description }}"{% endif %}
---

This module is a singularity container wrapper for {{ name }}.
{% if description %}{{ description }}{% endif %}
After [installing shpc](#install) you will want to install this container module:

```bash
$ shpc install {{ name }}
```

Or a specific version:

```bash
$ shpc install {{ name }}:{{ versions.0 }}
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load {{ name }}/{{ versions.0 }}
$ module help {{ name }}/{{ versions.0 }}
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you'll be able to load it to make the following commands accessible:

#### {{ prefix }}{{ flatname }}-run:

```bash
$ singularity run {% if bindpaths %}-B {{ bindpaths }} {% endif %}<container>
```

#### {{ prefix }}{{ flatname }}-shell:

```bash
$ singularity shell -s {{ singularity_shell }} {% if bindpaths %}-B {{ bindpaths }} {% endif %}<container>
```

#### {{ prefix }}{{ flatname }}-exec:

```bash
$ singularity exec -s {{ singularity_shell }} {% if bindpaths %}-B {{ bindpaths }} {% endif %}<container> "$@"
```

#### {{ prefix }}{{ flatname }}-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### {{ prefix }}{{ flatname }}-inspect-deffile:

```bash
$ singularity inspect -d <container>
```

{% if aliases %}{% for alias in aliases %}
#### {{ alias.name }}
       
```bash
$ singularity exec {% if bindpaths %}-B {{ bindpaths }} {% endif %}{% if alias.options %}{{ alias.options }} {% endif %}<container> {{ alias.command }}
```

{% endfor %}{% else %}

#### {{ prefix }}{{ flatname }}

```bash
$ singularity run {% if bindpaths %}-B {{ bindpaths }}{% endif %}<container>
```
{% endif %}

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
