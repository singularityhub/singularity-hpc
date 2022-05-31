-- Lmod Module
-- Module for View created by singularity-hpc (https://github.com/singularityhub/singularity-hpc)
--

{% for module in system_modules %}
module load("{{ module }}"){% endfor %}

local view_dir = string.gsub(myFileName():match("(.*[/])") or ".","/%a*/$","")
local view_name = string.gsub(view_dir,".*/","")
local view_module = '.view_' .. view_name
local view_modulefile = view_dir .. '/' .. view_module .. '.lua'

if isFile(view_modulefile) then
  load(view_module)
end
