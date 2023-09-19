.. _getting_started-user-guide:

==========
User Guide
==========

Singularity Registry HPC (shpc) will allow you to install Singularity containers as
modules. This means that you can install them as a cluster admin, or as a cluster user.
This getting started guide will walk you through setting up a local registry,
either for yourself or your user base. If you haven't read :ref:`getting_started-installation`
you should do that first.

Why shpc?
=========

Singularity Registry HPC is created to be modular, meaning that we support a distinct
set of container technologies and module systems. The name of the library "Singularity
Registry HPC" does not refer specifically to the container technology "Singularity,"
but more generally implies the same spirit -- a single entity that is "one library to rule them all!"


What is a registry?
===================

A registry consists of a database of local containers configuration files, ``container.yaml``
files organized in the root of the shpc install in one of the ``registry`` folders. The namespace
is organized by Docker unique resources identifiers. When you install an identifier
as we saw above, the container binaries and customized module files are added to
the ``module_dir`` defined in your settings, which defaults to ``modules`` in the
root of the install. You should see the :ref:`getting_started-developer-guide`
for more information about contributing containers to this registry.


Really Quick Start
==================

Once you have shpc installed, make sure you tell shpc what your module software is
(note that you only need to run this command if you aren't using Lmod, which is the
default).

.. code-block:: console

    $ shpc config set module_sys tcl
    $ shpc config set module_sys lmod  # default


You can then easily install, load, and use modules:

.. code-block:: console

    $ shpc install biocontainers/samtools
    $ module load biocontainers/samtools
    $ samtools

Or set a configuration value on the fly for any command:

.. code-block:: console

    $ shpc install -c set:views_base:/tmp/views biocontainers/samtools

The above assumes that you've installed the software, and have already
added the modules folder to be seen by your module software. If your module
software doesn't see the module, remember that you need to have done:

.. code-block:: console

    $ module use $(pwd)/modules


Also know that by default, we use a remote registry, `shpc-registry on GitHub <https://github.com/singularityhub/shpc-registry>`_ to find recipes for. If you want to use a local filesystem registry (a clone of that registry or your own custom) see the following sections, where we will walk through these steps in more detail.


Quick Start
===========

After  :ref:`getting_started-installation`, and let's say shpc is installed
at ``~/singularity-hpc`` you can edit your settings in ``settings.yaml``.
Importantly, make sure your shpc install is configured to use the right module
software, which is typically lmod or tcl. Here is how to change from the default
"lmod" to "tcl" and then back:

.. code-block:: console

    $ shpc config set module_sys tcl
    $ shpc config set module_sys lmod # this is the default, which we change back to!


Once you have the correct module software indicated, try installing a container:

.. code-block:: console

    $ shpc install python

Make sure that the local ./modules folder can be seen by your module software
(you can run this in a bash profile or manually, and note that if you want to
use Environment Modules, you need to add ``--module-sys tcl``).

.. code-block:: console

    $ module use ~/singularity-hpc/modules


And then load the module!

.. code-block:: console

    $ module load python/3.9.2-slim

If the module executable has a conflict with something already loaded, it
will tell you, and it's up to you to unload the conflicting modules before you
try loading again. If you want to quickly see commands that are supported, use module
help:

.. code-block:: console

    $ module help python/3.9.2-slim

If you want to add the modules folder to your modules path more permanently,
you can add it to ``MODULEPATH`` in your bash profile.

.. code-block:: console

    export MODULEPATH=$HOME/singularity-hpc/modules:$MODULEPATH


For more detailed tutorials, you should continue reading,
and see :ref:`getting_started-use-cases`. Also see the :ref:`getting_started-commands-config` for how to update configuration values with ``shpc config``.


Setup
=====

Setup includes, after installation, editing any configuration values to
customize your install. The configuration file will default to ``shpc/settings.yml``
in the installed module, however you can create your own user settings file to
take preference over this one as follows:

.. code-block:: console

    $ shpc config inituser


When you create a user settings file (or provide a custom settings file one off to
the client) the shpc default settings will be read first, and then updated by your file.
We do this so that if the default file updates and your user settings is missing a variable,
we still use the default. The defaults in either file are likely suitable for most. For any configuration value
that you might set, the following variables are available to you:

 - ``$install_dir``: the shpc folder
 - ``$root_dir``: the parent directory of shpc (where this README.md is located)


Additionally, the variables ``module_base``, ``container_base``, and ``registry``
can be set with environment variables that will be expanded at runtime. You cannot
use the protected set of substitution variables (``$install_dir`` and ``$root_dir``)
as environment variables, as they will be subbed in by shpc before environment
variable replacement. A summary table of variables is included below, and then further discussed in detail.


.. list-table:: Settings
   :widths: 25 65 10
   :header-rows: 1

   * - Name
     - Description
     - Default
   * - module_sys
     - Set a default module system. Currently lmod and tcl are supported
     - lmod
   * - registry
     - A list of full paths to one or more registry remotes (e.g., GitHub addresses) or local directories (each with subfolders with container.yaml recipes)
     - ["https://github.com/singularityhub/shpc-registry"]
   * - sync_registry
     - A default remote to sync from (is not required to have an API/docs, as it is cloned).
     - https://github.com/singularityhub/shpc-registry
   * - module_base
     - The install directory for modules
     - $root_dir/modules
   * - wrapper_base
     - The install directory for script wrappers
     - $root_dir/modules
   * - container_base
     - Where to install containers. If not defined, they are installed in "containers" in the install root
     - $root_dir/containers
   * - container_tech
     - The container technology to use (singularity or podman)
     - singularity
   * - views_base
     - The default root for creating custom views. Defaults to ``views`` in the root directory.
     - $root_dir/views
   * - default_view
     - Install to this default view (e.g., meaning you always create a second symlink tree of the same modules)
     - unset
   * - updated_at
     - a timestamp to keep track of when you last saved
     - never
   * - label_separator
     - When parsing labels, replace newlines with this string
     - ', '
   * - default_version
     - Should a default version be used?
     - module_sys
   * - singularity_module
     - if defined, add to module script to load this Singularity module first
     - null
   * - module_name
     - Format string for module commands exec,shell,run (not aliases) can include ``{{ registry }}``, ``{{ repository }}``, ``{{ tool }}`` and ``{{ version }}``
     - ``'{{ tool }}'``
   * - bindpaths
     - string with comma separated list of paths to binds. If set, expored to SINGULARITY_BINDPATH
     - null
   * - singularity_shell
     - exported to SINGULARITY_SHELL
     - /bin/sh
   * - podman_shell
     - The shell used for podman
     - /bin/sh
   * - docker_shell
     - The shell used for docker
     - /bin/sh
   * - test_shell
     - The shell used for the test.sh file
     - /bin/bash
   * - wrapper_shell
     - The shell used for wrapper scripts
     - /bin/bash
   * - wrapper_scripts:enabled
     - enable or disable generation of wrapper scripts, instead of module aliases
     - false
   * - wrapper_scripts:docker
     - The name of the generic wrapper script template for docker
     - docker.sh
   * - wrapper_scripts:podman
     - The name of the generic wrapper script template for podman
     - docker.sh
   * - wrapper_scripts:singularity
     - The name of the generic wrapper script template for singularity
     - singularity.sh
   * - namespace
     - Set a default module namespace that you want to install from.
     - null
   * - environment_file
     - The name of the environment file to generate and bind to the container.
     - 99-shpc.sh
   * - enable_tty
     - For container technologies that require -t for tty, enable (add) or disable (do not add)
     - true
   * - config_editor
     - The editor to use for your config editing
     - vim
   * - features
     - A key, value paired set of features to add to the container (see table below)
     - All features default to null


Note that any configuration value can be set permanently by using ``shpc config``
or manually editing the file, but you can also set config values "one off." As an example,
here is a "one off" command to install to a different shpc module root:

.. code-block:: console

    $ shpc install -c set:modules_base:/tmp/modules ghcr.io/autamus/clingo

These settings will be discussed in more detail in the following sections.

Features
--------

Features are key value pairs that you can set to a determined set of values
to influence how your module files are written. For example, if you set the
gpu feature to "nvidia" in your settings file:

.. code-block:: yaml

    container_features:
      gpu: "nvidia"


and a container.yaml recipe has a gpu:true container feature to say "this container
supports gpu":

.. code-block:: yaml

    features:
      gpu: true

Given that you are installing a module for a Singularity container, the ``--nv``
option will be added. Currently, the following features are supported:


.. list-table:: Title
   :widths: 10 40 25 25
   :header-rows: 1

   * - Name
     - Description
     - Default
     - Options
   * - gpu
     - If the container technology supports it, add flags to indicate using gpu.
     - null
     - nvidia, amd, null
   * - x11
     - Bind mount ~/.Xauthority or a custom path
     - null
     - true (uses default path ~/.Xauthority), false/null (do not enable) or a custom path to an x11 file
   * - home
     - Specify and bind mount a custom home path
     - null
     - custom path for the home, or false/null


Modules Folder
--------------

The first thing you want to do is configure your module location, if you want it different
from the default. The path can be absolute or relative to ``$install_dir`` (the shpc
directory) or ``$root_dir`` (one above that) in your
configuration file at ``shpc/settings.yml``. If you are happy
with module files being stored in a ``modules`` folder in the present working
directory, you don't need to do any configuration. Otherwise, you can customize
your install:

.. code-block:: console

    # an absolute path
    $ shpc config set module_base /opt/lmod/modules

    # or a path relative to a variable location remember to escape the "$"
    $ shpc config set module_base \$root_dir/modules


This directory will be the base where lua files are added, and containers are stored
in a directory alongside it. For example, if you were to add a container with unique
resource identifier `python/3.8` you would see:

.. code-block:: console

    $install_dir/modules/
    └── python
        └── 3.9.2
            └── module.lua

    $install_dir/containers/
    └── python
        └── 3.9.2
            └── python-3.9.2.sif

Singularity Registry HPC uses this simple directory structure to ensure
a unique namespace.


Wrapper Base
------------

By default, if you do not set a wrapper script base they will be stored alongside
modules. However, for large installations, we recommend you customize this path
to be somewhere else. This way, you can avoid warnings from your module software
about having too many files.

.. code-block:: console

    # an absolute path
    $ shpc config set wrapper_base /opt/lmod/wrappers


Container Images Folder
-----------------------

If you don't want your container images (sif files) to live in the root of shpc
in a directory called "containers," then you should define the ``container_base`` to be something
different. For example:

.. code-block:: console

    $ mkdir -p /tmp/containers
    $ shpc config set container_base /tmp/containers


The same hierarchy will be preserved as to not put all containers in the same
directory. It's strongly recommended to keep modules separate from containers
for faster loading (applies to container technologies like Singularity that
pull binary files directly).


Registry
--------

The registry parameter is a list of one or more registry locations (filesystem
directories or remote GitHub repositories with the same structure) where shpc will search
for ``container.yaml`` files. The default registry used to be shipped with shpc, but as of
version 0.1.0 is provided remotely. This means that by default, you don't need to worry about
updating or syncing recipes - they will always be retrieved from the latest, as the remote registry
`shpc-registry  <https://github.com/singularityhub/shpc-registry>`_ is automatically updated.
However, you have several options for managing your own (or updating) recipes.

1. Use the default remote, no additional work needed
2. Clone the default remote to a local filesystem folder and manage manually (e.g., git pull)
3. Create your own local registry in addition (or without) the remote.
4. For any local registry, you can sync (``shpc sync``) from a remote.

If you want to do the first, no further action is needed! Each of these remaining
examples will be described here, and for instructions for creating your own
registry, see :ref:`getting_started-developer-guide`.

1. Use the Default Remote
^^^^^^^^^^^^^^^^^^^^^^^^^

Congratulations, you are done! This is the default and you don't need to make
any changes.


2. Clone a Remote Registry
^^^^^^^^^^^^^^^^^^^^^^^^^^

It could be the case that you want to start with a remote registry, but keep it locally
with your own changes or secrets. This is essentially turning a remote registry into a filesystem
(local) one. The easiest thing to do here is to clone it to your filesyste, and then add to shpc as a filesystem
registry.

.. code-block:: console

    # Clone to a special spot
    $ git clone https://github.com/singularityhub/shpc-registry /opt/lmod/my-registry

    # change to your own registry of container yaml configs
    $ shpc config add registry:/opt/lmod/my-registry

Since add is adding to a list, you might want to open your settings.yaml and ensure that
the order is to your liking. The order determines the search path, and you might have
preferences about what is searched first.

3. Create A Local Registry
^^^^^^^^^^^^^^^^^^^^^^^^^^

This would correspond to the same set of steps as above, but starting from scratch!
For example:

.. code-block:: console

    $ mkdir -p /opt/lmod/my-registry
    $ cd /opt/lmod/my-registry


And then you might want to inspect :ref:`getting_started-commands-add` to see
how to use ``shpc add`` to generate new container.yaml files.
See :ref:`getting_started-creating-filesystem-registry` for instructions on how to
create a registry and :ref:`getting_started-developer-manual-registry-entries` to
populate the registry with new entries.
After that, you'll still want to
ensure your filesystem registry is known to shpc:

.. code-block:: console

    $ shpc config add registry:/opt/lmod/my-registry


4. Sync from a Remote
^^^^^^^^^^^^^^^^^^^^^

See :ref:`getting_started-commands-sync-registry:` for instructions
of how to sync from a remote. You'll want to ensure you have added a filesystem
registry to be known to shpc to sync to.

Want to design your own remote registry? See the :ref:`getting_started-developer-guide`.


Default Version
---------------

The default version setting is there to support you telling shpc how you want module versions to be selected.
There are four options:

 - ``null`` do not set any kind of default version, it will be manually controlled by the installer (``false`` also supported for backwards compatibility)
 - ``module_sys``: allow the module software to choose (``true`` also supported for backwards compatibility)
 - ``last_installed``: always set default version to the last version installed
 - ``first_installed``: only set default version for the first installed


Module Names
------------

The setting ``module_name`` is a format string in `Jinja2 <https://jinja.palletsprojects.com/en/3.0.x/>`_
that is used to generate your module command names. For each module, in addition
to aliases that are custom to the module, a set of commands for run, exec,
shell, inspect, and container are generated. These commands will use the ``module_name`` format string
to determine their names. For example, for a python container with the default ``module_name``
of "{{ tool }}" we will derive the following aliases for a Singularity module:

.. code-block:: console

    python-shell
    python-run
    python-exec
    python-inspect-deffile
    python-inspect-runscript
    python-container

A container identifier is parsed as follows:

.. code-block:: console

    # quay.io   /biocontainers/samtools:latest
    # <registry>/ <repository>/  <tool>:<version>


So by default, we use tool because it's likely closest to the command that is wanted.
But let's say you had two versions of samtools - the namespaces would conflict! You
would want to change your format string to ``{{ repository }}-{{ tool }}`` to be
perhaps "biocontainers-samtools-exec" and "another-samtools-exec."
If you change the format string to ``{{ tool }}-{{ version }}`` you would see:

.. code-block:: console

    python-3.9.5-alpine-shell
    python-3.9.5-alpine-run
    python-3.9.5-alpine-exec
    python-3.9.5-alpine-deffile
    python-3.9.5-alpine-runscript
    python-3.9.5-alpine-container


And of course you are free to add any string that you wish, e.g., ``plab-{{ tool }}``

.. code-block:: console

    plab-python-shell

These prefixes are currently only provided to the automatically generated
commands. Aliases that are custom to the container are not modified.


Module Software
---------------

The default module software is currently Lmod, and there is also support for environment
modules that only use tcl (tcl). If you
are interested in adding another module type, please `open an issue <https://github.com/singularityhub/singularity-hpc>`_ and
provide description and links to what you have in mind. You can either specify the
module software on the command line:


.. code-block:: console

    $ shpc install --module-sys tcl python


or you can set the global variable to what you want to use (it defaults to lmod):

.. code-block:: console

    $ shpc config set module_sys tcl


The command line argument, if provided, always over-rides the default.


Container Technology
--------------------

The default container technology to pull and then provide to users is Singularity,
and we have also recently added Podman and Docker, and will add support for Shifter and Sarus soon.
Akin to module software, you can specify the container technology to use on a global
setting, or via a one-off command:


.. code-block:: console

    $ shpc install --container-tech podman python


or for a global setting:

.. code-block:: console

    $ shpc config set container_tech podman


If you would like support for a different container technology that has not been
mentioned, please also `open an issue <https://github.com/singularityhub/singularity-hpc>`_ and
provide description and links to what you have in mind.

Wrapper Scripts
---------------

Singularity HPC allows for global definition of wrapper scripts, meaning that instead of writing a module alias to run a container for some given alias,
we generate a wrapper script of the same name instead. Since the settings.yml is global, all wrapper scripts defined here are specific to replacing aliases.
Container-specific scripts you'll want to include in the container.yaml are described in :ref:`getting_started-developer-guide`. Let's take a look at the settings:


.. code-block:: yaml

    wrapper_scripts:

      # Enable wrapper scripts, period. If enabled, generate scripts for aliases instead of commands
      # if enabled, we also allow container-specific wrapper scripts.
      enabled: false

      # use for docker aliases
      docker: docker.sh

      # use for podman aliases
      podman: docker.sh

      # use for singularity aliases
      singularity: singularity.sh

Since these are nested values, to get the current value you can use a ``:`` to separate
the fields, e.g.,:

.. code-block:: console

    $ shpc config get wrapper_scripts:enabled
    wrapper_scripts:enabled        False

And if you want to change the default, just add another level:

.. code-block:: console

    $ shpc config set wrapper_scripts:enabled true
    Updated wrapper_scripts:enabled to be true

And don't forget you can manually update the file in an editor:

.. code-block:: console

    $ shpc config edit

Since different container technologies might expose different environment variables (e.g., ``SINGULARITY_OPTS`` vs ``PODMAN_OPTS``)
they are organized above based on the container technology. If you want to customize the wrapper script, simply replace the relative paths
above (e.g., ``singularity.sh``) with an absolute path to a file that will be used instead. For global alias scripts such as these,
Singularity HPC will look for:

1. An absolute path first, if found is used first.
2. Then a script name in the shpc/main/wrappers directory

Here is an example of using wrapper scripts for the "python" container, which doesn't have container specific wrappers. What you see
is the one entrypoint, `python`, being placed in a "bin" subdirectory that the module will see instead of defining the alias.


.. code-block:: console

    modules/python/
    └── 3.9.10
        ├── 99-shpc.sh
        ├── bin
        │   └── python
        └── module.lua

For container specific scripts, you can add sections to a ``container.yaml`` to specify the script (and container type)
and the scripts must be provided alongside the container.yaml to install.

.. code-block:: yaml

    docker_scripts:
      fork: docker_fork.sh
    singularity_scripts:
      fork: singularity_fork.sh

The above says "given generation of a docker or podman container, write a script named "fork" that uses "docker_fork.sh" as a template"
and the same for Singularity. And then I (the developer) would provide the custom scripts alongside container.yaml:

.. code-block:: console

    registry/vanessa/salad/
    ├── container.yaml
    ├── docker_fork.sh
    └── singularity_fork.sh

And here is what those scripts look like installed. Since we are installing for just one container technology, we are seeing the alias wrapper for salad as "salad" and the container-specific wrapper for fork as "fork."


.. code-block:: console

    modules/vanessa/salad/
    └── latest
        ├── 99-shpc.sh
        ├── bin
        │   ├── fork
        │   └── salad
        └── module.lua


We currently don't have a global argument to enable alias wrappers but not container wrappers. If you see a need for this please let us know.

Where are wrapper scripts stored?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Since we don't allow overlap
of the name of an alias wrapper script (e.g., ``bin/python`` as a wrapper to a python entrypoint) from a custom container wrapper script (e.g., a wrapper script with name "python" under a container.yaml) we can keep them both in the modules directory. If you see a need to put them elsewhere please let us know.

.. _getting_started-commands:
.. _getting_started-commands-views:

Views
=====

A view is a custom splicing of a set of installed modules that are intended to be used together, or loaded
with other system modules. The concept is similar to a database in that you can only include in the view
what you have in your shpc install, and the views themselves are done via symlinks to not redundantly store
containers. If you want to generate a separate, non-symlink view, the suggested approach is to simply
use a different shpc install.

Views Base
----------

By default, your modules are installed to your ``module_base`` described in settings with a complete
namespace, meaning the full name of the container registry from where they arise. We do this so that the namespace
is consistent and there are no conflicts. However, for views we use a simplified tree to install from,
meaning the module full names are _just_ the final container name. As an example, ``ghcr.io/autamus/clingo`` in
a view would simply install to ``clingo``.

Views are installed to the ``views_base`` in your settings, which defaults to
``$root_dir/views``. To create a new named view:


Creating a New View
-------------------

To create a new view, you just need to provide a name to ``shpc view create``:

.. code-block:: console

    $ shpc view create mpi
    View mpi was created in /home/vanessa/Desktop/Code/shpc/views/mpi

The above would be an example to create a new named "mpi," perhaps for a specific kind of mpi
container to be installed there. Since it will be under the same directory, you'll be able to use
this custom set of modules together. You can also create a view from an existing view.yaml file,
perhaps one of your own existint views or one that has been shared with you!


.. code-block:: console

    $ shpc view create second-mpi views/mpi/view.yaml
    Creating link $module_base/ghcr.io/autamus/clingo/5.5.1/module.lua -> $views_base/second-mpi/clingo/5.5.1.lua
    Module ghcr.io/autamus/emacs:27.2 was created.
    Creating link $module_base/ghcr.io/autamus/emacs/27.2/module.lua -> $views_base/second-mpi/emacs/27.2.lua


Loading a View
--------------

When you are ready to use your view, the "get" command returns the path:

.. code-block:: console

    $ shpc view get mpi
    /home/vanessa/Desktop/Code/shpc/views/mpi

So you will be able to load as follows:

.. code-block:: console

    $ module use $(shpc view get mpi)


Installing Modules to a View
----------------------------

Installing a module means generating a symlink for a module to your view, and with a
shortened name. We do this assuming that views are always smaller versions of the entire
module tree, and that we want them to be easier to interact with (e.g., shorter names).
To make interactions as easy as possible, if you install a module to your view that does
not exist in the main shpc tree, it will be installed there first and linked. When you
ask to install a module, always refer to the full name:

.. code-block:: console

    # install to the mpi view the module "ghcr.io/autamus/clingo"
    $ shpc view install mpi ghcr.io/autamus/clingo
    Module ghcr.io/autamus/clingo:5.5.1 was created.
    Creating link $module_base/ghcr.io/autamus/clingo/5.5.1/module.lua -> $views_base/mpi/clingo/5.5.1.lua


This will create symlinks to your previously installed modules in the view:

.. code-block:: console

    $ tree views
    views/
    └── mpi
        ├── clingo
        │   └── 5.5.1.lua -> /home/vanessa/Desktop/Code/shpc/modules/ghcr.io/autamus/clingo/5.5.1/module.lua
        └── view.yaml

Since we are linking the same file, the same containers will be shared.

Always Install to a View
------------------------

If you always want to install to an (existing) named view, simply set the ``default_view`` to a name:

.. code-block:: console

    $ shpc config set default_view mpi

You should obviously create the view first or you'll get an error message that it does not exist!
When you have a default view set, any install that you do will install to the module base and also your view.

.. code-block:: console

    $ shpc install ghcr.io/autamus/emacs
    ...
    Module ghcr.io/autamus/emacs:27.2 was created.
    Creating link $module_base/ghcr.io/autamus/emacs/27.2/module.lua -> $views_base/mpi/emacs/27.2.lua

And we can confirm it was created!

.. code-block:: console

    $ tree views/mpi
    views/mpi/
    ├── clingo
    │   └── 5.5.1.lua -> /home/vanessa/Desktop/Code/shpc/modules/ghcr.io/autamus/clingo/5.5.1/module.lua
    ├── emacs
    │   └── 27.2.lua -> /home/vanessa/Desktop/Code/shpc/modules/ghcr.io/autamus/emacs/27.2/module.lua
    └── view.yaml

The above can be useful for a permanent view you want to install everything to, or if you want to enable a view
for a short period of time to install to it. If you want to disable this, then just do:

.. code-block:: console

    $ shpc config set default_view null

And note you can also ask to install to a view "one off":

.. code-block:: console

    $ shpc install --view mpi ghcr.io/autamus/emacs


List Views
----------

If you want to list the views, just do:

.. code-block:: console

    $ shpc view list
                   mpi
            second-mpi

In the example above you have two views, mpi and second-mpi, and each
has it's own tree in views:

.. code-block:: console

    views/
    ├── mpi
    |   ...
    │   └── view.yaml
    └── second-mpi
        ...
        └── view.yaml


List Modules Installed to a View
--------------------------------

Listing modules installed to a view looks like the following:

.. code-block:: console

    $ shpc view list mpi
        ghcr.io/autamus/emacs:27.2

This is read directly from the view.yaml file.

Edit a View
-----------

While this isn't yet going to be useful (since we don't have additional modules to load)
you can technically edit a view as follows:

.. code-block:: console

    $ shpc view edit mpi

This might be just an easy way to view it for the time being!

Add System Modules to a View
----------------------------

Views have support for customization, such as a system module that you always want loaded.
We do this by way of an extra view_module that is generated in the root of the view (and
always attempted to be loaded) by the installed modules. For example, let's say that when
we load a view module named mpi, we always want to load a system module named "openmpi" and "mymod." We could do:

.. code-block:: console

    $ shpc view add <view> system_modules <name1> <name2>
    $ shpc view add mpi system_modules openmpi mymod
    Wrote updated .view_module: /home/vanessa/Desktop/Code/shpc/views/mpi/.view_module

The add command always requires a named view attribute (e.g.,``system_modules`` is a list) and
then one or more values to add to it. This will write the view module to your view,
and the module file symlinked should always attempt to try loading it. Note that if you are using
modules version `earlier than 4.8 <https://github.com/cea-hpc/modules/issues/392>`_ the ``try-load``
command is not available so you will not have support for view customizations.

Remove System Modules from A View
---------------------------------

Of course an "add" command would not be complete without a "remove" command! To remove modules:

.. code-block:: console

    $ shpc view remove mpi system_modules mymod
    Wrote updated .view_module: /home/vanessa/Desktop/Code/shpc/views/mpi/.view_module


Note that if you edit the files manually, you would need to edit the view.yaml AND the hidden
.view_module that is always updated from it.


Add and Remove Depends On Modules to a View
-------------------------------------------

You can add (or remove) a ``depends_on`` clause to a view, just like with system modules.
The syntax is the same, however you specify a different key to add to:

.. code-block:: console

    $ shpc view add <view> depends_on <name1> <name2>
    $ shpc view add mpi depends_on openmpi
    $ shpc view remove mpi depends_on openmpi

When you add a ``depends_on`` or ``system_modules`` to a view, what we are doing under
the hood is adding a ``.view_module`` that will be loaded with the view, and it includes these
extra parameters.

.. code-block:: console

    views/
    └── mpi
      ├── python
      ├── view.yaml
      ├── .view_module
      └── 3.11-rc.lua -> /home/vanessa/Desktop/Code/shpc/modules/python/3.11-rc/module.lua

Here are example contents of ``.view_module`` (this will vary depending on your module software):

.. code-block:: tcl

    module load("myextraprogram")
    depends_on("openmpi")


If you want any extra features added to this custom file (e.g., to support loading in a view)
please open an issue for discussion.


Delete a View
-------------

If you want to nuke a view, just ask for it to be deleted.

.. code-block:: console

    $ shpc view delete mpi


By default you'll be asked for a confirmation. To force deletion:

.. code-block:: console

     $ shpc view delete mpi --force


Uninstall from a View
---------------------

Uninstalling from a view is simply removing the symbolic link for a module, and it does
not influence your module tree. You can uninstall either a specific symlinked version:

.. code-block:: console

     $ shpc view uninstall mpi ghcr.io/autamus/emacs:27.2

Or the entire tree of symlinks (e.g., all versions of emacs that are symlinked):

.. code-block:: console

     $ shpc view uninstall mpi ghcr.io/autamus/emacs


If you look in the view.yaml, it will be updated with what you install or uninstall. We do this
so you can share the file with a collaborator and then can regenerate the view, discussed next.


Using a View
-------------

You can easily use a view as follows:

.. code-block:: console

    $ module use $(shpc view get mpi)
    $ module load clingo/5.5.1


This is much more efficient compared to the install that uses the full paths:

.. code-block:: console

    $ module use ./modules
    $ module load ghcr.io/autamus/clingo/5.5.1/module


Since we install based on the container name *and* version tag, this even gives you
the ability to install versions from different container bases in the same root.
If there is a conflict, you will be given the option to exit (and abort) or continue.


.. warning::

    Be cautious about creating symlinks in containers or other contexts where a bind
    could eliminate the symlink or make the path non-existent.


Commands
========

The following commands are available! For any command, the default module system
is lmod, and you can change this to tcl by way of adding the ``--module-sys`` argument
after your command of interest.

.. code-block:: console

    $ shpc <command> --module-sys tcl <args>


.. _getting_started-commands-config:


Config
------

If you want to edit a configuration value, you can either edit the ``shpc/settings.yml``
file directly, or you can use ``shpc config``, which will accept:

 - set to set a parameter and value
 - get to get a parameter by name
 - add to add a value to a parameter that is a list (e.g., registry)
 - remove to remove a value from a parameter that is a list

The following example shows changing the default module_base path from the install directory modules folder.

.. code-block:: console

    # an absolute path
    $ shpc config set module_base /opt/lmod/modules

    # or a path relative to the install directory, remember to escape the "$"
    $ shpc config set module_base \$install_dir/modules


And then to get values:

.. code-block:: console

    $ shpc config get module_base


And to add and remove a value to a list:

.. code-block:: console

    $ shpc config add registry /tmp/registry
    $ shpc config remove registry /tmp/registry


You can also open the config in the editor defined in settings at ``config_editor``

.. code-block:: console

    $ shpc config edit


which will first look at the environment variables ``$EDITOR`` and ``$VISUAL`` and will
fall back to the ``config_editor`` in your user settings (vim by default).

.. _getting_started-commands-show:

Show
----

The most basic thing you might want to do is install an already existing
recipe in the registry. You might first want to show the known registry entries
first. To show all entries, you can run:

.. code-block:: console

    $ shpc show
    tensorflow/tensorflow
    python
    singularityhub/singularity-deploy

The default will not show versions available. To flatten out this list and include versions for each, you can do:

.. code-block:: console

    $ shpc show --versions
    tensorflow/tensorflow:2.2.2
    python:3.9.2-slim
    python:3.9.2-alpine
    singularityhub/singularity-deploy:salad


To filter down the result set, use ``--filter``:


.. code-block:: console

    $ shpc show --filter bio
    biocontainers/bcftools
    biocontainers/vcftools
    biocontainers/bedtools
    biocontainers/tpp

Set a limit of results with `--limit`:

.. code-block:: console

    $ shpc show --filter bio --limit 5


To get details about a package, you would then add it's name to show:

.. code-block:: console

    $ shpc show python

Finally, to show recipes in a local filesystem registry (that may not be added to your
shpc config) you can specify the path with ``--registry``. All of the above should work
except with this argument, e.g.,:

.. code-block:: console

    $ shpc show --registry .

.. _getting_started-commands-install:


Install
-------


And then you can install a version that you like (or don't specify to default to
the latest, which in this case is 3.9.2-slim). You will see the container pulled,
and then a message to indicate that the module was created.


.. code-block:: console

    $ shpc install python
    ...
    Module python/3.9.2 is created.


.. code-block:: console

    $ tree modules/
    modules/
    └── python
        └── 3.9.2
            └── module.lua

    $ tree containers/
    containers/
    └── python
        └── 3.9.2
            └── python-3.9.2.sif


You can also install a specific tag (as shown in list).

.. code-block:: console

    $ shpc install python:3.9.2-alpine


Note that Lmod is the default for the module system, and Singularity for
the container technology.
If you don't have any module software on your system, you can now test interacting
with the module via the :ref:`getting_started-development` instructions.

.. _getting_started-commands-install-private:


Install Private Images
----------------------

What about private containers on Docker Hub? If you have a private image, you can
simply use `Singularity remote login <https://github.com/sylabs/singularity-userdocs/blob/master/singularity_and_docker.rst#singularity-cli-remote-command>`_ before attempting the install and everything should work.

.. _getting_started-commands-install-local:


Install Local Image
-------------------

The concept of installing a local image means that you are selecting a container.yaml recipe from an existing registry,
however instead of pulling it, you are pairing it was a particular URI of a local image. As an example, let's say we have pulled a local
samtools container:

.. code-block:: console

    $ singularity pull docker://quay.io/biocontainers/samtools:1.10--h2e538c0_3

We might then want to install it to the samtools namespace and using the same metadata (e.g., aliases, environment, etc.):

.. code-block:: console

    $ shpc install quay.io/biocontainers/samtools:1.10--h2e538c0_3 samtools_1.2--0.sif

This is similar to an ``shpc add``, however instead of needing to write a container.yaml in a local
filesystem, you are using an existing one. The use case or assumption here is that you have a local
directory of containers that can be matched to existing shpc recipes. Finally to request using the
container path "as is" without copying anything into your container folder, add ``--keep-path``:


.. code-block:: console
    $ shpc install quay.io/biocontainers/samtools:1.10--h2e538c0_3 samtools_1.2--0.sif --keep-path

This feature is supported for shpc versions 0.1.15 and up.


.. _getting_started-commands-namespace:


Namespace
---------

Let's say that you are exclusively using continers in the namespace ghcr.io/autamus.

.. code-block:: console

    registry/ghcr.io/
    └── autamus
        ├── abi-dumper
        ├── abyss
        ├── accumulo
        ├── addrwatch
        ...
        ├── xrootd
        ├── xz
        └── zlib


It can become arduous to type the entire namespace every time! For this purpose,
you can set a namespace:

.. code-block:: console

    $ shpc namespace use ghcr.io/autamus

And then instead of asking to install clingo as follows:

.. code-block:: console

    $ shpc install ghcr.io/autamus/clingo


You can simply ask for:


.. code-block:: console

    $ shpc install clingo


And when you are done, unset the namespace.


.. code-block:: console

    $ shpc namespace unset


Note that you can also set the namespace as any other setting:

.. code-block:: console

    $ shpc config set namespace ghcr.io/autamus

Namespaces currently work with:

 - install
 - uninstall
 - show
 - add
 - remove
 - check


.. _getting_started-commands-list:

List
----

Once a module is installed, you can use list to show installed modules (and versions).
The default list will flatten out module names and tags into a single list
to make it easy to copy paste:

.. code-block:: console

    $ shpc list
        biocontainers/samtools:v1.9-4-deb_cv1
                        python:3.9.2-alpine
                        python:3.9.5-alpine
                        python:3.9.2-slim
                      dinosaur:fork
                 vanessa/salad:latest
                         salad:latest
      ghcr.io/autamus/prodigal:latest
      ghcr.io/autamus/samtools:latest
        ghcr.io/autamus/clingo:5.5.0


However, if you want a shorter version that shows multiple tags alongside
each unique module name, just add ``--short``:

.. code-block:: console

    $ shpc list --short

        biocontainers/samtools: v1.9-4-deb_cv1
                        python: 3.9.5-alpine, 3.9.2-alpine, 3.9.2-slim
                      dinosaur: fork
                 vanessa/salad: latest
                         salad: latest
      ghcr.io/autamus/prodigal: latest
      ghcr.io/autamus/samtools: latest
        ghcr.io/autamus/clingo: 5.5.0


.. _getting_started-commands-update:

Update
------

As of version 0.0.52, you can request on demand updates of container.yaml recipes,
where an update means we ping the registry or resource for the module and find
updated tags. An update generally means that:

 - We start with the 50 latest tags of the container, as determined by `crane.ggcr.dev <https://crane.ggcr.dev/ls/quay.io/biocontainers/samtools>`_
 - We filter according to any recipe ``filters`` in the container.yaml
 - Given a convention of including a hash, we try to remove it and generate a loose version
 - Any versions (including latest) that cannot be sorted based on some semblance to a version are filtered out
 - We sort the list, and given duplicates of some major minor (ignoring the last part of): ``<major>.<minor>.<ignored>`` we take the first seen in the sorted list.
 - Then we take the top 5 newest to add.
 - We then filter down to not include any versions older than the current oldest in the container.yaml

This action is run automatically on CI for you, however it's just done once a month and you are welcome to run it on your own, and contribute
changes to container.yaml files that you think are meaningful. To update one container
module recipe in the registry:

.. code-block:: console

    $ shpc update quay.io/biocontainers/samtools
    Looking for updated digests for quay.io/biocontainers/samtools
    >> quay.io/biocontainers/samtools
    >> Latest
    1.15--h3843a85_0:sha256:d68e1b5f504dc60eb9f2a02eecbac44a63f144e7d455b3fb1a25323c667ca4c4
    >> Tags
    + 1.9--h8571acd_11:sha256:3883c91317e7b6b62e31c82e2cef3cc1f3a9862633a13f850a944e828dd165ec
    + 1.8--h46bd0b3_5:sha256:e495550231927c4b9b23a9f5920906f608129bf470dc3409ef7c6eecf0fa6d8e
    + 1.7--2:sha256:9b3e923c44aa401e3e2b3bff825d36c9b07e97ba855ca04a368bf7b32f28aa97
    + 1.6--he673b24_3:sha256:42031f060cde796279c09e6328d72bbce70d83a8f96e161faee3380ab689246d
    + 1.5--2:sha256:9a2f99c26cee798e3b799447a7cfa0fbb0c1ce27c42eef7a3c1289ba871f55cb
    1.12--h9aed4be_1:sha256:5fd5f0937adf8a24b5bf7655110e501df78ae51588547c8617f17c3291a723e1
    1.15--h3843a85_0:sha256:d68e1b5f504dc60eb9f2a02eecbac44a63f144e7d455b3fb1a25323c667ca4c4
    1.10--h2e538c0_3:sha256:84a8d0c0acec87448a47cefa60c4f4a545887239fcd7984a58b48e7a6ac86390
    1.14--hb421002_0:sha256:88632c41eba8b94b7a2a1013f422aecf478a0cb278740bcc3a38058c903d61ad
    1.13--h8c37831_0:sha256:04da5297386dfae2458a93613a8c60216d158ee7cb9f96188dad71c1952f7f72
    1.11--h6270b1f_0:sha256:141120f19f849b79e05ae2fac981383988445c373b8b5db7f3dd221179af382b


or to ask for a dry run, meaning we check for updates but don't perform them.

.. code-block:: console

    $ shpc update quay.io/biocontainers/samtools --dry-run


If you want to look for a specific string or pattern in the tags, just add ``--filter``

.. code-block:: console

    $ shpc update redis --dry-run --filter alpine

Since no tags are deleted, this will add the latest set found with the term "alpine." You can also use this
strategy to add a specific tag:


.. code-block:: console

    $ shpc update redis --dry-run --filter 6.0-rc-alpine

The current implementation just supports updating from a Docker / oras registry (others can come after if requested).
As of version 0.0.58, there is support to ask to update all recipes - just leave out the name!

.. code-block:: console

    $ shpc update

If you are using an earlier release than 0.0.58 you can accomplish the same as follows:

.. code-block:: console

    $ for name in $(shpc show); do
        shpc update ${name} --dry-run
      done


Let us know if there are other features you'd like for update! For specific recipes
it could be that a different method of choosing or sorting tags (beyond the defaults mentioned above
and filter) is needed.

.. _getting_started-commands-sync-registry:


Sync Registry
-------------

A sync is when we take your local filesystem registry, and retrieve updates from the remote defined at
``sync_registry`` in your settings.yaml. Since sync will be writing recipes to the filesystem
it only works if you target a filesystem registry (meaning that the default registry
as a remote will not work).

.. note::

   By default, the first filesystem registry found in your settings under the registry list will
   be used. To provide a one off registry folder (that should exist but does not need to be in your
   defined list) you can use ``--registry``.

As an example, if we do this without changing the defaults:

.. code-block:: console

    $ shpc sync-registry
    This command is only supported for a filesystem registry! Add one or use --registry.

We can then make a dummy directory to support sync. You could also make this directory and add to your settings proper under ``registry``.

.. code-block:: console

    $ mkdir -p ./registry
    $ shpc sync-registry --registry ./registry

Will compare your main registry folder against the main branch and only add new recipes
that you do not have. To ask to update from a specific reference (tag or branch):

.. code-block:: console

    $ shpc sync-registry --registry ./registry --tag 0.0.58

You can also ask to add just a specific container:

.. code-block:: console

    $ shpc sync-registry --registry ./registry quay.io/not-local/container

You can also ask to add new containers and completely update container.yaml files.

.. code-block:: console

    $ shpc sync-registry --registry ./registry --all

This means we do a side by side comparison of your filesystem registry and the upstream, and we add new
recipes folders that you don't have, and we replace any upstream files into recipes that you do have.
Be careful with this option, as if you've made changes to a container.yaml or associated
file in the upstream they will be lost. For this reason, we always recommend that you do a dry run first:

.. code-block:: console

    $ shpc sync-registry --registry ./registry --dry-run

Finally, if you have a more complex configuration that you want to automate, you can provide a
yaml file with your specifications:


.. code-block:: yaml

    sync_registry:
      "/tmp/github-shpc": "https://github.com/singularityhub/shpc-registry"
      "/tmp/gitlab-shpc": "https://gitlab.com/singularityhub/shpc-registry"


The above says to sync each respective local filesystem registry (key) with the remote (value).
And then do:


.. code-block:: console

    $ shpc sync-registry --config-file registries.yaml

.. _getting_started-commands-inspect:

Inspect
-------

Once you install a module, you might want to inspect the associated container! You
can do that as follows:

.. code-block:: console

    $ shpc inspect python:3.9.2-slim
    👉️ ENVIRONMENT 👈️
    /.singularity.d/env/10-docker2singularity.sh : #!/bin/sh
    export PATH="/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
    export LANG="${LANG:-"C.UTF-8"}"
    export GPG_KEY="${GPG_KEY:-"E3FF2839C048B25C084DEBE9B26995E310250568"}"
    export PYTHON_VERSION="${PYTHON_VERSION:-"3.9.2"}"
    export PYTHON_PIP_VERSION="${PYTHON_PIP_VERSION:-"21.0.1"}"
    export PYTHON_GET_PIP_URL="${PYTHON_GET_PIP_URL:-"https://github.com/pypa/get-pip/raw/b60e2320d9e8d02348525bd74e871e466afdf77c/get-pip.py"}"
    export PYTHON_GET_PIP_SHA256="${PYTHON_GET_PIP_SHA256:-"c3b81e5d06371e135fb3156dc7d8fd6270735088428c4a9a5ec1f342e2024565"}"
    /.singularity.d/env/90-environment.sh : #!/bin/sh
    # Custom environment shell code should follow

    👉️ LABELS 👈️
    org.label-schema.build-arch : amd64
    org.label-schema.build-date : Sunday_4_April_2021_20:51:45_MDT
    org.label-schema.schema-version : 1.0
    org.label-schema.usage.singularity.deffile.bootstrap : docker
    org.label-schema.usage.singularity.deffile.from : python@sha256:85ed629e6ff79d0bf796339ea188c863048e9aedbf7f946171266671ee5c04ef
    org.label-schema.usage.singularity.version : 3.6.0-rc.4+501-g42a030f8f

    👉️ DEFFILE 👈️
    bootstrap: docker
    from: python@sha256:85ed629e6ff79d0bf796339ea188c863048e9aedbf7f946171266671ee5c04ef


We currently don't show the runscript, as they can be very large. However, if you want
to see it:

    $ shpc inspect --runscript python:3.9.2-slim


Or to get the entire metadata entry dumped as json to the terminal:

.. code-block:: console

    $ shpc inspect --json python:3.9.2-slim


.. _getting_started-commands-test:


Test
----

Singularity HPC makes it easy to test the full flow of installing and interacting
with modules. This functionality requires a module system (e.g., Lmod) to be installed,
and the assumption is that the test is being run in a shell environment where any
supporting modules (e.g., loading Singularity or Podman) would be found if needed.
This is done by way of extending the exported ``$MODULEPATH``. To run a test, you
can do:

.. code-block:: console

    $ shpc test python


If you don't have it, you can run tests in the provided docker container.

.. code-block:: console

    docker build -t singularity-hpc .
    docker run --rm -it singularity-hpc shpc test python


Note that the ``Dockerfile.tcl`` builds an equivalent container with tcl modules.

.. code-block:: console

    $ docker build -f Dockerfile.tcl -t singularity-hpc .


If you want to stage a module install (e.g., install to a temporary directory and not remove it) do:


.. code-block:: console

    shpc test --stage python


To do this with Docker you would do:

.. code-block:: console

    $ docker run --rm -it singularity-hpc bash
    [root@1dfd9fe90443 code]# shpc test --stage python
    ...
    /tmp/shpc-test.fr1ehcrg


And then the last line printed is the directory where the stage exists,
which is normally cleaned up. You can also choose to skip testing the module
(e.g., lmod):


.. code-block:: console

    shpc test --skip-module python


Along with testing the container itself (the commands are defined in the ``tests``
section of a ``container.yaml``.


.. code-block:: console

    shpc test --skip-module --commands python

.. _getting_started-commands-uninstall:

Uninstall
---------

To uninstall a module, since we are targeting a module folder, instead of
providing a container unique resource identifier like `python:3.9.2-alpine`,
we provide the module path relative to your module directory. E.g.,

.. code-block:: console

    $ shpc uninstall python:3.9.2-alpine


You can also uninstall an entire family  of modules:

.. code-block:: console

    $ shpc uninstall python

The uninstall will go up to the top level module folder but not remove it
in the case that you've added it to your ``MODULEPATH``. As of version 0.1.18,
you can also ask to uninstall all:


.. code-block:: console

    $ shpc uninstall --all --force



.. _getting_started-commands-pull:

Pull
----

Singularity Registry HPC tries to support researchers that cannot afford to
pay for a special Singularity registry, and perhaps don't want to pull
from a Docker URI. For this purpose, you can use the `Singularity Deploy <https://github.com/singularityhub/singularity-deploy>`_
template to create containers as releases associated with the same GitHub
repository, and then pull them down directly with the shpc client with
the ``gh://`` unique resource identifier as follows:

.. code-block:: console

    $ shpc pull gh://singularityhub/singularity-deploy/0.0.1:latest
    $ shpc pull gh://singularityhub/singularity-deploy/0.0.1:salad
    $ shpc pull gh://singularityhub/singularity-deploy/0.0.1:pokemon


In the example above, our repository is called ``singularityhub/singularity-deploy``,
and in the root we have three recipes:

 - Singularity (builds to latest)
 - Singularity.salad
 - Singularity.pokemon

And in the ``VERSION`` file in the root, we have ``0.0.1`` which corresponds with
the GitHub release. This will pull to a container.  For example:

.. code-block:: console

    $ shpc pull gh://singularityhub/singularity-deploy/0.0.1:latest
    singularity pull --name /home/vanessa/Desktop/Code/singularity-hpc/singularityhub-singularity-deploy.latest.sif https://github.com/singularityhub/singularity-deploy/releases/download/0.0.1/singularityhub-singularity-deploy.latest.sif
    /home/vanessa/Desktop/Code/singularity-hpc/singularityhub-singularity-deploy.latest.sif

And then you are ready to go!

.. code-block:: console

    $ singularity shell singularityhub-singularity-deploy.latest.sif
    Singularity>


See the `Singularity Deploy <https://github.com/singularityhub/singularity-deploy>`_ repository
for complete details for how to set up your container! Note that this uri (``gh://``)
can also be used in a registry entry.

.. _getting_started-commands-shell:

Shell
-----

If you want a quick way to shell into an installed module's container
(perhaps to look around or debug without the module software being available) you can use
``shell``. For example:

.. code-block:: console

    $ shpc shell vanessa/salad:latest
    Singularity> /code/salad fork

     My life purpose: I cut butter.

                       ________  .====
                      [________>< :===
                                 '====



If you want to interact with the shpc Python client directly, you can
do shell without a module identifier. This will give you a python terminal,
which defaults to ipython, and then python and
bypython (per what is available on your system). To start a shell:

.. code-block:: console

    $ shpc shell


or with a specific interpreter:

.. code-block:: console

    $ shpc shell -i python


And then you can interact with the client, which will be loaded.

.. code-block:: python

    client
    [shpc-client]

    client.list()
    python

    client.install('python')

.. _getting_started-commands-show:


Show
----

As shown above, show is a general command to show the metadata file for a registry entry:

.. code-block:: console

    $ shpc show python
    docker: python
    latest:
      3.9.2-slim: sha256:85ed629e6ff79d0bf796339ea188c863048e9aedbf7f946171266671ee5c04ef
    tags:
      3.9.2-slim: sha256:85ed629e6ff79d0bf796339ea188c863048e9aedbf7f946171266671ee5c04ef
      3.9.2-alpine: sha256:23e717dcd01e31caa4a8c6a6f2d5a222210f63085d87a903e024dd92cb9312fd
    filter:
    - 3.9.*
    maintainer: '@vsoch'
    url: https://hub.docker.com/_/python
    aliases:
      python: /usr/local/bin/python

Or without any arguments, it will show a list of all registry entries available:

.. code-block:: console

    $ shpc show
    python

.. _getting_started-commands-check:


Check
-----

How do you know if there is a newer version of a package to install? In
the future, if you pull updates from the main repository, we will have a bot
running that updates container versions (digests) as well as tags. Here
is how to check if a module (the tag) is up to date.

.. code-block:: console

    $ shpc check tensorflow/tensorflow
    ⭐️ latest tag 2.2.2 is up to date. ⭐️


And if you want to check a specific digest for tag (e.g., if you use "latest" it
is subject to change!)

.. code-block:: console

    $ shpc check tensorflow/tensorflow:2.2.2
    ⭐️ tag 2.2.2 is up to date. ⭐️

As a trick, you can loop through registry entries with ``shpc list``. The return
value will be 0 is there are no updates, and 1 otherwise. This is how
we check for new recipes to test.

.. code-block:: console

    $ for name in $(shpc list); do
        shpc check $name
     done
    ⭐️ tag 3.1.1 is up to date. ⭐️
    ⭐️ tag 3.9.10 is up to date. ⭐️
    ⭐️ tag latest is up to date. ⭐️
    ⭐️ tag 1.14 is up to date. ⭐️
    ⭐️ tag 5.5.1 is up to date. ⭐️
    ⭐️ tag 1.54.0 is up to date. ⭐️



.. _getting_started-commands-add:

Add
---

It might be the case that you have a container locally, and you want to
make it available as a module (without pulling it from a registry). You might also
have a container on Docker Hub that you want to contribute to the registry!
shpc does support the "add" command to perform both of these functions.
The steps for adding a container are:

1. Running ``shpc add`` to create a container.yaml in the registry namespace
2. Customizing the container.yaml to your liking
3. Running ``shpc install`` to formally install your new container.

In the case of a docker image that is public (that you can share) you are encouraged
to contribute your recipe directly to shpc for others to use, and once in the repository
tags will also get updated automatically.

.. warning::

    The add command only works for a local filesystem registry. This means it will
    not work with the default settings that retrieve recipes from a remote registry!
    To use add and create your own filesystem folder, you can use ``--registry`` with
    a newly created directory (that you can then add to your settings.yaml registry
    list).


Creating a Local Registry
^^^^^^^^^^^^^^^^^^^^^^^^^

For any of the commands below you can create a local registry very easily - it's just a directory!

.. code-block:: console

    $ mkdir -p registry

And then use it via a one off command to add, e.g.,:

.. code-block:: console

    $ shpc add --registry ./registry docker://vanessa/pokemon


Add a Local Container
^^^^^^^^^^^^^^^^^^^^^

As an example, let's start with the container ``salad_latest.sif``. We have it
on our local machine and cannot pull it from a registry. First, let's run ``shpc add``
and tell shpc that we want it under the ``dinosaur/salad`` namespace.

.. code-block:: console

    $ shpc add salad_latest.sif dinosaur/salad:latest
    Registry entry dinosaur/salad:latest was added! Before shpc install, edit:
    /home/vanessa/Desktop/Code/shpc/registry/dinosaur/salad/container.yaml

At this point, you should open up the container.yaml generated and edit to your liking.
This usually means updating the description, maintainer, aliases, and possibly providing a url
to find more information or support. Also notice we've provided the tag to be latest. If you update this registry
entry in the future with a new version, you'll want to provide a new tag. If you provide
an existing tag, you'll be asked to confirm before continuing. When you are happy,
it's time to install it, just as you would a regular container!

.. code-block:: console

    $ shpc install dinosaur/salad:latest


And this will generate the expected module and container in your respective directory bases:


.. code-block:: console

    $ tree modules/dinosaur/salad/
    modules/dinosaur/salad/
    └── latest
        ├── 99-shpc.sh
        └── module.lua

    1 directory, 2 files

    $ tree containers/dinosaur/salad/
    containers/dinosaur/salad/
    └── latest
        └── sha256:77c7326e74d0e8b46d4e50d99e848fc950ed047babd60203e17449f5df8f39d4.sif

    1 directory, 1 file


Add a Registry Container
^^^^^^^^^^^^^^^^^^^^^^^^

Let's say we want to generate a container.yaml recipe for a container on Docker Hub.
Let's say we want to add `vanessa/pokemon <https://hub.docker.com/r/vanessa/pokemon>`_.
First, let's run ``shpc add``. Note that we provide the ``docker://`` unique resource
identifier to tell shpc it's from a Docker (OCI) registry.

.. code-block:: console

    $ shpc add docker://vanessa/pokemon
    Registry entry vanessa/pokemon:latest was added! Before shpc install, edit:
    /home/vanessa/Desktop/Code/shpc/registry/vanessa/pokemon/container.yaml


And that's it! The container module will use the same namespace, ``vanessa/pokemon`` as the Docker image,
and we do this purposefully as a design decision. Note that ``add`` previously would add the container directly to the module
directory, and as of version 0.0.49 it's been updated to generate the container.yaml first.

.. _getting_started-commands-remove:

Remove
------

As of version ``0.1.17`` you can easily remove a container.yaml entry too!
This remove command takes a pattern, and not providing one will remove all entries
from the registry (useful if you want to create a new one but preserve the automation).
Here is how to remove a specific namespace of container yamls:

.. code-block:: console

    $ shpc remove quay.io/biocontainers
    Searching for container.yaml matching quay.io/biocontainers to remove...
    Are you sure you want to remove 8367 container.yaml recipes? (yes/no)?


To remove all modules:

.. code-block:: console

    $ shpc remove
    Searching for container yaml to remove...
    Are you sure you want to remove 264 container.yaml recipes? (yes/no)? yes
    Removal complete!

This command can be useful if you want to start with a populated registry
as a template for your own registry.

Get
---

If you want to quickly get the path to a container binary, you can use get.

.. code-block:: console

    $ shpc get vanessa/salad:latest
    /home/vanessa/Desktop/Code/singularity-hpc/containers/vanessa/salad/latest/vanessa-salad-latest-sha256:8794086402ff9ff9f16c6facb93213bf0b01f1e61adf26fa394b78587be5e5a8.sif

    $ shpc get tensorflow/tensorflow:2.2.2
    /home/vanessa/Desktop/Code/singularity-hpc/containers/tensorflow/tensorflow/2.2.2/tensorflow-tensorflow-2.2.2-sha256:e2cde2bb70055511521d995cba58a28561089dfc443895fd5c66e65bbf33bfc0.sif

If you select a higher level module directory or there is no sif, you'll see:

.. code-block:: console

    $ shpc get tensorflow/tensorflow
    tensorflow/tensorflow is not a module tag folder, or does not have a sif binary.


You can add ``-e`` to get the environment file:


.. code-block:: console

    $ shpc get -e tensorflow/tensorflow


We could update this command to allow for listing all sif files within a top level
module folder (for different versions). Please open an issue if this would be useful for
you.
