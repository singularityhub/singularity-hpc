#%Module

#=====
# View for singularity-hpc (https://github.com/singularityhub/singularity-hpc)
#=====

{% if system_modules %}module load {% for module in system_modules %}{{ module }} {% endfor %}{% endif %}
{% if depends_on %}depends-on {% for depend in depends_on %}{{ depend }} {% endfor %}{% endif %}
