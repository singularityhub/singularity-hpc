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

While the library is currently focused on Singularity containers (hence
the name) it's created to be modular, meaning that if another container technology
is wanted, it can be added. The module name would still be appropriate, as
singularity does imply a single entity that is "one library to rule them all!"


Quick Start
===========

After  :ref:`getting_started-installation`, and let's say shpc is installed 
at ``~/singularity-hpc`` you can install a container:

.. code-block:: console

    $ shpc install python
    
Add the modules folder to your lmod (you can run this in a bash profile or
manually).


.. code-block:: console

    $ module use ~/singularity-hpc/modules


And then load the module!

.. code-block:: console

    $ module load python/3.9.2



Creating a Registry
===================

A registry consists of a database of local containers files, which are added
to LMOD as executables for your user base. This typically means that you are a
linux administrator of your cluster, and shpc should be installed for you to use
(but your users will not be interacting with it).

The Registry Folder
-------------------

Although you likely will add custom containers, it's very likely that you
want to provide a set of core containers that are fairly standard, like Python
and other scientific packages. For this reason, Singularity Registry HPC
comes with a registry folder, or a folder with different containers and versions
that you can easily install. For example, here is a recipe for a Python 3.9.2 container
that would be installed to your modules as we showed above:

.. code-block:: yaml

    docker: python
    latest:
      3.9.2: sha256:7d241b7a6c97ffc47c72664165de7c5892c99930fb59b362dd7d0c441addc5ed
    tags:
      3.9.2: sha256:7d241b7a6c97ffc47c72664165de7c5892c99930fb59b362dd7d0c441addc5ed
      3.9.2-alpine: sha256:23e717dcd01e31caa4a8c6a6f2d5a222210f63085d87a903e024dd92cb9312fd
    filter:
    - 3.9.*
    maintainer: '@vsoch'
    url: https://hub.docker.com/_/python
    aliases:
      python: python

And then you would install the lmod file and container as follows:

.. code-block:: console

    $ shpc install python:3.9.2

But since latest is already 3.9.2, you could leave out the tag.

.. code-block:: console

    $ shpc install python


And the module folder shown previously would be generated. Currently, we assume
that any new install will re-pull the container (and remove a previous one).
We will eventually update this to only re-generate if the hash is different.

Contributing Registry Recipes
-----------------------------

If you want to add a new registry file, you are encouraged to contribute it here
for others to use. Once it's added to the repository, the versions will be automatically
updated with a nightly run. This means that you can pull the repository to get
updated recipes, and then check for updates (this command is not developed yet):


.. code-block:: console

    $ shpc check python
    ==> You have python 3.7 installed, but the latest is 3.8. Would you like to install?
    yes/no : yes


It's reasonable that you can store your recipes alongside these files, in the ``registry``
folder. If you see a conflict and want to request allowing for a custom install path
for recipes, 


Setup
-----

Setup includes, after installation, editing any configuration values to
customize your install. The defaults are likely suitable for most.
For any configuration value that you might set, the following variables
are available to you:

 - ``$install_dir``: the shpc folder
 - ``$root_dir``: the parent directory of shpc (where this README.md is located)


A summary table of variables is included below, and then further discussed in detail.


.. list-table:: Title
   :widths: 25 65 10
   :header-rows: 1

   * - Name
     - Description
     - Default
   * - plugins_enabled
     - A list of plugins enabled. Currently only lmod is supported.
     - [lmod]
   * - registry
     - The full path to the registry folder (with subfolders with container.yaml recipes)
     - $root_dir/registry
   * - lmod_base
     - The install directory for modules. Defaults to the install directory/modules
     - $root_dir/modules
   * - database_disable
     - disable keeping a sqlite database with metadata
     - false
   * - database_file
     - default database file
     - $root_dir/shpc.db
   * - updated_at
     - a timestamp to keep track of when you last saved
     - never
   * - singularity_module
     - if defined, add to lmod script to load this Singularity module first
     - null
   * - lmod_dir_prefix
     - If set, prefix module folder names with prefix (for namespacing)
     - ""
   * - lmod_exc_prefix
     - If set, prefix module alias names with prefix (another kind of namespacing)
     - ""
   * - bindpaths
     - string with comma separated list of paths to binds. If set, expored to SINGULARITY_BINDPATH
     - null
   * - singularity_shell
     - exported to SINGULARITY_SHELL, defaults to /bin/bash.
     - /bin/bash



Modules Folder
^^^^^^^^^^^^^^

The first thing you want to do is configure your module location, if you want it different
from the default. The path can be absolute or relative to ``$install_dir`` (the shpc
directory) or ``$root_dir`` (one above that) in your
configuration file at ``shpc/settings.yml``. If you are happy
with module files being stored in a ``modules`` folder in the present working
directory, you don't need to do any configuration. Otherwise, you can customize
your install:

.. code-block:: console

    # an absolute path
    $ shpc config lmod_base:/opt/lmod/modules

    # or a path relative to a variable location remember to escape the "$"
    $ shpc config lmod_base:\$root_dir/modules


This directory will be the base where lua files are added, and container are stored.
For example, if you were to add a container with unique resource identifier `python/3.8`
you would see:

.. code-block:: console

    $install_dir/modules/
    └── python
        └── 3.9.2
            ├── module.lua
            └── python-3.9.2.sif

Although your LMOD path might have multiple locations, Singularity Registry HPC 
assumes this one location to install container modules to in order to ensure
a unique namespace. 


Database Setup
^^^^^^^^^^^^^^

By default, shpc installs with the ability to create a local database for you
to keep track of your containers (as an admin), which is not accessible to the
user. However, it's not entirely needed because you can easily use lmod. Here
are the configuration options available to you:


.. code-block:: yaml

    # disable keeping a sqlite database with metadata
    database_disable: false

    # default database file
    database_file: "$install_dir/shpc.db"


See the :ref:`getting_started-commands-config` for how to update these
values with the command line client ``shpc config``.


Registry
^^^^^^^^

The registry folder in the root of the repository, but you can change it to
be a custom one with the config variable ``registry``


.. code-block:: console

    # change to your own registry of container yaml configs
    $ shpc config registry:/opt/lmod/registry



Module Software
---------------

The default module software is currently LMOD, but others could be added. If you
are interested in adding another module type, please `open an issue <https://github.com/singularityhub/singularity-hpc>`_ and
provide description and links to what you have in mind. Currently, only lmod is
supported.

Container Technology
--------------------

The default container technology to pull and then provide to users is Singularity,
which makes sense because we can add executables to the path that are Singularity containers.
If you would like support for a different container technology, please also
`open an issue <https://github.com/singularityhub/singularity-hpc>`_ and
provide description and links to what you have in mind. Currently, only lmod is
supported.


.. _getting_started-commands:

Commands
========

The following commands are available!

.. _getting_started-commands-config:


Config
------

If you want to edit a configuration value, you can either edit the ``shpc/settings.yml``
file directly, or you can use ``shpc config``. The following example shows changing
the default lmod_base path from the install directory modules folder.

.. code-block:: console

    # an absolute path
    $ shpc config lmod_base:/opt/lmod/modules

    # or a path relative to the install directory, remember to escape the "$"
    $ shpc config lmod_base:\$install_dir/modules


List and Install
----------------

The most basic thing you might want to do is install an already existing
recipe in the registry. You might first want to list the known packages
first. To list all packages, you can run:


.. code-block:: console

    $ shpc list
    [shpc-client] [database|sqlite:////home/vanessa/Desktop/Code/singularity-hpc/shpc.db]
    python


To get details about a package, you would then do:

.. code-block:: console

    $ shpc show python
    [shpc-client] [database|sqlite:////home/vanessa/Desktop/Code/singularity-hpc/shpc.db]


And then you can install a version that you like (or don't specify to default to
the latest, which in this case is 3.9.2).


.. code-block:: console
    
    $ shpc install python

You will see the container pulled, and then a message to indicate that the module
was created. 

.. code-block:: console

    [shpc-client] [database|sqlite:////home/vanessa/Desktop/Code/singularity-hpc/shpc.db]
    Module python/3.9.2 is created.


.. code-block:: console

    $ tree modules/
    modules/
    └── python
        └── 3.9.2
            ├── module.lua
            └── python-3.9.2.sif

    2 directories, 2 files
    
    
Note that since we only have one module system (lmod) and one
HPC container technology (Singularity) these are the defaults. However, they
are parser options and can be customized to use something else if this is
added in the future.

If you don't have lmod on your system, you can now test interacting
with the module via the :ref:`getting_started-development` instructions.


Add
---

**todo**


Images
------


**todo**


Check
-----

**todo**


Writing Registry Entries
========================

An entry in the registry is a container.yaml file that lives in the ``registry``
folder. You should create subfolders based on a package name. Multiple versions
will be represented in the same file, and will install to the admin user's module
folder with version subfolders. E.g., Python would look like:


.. code-block:: console

    ./registry
        python/
          container.yaml


And this is what gets installed to the modules folder, where each is kept in
a separate directory based on version.

.. code-block:: console

    $ tree modules/
    modules/
    └── python
        └── 3.9.2
            ├── module.lua
            └── python-3.9.2.sif

    2 directories, 2 files

So different versions could exist alongside one another.

Registry Yaml Files
===================

The typical registry yaml file will reference a container from a registry,
one or more versions, and a maintainer GitHub alias that can be pinged
for any issues:


.. code-block:: yaml

    docker: python
    latest:
      3.9.2-slim: "sha256:85ed629e6ff79d0bf796339ea188c863048e9aedbf7f946171266671ee5c04ef"
    tags:
      3.9.2-slim: "sha256:85ed629e6ff79d0bf796339ea188c863048e9aedbf7f946171266671ee5c04ef"
      3.9.2-alpine: "sha256:23e717dcd01e31caa4a8c6a6f2d5a222210f63085d87a903e024dd92cb9312fd"
    filter:
      - "3.9.*"
    maintainer: "@vsoch"
    url: https://hub.docker.com/_/python
    aliases:
      python: /usr/local/bin/python

How should you choose container bases to contribute? You might consider using
smaller images, when possible (take advantage of multi-stage builds) and
for aliases, make sure (if possible) that you use full paths. If there is a
directive that you need for creating the LMOD lua file that isn't there, please
open an issue so it can be added. Finally, if you don't have time to contribute directly, suggesting an idea via an issue
or Slack to a maintainer (@vsoch).


Registry Yaml Fields
====================

Fields include:

.. list-table:: Title
   :widths: 25 65 10
   :header-rows: 1

   * - Name
     - Description
     - Required
   * - docker
     - A Docker uri, which should include the registry but not tag
     - true
   * - tags
     - A list of available tags
     - true
   * - latest
     - The latest tag, along with the digest that will be updated by a bot in the repository (e.g., tag: digest)
     - true
   * - maintainer
     - The GitHub alias of a maintainer to ping in case of trouble
     - true
   * - filter
     - A list of patterns to use for adding new tags. If not defined, all are added 
     - false
   * - aliases
     - Named entrypoints for container (dict)
     - false
   * - url
     - Documentation or other url for the container uri
     - false
   * - description
     - Additional information for the registry entry
     - false

Other supported (but not yet developed) fields could include different unique
resource identifiers to pull/obtain other kinds of containers. For this
current version, since we are assuming HPC and Singularity, we will typically
pull a Docker unique resource identifier with singularity, e.g.,:


.. code-block:: console

    $ singularity pull docker://python:3.9.2


Updating Registry Yaml Files
============================

We will be developing a GitHub action that automatically parses new versions
for a container, and then updates the registry packages. The algorithm we will
use is the following:

 - If docker, retrieve all tags for the image
 - Update tags:
   - if one or more filters ("filter") are defined, add new tags that match
   - otherwise, add all new tags
 - If latest is defined and a version string can be parsed, update latest
 - For each of latest and tags, add new version information


.. _getting_started-development:

Development or Testing
======================

If you first want to test singularity-hpc (shpc) with an LMOD installed in 
a container, a ``Dockerfile`` is provided. The assumption is that
you have LMOD installed on your cluster or in the container. If not, you
can find instructions `here <https://lmod.readthedocs.io/en/latest/030_installing.html>`_.


.. code-block:: console
    
    $ docker build -t singularity-hpc .

If you are developing the library and need lmod, you can easily bind your
code as follows:


.. code-block:: console

    $ docker run -it --rm -v $PWD/:/code --entrypoint bash singularity-hpc

Once you are in the container, you can direct LMOD to use your module files:

.. code-block:: console

    $ module use /code/modules

Then you can use spider to see the modules:

.. code-block:: console

    # module spider python

    --------------------------------------------------------------------------------------------------------------------------------------------------------------
      python/3.9.2: python/3.9.2/module
    --------------------------------------------------------------------------------------------------------------------------------------------------------------

        This module can be loaded directly: module load python/3.9.2/module
    ```

Make sure to write to files outside of the container so you don't muck with permissions.
Since we are using module use, this means that you can create module files as a user
or an admin - it all comes down to who has permission to write to the modules
folder, and of course use it. Note that I have not tested this on an HPC system
but plan to shortly.
