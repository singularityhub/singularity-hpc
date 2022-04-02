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

    $ shpc config set module_sys:tcl
    $ shpc config set module_sys:lmod  # default


You can then easily install, load, and use modules:

.. code-block:: console

    $ shpc install biocontainers/samtools
    $ module load biocontainers/samtools
    $ samtools

Or set a configuration value on the fly for any command:

.. code-block:: console

    $ shpc install -c set:symlink_base:/tmp/modules biocontainers/samtools

The above assumes that you've installed the software, and have already
added the modules folder to be seen by your module software. If your module
software doesn't see the module, remember that you need to have done:

.. code-block:: console

    $ module use $(pwd)/modules


We walk through these steps in more detail in the next section.


Quick Start
===========

After  :ref:`getting_started-installation`, and let's say shpc is installed 
at ``~/singularity-hpc`` you can edit your settings in ``settings.yaml``.
Importantly, make sure your shpc install is configured to use the right module
software, which is typicall lmod or tcl. Here is how to change from the default 
"lmod" to "tcl" and then back:

.. code-block:: console

    $ shpc config set module_sys:tcl
    $ shpc config set module_sys:lmod # this is the default, which we change back to!


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


.. list-table:: Title
   :widths: 25 65 10
   :header-rows: 1

   * - Name
     - Description
     - Default
   * - module_sys
     - Set a default module system. Currently lmod and tcl are supported
     - lmod
   * - registry
     - A list of full paths to one or more registry folders (with subfolders with container.yaml recipes)
     - [$root_dir/registry]
   * - module_base
     - The install directory for modules
     - $root_dir/modules
   * - container_base
     - Where to install containers. If not defined, they are installed in "containers" in the install root
     - $root_dir/containers
   * - container_tech
     - The container technology to use (singularity or podman)
     - singularity
   * - symlink_base
     - If set, where you want to install a simplified module tree to using ``--symlink-tree``
     - $root_dir/symlinks
   * - symlink_tree
     - If set to true, ALWAYS generate a symlink tree given that a symlink base is defined regardless of ``--symlink-tree`` flag
     - false
   * - updated_at
     - a timestamp to keep track of when you last saved
     - never
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
or manually editing the file, but you can also set config values "one off" as follows:

.. code-block:: console

    $ shpc install -c set:symlink_base:/tmp/modules ghcr.io/autamus/clingo


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
    $ shpc config set module_base:/opt/lmod/modules

    # or a path relative to a variable location remember to escape the "$"
    $ shpc config set module_base:\$root_dir/modules


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


Container Images Folder
-----------------------

If you don't want your container images (sif files) to live in the root of shpc
in a directory called "containers," then you should define the ``container_base`` to be something
different. For example:

.. code-block:: console

    $ mkdir -p /tmp/containers
    $ shpc config set container_base:/tmp/containers


The same hierarchy will be preserved as to not put all containers in the same
directory. It's strongly recommended to keep modules separate from containers
for faster loading (applies to container technologies like Singularity that
pull binary files directly).


Registry
--------

The registry parameter is a list of one or more registry locations (filesystem
directories) where shpc will search for ``container.yaml`` files. The default
registry shipped with shpc is the folder in the root of the repository, but 
you can add or remove entries via the config variable ``registry``


.. code-block:: console

    # change to your own registry of container yaml configs
    $ shpc config add registry:/opt/lmod/registry


# Note that "add" is used for lists of things (e.g., the registry config variable is a list)
and "set" is used to set a key value pair.

Symlink Base
------------

By default, your modules are installed to your ``module_base`` described above with a complete
namespace, meaning the container registry from where they arise. We do this so that the namespace
is consistent and there are no conflicts. However, if you want a simplified tree to install from,
meaning the module full names are _just_ the final container name, you can set the ``symlink_base``
in your settings to a different root. For example, let's say we want to install a set of modules.
We can use the default ``symlink_base`` of ``$root_dir/symlinks`` or set our own ``symlink_base``
in the settings.yaml. We could do:

.. code-block:: console

    $ shpc install ghcr.io/autamus/clingo --symlink-tree
    $ shpc install ghcr.io/autamus/samtools --symlink-tree

Then, for example, if you want to load the modules, you'll see the shorter names are
available!

.. code-block:: console

    $ module use ./symlinks
    $ module load clingo/5.5.1/module

This is much more efficient compared to the install that uses the full paths:

.. code-block:: console

    $ module use ./modules
    $ module load ghcr.io/autamus/clingo/5.5.1/module

Since we install based on the container name *and* version tag, this even gives you
the ability to install versions from different container bases in the same root.
If there is a conflict, you will be given the option to exit (and abort) or continue.
Finally, if you need an easy way to run through the containers you've already installed
to create the links:


.. code-block:: console

    for module in $(shpc list); do
        shpc install $module --symlink-tree
    done

And that will reinstall the modules you have installed, but in their symlink tree location.


.. warning::

    Be cautious about creating symlinks in containers or other contexts where a bind
    could eliminate the symlink or make the path non-existent.


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
to aliases that are custom to the module, a set of commands for run, inspect, exec,
and shell are generated. These commands will use the ``module_name`` format string
to determine their names. For example, for a python container with the default ``module_name``
of "{{ tool }}" we will derive the following aliases for a Singularity module:

.. code-block:: console

    python-shell
    python-run
    python-exec
    python-inspect-deffile
    python-inspect-runscript

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

    $ shpc config set module_sys:tcl


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

    $ shpc config set container_tech:podman


If you would like support for a different container technology that has not been
mentioned, please also `open an issue <https://github.com/singularityhub/singularity-hpc>`_ and
provide description and links to what you have in mind.

Wrapper Scripts
---------------

Singularity HPC allows for global definition of wrapper scripts, meaning that instead of writing a module alias to run a container for some given alias,
we generate a wrapper script of the same name instead. Since the settings.yml is global, all wrapper scripts defined here are specific to replacing aliases.
Container-specific scripts you'll want to include in the container.yaml are described in the developer docs. Let's take a look at the settings:


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
    $ shpc config set module_base:/opt/lmod/modules

    # or a path relative to the install directory, remember to escape the "$"
    $ shpc config set module_base:\$install_dir/modules


And then to get values:

.. code-block:: console

    $ shpc config get module_base


And to add and remove a value to a list:

.. code-block:: console

    $ shpc config add registry:/tmp/registry
    $ shpc config remove registry:/tmp/registry


You can also open the config in the editor defined in settings at ``config_editor``

.. code-block:: console

    $ shpc config edit
    

which defaults to vim.

Show and Install
----------------

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


To get details about a package, you would then add it's name to show:

.. code-block:: console

    $ shpc show python


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


Install Private Images
----------------------

What about private containers on Docker Hub? If you have a private image, you can
simply use `Singularity remote login <https://github.com/sylabs/singularity-userdocs/blob/master/singularity_and_docker.rst#singularity-cli-remote-command>`_ before attempting the install and everything should work.

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

    $ shpc config set namespace:ghcr.io/autamus

Namespaces currently work with:

 - install
 - uninstall
 - show
 - add
 - check

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

    shpc test python


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
in the case that you've added it to your ``MODULEPATH``.

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


Shell
-----

If you want a quick way to shell into an installed module's container
(perhaps to look around or debug without the module software being available) you can use
``shell``. For example:

.. code-block:: console

    shpc shell vanessa/salad:latest
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
Also note that ``add`` is only supported for Singularity, as Docker and Podman containers are 
typically provided via registries. If you are looking for support for add for another
container technology, please `open a new issue <https://github.com/singularityhub/singularity-hpc/issues>`_.


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
