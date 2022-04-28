# https://github.com/cea-hpc/modules/issues/392
if {[info exists ModuleTool] && $ModuleTool eq {Modules}
    && [versioncmp $ModuleToolVersion 4.8] >= 0} {
    module try-load .view_module
}
