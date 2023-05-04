.. _getting_started-developer-guide:

===============
Developer Guide
===============

This developer guide includes more complex interactions like contributing
registry entries and building containers. If you haven't read :ref:`getting_started-installation`
you should do that first.

.. _getting_started-developer-environment:


Environment
===========

After installing shpc to a local environment, you can use pre-commit to help
with linting and formatting. To do that:


.. code-block:: console

    $ pip install -r .github/dev-requirements.txt

Then to run:


.. code-block:: console

    $ pre-commit run --all-files

You can also install as a hook:


.. code-block:: console

    $ pre-commit install

.. _getting_started-developer-commands:


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

And you could easily pipe this to a file. Here is how we generate this programmatically in a loop:


.. code-block:: console

    for module in $(shpc show --registry ../shpc-registry); do
        flatname=${module#/}
        name=$(echo ${flatname//\//-})
        echo "Generating docs for $module, _library/$name.md"
        shpc docgen --registry ../shpc-registry --registry-url https://github.com/singularityhub/shpc-registry $module > "_library/${name}.md"
    done

.. _getting_started-creating-filesystem-registry:

Creating a FileSystem Registry
==============================

A filesystem registry consists of a database of local containers files, which are added
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


The module folder will be generated, with the structure discussed in the User Guide.
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

.. _getting_started-creating-remote-registry:


Creating a Remote Registry
==========================

If you want to create your own remote registry (currently supported to be on GitHub or GitLab)
the easiest thing to do is start with one of our shpc provided registries as a template:

 - `**GitHub** <https://github.com/singularityhub/shpc-registry>`_
 - `**GitLab** <https://gitlab.com/singularityhub/shpc-registry>`_

This means (for either) you'll want to clone the original repository:

.. code-block:: console

    $ git clone https://github.com/singularityhub/shpc-registry my-registry
    $ cd my-registry

Ensure you do a fetch to get the github pages branch, which deploys the web interface!

.. code-block:: console

    $ git fetch

At this point, you can create an empty repository to push to. If you don't mind
it being a fork, you can also just fork the original repository (and then pull
from it instead). GitLab has a feature to fork and then remove the fork, so that
is an option too. Ensure that you push the gh-pages branch too (for GitHub only):

.. code-block:: console

    $ git checkout gh-pages
    $ git push origin gh-pages

Once you have your cloned registry repository, it's up to you for how you want
to delete / edit / add containers! You'll likely use ``shpc add`` to generate new
configs, and you might want to delete most of the default containers provided.
Importantly, you should take note of the workflows in the repository. Generally:

 - We have an update workflow (GitHub) that will check for new versions of containers. This still need to be ported to GitLab.
 - The docs workflow (on GitHub, this is in the .github-ci.yaml) will deploy docs to GitHub/GitLab pages.

For each of GitLab and GitHub, ensure after you deploy that your pages are enabled.
It helps to ensure the website (static) URL is in the description to be easily find-able.
Once it's deployed, ensure you see your containers, and clicking the ``</>`` (code)
icon shows the library.json that shpc will use. Finally, akin to adding a filesystem registry,
you can just do the same, but specify your remote URL:

.. code-block:: console

    $ shpc config add registry https://github.com/singularityhub/shpc-registry

And that's it!

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

.. _getting_started-development-registry-yaml-files:


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
the file can have any of the fields mentioned above, and can be organized in any relative path to the container directory that you deem appropriate.
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
is mounted into the container. For the above, the following will be written:

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


.. _getting_started-development-github-action:

GitHub Action
=============

As of version ``0.1.17`` we provide a GitHub action that will allow you to update
a registry from an container binary cache. Does any of this not make sense?
Don't worry! We have a full tutorial below to walk you through this process.
For now, here is how to use the action provided here alongside your remote
registry (e.g., running in GitHub actions) to update from a container executable
cache of interest. For the example here, we are updating the ``singularityhub/shpc-registry``
from binaries in the ``singularityhub/shpc-registry-cache`` that happens to contain
over 8K BioContainers.

.. code-block:: yaml

    name: Update BioContainers

    on:
      pull_request: []
      schedule:
      - cron: 0 0 1 * *

    jobs:
      auto-scan:
        runs-on: ubuntu-latest
        steps:
        - name: Checkout
          uses: actions/checkout@v3
          with:
            fetch-depth: '0'

        - name: Create conda environment
          run: conda create --quiet -c conda-forge --name cache spython

        - name: Derive BioContainers List
          run: |
            export PATH="/usr/share/miniconda/bin:$PATH"
            source activate cache
            pip install -r .github/scripts/dev-requirements.txt
            python .github/scripts/get_biocontainers.py /tmp/biocontainers.txt
            head /tmp/biocontainers.txt

          # registry defaults to PWD, branch defaults to main
        - name: Update Biocontainers
          uses: singularityhub/singularity-hpc/actions/cache-update@main
          with:
            token: ${{ secrets.GITHUB_TOKEN }}
            cache: https://github.com/singularityhub/shpc-registry-cache
            min-count-inclusion: 10
            max-count-inclusion: 1000
            additional-count-inclusion: 25
            # Defaults to shpc docs, this gets formatted to include the entry_name
            url_format_string: "https://biocontainers.pro/tools/%s"
            pull_request: "${{ github.event_name != 'pull_request' }}"
            namespace: quay.io/biocontainers
            listing: /tmp/biocontainers.txt

The listing we derive in the third step is entirely optional, however providing one
will (in addition to updating from the cache) ensure that entries provided there are also added,
albeit without aliases. The namespace is provided to supplement the listing.
The reason we allow this additional listing is because the cache often misses being able
to extract a listing of aliases for some container, and we still wait to add it to the registry
(albeit without aliases).


Developer Tutorial
==================

This is currently a small tutorial that will include some of the lessons above and
show you how to:

1. Create a new remote registry on GitHub with automated updates
2. Create a new container executable cache
3. Automate updates of the cache to your registry

Preparing a Remote Registry
---------------------------

To start, `create a new repository <https://docs.github.com/en/get-started/quickstart/create-a-repo>`_
and follow the instructions in :ref:`getting_started-creating-remote-registry` to
create a remote registry. We will briefly show you the most basic clone and adding
a few entries to it here.

.. code-block:: console

    # Clone the shpc-registry as a template
    $ git clone https://github.com/singularityhub/shpc-registry /tmp/my-registry
    $ cd /tmp/my-registry

The easiest way to delete the entries (to make way for your own) is to use shpc itself!
Here is how we can use ``shpc show`` to remove the entries. First, make sure that
shpc is installed (:ref:`getting_started-installation`) and ensure your registry
is the only one in the config registry section. You can use ``shpc config edit``
to quickly see it. It should look like this:

.. code-block:: yaml

    # This is the default line you can comment out / remove
    # registry: [https://github.com/singularityhub/shpc-registry]
    # This is your new registry path, you'll need to add this.
    # Please preserve the flat list format for the yaml loader
    registry: [/tmp/my-registry]

After making the above change, exit and do a sanity check to make sure your active config is the one you think it is:

.. code-block:: console

    $ shpc config get registry
    registry                       ['/tmp/my-registry']


Deleting Entries
^^^^^^^^^^^^^^^^

If you want to start freshly, you can choose to delete all the existing entries
(and this is optional, you can continue the tutorial without doing this!)
To do this, use the ``shpc remove`` command, which will remove all registry entries.
We recommend deleting quay.io first since most entries live there and it will
speed up the subsequent operation.

.. code-block:: console

    $ rm -rf quay.io/biocontainers
    $ shpc remove # answer yes to confirmation

If you do a git status after this, you'll see many entries removed.
Save your changes with a commit.

.. code-block:: console

    $ git commit -a -s -m 'emptying template registry'

After this you will have only a skeleton set of files, and most importantly,
the .github directory with automation workflows. Feel free to remove or edit files
such as the ``FUNDING.yml`` and ``ISSUE_TEMPLATE``.

Fetch GitHub Pages
^^^^^^^^^^^^^^^^^^

Next, use "fetch" to get GitHub pages.

.. code-block:: console

    $ git fetch

At this point you can edit the ``.git/config`` to be your new remote.

.. code-block:: console

    # Update the remote to be your new repository
    vim .git/config

As an example, here is a diff where I changed the original registry to a new one I created called `vsoch/test-registry`:

.. code-block:: git

    [core]
            repositoryformatversion = 0
            filemode = true
            bare = false
            logallrefupdates = true
    [remote "origin"]
            # url = https://github.com/singularityhub/shpc-registry
            url = git@github.com:vsoch/test-registry
            fetch = +refs/heads/*:refs/remotes/origin/*
    [branch "main"]
            remote = origin
            merge = refs/heads/main

Note that in the above, we also change "https://" to be "git" to use a different protocol.
You should only do this change after you've fetched, as you will no longer be connected to the original
remote! Finally, you'll need to change the "baseurl" in `_config.yaml` to be the name of your GitHub repository:

```diff
- baseurl: "/shpc-registry" #important: start with /
+ baseurl: "/my-shpc-registry" #important: start with /
```

If you forget this step, the pages will render, but the style sheets will be broken.

Push Branches to your New Remote
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Note that we will want to push both main and GitHub pages branches.
Now that you've changed the remote and commit,
create the repository in GitHub, and push your changes and then push to your main branch. We do this
push before gh-pages so "main" becomes the primary branch.

.. code-block:: console

    $ git push origin main

Then you can checkout the gh-pages branch to do the same cleanup and push.
Here is the checkout:

.. code-block:: console

    $ git checkout gh-pages

And how to do the cleanup. This cleanup is easier - just delete the markdown files in ``_library``.

.. code-block:: console

    $ rm -rf _library/*.md

And then commit and push to gh-pages.

.. code-block:: console

    $ git commit -a -s -m 'emptying template registry gh-pages'
    $ git push origin gh-pages

Note that since the main branch will try to checkout gh-pages to generate the docs,
the first documentation build might fail. Don't worry about this - the branch
will exist the second time when you add recipes.

Manually Adding Registry Entries
--------------------------------

.. _getting_started-developer-manual-registry-entries:

Great! Now you have an empty registry on your filesystem that will be pushed to GitHub
to serve as a remote. Make sure you are back on the main branch:

.. code-block:: console

    $ git checkout main

Let's now add some containers! There are two ways to go about this:

 - Manually add a recipe locally, optionally adding discovered executables
 - Use a GitHub action to do the same.

We will start with the manual approach. Here is how to add a container.yaml recipe file,
without any customization for executable discovery:

.. code-block:: console

    $ shpc add docker://vanessa/salad:latest
    Registry entry vanessa/salad was added! Before shpc install, edit:
    /tmp/my-registry/vanessa/salad/container.yaml

You could then edit that file to your liking.

Like for ``shpc update`` :ref:`getting_started-commands-update`, tags are automatically
populated using `crane.ggcr.dev <https://crane.ggcr.dev/ls/quay.io/biocontainers/samtools>`_,
which only returns the 50 latest tags and obviously can only access public images.
If you see a ``crane digest`` error instead of tags, you'll have to populate the tags yourself.

Executables are by default missing. If you want shpc
to discover executables, you'll need to install guts:

.. code-block:: console

    pip install git+https://github.com/singularityhub/guts@main


And then use the provided script to generate the container.yaml (with executables discovered):

.. code-block:: console

    $ python .github/scripts/add_container.py --maintainer "@vsoch" --description "The Vanessa Salad container" --url "https://github.com/vsoch/salad" docker://vanessa/salad:latest

That will generate a container.yaml with executables discovered:

.. code-block:: yaml

    url: https://github.com/vsoch/salad
    maintainer: '@vsoch'
    description: The Vanessa Salad container
    latest:
      latest: sha256:e8302da47e3200915c1d3a9406d9446f04da7244e4995b7135afd2b79d4f63db
    tags:
      latest: sha256:e8302da47e3200915c1d3a9406d9446f04da7244e4995b7135afd2b79d4f63db
    docker: vanessa/salad
    aliases:
      salad: /code/salad


You can then push this to GitHub. If you are curious about how the docs are generated, you can
try it locally:

.. code-block:: console

   $ git checkout gh-pages
   $ ./generate.sh
   Generating docs for vsoch/salad, _library/vsoch-salad.md


There is also an associated workflow to run the same on your behalf. Note that you'll need
to:

1. Go to the ``repository --> Settings --> Actions --> Workflow Permissions`` and enable read and write.
2. Directly under that, check the box to allow actions to open pull requests for this to work.

If you get a message about push being denied to the bot, you forgot to do one of these steps!
The workflow is under ``Actions --> shpc new recipe manual --> Run Workflow``.
Remember that any container, once it goes into the registry, will have tags
and digests automatically updated via the "Update Containers" action workflow.

Creating a Cache
----------------

This is an advanced part of the developer tutorial! Let's say that you don't
want to go through the above to manually run commands. Instead of manually adding entries
in this manner, let's create an automated way to populate
entries from a cache. You can read more about the algorithm we use to derive aliases
in the `shpc-registry-cache <https://github.com/singularityhub/shpc-registry-cache>`_
repository, along with cache generation details. You will primarily need two things:

1. A text listing of containers to add to the cache, ideally automatically generated
2. A workflow that uses it to update your cache.

Both of these files should be in a GitHub repository that you create. E.g.,:

.. code-block:: console

    containers.txt
    .github/
    └── workflows
        └── update-cache.yaml

For the main shpc registry cache linked above, we derive a list of biocontainers.txt
on the fly from the current depot listing. You might do the same for a collection of
interest, or just to try it out, create a small listing of your own containers
in a ``containers.txt`` e.g.,:

.. code-block:: console

    python
    rocker/r-ver
    julia

You can find further dummy examples in the `container-executable-discovery <https://github.com/singularityhub/container-executable-discovery/>`_
repository along with variables that the action accepts. As an example of our
small text file above, we might have:

.. code-block:: yaml

    name: Update Cache

    on:
      workflow_dispatch:
      schedule:
      # Weekly, monday and thursday
      - cron: 0 0 * * 1,4

    jobs:
      update-cache:
        runs-on: ubuntu-latest
        steps:
        - name: Checkout
          uses: actions/checkout@v3

        - name: Update Cache Action
          uses: singularityhub/container-executable-discovery@main
          with:
            token: ${{ secrets.GITHUB_TOKEN }}
            repo-letter-prefix: true
            listing: ./containers.txt
            dry_run: ${{ github.event_name == 'pull_request' }}


And this would use out containers.txt listing to populate the cache in the repository
we've created. Keep in mind that caches are useful beyond Singularity Registry HPC -
knowing the paths and executables within a container is useful for other applied and
research projects too!

Updating a Registry from a Cache
--------------------------------

Once you have a cache, it's fairly easy to use another action provided by shpc
directly from it. This is the :ref:`getting_started-development-github-action` mentioned
above. The full example provided there does two things:

1. Updates your registry from the cache entries
2. Derives an additional listing to add containers that were missed in the cache.

And you will want to put the workflow alongside your newly created registry.
The reason for the second point is that there are reasons we are unable to extract
container binaries to the filesystem. In the case of any kind of failure, we might
not have an entry in the cache, however we still want to add it to our registry!
With the addition of the ``listing`` variable and the step to derive the listing
of BioContainers in the example above, we are still able to add these missing
containers, albeit without aliases. Here is an example just updating
from the cache (no extra listing):


.. code-block:: yaml

    name: Update BioContainers

    on:
      pull_request: []
      schedule:
      - cron: 0 0 1 * *

    jobs:
      auto-scan:
        runs-on: ubuntu-latest
        steps:
        - name: Checkout
          uses: actions/checkout@v3

          # registry defaults to PWD, branch defaults to main
        - name: Update Containers
          uses: singularityhub/singularity-hpc/actions/cache-update@main
          with:
            token: ${{ secrets.GITHUB_TOKEN }}
            # Change this to your cache path
            cache: https://github.com/singularityhub/shpc-registry-cache
            min-count-inclusion: 10
            max-count-inclusion: 1000
            additional-count-inclusion: 25
            # Defaults to shpc docs, this gets formatted to include the entry_name
            url_format_string: "https://biocontainers.pro/tools/%s"
            pull_request: "${{ github.event_name != 'pull_request' }}"


The url format string expects a container identifier somewhere, and feel free
to link to your registry base if you are unable to do this. You will want to change
the ``cache`` to be your remove cache repository, and then adjust the parameters to
your liking:

- **min-count-inclusion**: is the threshold count by which under we include ALL aliases. A rare alias is likely to appear fewer times across all containers.
- **additional-count-inclusion**: an additional number of containers to add after the initial set under ``min-count-inclusion`` is added (defaults to 25)
- **max-count-inclusion**: don't add counts over this threshold (set to 1000 for biocontainers).

Since the cache will generate a global counts.json and skips.json, this means the size of your cache
can influence the aliases chosen. It's recommended to create your entire cache first and then to
add it to your registry to update.
