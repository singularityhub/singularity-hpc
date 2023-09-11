#!{{ settings.wrapper_shell }}

{% if '/csh' in settings.wrapper_shell %}set {% endif %}script=`realpath $0`
{% if '/csh' in settings.wrapper_shell %}set {% endif %}wrapperDir={% if settings.wrapper_base %}"{{ wrapper_dir }}"{% else %}`dirname $script`{% endif %}
{% if '/csh' in settings.wrapper_shell %}set {% endif %}moduleDir=`dirname $wrapperDir`

{% block content %}{% endblock %}
