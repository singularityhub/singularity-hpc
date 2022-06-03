{% if not settings.default_version %}if (mode() == "load") then
  if ( myModuleUsrName() ~= myModuleFullName() and myModuleUsrName() ~= string.gsub(myModuleFullName(),"/module$","") ) then
    LmodError("Default modules are disabled by your systems administrator. You must specify `module load <name>/<version>`.")
  end
end{% endif %}
