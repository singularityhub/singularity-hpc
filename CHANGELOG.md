# CHANGELOG

This is a manually generated log to track changes to the repository for each release.
Each section should include general headers such as **Implemented enhancements**
and **Merged pull requests**. Critical items to know are:

 - renamed commands
 - deprecated / removed commands
 - changed defaults
 - backward incompatible changes (recipe file format? image file format?)
 - migration guidance (how to convert images?)
 - changed behaviour (recipe sections work differently)

The versions coincide with releases on pip. Only major versions will be released as tags on Github.

## [0.0.x](https://github.scom/singularityhub/singularity-hpc/tree/master) (0.0.x)
 - Podman support (0.0.24)
   - container_tech is now a settings.yml variable
   - allow for custom test interpreter "test_shell"
   - adding config edit for interactive edit
   - adding show --filter to filter list of modules shown
   - split documentation into user and developer guide
   - added automated spell checking with crate-ci/typos
   - support for container features
   - shpc get -e to show path to an envrironment file
   - adding namespaces to make module install, show, inspect easier
   - added support for env section to render to bound environment file
   - added support for container features like gpu
   - allowing for a `container:tag` convention to be used for commands.
   - list defaults to showing modules/tags one per line, unless --short used
 - container url does not render in docs (0.0.23)
 - addition of tcl modules, removal of un-needed database (0.0.22)
 - first update of all containers, and bugfix to pull (0.0.21)
 - allowing for a custom container base, container_base (0.0.2)
   - adding more nvidia containers, rapidsai and paraview
 - more packages and shell for a container (0.0.19)
 - adding description to docgen, and descriptions for all containers (0.0.18)
   - descriptions are now required
 - adding docgen command (0.0.17)
 - additional recipes and bug fix for uninstall (0.0.16)
 - updating testing to be with ubuntu (on native) (0.0.15)
 - start to addition of shpc test (0.0.14)
 - Bugfix and better documentation for show/pull/list (0.0.13)
 - Adding support for pull from a GitHub release! (0.0.11)
 - Initial creation of project (0.0.1)

