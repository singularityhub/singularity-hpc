#%Module

#=====
# Created by singularity-hpc (https://github.com/singularityhub/singularity-hpc)
# ##
# {{ name }} on {{ creation_date }}
#=====

proc ModulesHelp { } {

    puts stderr "This module is a {{ command }} container wrapper for {{ name }} v{{ version }}"
    {% if description %}puts stderr "{{ description }}"{% endif %}
    puts stderr ""
    puts stderr "Container:"
    puts stderr " - {{ image }}"
    puts stderr "Commands include:"
    puts stderr " - {|module_name|}-run:"
    puts stderr "       {{ command }} run -i{% if tty %}t{% endif %} --rm {% if envfile %}--env-file  {{ module_dir }}/{{ envfile }}{% endif %} {% if bindpaths %}-v {{ bindpaths }} {% endif %} -v . -w . <container>"
    puts stderr " - {|module_name|}-shell:"
    puts stderr "       {{ command }} run -i{% if tty %}t{% endif %} --rm --entrypoint {{ shell }}{% if envfile %} --env-file {{ module_dir }}/{{ envfile }}{% endif %} {% if bindpaths %}-v {{ bindpaths }} {% endif %} -v . -w . <container>"
    puts stderr " - {|module_name|}-exec:"
    puts stderr "       {{ command }} run -i{% if tty %}t{% endif %} --rm --entrypoint {{ shell }}{% if envfile %} --env-file  {{ module_dir }}/{{ envfile }}{% endif %} {% if bindpaths %}-v {{ bindpaths }} {% endif %} -v . -w . <container> $*"
    puts stderr " - {|module_name|}-inspect:"
    puts stderr "       {{ command }} inspect <container>"
{% if aliases %}{% for alias in aliases %}    puts stderr " - {{ alias.name }}:"
    puts stderr "       {{ command }} run -i{% if tty %}t{% endif %} --entrypoint {{ alias.entrypoint }} {% if envfile %}--envfile  {{ module_dir }}/{{ envfile }} {% endif %}{% if bindpaths %}-v {{ bindpaths }} {% endif %}{% if alias.options %}{{ alias.options }} {% endif %} -v . -w . <container> {{ alias.args }}"
{% endfor %}{% endif %}

    puts stderr "For each of the above, you can export:"
    puts stderr "        - DOCKER_OPTS: to define custom options for {{ command }}"
    puts stderr "        - DOCKER_COMMAND_OPTS: to define custom options for the command"

}

# Environment
setenv DOCKER_OPTS ""
setenv DOCKER_COMMAND_OPTS ""

# Variables

set name        "{{ name }}"
set version     "{{ version }}"
set progdir     "{{ module_dir }}"
set description "$name - $version"
set containerPath "{{ image }}"
set workdir [pwd]
{% if description %}set notes       "{{ description }}"{% endif %}
{% if url %}set homepage    "{{ url }}"{% endif %}
set helpcommand "This module is a {{ docker }} container wrapper for {{ name }} v{{ version }}. {% if description %}{{ description }}{% endif %}"
{% if labels %}{% for key, value in labels.items() %}set {{ key }} {{ value }}
{% endfor %}{% endif %}

# conflict with modules with the same name
conflict {{ name }}
{% if aliases %}{% for alias in aliases %}{% if alias.name != name %}conflict {{ alias.name }}{% endif %}
{% endfor %}{% endif %}

# interactive shell to any container, plus exec for aliases
set shellCmd "{{ command }} \${DOCKER_OPTS} run \${DOCKER_COMMAND_OPTS} --rm -i{% if tty %}t{% endif %} --entrypoint {{ shell }} {% if envfile %}--env-file {{ module_dir }}/{{ envfile }}{% endif %} {% if bindpaths %}-v {{ bindpaths }} {% endif %} -v $workdir -w $workdir ${containerPath}" 

# execCmd needs entrypoint to be the executor
set execCmd "{{ command }} \${DOCKER_OPTS} run -i{% if tty %}t{% endif %} \${DOCKER_COMMAND_OPTS} --rm {% if envfile %} --env-file {{ module_dir }}/{{ envfile }}{% endif %} {% if bindpaths %}-v {{ bindpaths }} -v $workdir -w $workdir {% endif %} "
set runCmd "{{ command }} \${DOCKER_OPTS} run -i{% if tty %}t{% endif %} \${DOCKER_COMMAND_OPTS} --rm {% if envfile %}--env-file  {{ module_dir }}/{{ envfile }}{% endif %} {% if bindpaths %}-v {{ bindpaths }} {% endif %} -v $workdir -w $workdir ${containerPath}"
set inspectCmd "{{ command }} \${DOCKER_OPTS} inspect ${containerPath}" 

# set_shell_function takes bashStr and cshStr
set-alias {|module_name|}-shell "${shellCmd}"

# exec functions to provide "alias" to module commands
{% if aliases %}{% for alias in aliases %}
set-alias {{ alias.name }} "${execCmd} {% if alias.options %} {{ alias.options }} {% endif %} --entrypoint {{ alias.entrypoint }} ${containerPath} {{ alias.command }}"
{% endfor %}{% endif %}

# A customizable exec function
set-alias {|module_name|}-exec "${execCmd} --entrypoint \"\" ${containerPath}"

# Always provide a container run
set-alias {|module_name|}-run "${runCmd}"

# Inspect runscript or deffile easily!
set-alias {|module_name|}-inspect "${inspectCmd} ${containerPath}"

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
