{% extends "bases/shell-script-base.sh" %}

{% block content %}singularity ${SINGULARITY_OPTS} inspect ${SINGULARITY_COMMAND_OPTS} -d {{ image }}{% endblock %}
