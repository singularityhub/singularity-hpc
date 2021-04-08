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

    $ module load python/3.9.2-slim

If the module executable as a conflict with something already loaded, it
will tell you, and it's up to you to unload the conflicting modules before you
try loading again. For more detailed tutorials, you should continue reading,
and see :ref:`getting_started-use-cases`.



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
for others to use. You should:

1. Add the recipe to the ``registry`` folder in its logical namespace, either a docker or GitHub uri
2. The name of the recipe should be ``container.yaml``. You can use another recipe as a template, or see details in :ref:`getting_started-writing-registry-entries`
3. You are encouraged to add tests and then test with ``shpc test``. See :ref:`getting_started-commands-test` for details about testing.
4. You should generally choose smaller images (if possible) and define aliases (entrypoints) for the commands that you think would be useful.

A shell entrypoint for the container will be generated automatically.
Once your recipe is added to the repository, the versions will be automatically
updated with a nightly run. This means that you can pull the repository to get
updated recipes, and then check for updates (the bot to do this is not developed yet):


.. code-block:: console

    $ shpc check python
    ==> You have python 3.7 installed, but the latest is 3.8. Would you like to install?
    yes/no : yes


It's reasonable that you can store your recipes alongside these files, in the ``registry``
folder. If you see a conflict and want to request allowing for a custom install path
for recipes, please open an issue.


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



Prefixes
^^^^^^^^

If you want your modules to have an alias prefix, you can
set ``lmod_exc_prefix`` (an alias prefix). If you want your modules
to have a directory prefix, simply create the directory and then update
the ``lmod_base`` path.

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

The default will not show versions available. To flatten out this list and include
versions for each, you can do:

.. code-block:: console

    $ shpc show
    tensorflow/tensorflow:2.2.2
    python:3.9.2-slim
    python:3.9.2-alpine
    singularityhub/singularity-deploy:salad


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
    
Note that since we only have one module system (lmod) and one
HPC container technology (Singularity) these are the defaults. However, they
are parser options and can be customized to use something else if this is
added in the future.

If you don't have lmod on your system, you can now test interacting
with the module via the :ref:`getting_started-development` instructions.

List
----

Once a module is installed, you can use list to show installed modules (and versions).

.. code-block:: console

    $ shpc list
    python: 3.9.2-alpine, 3.9.2-slim


Inspect
-------

Once you install a module, you might want to inspect the associated container! You
can do that as follows:

.. code-block:: console

    $ shpc inspect python/3.9.2-slim
    [shpc-client] [database|dummy]
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

    $ shpc inspect --runscript python/3.9.2-slim


Or to get the entire metadata entry dumped as json to the terminal:

.. code-block:: console

    $ shpc inspect --json python/3.9.2-slim


.. _getting_started-commands-test:


Test
----

Singularity HPC makes it easy to test the full flow of installing and interacting
with modules. This functionality requires lmod to be installed. 

.. code-block:: console

    shpc test python


If you don't have it, you can run tests in the provided docker container. 

.. code-block:: console

    docker build -t singularity-hpc .
    docker run --rm -it singularity-hpc shpc test python


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
(e.g., typically lmod):


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

    $ shpc uninstall python/3.9.2-alpine


You can also uninstall an entire family  of modules:

.. code-block:: console

    $ shpc uninstall python



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

You can also interact with your registry interactively, and the easiest
way to do that is to use the shell. It defaults to ipython, and then python and
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
    [shpc-client] [database|sqlite:////home/vanessa/Desktop/Code/singularity-hpc/shpc.db]
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
    [shpc-client] [database|sqlite:////home/vanessa/Desktop/Code/singularity-hpc/shpc.db]
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

    $ shpc check tensorflow/tensorflow/2.2.2
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

    $ shpc add salad_latest.sif vanessa/salad/latest

If the unique resource identifier corresponds with a registry entry, you
will not be allowed to create it, as this would create a namespace conflict.
Since we don't have a configuration file to define custom aliases, the container
will just be exposed as it's command to run it.

Get
---

If you want to quickly get the path to a container binary, you can use get.

.. code-block:: console

    $ shpc get vanessa/salad/latest
    /home/vanessa/Desktop/Code/singularity-hpc/modules/vanessa/salad/latest/vanessa-salad-latest-sha256:8794086402ff9ff9f16c6facb93213bf0b01f1e61adf26fa394b78587be5e5a8.sif

    $ shpc get tensorflow/tensorflow/2.2.2
    /home/vanessa/Desktop/Code/singularity-hpc/modules/tensorflow/tensorflow/2.2.2/tensorflow-tensorflow-2.2.2-sha256:e2cde2bb70055511521d995cba58a28561089dfc443895fd5c66e65bbf33bfc0.sif

If you select a higher level module directory or there is no sif, you'll see:

.. code-block:: console

    $ shpc get tensorflow/tensorflow
    tensorflow/tensorflow is not a module tag folder, or does not have a sif binary.


We could update this command to allow for listing all sif files within a top level
module folder (for different versions). Please open an issue if this would be useful for
you.


.. _getting_started-writing-registry-entries:


Writing Registry Entries
========================

An entry in the registry is a container.yaml file that lives in the ``registry``
folder. You should create subfolders based on a package name. Multiple versions
will be represented in the same file, and will install to the admin user's module
folder with version subfolders. E.g., two registry entries, one for python
(a single level name) and for tensorflow (a more nested name) would look like
this:

.. code-block:: console

    registry/
    ├── python
    │       └── container.yaml
    └── tensorflow
        └── tensorflow
            └── container.yaml


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

Docker Hub
----------

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


The above shows the simplest form of representing an alias, where each is
a key (python) and value (/usr/local/bin/python) set. As an alternative,
for aliases with more complex settings (e.g., additional arguments to provide
to exec) you can describe these same attributes as a list. Here is an example
for tensorflow:

.. code-block:: yaml

    docker: tensorflow/tensorflow
    latest:
      2.2.2: sha256:e2cde2bb70055511521d995cba58a28561089dfc443895fd5c66e65bbf33bfc0
    tags:
      2.2.2: sha256:e2cde2bb70055511521d995cba58a28561089dfc443895fd5c66e65bbf33bfc0
    filter:
    - 2.*
    maintainer: '@vsoch'
    url: https://hub.docker.com/r/tensorflow/tensorflow
    aliases:
    - name: python
      command: python
      options: "--nv"


Since we want to add the "--nv" flag, we add it as an option. Keep in mind
that since we have a list, you technically could provide duplicate commands.
However, the list is parsed into a dictionary, so only unique values are 
enforced. If you accidentally have a repeated value, a warning will be printed.

Singularity Deploy
------------------

Using `Singularity Deploy <https://github.com/singularityhub/singularity-deploy>`_
you can easily deploy a container as a GitHub release! See the repository for
details. The registry entry should look like:

.. code-block:: yaml

    gh: singularityhub/singularity-deploy
    latest:
      salad: "0.0.1"
    tags:
      salad: "0.0.1"
    maintainer: "@vsoch"
    url: https://github.com/singularityhub/singularity-deploy
    aliases:
      salad: /code/salad

Where ``gh`` corresponds to the GitHub repository, the tags are the
extensions of your Singularity recipes in the root, and the "versions"
(e.g., 0.0.1) are the release numbers. There are examples in the registry
(as shown above) for details.


Choosing Containers to Contribute
---------------------------------

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

    $ docker run -it --rm -v $PWD/:/code singularity-hpc

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
