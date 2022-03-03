{% extends "bases/shell-script-base.sh" %}

{% block content %}singularity ${SINGULARITY_OPTS} exec ${SINGULARITY_COMMAND_OPTS} {% if features.gpu %}{{ features.gpu }} {% endif %}{% if features.home %}-B {{ features.home }} --home {{ features.home }} {% endif %}{% if features.x11 %}-B {{ features.x11 }} {% endif %}{% if settings.environment_file %}-B $moduleDir/{{ settings.environment_file }}:/.singularity.d/env/{{ settings.environment_file }}{% endif %} {% if settings.bindpaths %}-B {{ settings.bindpaths }}{% endif %} {% if alias.singularity_options %} {{ alias.singularity_options }} {% endif %} {{ image }} {{ alias.command }} {% if '/sh' in settings.wrapper_shell or '/bash' in settings.wrapper_shell %}"$@"{% elif '/csh' in settings.wrapper_shell %}$argv:q{% endif %}
{% endblock %}
