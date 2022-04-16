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

## [0.0.x](https://github.com/singularityhub/singularity-hpc/tree/main) (0.0.x)
 - support for views create, delete, edit, install, uninstall (0.0.54)
  - also including cleanup of module in views on uninstall
  - ability to set custom config variable on the fly with -c
 - add support for shpc update so container can be updated without binoc (0.0.53)
 - better error message if container tag does not exist on update (0.0.52)
 - minimum version of spython required is 0.2.0 to support apptainer (0.0.51)
 - add support for TCL and LMOD default version, multiple variants (0.0.50)
 - refactor to "add" to generate a container.yaml first (0.0.49)
 - Properly cleanup empty module directories, and asking to remove a container that doesn't exist now logs a _warning_ (0.0.48)
 - wrapper script generation permissions error (0.0.47)
 - fixing but with stream command repeating output (0.0.46)
 - Adding support for wrapper scripts for global and container.yaml (0.0.45)
 - Lua and tcl module file bug fixes for shell functions and aliases (0.0.44)
  - restoring -B for Singularity bindpaths over using envar
 - default containers directory should be separate from modules (0.0.43)
 - remove redundancy of manual bindpaths and SINGULARITY_BINDPATH (0.0.42)
 - Do not unset container environment vars if they are already set (0.0.41)
 - Central config should be read first (and updated with user config) (0.0.4)
 - Add support for oras pull for singularity (0.0.39)
 - Bug with setting a nested value (0.0.38)
 - Adding quotes around tcl descriptions (0.0.37)
 - fixing bug with container install (does not honor module directory) (0.0.36)
 - `.version` file should be written in top level of module folders [#450](https://github.com/singularityhub/singularity-hpc/issues/450) (0.0.35)
  - tcl module functions need `$@` to handle additional arguments
 - Tcl modules use shell functions for bash, to export to child shells (0.0.34)
   - fixed missing singularity -B flag for custom home feature
   - fixed singularity.tcl to always replace $ with \$ for custom home feature
   - fixed missing features.home occurrence in docker.tcl
 - New features for X11 and custom home (0.0.33)
 - Adding singularity and docker specific options (0.0.32)
   - Adding more documentation on aliases
   - Bugfix to output error message if path does not exist for inspect
 - Fixing bug with using variables in recipe options (0.0.31)
 - Removing un-used defaults and lmod_base (0.0.30)
 - Allow environment variables in settings (0.0.29)
   - User settings file creation and use with shpc config inituser
   - registry is now a list to support multiple registry locations
   - config supports add/remove to append/delete from list
 - Add test for docker and podman (0.0.28)
   - namespace as format string for command named renamed to repository
   - shpc test/uninstall should be run for all tests
   - bug with uninstall
   - adding user and group ids to docker and podman commands
   - remove conflict with entire module name, should only be for aliases
   - fix documentation of commands in Lua module template
 - Cleanup of module files and docker requirement bugfix (0.0.27)
 - Docker support (0.0.26)
   - added an enable_tty setting to allow disabling add -t in recipes
   - enforced not adding extra settings to setting.yml
   - settings are validated when an update is attempted
 - Podman support (0.0.25)
   - container_tech is now a settings.yml variable
   - allow for custom test interpreter "test_shell"
   - adding config edit for interactive edit
   - adding show --filter to filter list of modules shown
   - split documentation into user and developer guide
   - added automated spell checking with crate-ci/typos
   - support for container features
   - shpc get -e to show path to an envrironment file
   - added support for env section to render to bound environment file
   - added support for container features like gpu
   - allowing for a `container:tag` convention to be used for commands.
   - list defaults to showing modules/tags one per line, unless --short used
 - adding namespaces to make module install, show, inspect easier (0.0.24)
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

