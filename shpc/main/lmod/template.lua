-- LMOD Module
-- Created by singularity-hpc (https://github.com/singularityhub/singularity-hpc)
-- ##
-- {{ name }} on {{ creation_date }}
--

help(
[[
This module is a singularity container wrapper for {{ name }} v{{ version }}
{% if description %}{{ description }}{% endif %}
]])

{% if singularity_module %}load("{{ singularity_module }}"){% endif %}

-- we probably don't need this
local MODULEPATH="{{ module_dir }}"

-- singularity environment variables to bind the paths and set shell
{% if bindpaths %}setenv("SINGULARITY_BINDPATH", "{{ bindpaths }}"){% endif %}
setenv("SINGULARITY_SHELL", "{{ singularity_shell }}")

-- interactive shell to any container
local containerPath = '{{ container_sif }}'
local shellCmd = "singularity shell -s {{ singularity_shell }} -B {% if bindpaths %}{{ bindpaths }}{% endif %} ".. containerPath
local execCmd = "singularity exec -B {% if bindpaths %}{{ bindpaths }}{% endif %} ".. containerPath

-- set_shell_function takes bashStr and cshStr
set_shell_function("{{ name }}-shell", shellCmd  ..  "$@",  shellCmd .. "$*")

-- exec functions to provide "alias" to module commands
{% for alias, entrypoint in aliases.items() %}
set_shell_function("{{ alias }}", execCmd .. "{{ entrypoint }}", execCmd .. "{{ entrypoint }}")
{% endfor %}

whatis("Name        : ", myModuleName())
whatis("Version     : ", myModuleVersion())
{% if description %}whatis("Category    : {{ description }}"){% endif %}
whatis("URL         : {{ url }}")
