---
title: 'Collaborative Container Modules with Singularity Registry HPC (shpc)'
tags:
  - containers
  - singularity
  - linux
  - registry
authors:
 - name: Vanessa Sochat
   orcid: 0000-0002-4387-3819
   affiliation: 1
affiliations:
 - name: Lawrence Livermore National Lab
   index: 1
date: 17 April 2021
bibliography: paper.bib
---

# Summary

Singularity Registry HPC is a collaborative framework to easily provide
containers as modules for high performance computing (HPC) centers.
Whether you are a user or a cluster administrator, installing the software
gives you an easy means to install Singularity containers [@Kurtzer2017-xj] as
environment modules [@environment_modules]. With over 150 containers readily avilable
from biocontainers [@da2017biocontainers] to Nvidia's Container Catalog [@noauthor_undated-kp] 
to brain imaging data structure apps [@gorgolewski2017bids], to core containers
on Docker Hub [@noauthor_undated-xn], and software from [@gamblin2015spack] made available via the Autamus registry [@autamus], with just a few clicks you quickly can assemble your own collection of custom containers modules for yourself or your user base.


## Background

Using environment modules on high performance computing clusters is a common
trend. Although writing the recipes can be complex and beyond the ability of the scientific
user, it's a fairly common practice for cluster administrators to provide
a set of natively installed recipes for their users. The practice is so common
that it's fairly easy to find repositories of lua files shared in version control (e.g., https://github.com/OSGConnect/modulefiles), or even generation of module files with well known package managers [@noauthor_undated-dj, @noauthor_undated-ae]. Using containers in this context is also not a novel idea [@noauthor_undated-rc, @noauthor_undated-r]. However, the majority of these approaches and tools do not make the process of installing container modules easy. They either require a root
user to build, writing complex recipes, or using a less than simple command line interface.
The package manager approaches require relying on some subset of system software, the
underlying operating system, or even making changes to the system. Using Singularity containers, although it requires the Singularity software, places no limitation on what can be installed.

Whether the user is an administrator or a researcher, installing Singularity HPC (shpc) is as easy as cloning the repository and using Python or pip to install in place:

```bash
git clone https://github.com/singularityhub/singularity-hpc
cd singularity-hpc
pip install -e .
```

While the defaults are suitable for most, there are three locations that 
can be customized, including the registry of container recipes, the module directory to which modules are installed, and the directory to which containers are installed. By default, containers
are installed alongside the respective modules. The user can then use `shpc show` to see readily
available recipes, or browse the [library](https://singularityhub.github.io/singularity-hpc/) for an easily searchable interface. Installation comes down to then installing a chosen module:

```bash
$ shpc install biocontainers/samtools
```

And then telling the environment modules software to use the shpc modules directory,
which defaults to `modules` in the repository. A cluster administrator would do
this for the user base, so the researcher does not have to. However, a researcher
is still empowered to add their own custom intallation directory of modules.

```bash
$ module use ./modules
```

The container can then be loaded, and is then available as an exposed set of 
shell aliases that look like simple executable commands:

```bash
$ module load biocontainers/samtools
$ samtools
```

Although the command is provided as simply samtools, in reality shpc is
providing an alias to a more complex interaction with the container, and importantly,
one that the user does not need to manually figure out. This is done
via a reproducible and easy to use registry, discussed next.


## Reproducible Science

Containers allow for encapsulation of an entire software package, including
everything from the libraries to the underlying operating system. By pinning
an exact version of a scientific software stack provided in a container and
exposed as a set of module commands, researchers on high performance computing
clusters can have more confidence in the reproducibility of their work.
Importantly, while interacting with a container is generally complicated
as the user needs to know the command to run, Singularity Registry HPC recipes
expose a set of shell aliases that are easy to understand and use for any container.
For example, when using the `biocontainers/samtools` container via Singularity, 
a user might typically need to pull the container, and then manually run any one 
of these commands to interact with it:

```bash
$ singularity pull docker://biocontainers/samtools:v1.9-4-deb_cv1
```

Note that the user needs to find a particular version on Docker Hub (the tag digest
represented as `v1.9-4-deb_cv1`) which unfortunately is a moving target - if the user
were to pull this container again, it might have changed. More ideally, the user
would choose an actual digest that is associated with an exact container:

```bash
$ singularity pull docker://biocontainers/samtools@sha256:da61624fda230e94867c9429ca1112e1e77c24e500b52dfc84eaf2f5820b4a2a
```

However in practice this is not common, as it requires extra clicks and knowledge
about container registries that the average user is unlikely to have.
The user then needs to execute a command to the container to use it:

```bash
# interact with samtools
$ singularity exec samtools_latest.sif /usr/bin/samtools
```

Notice that if the container does not provide its main software added to the path, the user
would need to shell inside and find it first, and ideally provide a full path so
that samtools in the container is used. This is no small task, as containers typically
differ in where some set of primary binaries are installed. Not using a full path
can lead to unexpected consequences. Since Singularity containers
have a seamless environent with the host, it could be possible, given an exec
of a general `samtools`, to actually hit a version outside the container on the user's
path. Instead of this complex workflow, Singularity Registry HPC makes it much easier.
After finding the `biocontainers/samtools` container via the library web interface
or the command line client, the user simply installs it.

```bash
$ shpc install biocontainers/samtools
...
Module biocontainers-samtools/v1.9-4-deb_cv1 was created.
```

Installing includes generation of a module file from the registry recipe
that exposes any and all important entrypoints, and pulls an exact hash of a container.
The user does not need to look in advance for a version if they are agnostic.
More realistically, a cluster administrator will install some subset of versions
that are available to the user, and then they can be discovered with environment
module search:

```bash
$ module spider samtools
------------------------------------------------------------------------------------------------------------------------------------------
  biocontainers/samtools/v1.9-4-deb_cv1: biocontainers/samtools/v1.9-4-deb_cv1/module
------------------------------------------------------------------------------------------------------------------------------------------

    This module can be loaded directly: module load biocontainers/samtools/v1.9-4-deb_cv1/module

    Help:
      This module is a singularity container wrapper for biocontainers/samtools vv1.9-4-deb_cv1
      Samtools is a suite of programs for interacting with high-throughput sequencing data.
      
      Container:
      
       - /code/modules/biocontainers/samtools/v1.9-4-deb_cv1/biocontainers-samtools-v1.9-4-deb_cv1-sha256:da61624fda230e94867c9429ca1112e1e77c24e500b52dfc84eaf2f5820b4a2a.sif
      
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
      
      
      For each of the above, you can export:
      
       - SINGULARITY_OPTS: to define custom options for singularity (e.g., --debug)
       - SINGULARITY_COMMAND_OPTS: to define custom options for the command (e.g., -b)
```

Importantly, the module system provides command line completion, so the user can
use tabs to autocomplete the load line:

```bash
$ module load biocontainers/samtools/v1.9-4-deb_cv1
```

And then all the commands to shell, run a custom exec, or simply use samtools
are available, also with autocomplete, for the user. Instead of needing to 
write a complex shell, exec, or run command using Singularity, a single
alias can be used:

```bash
$ biocontainer-samtools-run
$ biocontainer-samtools-shell
$ biocontainer-samtools-exec echo "Hello World"
```

Even inspecting metadata, which typically requires another more complex
command, is easy. With a tab autocompletion, it's easy to inspect the runscript
or entire container recipe for any container:

```bash
$ biocontainers-samtools-inspect-runscript
$ biocontainers-samtools-inspect-deffile
```

Finally, the core software in the container is also exposed as one or more aliase.s
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

$ singularity exec --home ${HOME} --bind ${HOME}/.local:/home/joyvan/.local minimal-notebook_latest.sif jupyter notebook --no-browser --port=12345 --ip 0.0.0.0
```

With Singularity Registry HPC, the interaction to run the notebook can be figured
out and written down once, and provided as a community recipe. In this case, it's
exposed as `run-notebook`:

```bash
$ run-notebook

I 12:01:45.417 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[C 12:01:45.421 NotebookApp] 
    
    To access the notebook, open this file in a browser:
        file:///home/vanessa/.local/share/jupyter/runtime/nbserver-1805124-open.html
    Or copy and paste one of these URLs:
        http://vanessa-ThinkPad-T490s:26253/?token=3b022fdfc193e22993e2623c0a191f4fc87f7a3bae7909ec
     or http://127.0.0.1:26253/?token=3b022fdfc193e22993e2623c0a191f4fc87f7a3bae7909ec
```

which automatically selects a random port, binds the expected directories, and 
gets the user up and running quickly. The administrator could easily provide
an example of loading and running this command as an interactive job, and then
connecting to the exposed ports. The above discussion only covers two of the over
160 containers that have been carefully crafted for ease of use. The open source,
collaborative nature of this registry is discussed next.


## Collaborative, Automated Recipes

Adding a container to the registry is as simple as creating a yaml file in
the registry folder. The file includes the container unique resource identifer
(e.g., a container on Docker Hub or another registry), and then a tag 
for the latest, and any other desired tags. A description and url is added for
updating the [library](https://singularityhub.github.io/singularity-hpc/),
and importantly, the creator then defines a set of aliases to expose to the user.
The default alias for shell, exec, run, and inspect will be generated automatically
for the module, so if the container has only one entrypoint exposed with run,
no further work is needed. The recipes are collaborative in nature because anyone
can open a pull request with a new recipe, or request a container be added by opening
an issue. Automation also ensures that adding new containers, or working on the
code base, is easy. Tests are run automatically for the software, and when adding
a new container, a maintainer simply needs to apply a `container-recipe` label
to trigger a workflow that discovers the new recipe, and tests installing the
container. On merge to the main branch, the documentation and library
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
it might not always be that way. It could also be the case that different module
systems arise. For this purpose, Singularity Registry HPC is designed in a modular
fashion. There is already support for containers served in a traditional registry like
Docker Hub, or served as GitHub releases generated by Singularity Deploy [@noauthor_undated-ok],
and the software is designed to make it easy to extend to other container
technologies or module systems.

# References
