.. _getting_started-developer-guide:

===============
Developer Guide
===============

This developer guide includes more complex interactions like contributing
registry entries and building containers. If you haven't read :ref:`getting_started-installation`
you should do that first.


Developer Commands
==================

Singularity Registry HPC has a few "developer specific" commands that likely will only be
used in automation, but are provided here for the interested reader.

Docgen
------

To generate documentation for a registry (e.g., see `this registry example <https://singularityhub.github.io/shpc-registry>`_ we can use docgen. Docgen, by way of needing to interact with the local filesystem,
currently only supports generation for a filesystem registry. E.g., here is how to generate a registry module
(from a local container.yaml) that ultimately will be found in GitHub pages:

.. code-block:: console

    $ shpc docgen --registry . --registry-url https://github.com/singularityhub/shpc-registry python
    
And you could easily pipe this to a file. Here is how we generate this programatically in a loop:


.. code-block:: console

    for module in $(shpc show --registry ../shpc-registry); do          
        flatname=${module#/}
        name=$(echo ${flatname//\//-})
        echo "Generating docs for $module, _library/$name.md"
        shpc docgen --registry ../shpc-registry --registry-url https://github.com/singularityhub/shpc-registry $module > "_library/${name}.md"
    done


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


And this is what gets installed to the modules and containers directories, where each is kept in
a separate directory based on version.

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

.. code-block:: yaml

    aliases:
    - name: python
      command: /usr/local/bin/python
      docker_options: -it


For each of the above, depending on the prefix of options that you choose, it will write them into the module files for Singularity and Docker, respectively.
This means that if you design a new registry recipe, you should consider how to run it for both kinds of technology. Also note that ``docker_options`` are
those that will also be used for Podman.

Overrides
---------

It might be the case that as your containers change over time, the set of any of:

- commands (aliases)
- docker_script
- singularity_script
- environment (env)
- features
- description

does too! Or it be the case that you have hundreds of aliases, and want to better organize them separately from the container.yaml. To support this, shpc
(as of version 0.0.56) has support for an ``overrides`` section in the container.yaml, meaning that you can define pairs of container
tags and relative path lookups to external files with any of the stated sections. A simple example might look like this:

.. code-block:: yaml

    docker: python
    url: https://hub.docker.com/_/python
    maintainer: '@vsoch'
    description: An interpreted, high-level and general-purpose programming language.
    latest:
      3.9.5-alpine: sha256:f189f7366b0d381bf6186b2a2c3d37f143c587e0da2e8dcc21a732bddf4e6f7b
    tags:
      3.9.2-alpine: sha256:f046c06388c0721961fe5c9b6184d2f8aeb7eb01b39601babab06cfd975dae01
    overrides:
      3.9.2-alpine: aliases/3.9.2-alpine.yaml
    aliases:
        python: /usr/local/bin/python


Since this file only has aliases, we chose to use a subdirectory called "aliases" to make that clear, however
the file can have any of the fields mentioned above, and can be organized in any relative path to the container directory that you deem apppropriate.
Here is what this corresponding file with relative path ``aliases/3.9.2-alpine.yaml`` might look like this:

.. code-block:: yaml

    aliases:
      python: /alias/path/to/python

Finally, for all fields mentioned above, the format is expected to follow the same convention as above (and it will be validated again on update).


Wrapper Script
--------------

Singularity HPC allows exposure of two kinds of wrapper scripts:

1. A global level wrapper intended to replace aliases. E.g., if an alias "samtools" is typically a direct container call, enabling a wrapper will generate an executable script "samtools" in a "bin" directory associated with the container, added to the path, to call instead. This is desired when MPI ("mpirun")  or scheduler (e.g. "srun" with Slurm) utilities are needed to run the scripts. This global script is defined in settings.yml and described in the user guide.
2. A container level wrapper that is specific to a container, described here.

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

You can look at ``registry/vanessa/salad`` for an example that includes Singularity
and Docker wrapper scripts. For example, when generating for a singularity container with
the global wrapped scripts enabled, we get one wrapper script for the alias "salad" and one for
the custom container script "fork":

.. code-block:: console

    $ tree modules/vanessa/salad/
    modules/vanessa/salad/
    └── latest
        ├── 99-shpc.sh
        ├── bin
        │   ├── fork
        │   └── salad
        └── module.lua

If we disable all wrapper scripts, the bin directory would not exist. If we set the default wrapper
scripts for singularity and docker in settings.yml and left enable to true, we would only see "fork."

How to write an alias wrapper script
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

First, decide if you want a global script (to replace or wrap aliases) OR a custom container script. For an alias derived (global) script, you should:

1. Write the new script file into shpc/main/wrappers.
2. Add an entry to shpc/main/wrappers/scripts referencing the script.

For these global scripts, the user can select to use it in their settings.yaml.
We will eventually write a command to list global wrappers available, so if you add a new one future users will know
about it. For alias wrapper scripts, the following variables are passed for rendering:

.. list-table:: Wrapper Script Variables
   :widths: 15 15 40 30
   :header-rows: 1

   * - Name
     - Type
     - Description
     - Example
   * - alias
     - dictionary
     - The entire alias in question, including subfields name, command, singularity_options or docker_options, singularity_script or docker_script, and args
     - ``{{ alias.name }}`` 
   * - settings
     - dictionary
     - Everything referenced in the user settings
     - ``{{ settings.wrapper_shell }}``
   * - container
     - dictionary
     - The container technology
     - ``{{ container.command }}`` renders to docker, singularity, or podman
   * - config
     - dictionary
     - The entire container config (container.yaml) structured the same
     - ``{{ config.docker }}``
   * - image
     - string
     - The name of the container binary (SIF) or unique resource identifier
     - ``{{ image }}``
   * - module_dir
     - string
     - The name of the module directory
     - ``{{ module_dir }}``
   * - features
     - dictionary
     - A dictionary of parsed features
     - ``{{ features.gpu }}``

     

How to write an container wrapper script
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you want to write a custom container.yaml script:

1. Add either (or both) of singularity_scripts/docker_scripts in the container.yaml, including an alias command and an associated script.
2. Write the script with the associated name into that folder.

For rendering, the same variables as for alias wrapper scripts are passed,
**except** ``alias`` which is now a *string* (the name of the alias defined
under singularity_scripts or docker_scripts) and should be used directly, e.g.
``{{ alias }}``.


Templating for both wrapper script types
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Note that you are free to use "snippets" and "bases" either as an inclusion or "extends" meaning you can
easily re-use code. For example, if we have the following registered directories under ``shpc/main/wrappers/templates`` 
for definition of bases and templates:

.. code-block:: console

    main/wrappers/templates/
    
    # These are intended for use with "extends"
    ├── bases
    │   ├── __init__.py
    │   └── shell-script-base.sh
    
    # These are top level template files, as specified in the settings.yml
    ├── docker.sh
    ├── singularity.sh

    # A mostly empty directory ready for any snippets!
    └── snippets

For example, a "bases" template to define a shell and some special command that might look like this:

.. code-block:: console

    #!{{ settings.wrapper_shell }}

    script=`realpath $0`
    wrapper_bin=`dirname $script`
    {% if '/csh' in settings.wrapper_shell %}set moduleDir=`dirname $wrapper_bin`{% else %}export moduleDir=$(dirname $wrapper_bin){% endif %}

    {% block content %}{% endblock %}


And then to use it for any container- or global- wrapper we would do the following in the wrapper script:

.. code-block:: console

    {% extends "bases/my-base-shell.sh" %}

    # some custom wrapper before stuff here

    {% block content %}{% endblock %}

    # some custom wrapper after stuff here


For snippets, which are intended to be more chunks of code you can throw in one spot
on the fly, you can do this:


.. code-block:: console

    {% include "snippets/export-envars.sh" %}
    # some custom wrapper after stuff here


Finally, if you want to add your own custom templates directory for which you
can refer to templates relatively, define ``wrapper_scripts`` -> ``templates`` as a full path
in your settings.


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


Oras
----

As of version 0.0.39 Singularity Registry HPC has support for oras, meaning
we can use the Singularity client to pull an oras endpoint. Instead of using
``docker:`` in the recipe, the container.yaml might look like this:

.. code-block:: yaml

    oras: ghcr.io/singularityhub/github-ci
    url: https://github.com/singularityhub/github-ci/pkgs/container/github-ci
    maintainer: '@vsoch'
    description: An example SIF on GitHub packages to pull with oras
    latest:
      latest: sha256:227a917e9ce3a6e1a3727522361865ca92f3147fd202fa1b2e6a7a8220d510b7
    tags:
      latest: sha256:227a917e9ce3a6e1a3727522361865ca92f3147fd202fa1b2e6a7a8220d510b7


And then given the ``container.yaml`` file located in ``registry/ghcr.io/singularityhub/github-ci/`` 
you would install with shpc and the Singularity container backend as follows:

.. code-block:: console

    $ shpc install ghcr.io/singularityhub/github-ci


**Important**: You should retrieve the image sha from the container registry and 
not from the container on your computer, as the two will often be different depending
on metadata added.

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

.. list-table:: Registry YAML Fields
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
     - Named entrypoints for container (dict) as described above
     - false
   * - overrides
     - Key value pairs to override container.yaml defaults.
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
     - Optional key, value paired set of features to enable for the container. Currently allowed keys: *gpu* *home* and *x11*.
     - varies
   * - singularity_scripts
     - key value pairs of wrapper names (e.g., executable called by user) and local container script for Singularity
     - false
   * - docker_scripts
     - key value pairs of wrapper names (e.g., executable called by user) and local container script for Docker or Singularity
     - false

A complete table of features is shown here. The

Fields include:

.. list-table:: Features
   :widths: 20 20 20 10 10 10
   :header-rows: 1

   * - Name
     - Description
     - Container.yaml Values
     - Settings.yaml Values
     - Default
     - Supported
   * - gpu
     - Add flags to the container to enable GPU support (typically amd or nvidia)
     - true or false
     - null, amd, or nvidia
     - null
     - Singularity
   * - x11
     - Indicate to bind an Xauthority file to allow x11
     - true or false
     - null, true (uses default ~/.Xauthority) or bind path
     - null
     - Singularity
   * - home
     - Indicate a custom home to bind
     - true or false
     - null, or path to a custom home
     - null
     - Singularity, Docker


For bind paths (e.g., home and x11) you can do a single path to indicate the same
source and destination (e.g., /my/path) or a double for customization of that (e,g., /src:/dest).
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

     - /home/vanessa/Desktop/Code/singularity-hpc/containers/python/3.9.2-slim/python-3.9.2-slim-sha256:85ed629e6ff79d0bf796339ea188c863048e9aedbf7f946171266671ee5c04ef.sif

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
and containers folder, and of course use it.
