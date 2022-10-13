-- Lmod Module
-- Module for View created by singularity-hpc (https://github.com/singularityhub/singularity-hpc)
--

{% for module in system_modules %}
load("{{ module }}"){% endfor %}{% for depends in depends_on %}
depends_on("{{ depends }}"){% endfor %}
