#!{{ wrapper_shell }}

{{ command }} ${PODMAN_OPTS} run ${PODMAN_COMMAND_OPTS} -i{% if tty %}t{% endif %} -u `id -u`:`id -g` --rm {% if envfile %}--env-file {{ module_dir }}/{{ envfile }}{% endif %} {% if bindpaths %}-v {{ bindpaths }} {% endif %}{% if features.home %}-v {{ features.home }} {% endif %} -v ${PWD} -w ${PWD} {% if alias.docker_options %} {{ alias.docker_options }} {% endif %} --entrypoint {{ alias.entrypoint }} {{ image }} {{ alias.args }} {% if '/sh' in wrapper_shell or '/bash' in wrapper_shell %}"$@"{% elif '/csh' in wrapper_shell %}$argv:q{% endif %}
