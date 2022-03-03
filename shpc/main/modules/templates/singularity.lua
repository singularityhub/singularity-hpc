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
       singularity run {% if features.gpu %}{{ features.gpu }} {% endif %}{% if features.home %}-B {{ features.home }} --home {{ features.home }} {% endif %}{% if features.x11 %}-B {{ features.x11 }} {% endif %}{% if settings.environment_file %}-B <moduleDir>/{{ settings.environment_file }}:/.singularity.d/env/{{ settings.environment_file }}{% endif %} {% if settings.bindpaths %}-B {{ settings.bindpaths }} {% endif %}<container> "$@"
 - {|module_name|}-shell:
       singularity shell -s {{ settings.singularity_shell }} {% if features.gpu %}{{ features.gpu }} {% endif %}{% if features.home %}-B {{ features.home }} --home {{ features.home }} {% endif %}{% if features.x11 %}-B {{ features.x11 }} {% endif %}{% if settings.environment_file %}-B <moduleDir>/{{ settings.environment_file }}:/.singularity.d/env/{{ settings.environment_file }}{% endif %} {% if settings.bindpaths %}-B {{ settings.bindpaths }} {% endif %}<container>
 - {|module_name|}-exec:
       singularity exec {% if features.gpu %}{{ features.gpu }} {% endif %}{% if features.home %}-B {{ features.home }} --home {{ features.home }} {% endif %}{% if features.x11 %}-B {{ features.x11 }} {% endif %}{% if settings.environment_file %}-B <moduleDir>/{{ settings.environment_file }}:/.singularity.d/env/{{ settings.environment_file }}{% endif %} {% if settings.bindpaths %}-B {{ settings.bindpaths }} {% endif %}<container> "$@"
 - {|module_name|}-inspect-runscript:
       singularity inspect -r <container>
 - {|module_name|}-inspect-deffile:
       singularity inspect -d <container>

{% if aliases %}{% for alias in aliases %} - {{ alias.name }}:
       singularity exec {% if features.gpu %}{{ features.gpu }} {% endif %}{% if features.home %}-B {{ features.home }} --home {{ features.home }} {% endif %}{% if features.x11 %}-B {{ features.x11 }} {% endif %}{% if settings.environment_file %}-B <moduleDir>/{{ settings.environment_file }}:/.singularity.d/env/{{ settings.environment_file }}{% endif %} {% if settings.bindpaths %}-B {{ settings.bindpaths }} {% endif %}{% if alias.singularity_options %}{{ alias.singularity_options }} {% endif %}<container> {{ alias.command }} "$@"
{% endfor %}{% endif %}

For each of the above, you can export:

 - SINGULARITY_OPTS: to define custom options for singularity (e.g., --debug)
 - SINGULARITY_COMMAND_OPTS: to define custom options for the command (e.g., -b)
]]) 

{% if settings.singularity_module %}load("{{ settings.singularity_module }}"){% endif %}

-- directory containing this modulefile (dynamically defined)
local moduleDir = myFileName():match("(.*[/])") or "."

-- singularity environment variable to set shell
setenv("SINGULARITY_SHELL", "{{ settings.singularity_shell }}")

-- Environment: only set options and command options if not already set
if not os.getenv("SINGULARITY_OPTS") then setenv ("SINGULARITY_OPTS", "") end
if not os.getenv("SINGULARITY_COMMAND_OPTS") then setenv ("SINGULARITY_COMMAND_OPTS", "") end

-- interactive shell to any container, plus exec for aliases
local containerPath = '{{ container_sif }}'
local shellCmd = "singularity ${SINGULARITY_OPTS} shell ${SINGULARITY_COMMAND_OPTS} -s {{ settings.singularity_shell }} {% if features.gpu %}{{ features.gpu }} {% endif %}{% if features.home %}-B {{ features.home }} --home {{ features.home }} {% endif %}{% if features.x11 %}-B {{ features.x11 }} {% endif %}{% if settings.environment_file %}-B " .. moduleDir .. "/{{ settings.environment_file }}:/.singularity.d/env/{{ settings.environment_file }}{% endif %} {% if settings.bindpaths %}-B {{ settings.bindpaths }}{% endif %} " .. containerPath
local execCmd = "singularity ${SINGULARITY_OPTS} exec ${SINGULARITY_COMMAND_OPTS} {% if features.gpu %}{{ features.gpu }} {% endif %}{% if features.home %}-B {{ features.home }} --home {{ features.home }} {% endif %}{% if features.x11 %}-B {{ features.x11 }} {% endif %}{% if settings.environment_file %}-B " .. moduleDir .. "/{{ settings.environment_file }}:/.singularity.d/env/{{ settings.environment_file }}{% endif %} {% if settings.bindpaths %}-B {{ settings.bindpaths }}{% endif %} "
local runCmd = "singularity ${SINGULARITY_OPTS} run ${SINGULARITY_COMMAND_OPTS} {% if features.gpu %}{{ features.gpu }} {% endif %}{% if features.home %}-B {{ features.home }} --home {{ features.home }} {% endif %}{% if features.x11 %}-B {{ features.x11 }} {% endif %}{% if settings.environment_file %}-B " .. moduleDir .. "/{{ settings.environment_file }}:/.singularity.d/env/{{ settings.environment_file }}{% endif %} {% if settings.bindpaths %}-B {{ settings.bindpaths }}{% endif %} " .. containerPath
local inspectCmd = "singularity ${SINGULARITY_OPTS} inspect ${SINGULARITY_COMMAND_OPTS} " 

-- set_shell_function takes bashStr and cshStr
set_shell_function("{|module_name|}-shell", shellCmd,  shellCmd)

-- conflict with modules with the same name
conflict("{{ parsed_name.tool }}"{% if name != parsed_name.tool %},"{{ name }}"{% endif %}{% if aliases %}{% for alias in aliases %}{% if alias.name != parsed_name.tool %},"{{ alias.name }}"{% endif %}{% endfor %}{% endif %})

-- if we have any wrapper scripts, add bin to path
{% if wrapper_scripts %}prepend_path("PATH", pathJoin(moduleDir, "bin")){% endif %}

-- "aliases" to module commands
{% if aliases %}{% for alias in aliases %}{% if alias.name not in wrapper_scripts %}set_shell_function("{{ alias.name }}", execCmd .. {% if alias.singularity_options %} "{{ alias.singularity_options }} " .. {% endif %} containerPath .. " {{ alias.command }} \"$@\"", execCmd .. {% if alias.singularity_options %} "{{ alias.singularity_options }} " .. {% endif %} containerPath .. " {{ alias.command }}"){% endif %}
{% endfor %}{% endif %}

{% if aliases %}
if (myShellName() == "bash") then
{% for alias in aliases %}{% if alias.name not in wrapper_scripts %}execute{cmd="export -f {{ alias.name }}", modeA={"load"}}{% endif %}
{% endfor %}
end{% endif %}

-- A customizable exec function
set_shell_function("{|module_name|}-exec", execCmd .. containerPath .. " \"$@\"",  execCmd .. containerPath)

-- Always provide a container run
set_shell_function("{|module_name|}-run", runCmd .. " \"$@\"",  runCmd)

-- Inspect runscript or deffile easily!
set_shell_function("{|module_name|}-inspect-runscript", inspectCmd .. " -r  " .. containerPath,  inspectCmd .. containerPath)
set_shell_function("{|module_name|}-inspect-deffile", inspectCmd .. " -d  " .. containerPath,  inspectCmd .. containerPath)

whatis("Name        : " .. myModuleName())
whatis("Version     : " .. myModuleVersion())
{% if description %}whatis("Description    : {{ description }}"){% endif %}
{% if url %}whatis("Url         : {{ url }}"){% endif %}
{% if labels %}{% for key, value in labels.items() %}whatis("{{ key }}    : {{ value }}")
{% endfor %}{% endif %}
