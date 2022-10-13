set view_dir "[file dirname [file dirname ${ModulesCurrentModulefile}] ]"
set view_name "[file tail ${view_dir}]"
set view_module ".view_module"
set view_modulefile "${view_dir}/${view_module}"

if {[file exists ${view_modulefile}]} {
    source ${view_modulefile}
}
