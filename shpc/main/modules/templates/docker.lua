-- Lmod Module
-- Created by singularity-hpc (https://github.com/singularityhub/singularity-hpc)
-- ##
-- {{ name }} on {{ creation_date }}
--

help(
[[
This module is a {{ command }} container wrapper for {{ name }} v{{ version }}
{% if description %}{{ description }}{% endif %}

Container:

 - {{ image }}

Commands include:

 - {|module_name|}-run:
       {{ command }} run --rm -i{% if tty %}t{% endif %} {% if envfile %}--env-file {{ module_dir }}/{{ envfile }}{% endif %} {% if bindpaths %}-v {{ bindpaths }} -v ${PWD} -w ${PWD} {% endif %}<container>
 - {|module_name|}-shell:
       {{ command }} run --rm -i{% if tty %}t{% endif %} {% if envfile %}--env-file {{ module_dir }}/{{ envfile }}{% endif %} {% if bindpaths %}-v {{ bindpaths }} -v ${PWD} -w ${PWD} {% endif %}<container>
 - {|module_name|}-exec:
       {{ command }} run -i{% if tty %}t{% endif %} --rm --entrypoint {{ shell }} {% if envfile %}--env-file {{ module_dir }}/{{ envfile }}{% endif %} {% if bindpaths %}-v {{ bindpaths }} {% endif %} -v ${PWD} -w ${PWD} <container> "$@"
 - {|module_name|}-inspect:
       {{ command }} inspect <container>

{% if aliases %}{% for alias in aliases %} - {{ alias.name }}:
       {{ command }} run --rm -i{% if tty %}t{% endif %} --entrypoint {{ alias.entrypoint }} {% if envfile %}--env-file {{ module_dir }}/{{ envfile }}{% endif %} {% if bindpaths %}-v {{ bindpaths }} {% endif %}{% if alias.options %}{{ alias.options }} {% endif %} -v ${PWD} -w ${PWD} <container> "{{ alias.args }}"
{% endfor %}{% endif %}

For each of the above, you can export:

 - DOCKER_OPTS: to define custom options for {{ command }}
 - DOCKER_COMMAND_OPTS: to define custom options for the command
]]) 

{% if podman_module %}load("{{ podman_module }}"){% endif %}
setenv ("DOCKER_OPTS", "")
setenv ("DOCKER_COMMAND_OPTS", "")

-- we probably don't need this
local MODULEPATH="{{ module_dir }}"

-- interactive shell to any container, plus exec for aliases
local containerPath = '{{ image }}'

local shellCmd = "{{ command }} ${DOCKER_OPTS} run -i{% if tty %}t{% endif %} ${DOCKER_COMMAND_OPTS} --entrypoint {{ shell }} --rm {% if envfile %}--env-file {{ module_dir }}/{{ envfile }}{% endif %} {% if bindpaths %}-v {{ bindpaths }} {% endif %} -v ${PWD} -w ${PWD} " .. containerPath
-- execCmd needs entrypoint to be the executor
local execCmd = "{{ command }} ${DOCKER_OPTS} run ${DOCKER_COMMAND_OPTS} -i{% if tty %}t{% endif %} --rm {% if envfile %}--env-file {{ module_dir }}/{{ envfile }}{% endif %} {% if bindpaths %}-v {{ bindpaths }} {% endif %} -v ${PWD} -w ${PWD} "
local runCmd = "{{ command }} ${DOCKER_OPTS} run ${DOCKER_COMMAND_OPTS} -i{% if tty %}t{% endif %} --rm {% if envfile %}--env-file {{ module_dir }}/{{ envfile }}{% endif %} {% if bindpaths %}-v {{ bindpaths }} {% endif %} -v ${PWD} -w ${PWD} " .. containerPath
local inspectCmd = "{{ command }} ${DOCKER_OPTS} inspect ${DOCKER_COMMAND_OPTS} " .. containerPath 

-- set_shell_function takes bashStr and cshStr
set_shell_function("{|module_name|}-shell", shellCmd,  shellCmd)

-- conflict with modules with the same name
conflict(myModuleName(){% if aliases %}{% for alias in aliases %},"{{ alias.name }}"{% endfor %}{% endif %})

-- exec functions to provide "alias" to module commands
{% if aliases %}{% for alias in aliases %}
set_shell_function("{{ alias.name }}", execCmd .. {% if alias.options %} "{{ alias.options }} " .. {% endif %} " --entrypoint {{ alias.entrypoint }} " .. containerPath .. " {{ alias.args }} $@", execCmd .. {% if alias.options %} "{{ alias.options }} " .. {% endif %} " --entrypoint {{ alias.entrypoint }} " .. containerPath .. " {{ alias.args }}")
{% endfor %}{% endif %}

{% if aliases %}
if (myShellName() == "bash") then
{% for alias in aliases %}execute{cmd="export -f {{ alias.name }}", modeA={"load"}}
{% endfor %}
end{% endif %}

-- A customizable exec function
set_shell_function("{|module_name|}-exec", execCmd .. " --entrypoint \"\" " .. containerPath .. " $@",  execCmd .. " --entrypoint \"\" " .. containerPath)

-- Always provide a container run
set_shell_function("{|module_name|}-run", runCmd .. " $@",  runCmd)

-- Inspect runscript or deffile easily!
set_shell_function("{|module_name|}-inspect", inspectCmd,  inspectCmd)

whatis("Name        : " .. myModuleName())
whatis("Version     : " .. myModuleVersion())
{% if description %}whatis("Description    : {{ description }}"){% endif %}
{% if url %}whatis("Url         : {{ url }}"){% endif %}
{% if labels %}{% for key, value in labels.items() %}whatis("{{ key }}    : {{ value }}")
{% endfor %}{% endif %}
