-- LMOD Module
-- Created by singularity-hpc (https://github.com/singularityhub/singularity-hpc)
-- ##
-- {{ name }} on {{ creation_date }}
--

help(
[[
This module is a singularity container wrapper for {{ name }} v{{ version }}
{% if description %}{{ description }}{% endif %}

Container:

 - {{ container_sif }}

Commands include:

 - {{ prefix }}{{ flatname }}-run:
       singularity run {% if bindpaths %}-B {{ bindpaths }} {% endif %}<container>
 - {{ prefix }}{{ flatname }}-shell:
       singularity shell -s {{ singularity_shell }} {% if bindpaths %}-B {{ bindpaths }} {% endif %}<container>
 - {{ prefix }}{{ flatname }}-exec:
       singularity exec -s {{ singularity_shell }} {% if bindpaths %}-B {{ bindpaths }} {% endif %}<container> "$@"
 - {{ prefix }}{{ flatname }}-inspect-runscript:
       singularity inspect -r <container>
 - {{ prefix }}{{ flatname }}-inspect-deffile:
       singularity inspect -d <container>

{% if aliases %}{% for alias in aliases %} - {{ alias.name }}:
       singularity exec {% if bindpaths %}-B {{ bindpaths }} {% endif %}{% if alias.options %}{{ alias.options }} {% endif %}<container> {{ alias.command }}
{% endfor %}{% else %} - {{ prefix }}{{ flatname }}: singularity run {% if bindpaths %}-B {{ bindpaths }}{% endif %}<container>{% endif %}

For each of the above, you can export:

 - SINGULARITY_OPTS: to define custom options for singularity (e.g., --debug)
 - SINGULARITY_COMMAND_OPTS: to define custom options for the command (e.g., -b)
]]) 

{% if singularity_module %}load("{{ singularity_module }}"){% endif %}

-- we probably don't need this
local MODULEPATH="{{ module_dir }}"

-- singularity environment variables to bind the paths and set shell
{% if bindpaths %}setenv("SINGULARITY_BINDPATH", "{{ bindpaths }}"){% endif %}
setenv("SINGULARITY_SHELL", "{{ singularity_shell }}")

-- interactive shell to any container, plus exec for aliases
local containerPath = '{{ container_sif }}'
local shellCmd = "singularity ${SINGULARITY_OPTS} shell ${SINGULARITY_COMMAND_OPTS} -s {{ singularity_shell }} {% if bindpaths %}-B {{ bindpaths }}{% endif %} " .. containerPath
local execCmd = "singularity ${SINGULARITY_OPTS} exec ${SINGULARITY_COMMAND_OPTS} {% if bindpaths %}-B {{ bindpaths }}{% endif %} "
local runCmd = "singularity ${SINGULARITY_OPTS} run ${SINGULARITY_COMMAND_OPTS} {% if bindpaths %}-B {{ bindpaths }}{% endif %} " .. containerPath .. " ${ SINGULARITY_COMMAND_ARGS }"
local inspectCmd = "singularity ${SINGULARITY_OPTS} inspect ${SINGULARITY_COMMAND_OPTS} " 

-- set_shell_function takes bashStr and cshStr
set_shell_function("{{ prefix }}{{ flatname }}-shell", shellCmd,  shellCmd)

-- conflict with modules with the same name
conflict(myModuleName(){% if aliases %}{% for alias in aliases %},"{{ alias.name }}"{% endfor %}{% endif %})

-- exec functions to provide "alias" to module commands
{% if aliases %}{% for alias in aliases %}
set_shell_function("{{ alias.name }}", execCmd .. {% if alias.options %} "{{ alias.options }} " .. {% endif %} containerPath .. " {{ alias.command }} $@", execCmd .. {% if alias.options %} "{{ alias.options }} " .. {% endif %} containerPath .. " {{ alias.command }} $*")
{% endfor %}{% endif %}

-- A customizable exec function
set_shell_function("{{ prefix }}{{ flatname }}-exec", execCmd .. containerPath .. " ${SINGULARITY_COMMAND_ARGS}  $@",  execCmd .. containerPath .. " ${SINGULARITY_COMMAND_ARGS} $*")

-- Always provide a container run
set_shell_function("{{ prefix }}{{ flatname }}-run", runCmd .. " $@",  runCmd .. " $*")

-- Inspect runscript or deffile easily!
set_shell_function("{{ prefix }}{{ flatname }}-inspect-runscript", inspectCmd .. " -r  " .. containerPath,  inspectCmd .. containerPath)
set_shell_function("{{ prefix }}{{ flatname }}-inspect-deffile", inspectCmd .. " -d  " .. containerPath,  inspectCmd .. containerPath)

whatis("Name        : " .. myModuleName())
whatis("Version     : " .. myModuleVersion())
{% if description %}whatis("Category    : {{ description }}"){% endif %}
{% if url %}whatis("URL         : {{ url }}"){% endif %}
{% if labels %}{% for key, value in labels.items() %}whatis("{{ key }}    : {{ value }}")
{% endfor %}{% endif %}
