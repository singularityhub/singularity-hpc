#%Module 1.0

#=====
# Created by singularity-hpc (https://github.com/singularityhub/singularity-hpc)
# ##
# {{ name }} on {{ creation_date }}
# TODO: finish this template, figure out commands
# create a shared base for TCL and LMOD
#=====

proc ModulesHelp { } {

    puts stderr "Container:"
    puts stderr " - {{ container_sif }}"
    puts stderr "Commands include:"
    puts stderr " - {{ prefix }}{{ flatname }}-run:"
    puts stderr "       singularity run {% if bindpaths %}-B {{ bindpaths }} {% endif %}<container>"
    puts stderr " - {{ prefix }}{{ flatname }}-shell:"
    puts stderr "       singularity shell -s {{ singularity_shell }} {% if bindpaths %}-B {{ bindpaths }} {% endif %}<container>"
    puts stderr " - {{ prefix }}{{ flatname }}-exec:"
    puts stderr "       singularity exec -s {{ singularity_shell }} {% if bindpaths %}-B {{ bindpaths }} {% endif %}<container> \"$@\""
    puts stderr " - {{ prefix }}{{ flatname }}-inspect-runscript:"
    puts stderr "       singularity inspect -r <container>"
    puts stderr " - {{ prefix }}{{ flatname }}-inspect-deffile:"
    puts stderr "       singularity inspect -d <container>"

{% if aliases %}{% for alias in aliases %}    puts stderr " - {{ alias.name }}:"
    puts stderr "       singularity exec {% if bindpaths %}-B {{ bindpaths }} {% endif %}{% if alias.options %}{{ alias.options }} {% endif %}<container> {{ alias.command }}"
{% endfor %}{% else %}    puts stderr " - {{ prefix }}{{ flatname }}: singularity run {% if bindpaths %}-B {{ bindpaths }}{% endif %}<container>"{% endif %}

    puts stderr "For each of the above, you can export:"

    puts stderr " - SINGULARITY_OPTS: to define custom options for singularity (e.g., --debug)"
    puts stderr " - SINGULARITY_COMMAND_OPTS: to define custom options for the command (e.g., -b)"

}

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

# conflict with modules with the same name
conflict {{ name }}
{% if aliases %}{% for alias in aliases %}conflict {{ alias.name }}
{% endfor %}{% endif %}

# singularity environment variables to bind the paths and set shell
{% if bindpaths %}setenv SINGULARITY_BINDPATH {{ bindpaths }}{% endif %}
setenv SINGULARITY_SHELL {{ singularity_shell }}

# interactive shell to any container, plus exec for aliases
set shellCmd "singularity \${SINGULARITY_OPTS} shell \${SINGULARITY_COMMAND_OPTS} -s {{ singularity_shell }} {% if bindpaths %}-B {{ bindpaths }}{% endif %} ${containerPath}" 
set execCmd "singularity \${SINGULARITY_OPTS} exec \${SINGULARITY_COMMAND_OPTS} {% if bindpaths %}-B {{ bindpaths }}{% endif %} "
set runCmd "singularity \${SINGULARITY_OPTS} run \${SINGULARITY_COMMAND_OPTS} {% if bindpaths %}-B {{ bindpaths }}{% endif %} ${containerPath} \${SINGULARITY_COMMAND_ARGS}"
set inspectCmd "singularity \${SINGULARITY_OPTS} inspect \${SINGULARITY_COMMAND_OPTS} " 

# set_shell_function takes bashStr and cshStr
set-alias "{{ prefix }}{{ flatname }}-shell" "${shellCmd} $*"


# exec functions to provide "alias" to module commands
{% if aliases %}{% for alias in aliases %}
set-alias "{{ alias.name }}" "${execCmd} {% if alias.options %} {{ alias.options }} {% endif %} ${containerPath} {{ alias.command }} $*"
{% endfor %}{% endif %}

# A customizable exec function
set-alias "{{ prefix }}{{ flatname }}-exec" "${execCmd} ${containerPath} \${SINGULARITY_COMMAND_ARGS}  $*"

# Always provide a container run
set-alias "{{ prefix }}{{ flatname }}-run" "${runCmd} $*"

# Inspect runscript or deffile easily!
set-alias "{{ prefix }}{{ flatname }}-inspect-runscript" "${inspectCmd} -r ${containerPath} $*"
set-alias "{{ prefix }}{{ flatname }}-inspect-deffile" "${inspectCmd} -d ${containerPath} $*"

#=====
# Module options
#=====
{% if description %}module-whatis   ${description}{% endif %}
{% if singularity_module %}module load {{ singularity_module }}{% endif %}
