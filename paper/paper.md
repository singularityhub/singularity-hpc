---
title: 'Collaborative Container Modules with Singularity Registry HPC'
tags:
  - containers
  - singularity
  - linux
  - registry
authors:
 - name: Vanessa Sochat
   orcid: 0000-0002-4387-3819
   affiliation: 1
 - name: Alec Scott
   orcid: 0000-0001-6255-1308
   affiliation: 2
affiliations:
 - name: Lawrence Livermore National Lab
   index: 1
 - name: University of Arizona Research Computing
   index: 2
date: 17 April 2021
bibliography: paper.bib
---

# Summary

Singularity Registry HPC, "shpc" (https://singularity-hpc.readthedocs.io/), is a collaborative framework to easily provide containers as modules for high performance computing (HPC) centers.
Whether you are a user or a cluster administrator, installing the software
gives you an easy means to install Singularity containers [@Kurtzer2017-xj] as
environment modules [@McLay2011-wu]. Unlike registry servers [@SRegistry] that expect a user to pull a container directly, shpc provides a simple command line client to manage 
this interaction for you, and make container commands easily available
as command line aliases. With over 150 containers readily avilable
from biocontainers [@da2017biocontainers] to Nvidia's Container Catalog [@noauthor_undated-kp] 
to brain imaging data structure apps [@gorgolewski2017bids], to core containers
on Docker Hub [@noauthor_undated-xn], and software from package managers like Spack [@gamblin2015spack] made available via the Autamus registry [@autamus], with just a few clicks you can quickly assemble your own collection of custom containers modules for yourself or your user base.


## Background

Using environment modules on high performance computing clusters is a common
trend. Although writing the recipes can be complex and beyond the ability of the scientific
user, it's a fairly common practice for cluster administrators to provide
a set of natively installed recipes for their users [@noauthor_undated-bt]. The practice is so common
that it's relatively easy to find repositories of lua files, a format for the popular module system LMOD [@McLay2011-wu], shared in version control (e.g., https://github.com/OSGConnect/modulefiles), or even generation of module files with well-known package managers like Spack [@noauthor_undated-ae] and EasyBuild [@noauthor_undated-dj]. Using containers in this context is also not a novel idea [@noauthor_undated-rc], and has been discussed previously [@noauthor_undated-rj]. However, the majority of these approaches and tools do not make the process of installing container modules easy. They either require a root user to build, writing complex recipes, or using a less-than-simple command line interface. The package manager approaches require relying on some subset of system software, the underlying operating system, or even making changes to the system. Using Singularity containers, although it requires the Singularity software, places relatively no limitation on what can be installed. Further, unlike traditional environment modules, a container as a module
requires no other dependencies, ensuring consistency in usage and fewer conflicts.

Whether the user is an administrator or a researcher, installing shpc is as easy as cloning the repository and using Python or pip to install in place:

```bash
$ git clone https://github.com/singularityhub/singularity-hpc
$ cd singularity-hpc

# install with pip
$ pip install -e .

# or with Python setuptools
% python setup.py develop
```

Although it's possible to install the software alongside other Python site packages, e.g.,
meaning either of these commands:

```bash
$ python setup.py install
$ pip install .
```

a local or development install is recommended to make it easy to retrieve updated recipes
from the registry on GitHub via a simple `git pull.`
While the defaults are suitable for most, there are three locations that 
can be customized, including the registry of container recipes, the module directory to which modules are installed, and the directory to which containers are installed. This
is done simply with `shpc config`:

```bash
$ shpc config lmod_base:/my/custom/path/modules
$ shpc config registry:/my/private/registry
$ shpc config container_base:/my/separate/containers
```

By default, containers are installed alongside the respective modules,
but as shown above, this can be changed. 
Users that don't want to interact with the shpc client to update settings can
open the "settings.yml" file directly, which is included in the repository.
The user can then use `shpc show` to see readily available recipes, or browse the [library](https://singularityhub.github.io/singularity-hpc/) for an easily searchable interface. Installation comes down to installing a chosen module, loading it, and using it:

```bash
$ shpc install biocontainers/samtools
$ module load biocontainers/samtools
$ samtools
```

While a user might need to add a new module directory for LMOD to find with 
`module use`, a cluster administrator would likely have modules loaded automatically for the user
via a bash profile. With the `module load` command, the researcher is empowered to add their own custom installation directory of modules that might not be available from their system administrators.

The container can then be loaded, and is then available as an exposed set of 
shell aliases that look like simple executable commands:

```bash
$ module load biocontainers/samtools
$ samtools
```

Although the command is provided as simply "samtools," in reality shpc is
providing an alias to a more complex interaction with the container, and importantly,
one that the user does not need to manually figure out. This is done
via a reproducible and easy-to-use registry, discussed next.


## Reproducible Science

Containers allow for encapsulation of an entire software package, including
everything from the libraries to the underlying operating system. By pinning
an exact version of a scientific software stack provided in a container,
exposed as a set of module commands, researchers on high performance computing
clusters can have more confidence in the reproducibility of their work [@Santana-Perez2015-wo, @Boettiger2014-cz, @Wandell2015-yt]. Importantly, while interacting with a container is generally complicated as the user needs to know some of the underlying structure of the container and
the command(s) to run, Singularity Registry HPC recipes
expose a set of shell aliases that are easy to understand and use for any container.
For example, when using the `biocontainers/samtools` container via Singularity, 
a user might typically need to pull the container:

```bash
$ singularity pull docker://biocontainers/samtools:v1.9-4-deb_cv1
```

manually run a command to interact with it:

```bash
# interact with samtools, without knowing the entrypoint
$ singularity run samtools_latest.sif 
```

Note that the user has no easy way, aside from looking at the original recipe
to build the container or shelling inside to inspect, what the run command will do.
Also note that the user needs to find a particular version on Docker Hub (the tag digest
represented as "v1.9-4-deb_cv1") which unfortunately is a moving target -- if the user
were to pull this container again, it might have changed. Ideally, the user
would choose an actual digest that is associated with an exact container:

```bash
$ digest=sha256:da61624fda230e94867c9429ca1112e1e77c24e500b52dfc84eaf2f5820b4a2a
$ singularity pull docker://biocontainers/samtools@${digest}
```

However, in practice this is not common, as it requires extra clicks and knowledge
about container registries that the average user is unlikely to have, or just not
have the time to think about. In the case that the user understands the underlying
structure of the container, they need to execute a command to the container to use it:

```bash
# interact with samtools
$ singularity exec samtools_latest.sif /usr/bin/samtools
```

The user may not know the path to the desired executable in advance, and need to
spend extra time exploring the container. This is no small task, as containers typically
differ in where some set of primary binaries are installed. Ideally, as shown above,
 the user would provide a full path so that samtools in the container is used.  Not using a full path can lead to unexpected consequences. Since Singularity containers
have a seamless environent with the host, it could be possible to 
actually hit a version of "samtools" available outside of the container on the user's
path. Instead of this complex workflow, Singularity Registry HPC makes it much easier.
After finding the `biocontainers/samtools` container via the library web interface
or the command line client, the user simply installs it:

```bash
$ shpc install biocontainers/samtools
...
Module biocontainers-samtools/v1.9-4-deb_cv1 was created.
```

Installing includes generation of a module file from the registry recipe,
a simple `container.yaml` file with basic metadata and description,
that exposes any and all important entrypoints, and pulls an exact hash of a container.
The user does not need to look in advance for a version if they want the latest provided
by the registry. More realistically, a cluster administrator will install some subset of versions
that are available to the user, and they can be discovered with environment
module search:

```bash
$ module spider samtools
------------------------------------------------------------------------------
  biocontainers/samtools/v1.9-4-deb_cv1: biocontainers/samtools/v1.9-4-deb_cv1
------------------------------------------------------------------------------

    This module can be loaded directly: 
    module load biocontainers/samtools/v1.9-4-deb_cv1/module

    Help:
      This module is a singularity container wrapper for
      biocontainers/samtools vv1.9-4-deb_cv1 Samtools is a suite of 
      programs for interacting with high-throughput sequencing data.
      
...
      
      Commands include:
      
       - biocontainers-samtools-run:
             singularity run <container>
       - biocontainers-samtools-shell:
             singularity shell -s /bin/bash <container>
       - biocontainers-samtools-exec:
             singularity exec -s /bin/bash <container> "$@"
       - biocontainers-samtools-inspect-runscript:
             singularity inspect -r <container>
       - biocontainers-samtools-inspect-deffile:
             singularity inspect -d <container>

       - samtools:
             singularity exec <container> /usr/bin/samtools
            
```

Notice that every module includes a help section with a description, 
a complete list of commands that map to interactions with the container,
and (not shown) a list of environment variables also available. 
Importantly, the module system provides command line completion, so the user can
use tabs to autocomplete the module names:

```bash
$ module load biocontainers/samtools/v1.9-4-deb_cv1
```

And then all the commands to shell, execute a custom command, or simply to use samtools
are available, also with autocomplete, for the user. Instead of needing to 
write these commands manually, a single alias can be used:

```bash
$ biocontainer-samtools-run
$ biocontainer-samtools-shell
$ biocontainer-samtools-exec echo "Hello World"
```

Even inspecting metadata, which typically requires another more complex
command, is easy. With tab autocompletion, it's easy to inspect the runscript
or entire container recipe for any container:

```bash
$ biocontainers-samtools-inspect-runscript
$ biocontainers-samtools-inspect-deffile
```

Finally, the core software in the container is also exposed as one or more aliases.
In the case of samtools, the samtools executable is likely desired:

```bash
$ samtools --help
Program: samtools (Tools for alignments in the SAM format)
Version: 1.9 (using htslib 1.9)

Usage:   samtools <command> [options]

Commands:
  -- Indexing
...
```

Another compelling example is using a notebook provided by Jupyter Stacks [@cook2017opinionated]. 
Running notebooks that can be exposed via networking ports tends to be very complicated.
A full interaction might look like the following:

```bash
# pull the latest container, a moving target
$ singularity pull docker://jupyter/minimal-notebook

$ singularity exec --home ${HOME} --bind ${HOME}/.local:/home/joyvan/.local \
   minimal-notebook_latest.sif \
   jupyter notebook --no-browser --port=12345 --ip 0.0.0.0
```

With Singularity Registry HPC, the interaction to run the notebook can be figured
out and written down once, and provided as a community recipe. In this case, it's
exposed as the command "run-notebook":

```bash
$ run-notebook

I 12:01:45.417 NotebookApp] Use Control-C to stop this server and shut ...
[C 12:01:45.421 NotebookApp] 
    
    To access the notebook, open this file in a browser:
    ...
    Or copy and paste one of these URLs:
    ...
```

which automatically selects a random port, binds the expected directories, and 
gets the user up and running quickly. A more advanced user could inspect help for the module
to get the full command and container path, and then edit it as desired, or export
a subset of environment variables to change behavior. Since Singularity tends
to be seamless with the host environment, common filesystem locations such as
temporary locations, the user's home directory, and other work locations are automatically
bound to the container, and arguments or options are passed to the different alias entrypoints. 
The administrator can easily provide an example of loading and running this command as an interactive job, and then connecting to the exposed ports. 

The above discussion only covers two of the over 160 containers that have been carefully crafted for ease of use. The open source, collaborative nature of this registry is discussed next.


## Collaborative, Automated Recipes

Adding a container to the registry is as simple as creating a yaml file in
the registry directory of the repository, organized by the container unique resource
identifier. The file also includes the container unique resource identifer
(e.g., a container on Docker Hub or another registry), and then a tag 
for the latest, and any other desired tags. If only a subset of tags are desired
to be automatically discovered during a recipe update, the recipe writer can
provide a filter to limit this set. A description and url is added for
updating the [library](https://singularityhub.github.io/singularity-hpc/),
and importantly, the creator then defines a set of aliases to expose to the user.
The default alias for shell, exec, run, and inspect are generated automatically
when a user installs the module, so if the container has only one entrypoint exposed with run,
no further work is needed. The recipes are collaborative in nature because anyone
can open a pull request with a new recipe, or request a container be added by opening
an issue. Automation also ensures that adding new containers, or working on the
code base is easy. Tests are run automatically for the software, and when adding
a new container, a maintainer simply needs to apply a `container-recipe` label
to trigger a workflow that discovers the new recipe, and tests installing the
container. Once a container is added, no further work is needed to update
versions for it. By way of a GitHub bot named Binoc (short for "binoculars"),
[@noauthor_undated-eh] both the latest version and newly available tags are 
updated automatically, following any filters that the recipe creator has provided for which tags should be added. Finally, on merge to the main branch, the documentation and library
are also automatically updated.

## Conclusion

Singularity Registry HPC makes it immensely easy to install containers as modules,
not just for an administrator, but also for a researcher. It is the first tool
of its kind to focus explicitly on containers installed as modules, and provide
not just a community collection of recipes, but also robust documentation, a library
interface, automation, and easy extendibility. As long as modules and containers
are used on HPC, it should be of interest to the larger scientific and high
performance computing communities.

While the Singularity software is currently popular for running containers on HPC,
it might not always be that way. Although LMOD [@McLay2011-wu] is the most popular
module system currently, there are several older versions such as environment modules [@environment_modules] and cmod [@noauthor_undated-jo] that could be supported on
user request, and it could be the case that new module systems arise. 
For this reason, Singularity Registry HPC is designed in a modular
fashion. There is already support for containers served in a traditional registry like
Docker Hub, or served as GitHub releases generated by Singularity Deploy [@noauthor_undated-ok],
and the software is designed to make it easy to extend to other container
technologies or module systems. You can read more about Singularity Registry HPC
on the GitHub repository (https://github.com/singularityhub/singularity-hpc) or
the main documentation site (https://singularity-hpc.readthedocs.io).

# References
