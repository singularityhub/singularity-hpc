-- LMOD Module
-- Created by singularity-hpc (https://github.com/singularityhub/singularity-hpc)
-- ##
-- {{ name }} on {{ creation_date }}
--

help(
[[
This module is a singularity container wrapper for {{ name }} v{{ version }}
{% if description %}{{ description }}{% endif %}

Commands include:

 - {{ prefix }}{{ flatname }}-shell:
       singularity shell -s {{ singularity_shell }} {% if bindpaths %}-B {{ bindpaths }} {% endif %}{{ container_sif }}

{% if aliases %}{% for alias in aliases %} - {{ alias.name }}:
       singularity exec {% if bindpaths %}-B {{ bindpaths }} {% endif %}{% if alias.options %}{{ alias.options }} {% endif %}{{ container_sif }} {{ alias.command }}")
{% endfor %}{% else %} - {{ prefix }}{{ flatname }}: singularity run {% if bindpaths %}-B {{ bindpaths }}{% endif %}{{ container_sif }}{% endif %}]]) 

{% if singularity_module %}load("{{ singularity_module }}"){% endif %}

-- we probably don't need this
local MODULEPATH="{{ module_dir }}"

-- singularity environment variables to bind the paths and set shell
{% if bindpaths %}setenv("SINGULARITY_BINDPATH", "{{ bindpaths }}"){% endif %}
setenv("SINGULARITY_SHELL", "{{ singularity_shell }}")

-- interactive shell to any container, plus exec for aliases
local containerPath = '{{ container_sif }}'
local shellCmd = "singularity shell -s {{ singularity_shell }} {% if bindpaths %}-B {{ bindpaths }}{% endif %} " .. containerPath
local execCmd = "singularity exec {% if bindpaths %}-B {{ bindpaths }}{% endif %} "
local runCmd = "singularity run {% if bindpaths %}-B {{ bindpaths }}{% endif %} " .. containerPath

-- set_shell_function takes bashStr and cshStr
set_shell_function("{{ prefix }}{{ flatname }}-shell", shellCmd,  shellCmd)

-- conflict with modules with the same name
conflict(myModuleName(){% if aliases %}{% for alias in aliases %},"{{ alias.name }}"{% endfor %}{% endif %})

-- exec functions to provide "alias" to module commands
{% if aliases %}{% for alias in aliases %}
set_shell_function("{{ alias.name }}", execCmd .. {% if alias.options %} "{{ alias.options }} " .. {% endif %} containerPath .. " {{ alias.command }} ", execCmd .. {% if alias.options %} "{{ alias.options }} " .. {% endif %} containerPath .. " {{ alias.command }}")
{% endfor %}{% else %}
-- If we don't have aliases, just have a container run
set_shell_function("{{ prefix }}{{ flatname }}", runCmd,  runCmd){% endif %}


whatis("Name        : " .. myModuleName())
whatis("Version     : " .. myModuleVersion())
{% if description %}whatis("Category    : {{ description }}"){% endif %}
{% if url %} whatis("URL         : {{ url }}"){% endif %}
{% if deffile %}whatis("Singularity Recipe    : {{ deffile }}"){% endif %}
{% if labels %}{% for key, value in labels.items() %}whatis("{{ key }}    : {{ value }}")
{% endfor %}{% endif %}
