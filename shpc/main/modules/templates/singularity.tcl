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
    puts stderr "       singularity run {% if features.gpu %}{{ features.gpu }} {% endif %}{% if features.home %}--home {{ features.home }} {% endif %}{% if features.x11 %}-B {{ features.x11 | replace("$", "\$") }} {% endif %}{% if envfile %}-B {{ module_dir }}/{{ envfile }}:/.singularity.d/env/{{ envfile }}{% endif %} {% if bindpaths %}-B {{ bindpaths }} {% endif %}<container>"
    puts stderr " - {|module_name|}-shell:"
    puts stderr "       singularity shell -s {{ singularity_shell }} {% if features.gpu %}{{ features.gpu }} {% endif %}{% if features.home %}--home {{ features.home }} {% endif %}{% if features.x11 %}-B {{ features.x11 | replace("$", "\$") }} {% endif %}{% if envfile %}-B {{ module_dir }}/{{ envfile }}:/.singularity.d/env/{{ envfile }}{% endif %} {% if bindpaths %}-B {{ bindpaths }} {% endif %}<container>"
    puts stderr " - {|module_name|}-exec:"
    puts stderr "       singularity exec {% if features.gpu %}{{ features.gpu }} {% endif %}{% if features.home %}--home {{ features.home }} {% endif %}{% if features.x11 %}-B {{ features.x11 | replace("$", "\$") }} {% endif %}{% if envfile %}-B {{ module_dir }}/{{ envfile }}:/.singularity.d/env/{{ envfile }}{% endif %} {% if bindpaths %}-B {{ bindpaths }} {% endif %}<container> $*"
    puts stderr " - {|module_name|}-inspect-runscript:"
    puts stderr "       singularity inspect -r <container>"
    puts stderr " - {|module_name|}-inspect-deffile:"
    puts stderr "       singularity inspect -d <container>"
    puts stderr ""    
{% if aliases %}{% for alias in aliases %}    puts stderr " - {{ alias.name }}:"
    puts stderr "       singularity exec {% if features.gpu %}{{ features.gpu }} {% endif %}{% if features.home %}--home {{ features.home }} {% endif %}{% if features.x11 %}-B {{ features.x11 | replace("$", "\$") }} {% endif %}{% if envfile %}-B {{ module_dir }}/{{ envfile }}:/.singularity.d/env/{{ envfile }}{% endif %} {% if bindpaths %}-B {{ bindpaths }} {% endif %}{% if alias.singularity_options %}{{ alias.singularity_options | replace("$", "\$") }} {% endif %}<container> {{ alias.command | replace("$", "\$") }}"
{% endfor %}{% else %}    puts stderr " - {|module_name|}: singularity run {% if features.gpu %}{{ features.gpu }} {% endif %}{% if features.home %}--home {{ features.home }} {% endif %}{% if features.x11 %}-B {{ features.x11 | replace("$", "\$") }} {% endif %}{% if envfile %}-B {{ module_dir }}/{{ envfile }}:/.singularity.d/env/{{ envfile }}{% endif %} {% if bindpaths %}-B {{ bindpaths }}{% endif %}<container>"{% endif %}
    puts stderr ""
    puts stderr "For each of the above, you can export:"
    puts stderr ""
    puts stderr " - SINGULARITY_OPTS: to define custom options for singularity (e.g., --debug)"
    puts stderr " - SINGULARITY_COMMAND_OPTS: to define custom options for the command (e.g., -b)"

}

# Environment
setenv SINGULARITY_OPTS ""
setenv SINGULARITY_COMMAND_OPTS ""

# Variables

set name        {{ name }}
set version     {{ version }}
set progdir     {{ module_dir }}
set description "$name - $version"
set containerPath {{ container_sif }}
{% if description %}set notes       "{{ description }}"{% endif %}
{% if url %}set homepage    "{{ url }}"{% endif %}
set helpcommand "This module is a singularity container wrapper for {{ name }} v{{ version }}. {% if description %}{{ description }}{% endif %}"
{% if labels %}{% for key, value in labels.items() %}set {{ key }} {{ value }}
{% endfor %}{% endif %}

# conflict with modules with the same alias name
conflict {{ name }}
{% if aliases %}{% for alias in aliases %}{% if alias != name %}conflict {{ alias.name }}{% endif %}
{% endfor %}{% endif %}

# singularity environment variables to bind the paths and set shell
{% if bindpaths %}setenv SINGULARITY_BINDPATH {{ bindpaths }}{% endif %}
setenv SINGULARITY_SHELL {{ singularity_shell }}

# interactive shell to any container, plus exec for aliases
set shellCmd "singularity \${SINGULARITY_OPTS} shell \${SINGULARITY_COMMAND_OPTS} -s {{ singularity_shell }} {% if features.gpu %}{{ features.gpu }} {% endif %}{% if features.home %}--home {{ features.home }} {% endif %}{% if features.x11 %}-B {{ features.x11 | replace("$", "\$") }} {% endif %}{% if envfile %}-B {{ module_dir }}/{{ envfile }}:/.singularity.d/env/{{ envfile }}{% endif %} {% if bindpaths %}-B {{ bindpaths }}{% endif %} ${containerPath}" 
set execCmd "singularity \${SINGULARITY_OPTS} exec \${SINGULARITY_COMMAND_OPTS} {% if features.gpu %}{{ features.gpu }} {% endif %}{% if features.home %}--home {{ features.home }} {% endif %}{% if features.x11 %}-B {{ features.x11 | replace("$", "\$") }} {% endif %}{% if envfile %}-B {{ module_dir }}/{{ envfile }}:/.singularity.d/env/{{ envfile }}{% endif %} {% if bindpaths %}-B {{ bindpaths }}{% endif %} "
set runCmd "singularity \${SINGULARITY_OPTS} run \${SINGULARITY_COMMAND_OPTS} {% if features.gpu %}{{ features.gpu }} {% endif %}{% if features.home %}--home {{ features.home }} {% endif %}{% if features.x11 %}-B {{ features.x11 | replace("$", "\$") }} {% endif %}{% if envfile %}-B {{ module_dir }}/{{ envfile }}:/.singularity.d/env/{{ envfile }}{% endif %} {% if bindpaths %}-B {{ bindpaths }}{% endif %} ${containerPath}"
set inspectCmd "singularity \${SINGULARITY_OPTS} inspect \${SINGULARITY_COMMAND_OPTS} " 

# set_shell_function takes bashStr and cshStr
set-alias {|module_name|}-shell "${shellCmd}"


# exec functions to provide "alias" to module commands
{% if aliases %}{% for alias in aliases %}
set-alias {{ alias.name }} "${execCmd} {% if alias.singularity_options %} {{ alias.singularity_options | replace("$", "\$") }} {% endif %} ${containerPath} {{ alias.command | replace("$", "\$") }}"
{% endfor %}{% endif %}

# A customizable exec function
set-alias {|module_name|}-exec "${execCmd} ${containerPath}"

# Always provide a container run
set-alias {|module_name|}-run "${runCmd}"

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
{% if singularity_module %}module load {{ singularity_module }}{% endif %}
