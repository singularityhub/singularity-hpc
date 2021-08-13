.. _getting_started-developer-guide:

===============
Developer Guide
===============

This developer guide includes more complex interactions like contributing
registry entries and building containers. If you haven't read :ref:`getting_started-installation`
you should do that first.


Creating a Registry
===================

A registry consists of a database of local containers files, which are added
to the module system as executables for your user base. This typically means that you are a
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

And then you would install the module file and container as follows:

.. code-block:: console

    $ shpc install python:3.9.2

But since latest is already 3.9.2, you could leave out the tag:

.. code-block:: console

    $ shpc install python


The module folder will be generated, with the structure discussed in the USer Guide. 
Currently, any new install will re-pull the container only if the hash is different, and only re-create the module otherwise.

Contributing Registry Recipes
-----------------------------

If you want to add a new registry file, you are encouraged to contribute it here
for others to use. You should:

1. Add the recipe to the ``registry`` folder in its logical namespace, either a docker or GitHub uri
2. The name of the recipe should be ``container.yaml``. You can use another recipe as a template, or see details in :ref:`getting_started-writing-registry-entries`
3. You are encouraged to add tests and then test with ``shpc test``. See :ref:`getting_started-commands-test` for details about testing.
4. You should generally choose smaller images (if possible) and define aliases (entrypoints) for the commands that you think would be useful.

A shell entrypoint for the container will be generated automatically.
When you open a pull request, a maintainer can apply
the ``container-recipe`` label and it will test your new or updated recipes accordingly.
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
a key (python) and value (/usr/local/bin/python) set.


Aliases
-------

Each recipe has an optional section for defining aliases in the modulefile; there are two ways of defining them. In the python sample recipe above the simple form is used, using key value pairs:

.. code-block:: yaml

    aliases:
      python: /usr/local/bin/python

This format is container technology agnostic, because the command (``python``) and executable it targets (``/usr/local/bin/python``) would be consistent between
Podman and Singularity, for example. A second form is allowed, using dicts, in those cases where the command requires to specify custom options for the container runtime. For instance, suppose the python interpreter above requires an isolated shell environment (``--cleanenv`` in Singularity):

.. code-block:: yaml

    aliases:
    - name: python
      command: /usr/local/bin/python
      singularity_options: --cleanenv


Or perhaps the container required the docker options ``-it`` because it was an interactive, terminal session:

    aliases:
    - name: python
      command: /usr/local/bin/python
      docker_options: -it


For each of the above, depending on the prefix of options that you choose, it will write them into the module files for Singularity and Docker, respectively.
This means that if you design a new registry recipe, you should consider how to run it for both kinds of technology. Also note that ``docker_options`` are
those that will also be used for Podman.


Environment Variables
---------------------

Finally, each recipe has an optional section for environment variables. For
example, the container ``vanessa/salad`` shows definition of one environment
variable:

.. code-block:: yaml

    docker: vanessa/salad
    url: https://hub.docker.com/r/vanessa/salad
    maintainer: '@vsoch'
    description: A container all about fork and spoon puns.
    latest:
      latest: sha256:e8302da47e3200915c1d3a9406d9446f04da7244e4995b7135afd2b79d4f63db
    tags:
      latest: sha256:e8302da47e3200915c1d3a9406d9446f04da7244e4995b7135afd2b79d4f63db
    aliases:
      salad: /code/salad
    env:
      maintainer: vsoch

And then during build, this variable is written to a ``99-shpc.sh`` file that
is mounted into the countainer. For the above, the following will be written:

.. code-block:: console

    export maintainer=vsoch

If a recipe does not have environment variables in the container.yaml, you have
two options for adding a variable after install. For a more permanent solution,
you can update the container.yaml file and install again. The container won't
be re-pulled, but the environment file will be re-generated. If you want to 
manually add them to the container, each module folder will have an environment
file added regardless of having this section or not, so you can export them there.
When you shell, exec, or run the container (all but inspect) you should be able
to see your environment variables:

.. code-block:: console

    $ echo $maintainer
    vsoch


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
directive that you need for creating the module file that isn't there, please
open an issue so it can be added. Finally, if you don't have time to contribute directly, suggesting an idea via an issue or Slack to a maintainer (@vsoch).


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
   * - env
     - A list of environment variables to be defined in the container (key value pairs, e.g. var: value)
     - false
   * - features
     - Optional key, value paired set of features to enable for the container. Currently allowed keys: *gpu*. Allowed values: *true*, *false* (default)
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

If you first want to test singularity-hpc (shpc) with an Lmod installed in 
a container, a ``Dockerfile`` is provided for Lmod, and ``Dockerfile.tcl``
for tcl modules. The assumption is that
you have a module system installed on your cluster or in the container. If not, you
can find instructions `here for lmod <https://lmod.readthedocs.io/en/latest/030_installing.html>`_
or `here for tcl <https://modules.readthedocs.io/en/latest/INSTALL.html>`_.


.. code-block:: console
    
    $ docker build -t singularity-hpc .

If you are developing the library and need the module software, you can easily bind your
code as follows:


.. code-block:: console

    $ docker run -it --rm -v $PWD/:/code singularity-hpc

Once you are in the container, you can direct the module software to use your module files:

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


or ask for help directly!

.. code-block:: console

    # module help python/3.9.2-slim

    ----------------------------------------------------- Module Specific Help for "python/3.9.2-slim/module" ------------------------------------------------------
    This module is a singularity container wrapper for python v3.9.2-slim


    Container:

     - /home/vanessa/Desktop/Code/singularity-hpc/modules/python/3.9.2-slim/python-3.9.2-slim-sha256:85ed629e6ff79d0bf796339ea188c863048e9aedbf7f946171266671ee5c04ef.sif

    Commands include:

     - python-run:
           singularity run <container>
     - python-shell:
           singularity shell -s /bin/bash <container>
     - python-exec:
           singularity exec -s /bin/bash <container> "$@"
     - python-inspect-runscript:
           singularity inspect -r <container>
     - python-inspect-deffile:
           singularity inspect -d <container>

     - python:
           singularity exec <container> /usr/local/bin/python"


    For each of the above, you can export:

     - SINGULARITY_OPTS: to define custom options for singularity (e.g., --debug)
     - SINGULARITY_COMMAND_OPTS: to define custom options for the command (e.g., -b)


Note that you typically can't run or execute containers within another container, but 
you can interact with the module system. Also notice that for every container, we expose easy
commands to shell, run, exec, and inspect. The custom commands (e.g., Python) are then provided below that.

Make sure to write to files outside of the container so you don't muck with permissions.
Since we are using module use, this means that you can create module files as a user
or an admin - it all comes down to who has permission to write to the modules
folder, and of course use it. Note that I have not tested this on an HPC system
but plan to shortly.
