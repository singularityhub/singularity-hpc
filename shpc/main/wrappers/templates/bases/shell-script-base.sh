#!{{ settings.wrapper_shell }}

script=`realpath $0`
wrapper_bin=`dirname $script`
{% if '/csh' in settings.wrapper_shell %}set moduleDir=`dirname $wrapper_bin`{% else %}export moduleDir=$(dirname $wrapper_bin){% endif %}

{% block content %}{% endblock %}
