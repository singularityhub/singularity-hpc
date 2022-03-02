{% extends "bases/shell-script-base.sh" %}

# See shpc/main/wrappers/snippets for what is added via this extend

# This is an example of a custom wrapper script for a docker container
# Note that we are showing an example of all the default args provided to the script!
# You don't need to use any of this syntax

{% block content %}{{ container.command }} ${PODMAN_OPTS} run ${PODMAN_COMMAND_OPTS} -i{% if settings.enable_tty %}t{% endif %} -u `id -u`:`id -g` --rm {% if settings.environment_file %}--env-file $moduleDir/{{ settings.environment_file }}{% endif %} {% if settings.bindpaths %}-v {{ settings.bindpaths }} {% endif %}{% if features.home %}-v {{ features.home }} {% endif %} -v ${PWD} -w ${PWD} --entrypoint /code/salad {{ image }} fork {% if '/sh' in settings.wrapper_shell or '/bash' in settings.wrapper_shell %}"$@"{% elif '/csh' in settings.wrapper_shell %}$argv:q{% endif %}{% endblock %}
