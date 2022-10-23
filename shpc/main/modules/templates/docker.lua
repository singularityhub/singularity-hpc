-- Lmod Module
-- Created by singularity-hpc (https://github.com/singularityhub/singularity-hpc)
-- ##
-- {{ module.name }} on {{ creation_date }}
--

help(
[[
This module is a {{ command }} container wrapper for {{ module.name }} v{{ module.tag.name }}
{% if description %}{{ module.config.description }}{% endif %}

Container:

 - {{ module.container_path }}

Commands include:

 - {|module_name|}-run:
       {{ command }} run -i{% if settings.enable_tty %}t{% endif %} -u `id -u`:`id -g` --rm {% if settings.environment_file %}--env-file <moduleDir>/{{ settings.environment_file }} {% endif %} {% if settings.bindpaths %}-v {{ settings.bindpaths }} {% endif %}{% if features.home %}-v {{ features.home }} {% endif %}-v ${PWD} -w ${PWD} <container> "$@"
 - {|module_name|}-shell:
       {{ command }} run -i{% if settings.enable_tty %}t{% endif %} -u `id -u`:`id -g` --rm {% if settings.environment_file %}--env-file <moduleDir>/{{ settings.environment_file }} {% endif %} {% if settings.bindpaths %}-v {{ settings.bindpaths }} {% endif %}{% if features.home %}-v {{ features.home }} {% endif %}--entrypoint {{ shell }} -v ${PWD} -w ${PWD}<container>
 - {|module_name|}-exec:
       {{ command }} run -i{% if settings.enable_tty %}t{% endif %} -u `id -u`:`id -g` --rm --entrypoint "" {% if settings.environment_file %}--env-file <moduleDir>/{{ settings.environment_file }} {% endif %} {% if settings.bindpaths %}-v {{ settings.bindpaths }} {% endif %}{% if features.home %}-v {{ features.home }} {% endif %} -v ${PWD} -w ${PWD} <container> "$@"
 - {|module_name|}-inspect:
       {{ command }} inspect <container>
 - {|module_name|}-container:
       echo "$PODMAN_CONTAINER"

{% if aliases %}{% for alias in aliases %} - {{ alias.name }}:
       {{ command }} run -i{% if settings.enable_tty %}t{% endif %} -u `id -u`:`id -g` --rm --entrypoint {{ alias.entrypoint }} {% if settings.environment_file %}--env-file <moduleDir>/{{ settings.environment_file }}{% endif %} {% if settings.bindpaths %}-v {{ settings.bindpaths }} {% endif %}{% if features.home %}-v {{ features.home }} {% endif %}{% if alias.docker_options %}{{ alias.docker_options }} {% endif %} -v ${PWD} -w ${PWD} <container> "{{ alias.args }}" "$@"
{% endfor %}{% endif %}

For each of the above, you can export:

 - PODMAN_OPTS: to define custom options for {{ command }}
 - PODMAN_COMMAND_OPTS: to define custom options for the command
 - PODMAN_CONTAINER: the container unique resource identifier
]])

{% include "includes/default_version.lua" %}
{% include "includes/load_view.lua" %}
{% if settings.podman_module %}load("{{ settings.podman_module }}"){% endif %}

-- Environment: only set options and command options if not already set
if not os.getenv("PODMAN_OPTS") then setenv ("PODMAN_OPTS", "") end
if not os.getenv("PODMAN_COMMAND_OPTS") then setenv ("PODMAN_COMMAND_OPTS", "") end

-- directory containing this modulefile, once symlinks resolved (dynamically defined)
local moduleDir = subprocess("realpath " .. myFileName()):match("(.*[/])") or "."

-- interactive shell to any container, plus exec for aliases
local containerPath = '{{ module.container_path }}'

-- service environment variable to access docker URI
setenv("PODMAN_CONTAINER", containerPath)

local shellCmd = "{{ command }} ${PODMAN_OPTS} run -i{% if settings.enable_tty %}t{% endif %} ${PODMAN_COMMAND_OPTS} -u `id -u`:`id -g` --rm --entrypoint {{ shell }} {% if settings.environment_file %}--env-file " .. moduleDir .. "/{{ settings.environment_file }}{% endif %} {% if settings.bindpaths %}-v {{ settings.bindpaths }} {% endif %}{% if features.home %}-v {{ features.home }} {% endif %} -v ${PWD} -w ${PWD} " .. containerPath
-- execCmd needs entrypoint to be the executor
local execCmd = "{{ command }} ${PODMAN_OPTS} run ${PODMAN_COMMAND_OPTS} -i{% if settings.enable_tty %}t{% endif %} -u `id -u`:`id -g` --rm {% if settings.environment_file %}--env-file " .. moduleDir .. "/{{ settings.environment_file }}{% endif %} {% if settings.bindpaths %}-v {{ settings.bindpaths }} {% endif %}{% if features.home %}-v {{ features.home }} {% endif %} -v ${PWD} -w ${PWD} "
local runCmd = "{{ command }} ${PODMAN_OPTS} run ${PODMAN_COMMAND_OPTS} -i{% if settings.enable_tty %}t{% endif %} -u `id -u`:`id -g` --rm {% if settings.environment_file %}--env-file " .. moduleDir .. "/{{ settings.environment_file }}{% endif %} {% if settings.bindpaths %}-v {{ settings.bindpaths }} {% endif %}{% if features.home %}-v {{ features.home }} {% endif %} -v ${PWD} -w ${PWD} " .. containerPath
local inspectCmd = "{{ command }} ${PODMAN_OPTS} inspect ${PODMAN_COMMAND_OPTS} " .. containerPath

-- conflict with modules with the same name
conflict("{{ parsed_name.tool }}"{% if name != parsed_name.tool %},"{{ module.name }}"{% endif %}{% if aliases %}{% for alias in aliases %}{% if alias.name != parsed_name.tool %},"{{ alias.name }}"{% endif %}{% endfor %}{% endif %})

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

{% if wrapper_scripts %}{% else %}set_shell_function("{|module_name|}-container", "echo " .. containerPath, "echo " .. containerPath)

-- set_shell_function takes bashStr and cshStr
set_shell_function("{|module_name|}-shell", shellCmd,  shellCmd)

-- A customizable exec function
set_shell_function("{|module_name|}-exec", execCmd .. " --entrypoint \"\" " .. containerPath .. " \"$@\"",  execCmd .. " --entrypoint \"\" " .. containerPath)

-- Always provide a container run
set_shell_function("{|module_name|}-run", runCmd .. " \"$@\"",  runCmd)

-- Inspect runscript or deffile easily!
set_shell_function("{|module_name|}-inspect", inspectCmd,  inspectCmd){% endif %}

whatis("Name        : " .. myModuleName())
whatis("Version     : " .. myModuleVersion())
{% if description %}whatis("Description    : {{ module.config.description }}"){% endif %}
{% if url %}whatis("Url         : {{ module.config.url }}"){% endif %}
{% if labels %}{% for key, value in labels.items() %}whatis("{{ key }}    : {{ value }}")
{% endfor %}{% endif %}
