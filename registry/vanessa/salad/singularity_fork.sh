{% extends "bases/shell-script-base.sh" %}

# See shpc/main/wrappers/snippets for what is added via this extend

# This is an example of a singularity wrapper script, under singularity_scripts
# Note that we are showing an example of all the default args provided to the script!
# You don't need to use any of this syntax

{% block content %}singularity ${SINGULARITY_OPTS} exec ${SINGULARITY_COMMAND_OPTS} {% if features.gpu %}{{ features.gpu }} {% endif %}{% if features.home %}-B {{ features.home }} --home {{ features.home }} {% endif %}{% if features.x11 %}-B {{ features.x11 }} {% endif %}{% if settings.environment_file %}-B $moduleDir/{{ settings.environment_file }}:/.singularity.d/env/{{ settings.environment_file }}{% endif %} {% if settings.bindpaths %}-B {{ settings.bindpaths }}{% endif %} {{ image }} /code/salad fork {% if '/sh' in settings.wrapper_shell or '/bash' in settings.wrapper_shell %}"$@"{% elif '/csh' in settings.wrapper_shell %}$argv:q{% endif %}{% endblock %}
