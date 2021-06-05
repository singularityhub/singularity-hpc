.. _manual-main:

==========================
Singularity Registry (HPC)
==========================

.. image:: https://img.shields.io/github/stars/singularityhub/singularity-hpc?style=social
    :alt: GitHub stars
    :target: https://github.com/singularityhub/singularity-hpc/stargazers



Singularity Registry HPC (shpc) is based off of the `Singularity Registry Client <https://github.com/singularityhub/sregistry-cli>`_, but instead of
being intended for general interaction with Singularity containers and a local database, it's optimized for managing containers
in an HPC environment. Currently, this includes:

 - `LMOD <https://lmod.readthedocs.io/en/latest/>`_

You can use shpc if you are:

1. a linux administrator wanting to manage containers as modules for your cluster
2. a cluster user that wants to maintain your own folder of custom modules
3. a cluster user that simply wants to pull Singularity images as GitHub packages.

The library contains a collection of module recipes that will install containers,
so you can easily use them or write your own. 
To see the code, head over to the `repository <https://github.com/singularityhub/singularity-hpc/>`_.
To browse modules available as containers, see `the library <https://singularityhub.github.io/singularity-hpc/>`_.


.. _main-getting-started:

-----------------------------------------------
Getting started with Singularity Registry (HPC)
-----------------------------------------------

Singularity Registry HPC (shpc) can be installed from pypi or directly from the repository. See :ref:`getting_started-installation` for
installation, and then the :ref:`getting-started` section for using the client.
You can browse modules available at the `Singularity HPC Library <https://singularityhub.github.io/singularity-hpc/>`_.

.. _main-support:

-------
Support
-------

* For **bugs and feature requests**, please use the `issue tracker <https://github.com/singularityhub/singularity-hpc/issues>`_.
* For **contributions**, visit Caliper on `Github <https://github.com/singularityhub/singularity-hpc>`_.

---------
Resources
---------

`GitHub Repository <https://github.com/singularityhub/singularity-hpc>`_
    The code for shpc on GitHub.

`Singularity HPC Library <https://github.com/singularityhub/singularity-hpc/issues>`_
    Shows modules available to install as containers.

`Autamus Registry <https://autamus.io>`_
    Provides many of the shpc container modules, built directly from spack.


.. toctree::
   :caption: Getting started
   :name: getting_started
   :hidden:
   :maxdepth: 2

   getting_started/index

.. toctree::
    :caption: API Reference
    :name: api-reference
    :hidden:
    :maxdepth: 1

    api_reference/shpc
    api_reference/internal/modules
