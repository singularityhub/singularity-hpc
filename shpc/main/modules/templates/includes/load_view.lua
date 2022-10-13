local view_dir = string.gsub(myFileName():match("(.*[/])") or ".","/%a*/$","")
local view_name = string.gsub(view_dir,".*/","")
local view_module = '.view_module'
local view_modulefile = view_dir .. '/' .. view_module .. '.lua'

if isFile(view_modulefile) then
  load(view_module)
end
