{% extends "bases/shell-script-base.sh" %}

{% block content %}{{ settings.singularity_path }} ${SINGULARITY_OPTS} inspect ${SINGULARITY_COMMAND_OPTS} -r {{ image }}{% endblock %}
