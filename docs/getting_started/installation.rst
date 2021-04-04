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
you use pip or another setup approach. Here is how to clone the repository 
and do a local install.

.. code:: console

    $ git clone git@github.com:singularityhub/singularity-hpc
    $ cd singularity-hpc
    $ pip install -e .[all]

or

.. code:: console

    $ git clone git@github.com:singularityhub/singularity-hpc
    $ cd singularity-hpc
    $ python setup.py install


You can then easily store your module files along with the install (the default until you
change it).


Install via pip
===============

However, you can also install shpc via Pypi (when it is available). If you 
install it to a system python or conda environment you will need write access
to the folder to update settings (this is done intentionally so only an admin
or owner of the Python environment can change them) 

.. code:: console

    $ pip install singularity-hpc[all]


And you will also need to change the default module path, unless you
can write to the install directory and want to still store your modules there.
Installation of singularity-hpc adds an executable, `shpc` to your path.

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


.. code:: console

    $ shpc --help

You'll want to configure and create your registry, discussed next in
 :ref:`getting-started`.
