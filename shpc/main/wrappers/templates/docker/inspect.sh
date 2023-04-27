{% extends "bases/shell-script-base.sh" %}

{% block content %}{{ container.command }} ${PODMAN_OPTS} inspect ${PODMAN_COMMAND_OPTS}  {{ image }}{% endblock %}
