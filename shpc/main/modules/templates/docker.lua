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
       {{ command }} run -i{% if settings.enable_tty %}t{% endif %} -u `id -u`:`id -g` --rm {% if settings.environment_file %}--env-file <moduleDir>/{{ settings.environment_file }} {% endif %} {% if settings.bindpaths %}-v {{ settings.bindpaths }} {% endif %}{% if features.home %}-v {{ features.home }} {% endif %}-v ${PWD} -w ${PWD} <container> "$@"
 - {|module_name|}-shell:
       {{ command }} run -i{% if settings.enable_tty %}t{% endif %} -u `id -u`:`id -g` --rm {% if settings.environment_file %}--env-file <moduleDir>/{{ settings.environment_file }} {% endif %} {% if settings.bindpaths %}-v {{ settings.bindpaths }} {% endif %}{% if features.home %}-v {{ features.home }} {% endif %}--entrypoint {{ shell }} -v ${PWD} -w ${PWD}<container>
 - {|module_name|}-exec:
       {{ command }} run -i{% if settings.enable_tty %}t{% endif %} -u `id -u`:`id -g` --rm --entrypoint "" {% if settings.environment_file %}--env-file <moduleDir>/{{ settings.environment_file }} {% endif %} {% if settings.bindpaths %}-v {{ settings.bindpaths }} {% endif %}{% if features.home %}-v {{ features.home }} {% endif %} -v ${PWD} -w ${PWD} <container> "$@"
 - {|module_name|}-inspect:
       {{ command }} inspect <container>

{% if aliases %}{% for alias in aliases %} - {{ alias.name }}:
       {{ command }} run -i{% if settings.enable_tty %}t{% endif %} -u `id -u`:`id -g` --rm --entrypoint {{ alias.entrypoint }} {% if settings.environment_file %}--env-file <moduleDir>/{{ settings.environment_file }}{% endif %} {% if settings.bindpaths %}-v {{ settings.bindpaths }} {% endif %}{% if features.home %}-v {{ features.home }} {% endif %}{% if alias.docker_options %}{{ alias.docker_options }} {% endif %} -v ${PWD} -w ${PWD} <container> "{{ alias.args }}" "$@"
{% endfor %}{% endif %}

For each of the above, you can export:

 - PODMAN_OPTS: to define custom options for {{ command }}
 - PODMAN_COMMAND_OPTS: to define custom options for the command
]]) 

{% if settings.podman_module %}load("{{ settings.podman_module }}"){% endif %}

-- Environment: only set options and command options if not already set
if not os.getenv("PODMAN_OPTS") then setenv ("PODMAN_OPTS", "") end
if not os.getenv("PODMAN_COMMAND_OPTS") then setenv ("PODMAN_COMMAND_OPTS", "") end

-- directory containing this modulefile (dynamically defined)
local moduleDir = myFileName():match("(.*[/])") or "."

-- interactive shell to any container, plus exec for aliases
local containerPath = '{{ image }}'

local shellCmd = "{{ command }} ${PODMAN_OPTS} run -i{% if settings.enable_tty %}t{% endif %} ${PODMAN_COMMAND_OPTS} -u `id -u`:`id -g` --rm --entrypoint {{ shell }} {% if settings.environment_file %}--env-file " .. moduleDir .. "/{{ settings.environment_file }}{% endif %} {% if settings.bindpaths %}-v {{ settings.bindpaths }} {% endif %}{% if features.home %}-v {{ features.home }} {% endif %} -v ${PWD} -w ${PWD} " .. containerPath
-- execCmd needs entrypoint to be the executor
local execCmd = "{{ command }} ${PODMAN_OPTS} run ${PODMAN_COMMAND_OPTS} -i{% if settings.enable_tty %}t{% endif %} -u `id -u`:`id -g` --rm {% if settings.environment_file %}--env-file " .. moduleDir .. "/{{ settings.environment_file }}{% endif %} {% if settings.bindpaths %}-v {{ settings.bindpaths }} {% endif %}{% if features.home %}-v {{ features.home }} {% endif %} -v ${PWD} -w ${PWD} "
local runCmd = "{{ command }} ${PODMAN_OPTS} run ${PODMAN_COMMAND_OPTS} -i{% if settings.enable_tty %}t{% endif %} -u `id -u`:`id -g` --rm {% if settings.environment_file %}--env-file " .. moduleDir .. "/{{ settings.environment_file }}{% endif %} {% if settings.bindpaths %}-v {{ settings.bindpaths }} {% endif %}{% if features.home %}-v {{ features.home }} {% endif %} -v ${PWD} -w ${PWD} " .. containerPath
local inspectCmd = "{{ command }} ${PODMAN_OPTS} inspect ${PODMAN_COMMAND_OPTS} " .. containerPath 

-- set_shell_function takes bashStr and cshStr
set_shell_function("{|module_name|}-shell", shellCmd,  shellCmd)

-- conflict with modules with the same name
conflict("{{ parsed_name.tool }}"{% if name != parsed_name.tool %},"{{ name }}"{% endif %}{% if aliases %}{% for alias in aliases %}{% if alias.name != parsed_name.tool %},"{{ alias.name }}"{% endif %}{% endfor %}{% endif %})

-- if we have any wrapper scripts, add the bin directory
{% if wrapper_scripts %}prepend_path("PATH", pathJoin(moduleDir, "bin")){% endif %}

-- "aliases" to module commands - generate only if not a wrapper script already generated
{% if aliases %}{% for alias in aliases %}{% if alias.name not in wrapper_scripts %}set_shell_function("{{ alias.name }}", execCmd .. {% if alias.docker_options %} "{{ alias.docker_options }} " .. {% endif %} " --entrypoint {{ alias.entrypoint }} " .. containerPath .. " {{ alias.args }} \"$@\"", execCmd .. {% if alias.docker_options %} "{{ alias.docker_options }} " .. {% endif %} " --entrypoint {{ alias.entrypoint }} " .. containerPath .. " {{ alias.args }}"){% endif %}
{% endfor %}{% endif %}

{% if aliases %}
if (myShellName() == "bash") then
{% for alias in aliases %}{% if alias.name not in wrapper_scripts %}execute{cmd="export -f {{ alias.name }}", modeA={"load"}}{% endif %}
{% endfor %}
end{% endif %}

-- A customizable exec function
set_shell_function("{|module_name|}-exec", execCmd .. " --entrypoint \"\" " .. containerPath .. " \"$@\"",  execCmd .. " --entrypoint \"\" " .. containerPath)

-- Always provide a container run
set_shell_function("{|module_name|}-run", runCmd .. " \"$@\"",  runCmd)

-- Inspect runscript or deffile easily!
set_shell_function("{|module_name|}-inspect", inspectCmd,  inspectCmd)

whatis("Name        : " .. myModuleName())
whatis("Version     : " .. myModuleVersion())
{% if description %}whatis("Description    : {{ description }}"){% endif %}
{% if url %}whatis("Url         : {{ url }}"){% endif %}
{% if labels %}{% for key, value in labels.items() %}whatis("{{ key }}    : {{ value }}")
{% endfor %}{% endif %}
