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
``lmod_base`` to be where you install modules.

.. code-block:: console

    # an absolute path
    $ shpc config lmod_base:/opt/lmod/shpc


If you pull or otherwise update the install of shpc, the module files will update
as well. A more detailed tutorial will be written when the library is more
fully developed.

Cluster User
============

If you are a cluster user, you can easily install shpc to your own space
(e.g., in ``$HOME`` or ``$SCRATCH`` where you keep software) and then
use the defaults for the lmod base (the modules folder that is created alongside
the install) and the registry. You can also pull the repository to get updated
registry entries. Once you have cloned:


.. code-block:: console

    $ git clone git@github.com:singularityhub/singularity-hpc.git
    $ cd singularity-hpc
    
You can then see modules available for install:


.. code-block:: console

    $ shpc list


And install a module to your local modules folder.


.. code-block:: console

    $ shpc install python


Finally, you can add the module folder to those that lmod knows about:

.. code-block:: console

    $ module use $HOME/singularity-hpc/modules
     
And then you can use your modules just as you would that are provided on
your cluster.

.. code-block:: console

    $ module load python/3.9.2-slim



Pull Singularity Images
=======================

shpc will also provide a means to build a singularity container via CI, keep
it in GitHub packages, and then pull. This feature is not yet developed. 
