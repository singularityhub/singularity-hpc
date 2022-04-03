{% if not settings.default_version %}if (mode() == "load") then
  if ( myModuleUsrName() ~= myModuleFullName() and myModuleUsrName() ~= string.gsub(myModuleFullName(),"/module$","") ) then
    LmodError("You must specify module <name>/<version>.")
  end
end{% endif %}
