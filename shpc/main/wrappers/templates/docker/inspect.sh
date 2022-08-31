{% extends "bases/shell-script-base.sh" %}

{% block content %}singularity ${PODMAN_OPTS} inspect ${PODMAN_COMMAND_OPTS}  {{ image }}{% endblock %}
