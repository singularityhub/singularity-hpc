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

    $ shpc config userinit


The defaults in either file are likely suitable for most. For any configuration value 
that you might set, the following variables are available to you:

 - ``$install_dir``: the shpc folder
 - ``$root_dir``: the parent directory of shpc (where this README.md is located)


Additionally, the variables ``module_base``, ``container_base``, and ``registry``
can be set with environment variables that will be expanded at runtime. You cannot
use the protected set of substitution variables (``$install_dir`` and ``$install_root``)
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
     - Where to install containers. If not defined, they are installed alongside modules.
     - null
   * - container_tech
     - The container technology to use (singularity or podman)
     - singularity
   * - updated_at
     - a timestamp to keep track of when you last saved
     - never
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


This directory will be the base where lua files are added, and container are stored.
For example, if you were to add a container with unique resource identifier `python/3.8`
you would see:

.. code-block:: console

    $install_dir/modules/
    └── python
        └── 3.9.2
            ├── module.lua
            └── python-3.9.2.sif

Although your module path might have multiple locations, Singularity Registry HPC 
assumes this one location to install container modules to in order to ensure
a unique namespace. 


Container Images Folder
-----------------------

If you don't want your container images (sif files) to live alongside your
module files, then you should define the ``container_base`` to be something
non-null (a path that exists). For example:

.. code-block:: console

    $ mkdir -p /tmp/containers
    $ shpc config set container_base:/tmp/containers


The same hierarchy will be preserved as to not put all containers in the same
directory.


Registry
--------

The registry parameter is a list of one or more registry locations (filesystem
directories) where shpc will search for ``container.yaml`` files. The default
registry shipped with shpc is the folder in the root of the repository, but 
you can add or remove entries via the config variable ``registry``


.. code-block:: console

    # change to your own registry of container yaml configs
    $ shpc config set registry:/opt/lmod/registry



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
            ├── module.lua
            └── python-3.9.2.sif

    2 directories, 2 files
    

You can also install a specific tag (as shown in list).
    
.. code-block:: console

    $ shpc install python:3.9.2-alpine
    

Note that Lmod is the default for the module system, and Singularity for
the container technology.
If you don't have any module software on your system, you can now test interacting
with the module via the :ref:`getting_started-development` instructions.


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

As a trick, you can loop through registry entries with ``shpc show``. The return
value will be 0 is there are no updates, and 1 otherwise. This is a trick
we use to check for new recipes to test.

.. code-block:: console



Add
---

It might be the case that you have a container locally, and you want to
make it available as a module (without pulling it from a registry). Although
this is discouraged because it means you will need to manually maintain
versions, shpc does support the "add" command to do this. You can simply provide
the container path and the unique resource identifier:

.. code-block:: console

    $ shpc add salad_latest.sif vanessa/salad:latest

If the unique resource identifier corresponds with a registry entry, you
will not be allowed to create it, as this would create a namespace conflict.
Since we don't have a configuration file to define custom aliases, the container
will just be exposed as it's command to run it.

Get
---

If you want to quickly get the path to a container binary, you can use get.

.. code-block:: console

    $ shpc get vanessa/salad:latest
    /home/vanessa/Desktop/Code/singularity-hpc/modules/vanessa/salad/latest/vanessa-salad-latest-sha256:8794086402ff9ff9f16c6facb93213bf0b01f1e61adf26fa394b78587be5e5a8.sif

    $ shpc get tensorflow/tensorflow:2.2.2
    /home/vanessa/Desktop/Code/singularity-hpc/modules/tensorflow/tensorflow/2.2.2/tensorflow-tensorflow-2.2.2-sha256:e2cde2bb70055511521d995cba58a28561089dfc443895fd5c66e65bbf33bfc0.sif

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
