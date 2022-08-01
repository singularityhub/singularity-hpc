.. _getting_started-use-cases:

=========
Use Cases
=========

Linux Administrator
===================

If you are a linux administrator, you likely want to clone the repository
directly (or use a release when they are available). Then you can install modules
for your users from the local ``registry`` folder, create your own module files
(and contribute them to the repository if they are useful!) and update the
``module_base`` to be where you install modules.

.. code-block:: console

    # an absolute path
    $ shpc config module_base:/opt/lmod/shpc


If you pull or otherwise update the install of shpc, the module files will update
as well. For example, if you start first by seeing what modules are available
to install:

.. code-block:: console

    $ shpc show


And then install a module to your shpc modules directory:

.. code-block:: console

    $ shpc install tensorflow/tensorflow
    Module tensorflow/tensorflow:2.2.2 was created.


Make sure that lmod knows about the folder

.. code-block:: console

    $ module use /opt/lmod/shpc
     
(And likely if you administer an Lmod install you have your preferred way of
doing this). And then you can use your modules just as you would that are provided on
your cluster.

.. code-block:: console

    $ module load tensorflow/tensorflow/2.2.2


You should then be able to use any of the commands that the tensorflow container
provides, e.g., python and python-shell:

.. code-block:: console

    $ python
    Python 3.6.9 (default, Oct 8 2020, 12:12:24) 
    [GCC 8.4.0] on linux
    Type “help”, “copyright”, “credits” or “license” for more information.
    >>> quit()

    $ tensorflow-tensorflow-shell
    ________                _______________         
    ___ __/__________________________________ ____/__ /________   __
    __ / _ _ \_ __ \_ ___/ __ \_ ___/_ /_  __ /_ __ \_ | /| / /
    _ /  / __/ / / /(__ )/ /_/ / /  _ __/  _ / / /_/ /_ |/ |/ / 
    /_/  \___//_/ /_//____/ \____//_/  /_/   /_/ \____/____/|__/
    You are running this container as user with ID 34633 and group 34633,
    which should map to the ID and group for your user on the Docker host. Great!
    Singularity> quit()


If you want to inspect aliases available or singularity commands to debug:

.. code-block:: console

    $ module spider tensorflow/tensorflow/2.2.2/module
    ----------------------------------------------------------------------------------------------------------------------------
     tensorflow/tensorflow/2.2.2: tensorflow/tensorflow/2.2.2/module
    ----------------------------------------------------------------------------------------------------------------------------
      This module can be loaded directly: module load tensorflow/tensorflow/2.2.2/module
      Help:
       This module is a singularity container wrapper for tensorflow/tensorflow v2.2.2
       Commands include:
        - tensorflow-tensorflow-shell:
               singularity shell -s /bin/bash /home/shpc-user/singularity-hpc/modules/tensorflow/tensorflow/2.2.2/tensorflow-tensorflow-2.2.2-sha256:e2cde2bb70055511521d995cba58a28561089dfc443895fd5c66e65bbf33bfc0.sif
        - python:
               singularity exec --nv /home/shpc-user/singularity-hpc/modules/tensorflow/tensorflow/2.2.2/tensorflow-tensorflow-2.2.2-sha256:e2cde2bb70055511521d995cba58a28561089dfc443895fd5c66e65bbf33bfc0.sif /usr/local/bin/python”)



Cluster User
============

If you are a cluster user, you can easily install shpc to your own space
(e.g., in ``$HOME`` or ``$SCRATCH`` where you keep software) and then
use the defaults for the lmod base (the modules folder that is created alongside
the install) and the registry. You can also pull the repository to get updated
registry entries.  If you haven't yet, clone the repository:


.. code-block:: console

    $ git clone git@github.com:singularityhub/singularity-hpc.git
    $ cd singularity-hpc
    
You can then see modules available for install:


.. code-block:: console

    $ shpc show


And install a module to your local modules folder.


.. code-block:: console

    $ shpc install python
    Module python/3.9.2-slim was created.


Finally, you can add the module folder to those that lmod knows about:

.. code-block:: console

    $ module use $HOME/singularity-hpc/modules
     
And then you can use your modules just as you would that are provided on
your cluster.

.. code-block:: console

    $ module load python/3.9.2-slim


An error will typically be printed if there is a conflict with another module name, and it's
up to you to unload the conflicting module(s) and try again. For this module, 
since we didn't use a prefix the container python will be exposed
as "python" - an easier one to see is "python-shell" - each container exposes
a shell command so you can quickly get an interactive shell. 
Every installed entry will have it's named suffixed with "shell" if you quickly want
an interactive session. For example:

.. code-block:: console

    $ python-shell
    Singularity>


And of course running just "python" gives you the Python interpreter. If you
don't know the command that you need, or want to see help for the module you
loaded, just do:

.. code-block:: console

    $ module spider python/3.9.2-slim/module
    ----------------------------------------------------------------------------------------------------------------------------
    python/3.9.2-slim: python/3.9.2-slim/module
    ----------------------------------------------------------------------------------------------------------------------------
      This module can be loaded directly: module load python/3.9.2-slim/module
      Help:
       This module is a singularity container wrapper for python v3.9.2-slim
       Commands include:
        - python-shell:
           singularity shell -s /bin/bash /home/shpc-user/singularity-hpc/modules/python/3.9.2-slim/python-3.9.2-slim-sha256:85ed629e6ff79d0bf796339ea188c863048e9aedbf7f946171266671ee5c04ef.sif
        - python:
           singularity exec /home/shpc-user/singularity-hpc/modules/python/3.9.2-slim/python-3.9.2-slim-sha256:85ed629e6ff79d0bf796339ea188c863048e9aedbf7f946171266671ee5c04ef.sif /usr/local/bin/python”)
    
    
The above not only shows you the description, but also the commands if you
need to debug. If you want to see metadata about the container (e.g., labels,
singularity recipe) then you can do:

.. code-block:: console

    $ module whatis python/3.9.2-slim
    python/3.9.2-slim/module             : Name    : python/3.9.2-slim
    python/3.9.2-slim/module             : Version   : module
    python/3.9.2-slim/module             : URL     : https://hub.docker.com/_/python
    python/3.9.2-slim/module             : Singularity Recipe  : bootstrap: docker 
    from: python@sha256:85ed629e6ff79d0bf796339ea188c863048e9aedbf7f946171266671ee5c04ef
    python/3.9.2-slim/module             : org.label-schema.build-arch  : amd64
    python/3.9.2-slim/module             : org.label-schema.build-date  : Sunday_4_April_2021_19:56:56_PDT
    python/3.9.2-slim/module             : org.label-schema.schema-version  : 1.0
    python/3.9.2-slim/module             : org.label-schema.usage.singularity.deffile.bootstrap  : docker
    python/3.9.2-slim/module             : org.label-schema.usage.singularity.deffile.from  : python@sha256:85ed629e6ff79d0bf796339ea188c863048e9aedbf7f946171266671ee5c04ef
    python/3.9.2-slim/module             : org.label-schema.usage.singularity.version  : 3.7.1-1.el7


If your workflow requires knowledge of the local path to the sif image, this information
can be output by using the "container" suffixed alias:

.. code-block:: console

    $ python-container
    /home/shpc-user/singularity-hpc/modules/python/3.9.2-slim/python-3.9.2-slim-sha256:85ed629e6ff79d0bf796339ea188c863048e9aedbf7f946171266671ee5c04ef.sif

or equivalently by accessing the value of the **SINGULARITY_CONTAINER** environment variable (or **PODMAN_CONTAINER** for each of Podman and Docker).


Adding Options
--------------

By default, some of the commands will come with singularity options. For example,
a container intended for gpu will have a features: gpu set to true, and this will add the ``--nv`` flag given that the user or cluster settings file has that feature enabled. However,
it could be the case that you want to define custom options at the time of use.
In this case, you can export the following custom environment variables to add them:

**SINGULARITY_OPTS**: will provide additional options to the base Singularity command, such as ``--debug``  
**SINGULARITY_COMMAND_OPTS**: will provide additional options to the command (e.g., exec), such as ``--cleanenv`` or ``--nv``.  


Custom Images that are Added
============================

If you add a custom image, the interaction is similar, whether you are a cluster
user or administrator. First, let's say we pull a container:

.. code-block:: console

    $ singularity pull docker://vanessa/salad
    
And we add it to our unique namespace in the modules folder:

.. code-block:: console

    $ shpc add salad_latest.sif vanessa/salad:latest
    
    
We can again load the custom module:

.. code-block:: console

    $ module load vanessa/salad/latest


Since we didn't define any aliases via a registry entry, the defaults provided
are to run the container (the squashed unique resource identifier, ``vanessa-salad-latest``
or the same shell, ``vanessa-salad-latest-shell``. Of course you can check this if you don't know:

.. code-block:: console

    $ module spider vanessa/salad/latest/module 
    --------------------------------------------------------------------------------------------------------------------------------------------------------
     vanessa/salad/latest: vanessa/salad/latest/module
    --------------------------------------------------------------------------------------------------------------------------------------------------------
      This module can be loaded directly: module load vanessa/salad/latest/module
      Help:
       This module is a singularity container wrapper for vanessa-salad-latest vNone
       Commands include:
        - vanessa-salad-latest-shell:
           singularity shell -s /bin/bash /home/shpc-user/singularity-hpc/modules/vanessa/salad/latest/vanessa-salad-latest-sha256:71d1f3e42c1ceee9c02295577c9c6dfba4f011d9b8bce82ebdbb6c187b784b35.sif
        - vanessa-salad-latest: singularity run /home/shpc-user/singularity-hpc/modules/vanessa/salad/latest/vanessa-salad-latest-sha256:71d1f3e42c1ceee9c02295577c9c6dfba4f011d9b8bce82ebdbb6c187b784b35.sif


And then use them! For example, the command without ``-shell`` just runs the container:

.. code-block:: console

    $ vanessa-salad-latest
     You think you have problems? I’m a fork.  
                /\
               //\\
               // \\
             ^  \\ //  ^
            / \  ) (  / \ 
            ) (  ) (  ) (
            \ \_/ /\ \_/ /
             \__ _)(_ __/
              \ \ / /
               ) \/ (
               | /\ |
               | )( |
               | )( |
               | \/ |
               )____(
              /   \
              \______/ 


And the command with shell does exactly that.

.. code-block:: console

    $ vanessa-salad-latest-shell
    Singularity> exit

If you need more robust commands than that, it's recommended to define your
own registry entry. If you think it might be useful to others, please contribute it
to the repository!


Pull Singularity Images
=======================

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
