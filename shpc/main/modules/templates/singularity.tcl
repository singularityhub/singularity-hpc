#%Module

#=====
# Created by singularity-hpc (https://github.com/singularityhub/singularity-hpc)
# ##
# {{ name }} on {{ creation_date }}
#=====

proc ModulesHelp { } {

    puts stderr "This module is a singularity container wrapper for {{ name }} v{{ version }}"
    {% if description %}puts stderr "{{ description }}"{% endif %}
    puts stderr ""
    puts stderr "Container:"
    puts stderr ""
    puts stderr " - {{ container_sif }}"
    puts stderr ""
    puts stderr "Commands include:"
    puts stderr ""
    puts stderr " - {|module_name|}-run:"
    puts stderr "       singularity run {% if features.gpu %}{{ features.gpu }} {% endif %}{% if features.home %}-B {{ features.home | replace("$", "\$") }} --home {{ features.home | replace("$", "\$") }} {% endif %}{% if features.x11 %}-B {{ features.x11 | replace("$", "\$") }} {% endif %}{% if settings.environment_file %}-B <moduleDir>/{{ settings.environment_file }}:/.singularity.d/env/{{ settings.environment_file }}{% endif %} {% if settings.bindpaths %}-B {{ settings.bindpaths }} {% endif %}<container> \"\$@\""
    puts stderr " - {|module_name|}-shell:"
    puts stderr "       singularity shell -s {{ settings.singularity_shell }} {% if features.gpu %}{{ features.gpu }} {% endif %}{% if features.home %}-B {{ features.home | replace("$", "\$") }} --home {{ features.home | replace("$", "\$") }} {% endif %}{% if features.x11 %}-B {{ features.x11 | replace("$", "\$") }} {% endif %}{% if settings.environment_file %}-B <moduleDir>/{{ settings.environment_file }}:/.singularity.d/env/{{ settings.environment_file }}{% endif %} {% if settings.bindpaths %}-B {{ settings.bindpaths }} {% endif %}<container>"
    puts stderr " - {|module_name|}-exec:"
    puts stderr "       singularity exec {% if features.gpu %}{{ features.gpu }} {% endif %}{% if features.home %}-B {{ features.home | replace("$", "\$") }} --home {{ features.home | replace("$", "\$") }} {% endif %}{% if features.x11 %}-B {{ features.x11 | replace("$", "\$") }} {% endif %}{% if settings.environment_file %}-B <moduleDir>/{{ settings.environment_file }}:/.singularity.d/env/{{ settings.environment_file }}{% endif %} {% if settings.bindpaths %}-B {{ settings.bindpaths }} {% endif %}<container> \"\$@\""
    puts stderr " - {|module_name|}-inspect-runscript:"
    puts stderr "       singularity inspect -r <container>"
    puts stderr " - {|module_name|}-inspect-deffile:"
    puts stderr "       singularity inspect -d <container>"
    puts stderr ""
{% if aliases %}{% for alias in aliases %}    puts stderr " - {{ alias.name }}:"
    puts stderr "       singularity exec {% if features.gpu %}{{ features.gpu }} {% endif %}{% if features.home %}-B {{ features.home | replace("$", "\$") }} --home {{ features.home | replace("$", "\$") }} {% endif %}{% if features.x11 %}-B {{ features.x11 | replace("$", "\$") }} {% endif %}{% if settings.environment_file %}-B <moduleDir>/{{ settings.environment_file }}:/.singularity.d/env/{{ settings.environment_file }}{% endif %} {% if settings.bindpaths %}-B {{ settings.bindpaths }} {% endif %}{% if alias.singularity_options %}{{ alias.singularity_options | replace("$", "\$") }} {% endif %}<container> {{ alias.command | replace("$", "\$") }} \"\$@\""
{% endfor %}{% endif %}
    puts stderr ""
    puts stderr "For each of the above, you can export:"
    puts stderr ""
    puts stderr " - SINGULARITY_OPTS: to define custom options for singularity (e.g., --debug)"
    puts stderr " - SINGULARITY_COMMAND_OPTS: to define custom options for the command (e.g., -b)"

}

# Environment - only set if not already defined
if { ![info exists ::env(SINGULARITY_OPTS)] } {
    setenv SINGULARITY_OPTS ""
} 
if { ![info exists ::env(SINGULARITY_COMMAND_OPTS)] } {
    setenv SINGULARITY_COMMAND_OPTS ""
} 

# Variables

set name        {{ name }}
set version     {{ version }}
set description "$name - $version"
set containerPath {{ container_sif }}
{% if description %}set notes       "{{ description }}"{% endif %}
{% if url %}set homepage    "{{ url }}"{% endif %}
set helpcommand "This module is a singularity container wrapper for {{ name }} v{{ version }}. {% if description %}{{ description }}{% endif %}"
{% if labels %}{% for key, value in labels.items() %}set {{ key }} "{{ value }}"
{% endfor %}{% endif %}

# directory containing this modulefile (dynamically defined)
set moduleDir   "[file dirname ${ModulesCurrentModulefile}]"

# conflict with modules with the same alias name
conflict {{ parsed_name.tool }}
{% if name != parsed_name.tool %}conflict {{ name }}{% endif %}
{% if aliases %}{% for alias in aliases %}{% if alias.name != parsed_name.tool %}conflict {{ alias.name }}{% endif %}
{% endfor %}{% endif %}

# singularity environment variable to set shell
setenv SINGULARITY_SHELL {{ settings.singularity_shell }}

# interactive shell to any container, plus exec for aliases
set shellCmd "singularity \${SINGULARITY_OPTS} shell \${SINGULARITY_COMMAND_OPTS} -s {{ settings.singularity_shell }} {% if features.gpu %}{{ features.gpu }} {% endif %}{% if features.home %}-B {{ features.home | replace("$", "\$") }} --home {{ features.home | replace("$", "\$") }} {% endif %}{% if features.x11 %}-B {{ features.x11 | replace("$", "\$") }} {% endif %}{% if settings.environment_file %}-B ${moduleDir}/{{ settings.environment_file }}:/.singularity.d/env/{{ settings.environment_file }}{% endif %} {% if settings.bindpaths %}-B {{ settings.bindpaths }}{% endif %} ${containerPath}"
set execCmd "singularity \${SINGULARITY_OPTS} exec \${SINGULARITY_COMMAND_OPTS} {% if features.gpu %}{{ features.gpu }} {% endif %}{% if features.home %}-B {{ features.home | replace("$", "\$") }} --home {{ features.home | replace("$", "\$") }} {% endif %}{% if features.x11 %}-B {{ features.x11 | replace("$", "\$") }} {% endif %}{% if settings.environment_file %}-B ${moduleDir}/{{ settings.environment_file }}:/.singularity.d/env/{{ settings.environment_file }}{% endif %} {% if settings.bindpaths %}-B {{ settings.bindpaths }}{% endif %} "
set runCmd "singularity \${SINGULARITY_OPTS} run \${SINGULARITY_COMMAND_OPTS} {% if features.gpu %}{{ features.gpu }} {% endif %}{% if features.home %}-B {{ features.home | replace("$", "\$") }} --home {{ features.home | replace("$", "\$") }} {% endif %}{% if features.x11 %}-B {{ features.x11 | replace("$", "\$") }} {% endif %}{% if settings.environment_file %}-B ${moduleDir}/{{ settings.environment_file }}:/.singularity.d/env/{{ settings.environment_file }}{% endif %} {% if settings.bindpaths %}-B {{ settings.bindpaths }}{% endif %} ${containerPath}"
set inspectCmd "singularity \${SINGULARITY_OPTS} inspect \${SINGULARITY_COMMAND_OPTS} " 

# set_shell_function takes bashStr and cshStr
set-alias {|module_name|}-shell "${shellCmd}"


# if we have any wrapper scripts, add bin to path
{% if wrapper_scripts %}prepend-path PATH "${moduleDir}/bin"{% endif %}

# "aliases" to module commands
{% if aliases %}if { [ module-info shell bash ] } {
  if { [ module-info mode load ] } {
{% for alias in aliases %} {% if alias.name not in wrapper_scripts %}    puts stdout "function {{ alias.name }}() { ${execCmd} {% if alias.singularity_options %} {{ alias.singularity_options | replace("$", "\$") }} {% endif %} ${containerPath} {{ alias.command | replace("$", "\$") }} \"\$@\"; }; export -f {{ alias.name }};"{% endif %}
{% endfor %}
  }
  if { [ module-info mode remove ] } {
{% for alias in aliases %} {% if alias.name not in wrapper_scripts %}    puts stdout "unset -f {{ alias.name }};"{% endif %}
{% endfor %}
  }
} else {
{% for alias in aliases %}{% if alias.name not in wrapper_scripts %} set-alias {{ alias.name }} "${execCmd} {% if alias.singularity_options %} {{ alias.singularity_options | replace("$", "\$") }} {% endif %} ${containerPath} {{ alias.command | replace("$", "\$") }}"{% endif %}
{% endfor %}
}{% endif %}

# A customizable exec function
if { [ module-info shell bash ] } {
  set-alias {|module_name|}-exec "${execCmd} ${containerPath} \"\$@\""
} else {
  set-alias {|module_name|}-exec "${execCmd} ${containerPath}"
}

# Always provide a container run
if { [ module-info shell bash ] } {
  set-alias {|module_name|}-run "${runCmd} \"\$@\""
} else {
  set-alias {|module_name|}-run "${runCmd}"
}

# Inspect runscript or deffile easily!
set-alias {|module_name|}-inspect-runscript "${inspectCmd} -r ${containerPath}"
set-alias {|module_name|}-inspect-deffile "${inspectCmd} -d ${containerPath}"


#=====
# Module options
#=====
module-whatis "    Name: {{ name }}"
module-whatis "    Version: {{ version }}"
{% if description %}module-whatis "    Description: ${description}"{% endif %}
{% if url %}module-whatis "    Url: {{ url }}"{% endif %}
{% if labels %}{% for key, value in labels.items() %}module-whatis "    {{ key }}: {{ value }}"
{% endfor %}{% endif %}
{% if settings.singularity_module %}module load {{ settings.singularity_module }}{% endif %}
