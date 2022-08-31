{% extends "bases/shell-script-base.sh" %}

{% block content %}singularity ${SINGULARITY_OPTS} shell ${SINGULARITY_COMMAND_OPTS} {% if features.gpu %}{{ features.gpu }} {% endif %}{% if features.home %}-B {{ features.home }} --home {{ features.home }} {% endif %}{% if features.x11 %}-B {{ features.x11 }} {% endif %}{% if settings.environment_file %}-B $moduleDir/{{ settings.environment_file }}:/.singularity.d/env/{{ settings.environment_file }}{% endif %} {% if settings.bindpaths %}-B {{ settings.bindpaths }}{% endif %} -s {{ settings.wrapper_shell }} {{ image }}
{% endblock %}
