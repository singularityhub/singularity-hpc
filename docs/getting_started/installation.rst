.. _getting_started-installation:

============
Installation
============

Singularity Registry HPC (shpc) can be installed from pypi, or from source. For either, it's
recommended that you create a virtual environment, if you have not already
done so.


Virtual Environment
===================

The recommended approach is to install from the repository directly, whether
you use pip or another setup approach, and to install a `known release <https://github.com/singularityhub/singularity-hpc/releases/>`_. Here is how to clone the repository and do a local install.

.. code:: console

    # Install release 0.0.24
    $ git clone -b 0.0.24 git@github.com:singularityhub/singularity-hpc
    $ cd singularity-hpc
    $ pip install -e .[all]

or (an example with python setuptools and installing from the main branch)

.. code:: console

    $ git clone git@github.com:singularityhub/singularity-hpc
    $ cd singularity-hpc
    $ python setup.py develop


if you install to a system python, meaning either of these commands:

.. code:: console

    $ python setup.py install
    $ pip install .

You will need to put the registry files elsewhere (update the ``registry`` config argument to the path), as they will not be installed
alongside the package. The same is the case for modules - if you install to system
python it's recommended to define ``lmod_base`` as something else, unless you
can write to your install location. Installing locally ensures that you
can easily store your module files along with the install (the default until you
change it). Installation of singularity-hpc adds an executable, `shpc` to your path.

```bash
$ which shpc
/opt/conda/bin/shpc
```

This executable should be accessible by an administrator, or anyone that you want
to be able to manage containers. Your user base will be interacting with your
containers via LMOD, so they do not need access to `shpc`. 
If you are a user creating your own folder of modules, you can add them
to your module path.

Once it's installed, you should be able to inspect the client!


.. code-block:: console

    $ shpc --help


You'll next want to configure and create your registry, discussed next in
 :ref:`getting-started`. Generally, remember that your modules will be installed in
 the ``modules`` folder, and container recipes are nested in ``registry``. If you don't
 want your container images (sif files) installed alongside your module recipes,
 then you can define ``container_base`` to be somewhere else. You
 can change these easily with ``shpc config``, as they are defined via these
 variables in the config:
 

.. code-block:: console
 

    $ shpc config set registry:/<DIR>
    $ shpc config set lmod_base:/<DIR> 
    $ shpc config set container_base:/<DIR> 


You can also easily (manually) update any settings in the ``shpc/settings.yaml`` file. 
Again, see the :ref:`getting-started` pages for next steps for setup and configuration,
and interacting with your modules.

.. warning::

    You must have your container technology of choice installed and on your $PATH
    to install container modules.
     

Environment Modules
-------------------

If you are using `environment modules (tcl) <http://modules.sourceforge.net/>`_
and you find that your aliases do not expand, you can use `shopt <https://www.gnu.org/software/bash/manual/html_node/The-Shopt-Builtin.html>`_ to fix this issue:

.. code-block:: console

    $ shopt expand_aliases || true
    $ shopt -s expand_aliases


Pypi
====

The module is available in pypi as `singularity-hpc <https://pypi.org/project/singularity-hpc/>`_,
and this is primarily to have a consistent means for release, and an interface to show the package. Since the registry
files will not install and you would need to change the registry path
and module base (making it hard to update from the git remote) we do not
encourage you to install from pip unless you know exactly what you are doing.
