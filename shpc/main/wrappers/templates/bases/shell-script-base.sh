#!{{ settings.wrapper_shell }}

{% if '/csh' in settings.wrapper_shell %}set {% endif %}script=`realpath $0`
{% if '/csh' in settings.wrapper_shell %}set {% endif %}wrapperDir=`dirname $script`/..

{% block content %}{% endblock %}
