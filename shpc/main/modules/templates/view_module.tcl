#%Module

#=====
# View for singularity-hpc (https://github.com/singularityhub/singularity-hpc)
#=====

{% for module in system_modules %}
module load {{ module }}{% endfor %}
