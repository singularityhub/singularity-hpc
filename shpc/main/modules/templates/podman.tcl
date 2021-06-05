#%Module 1.0

#=====
# Created by singularity-hpc (https://github.com/singularityhub/singularity-hpc)
# ##
# {{ name }} on {{ creation_date }}
#=====

proc ModulesHelp { } {

    puts stderr "This module is a podman container wrapper for {{ name }} v{{ version }}"
    {% if description %}puts stderr "{{ description }}"{% endif %}
    puts stderr ""
    puts stderr "Container:"
    puts stderr " - {{ image }}"
    puts stderr "Commands include:"
    puts stderr " - {|module_name|}-run:"
    puts stderr "       podman run -it --rm {% if envfile %}--env-file  {{ module_dir }}/{{ envfile }}{% endif %} {% if bindpaths %}-v {{ bindpaths }} {% endif %} -v . -w . <container>"
    puts stderr " - {|module_name|}-shell:"
    puts stderr "       podman run -it --rm --entrypoint {{ shell }}{% if envfile %} --env-file {{ module_dir }}/{{ envfile }}{% endif %} {% if bindpaths %}-v {{ bindpaths }} {% endif %} -v . -w . <container>"
    puts stderr " - {|module_name|}-exec:"
    puts stderr "       podman run -it --rm --entrypoint {{ shell }}{% if envfile %} --env-file  {{ module_dir }}/{{ envfile }}{% endif %} {% if bindpaths %}-v {{ bindpaths }} {% endif %} -v . -w . <container> $*"
    puts stderr " - {|module_name|}-inspect:"
    puts stderr "       podman inspect <container>"
{% if aliases %}{% for alias in aliases %}    puts stderr " - {{ alias.name }}:"
    puts stderr "       podman run -it --entrypoint {{ alias.entrypoint }} {% if envfile %}--envfile  {{ module_dir }}/{{ envfile }} {% endif %}{% if bindpaths %}-v {{ bindpaths }} {% endif %}{% if alias.options %}{{ alias.options }} {% endif %} -v . -w . <container> {{ alias.args }}"
{% endfor %}{% endif %}

    puts stderr "For each of the above, you can export:"
    puts stderr "        - PODMAN_OPTS: to define custom options for podman"
    puts stderr "        - PODMAN_COMMAND_OPTS: to define custom options for the command"

}

# Variables

set name        "{{ name }}"
set version     "{{ version }}"
set progdir     "{{ module_dir }}"
set description "$name - $version"
set containerPath "{{ image }}"
set workdir [pwd]
{% if description %}set notes       "{{ description }}"{% endif %}
{% if url %}set homepage    "{{ url }}"{% endif %}
set helpcommand "This module is a podman container wrapper for {{ name }} v{{ version }}. {% if description %}{{ description }}{% endif %}"
{% if labels %}{% for key, value in labels.items() %}set {{ key }} {{ value }}
{% endfor %}{% endif %}

# conflict with modules with the same name
conflict {{ name }}
{% if aliases %}{% for alias in aliases %}{% if alias.name != name %}conflict {{ alias.name }}{% endif %}
{% endfor %}{% endif %}

# interactive shell to any container, plus exec for aliases
set shellCmd "podman \${PODMAN_OPTS} run \${PODMAN_COMMAND_OPTS} --rm -it --entrypoint {{ shell }} {% if envfile %}--env-file {{ module_dir }}/{{ envfile }}{% endif %} {% if bindpaths %}-v {{ bindpaths }} {% endif %} -v $workdir -w $workdir ${containerPath}" 

# execCmd needs entrypoint to be the executor
set execCmd "podman \${PODMAN_OPTS} run -it \${PODMAN_COMMAND_OPTS} --rm {% if envfile %} --env-file {{ module_dir }}/{{ envfile }}{% endif %} {% if bindpaths %}-v {{ bindpaths }} -v $workdir -w $workdir {% endif %} "
set runCmd "podman \${PODMAN_OPTS} run -it \${PODMAN_COMMAND_OPTS} --rm {% if envfile %}--env-file  {{ module_dir }}/{{ envfile }}{% endif %} {% if bindpaths %}-v {{ bindpaths }} {% endif %} -v $workdir -w $workdir ${containerPath}"
set inspectCmd "podman \${PODMAN_OPTS} inspect ${containerPath}" 

# set_shell_function takes bashStr and cshStr
set-alias "{|module_name|}-shell" "${shellCmd}"

# exec functions to provide "alias" to module commands
{% if aliases %}{% for alias in aliases %}
set-alias "{{ alias.name }}" "${execCmd} {% if alias.options %} {{ alias.options }} {% endif %} --entrypoint {{ alias.entrypoint }} ${containerPath} {{ alias.command }} $*"
{% endfor %}{% endif %}

# A customizable exec function
set-alias "{|module_name|}-exec" "${execCmd} --entrypoint \"\" ${containerPath} $*"

# Always provide a container run
set-alias "{|module_name|}-run" "${runCmd} $*"

# Inspect runscript or deffile easily!
set-alias "{|module_name|}-inspect" "${inspectCmd} ${containerPath} $*"

#=====
# Module options
#=====
module-whatis "    Name: {{ name }}"
module-whatis "    Version: {{ version }}"
{% if description %}module-whatis "    Description: ${description}"{% endif %}
{% if url %}module-whatis "    Url: {{ url }}"{% endif %}
{% if labels %}{% for key, value in labels.items() %}module-whatis "    {{ key }}: {{ value }}"
{% endfor %}{% endif %}
{% if podman_module %}module load {{ podman_module }}{% endif %}
