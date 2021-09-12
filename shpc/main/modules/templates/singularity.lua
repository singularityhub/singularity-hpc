-- Lmod Module
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

 - {|module_name|}-run:
       singularity run {% if features.gpu %}{{ features.gpu }} {% endif %}{% if features.home %}--home {{ features.home }} {% endif %}{% if features.x11 %}-B {{ features.x11 }} {% endif %}{% if envfile %}-B {{ module_dir }}/{{ envfile }}:/.singularity.d/env/{{ envfile }}{% endif %} {% if bindpaths %}-B {{ bindpaths }} {% endif %}<container>
 - {|module_name|}-shell:
       singularity shell -s {{ singularity_shell }} {% if features.gpu %}{{ features.gpu }} {% endif %}{% if features.home %}--home {{ features.home }} {% endif %}{% if features.x11 %}-B {{ features.x11 }} {% endif %}{% if envfile %}-B {{ module_dir }}/{{ envfile }}:/.singularity.d/env/{{ envfile }}{% endif %} {% if bindpaths %}-B {{ bindpaths }} {% endif %}<container>
 - {|module_name|}-exec:
       singularity exec {% if features.gpu %}{{ features.gpu }} {% endif %}{% if features.home %}--home {{ features.home }} {% endif %}{% if features.x11 %}-B {{ features.x11 }} {% endif %}{% if envfile %}-B {{ module_dir }}/{{ envfile }}:/.singularity.d/env/{{ envfile }}{% endif %} {% if bindpaths %}-B {{ bindpaths }} {% endif %}<container> "$@"
 - {|module_name|}-inspect-runscript:
       singularity inspect -r <container>
 - {|module_name|}-inspect-deffile:
       singularity inspect -d <container>

{% if aliases %}{% for alias in aliases %} - {{ alias.name }}:
       singularity exec {% if features.gpu %}{{ features.gpu }} {% endif %}{% if features.home %}--home {{ features.home }} {% endif %}{% if features.x11 %}-B {{ features.x11 }} {% endif %}{% if envfile %}-B {{ module_dir }}/{{ envfile }}:/.singularity.d/env/{{ envfile }}{% endif %} {% if bindpaths %}-B {{ bindpaths }} {% endif %}{% if alias.singularity_options %}{{ alias.singularity_options }} {% endif %}<container> {{ alias.command }}
{% endfor %}{% else %} - {|module_name|}: singularity run {% if features.gpu %}{{ features.gpu }} {% endif %}{% if features.home %}--home {{ features.home }} {% endif %}{% if features.x11 %}-B {{ features.x11 }} {% endif %}{% if envfile %}-B {{ module_dir }}/{{ envfile }}:/.singularity.d/env/{{ envfile }}{% endif %} {% if bindpaths %}-B {{ bindpaths }}{% endif %}<container>{% endif %}

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
setenv ("SINGULARITY_OPTS", "")
setenv ("SINGULARITY_COMMAND_OPTS", "")

-- interactive shell to any container, plus exec for aliases
local containerPath = '{{ container_sif }}'
local shellCmd = "singularity ${SINGULARITY_OPTS} shell ${SINGULARITY_COMMAND_OPTS} -s {{ singularity_shell }} {% if features.gpu %}{{ features.gpu }} {% endif %}{% if features.home %}--home {{ features.home }} {% endif %}{% if features.x11 %}-B {{ features.x11 }} {% endif %}{% if envfile %}-B {{ module_dir }}/{{ envfile }}:/.singularity.d/env/{{ envfile }}{% endif %} {% if bindpaths %}-B {{ bindpaths }}{% endif %} " .. containerPath
local execCmd = "singularity ${SINGULARITY_OPTS} exec ${SINGULARITY_COMMAND_OPTS} {% if features.gpu %}{{ features.gpu }} {% endif %}{% if features.home %}--home {{ features.home }} {% endif %}{% if features.x11 %}-B {{ features.x11 }} {% endif %}{% if envfile %}-B {{ module_dir }}/{{ envfile }}:/.singularity.d/env/{{ envfile }}{% endif %} {% if bindpaths %}-B {{ bindpaths }}{% endif %} "
local runCmd = "singularity ${SINGULARITY_OPTS} run ${SINGULARITY_COMMAND_OPTS} {% if features.gpu %}{{ features.gpu }} {% endif %}{% if features.home %}--home {{ features.home }} {% endif %}{% if features.x11 %}-B {{ features.x11 }} {% endif %}{% if envfile %}-B {{ module_dir }}/{{ envfile }}:/.singularity.d/env/{{ envfile }}{% endif %} {% if bindpaths %}-B {{ bindpaths }}{% endif %} " .. containerPath
local inspectCmd = "singularity ${SINGULARITY_OPTS} inspect ${SINGULARITY_COMMAND_OPTS} " 

-- set_shell_function takes bashStr and cshStr
set_shell_function("{|module_name|}-shell", shellCmd,  shellCmd)

-- conflict with modules with the same name
conflict(myModuleName(){% if aliases %}{% for alias in aliases %}{% if alias.name != name %},"{{ alias.name }}"{% endif %}{% endfor %}{% endif %})

-- exec functions to provide "alias" to module commands
{% if aliases %}{% for alias in aliases %}
set_shell_function("{{ alias.name }}", execCmd .. {% if alias.singularity_options %} "{{ alias.singularity_options }} " .. {% endif %} containerPath .. " {{ alias.command }} $@", execCmd .. {% if alias.singularity_options %} "{{ alias.singularity_options }} " .. {% endif %} containerPath .. " {{ alias.command }}")
{% endfor %}{% endif %}

{% if aliases %}
if (myShellName() == "bash") then
{% for alias in aliases %}execute{cmd="export -f {{ alias.name }}", modeA={"load"}}
{% endfor %}
end{% endif %}

-- A customizable exec function
set_shell_function("{|module_name|}-exec", execCmd .. containerPath .. " $@",  execCmd .. containerPath)

-- Always provide a container run
set_shell_function("{|module_name|}-run", runCmd .. " $@",  runCmd)

-- Inspect runscript or deffile easily!
set_shell_function("{|module_name|}-inspect-runscript", inspectCmd .. " -r  " .. containerPath,  inspectCmd .. containerPath)
set_shell_function("{|module_name|}-inspect-deffile", inspectCmd .. " -d  " .. containerPath,  inspectCmd .. containerPath)

whatis("Name        : " .. myModuleName())
whatis("Version     : " .. myModuleVersion())
{% if description %}whatis("Description    : {{ description }}"){% endif %}
{% if url %}whatis("Url         : {{ url }}"){% endif %}
{% if labels %}{% for key, value in labels.items() %}whatis("{{ key }}    : {{ value }}")
{% endfor %}{% endif %}
