#!{{ settings.wrapper_shell }}

{% if '/csh' in settings.wrapper_shell %}set {% endif %}script=`realpath $0`
{% if '/csh' in settings.wrapper_shell %}set {% endif %}wrapper_bin=`dirname $script`
{% if '/csh' in settings.wrapper_shell %}set {% endif %}moduleDir=`dirname $wrapper_bin`

{% block content %}{% endblock %}
