# Singularity Registry HPC (shpc)

[![GitHub actions status](https://github.com/singularityhub/singularity-hpc/workflows/singularity-hpc/badge.svg?branch=main)](https://github.com/singularityhub/singularity-hpc/actions?query=branch%3Amain+workflow%3Asingularity-hpc)
[![DOI](https://zenodo.org/badge/354130612.svg)](https://zenodo.org/badge/latestdoi/354130612)
[![DOI](https://joss.theoj.org/papers/10.21105/joss.03311/status.svg)](https://doi.org/10.21105/joss.03311)


![https://raw.githubusercontent.com/singularityhub/singularity-hpc/main/docs/assets/img/shpc.png](https://raw.githubusercontent.com/singularityhub/singularity-hpc/main/docs/assets/img/shpc.png)

Singularity HPC is optimized for managing containers in an HPC environment. Currently, this includes
module technologies:

 - [Lmod](https://lmod.readthedocs.io/en/latest/)
 - [Environment Modules](http://modules.sourceforge.net/)

And container technologies:

 - [Singularity](https://github.com/sylabs/singularity)
 - [Podman](https://podman.io)
 - [Docker](https://docker.io)


You can use shpc if you are:

1. a linux administrator wanting to manage containers as modules for your cluster
2. a cluster user that wants to maintain your own folder of custom modules
3. a cluster user that simply wants to pull Singularity images as GitHub packages.

A module technology is required in all cases.

📖️ Read the [documentation](https://singularity-hpc.readthedocs.io/en/latest/) 📖️
⭐️ Browse the [container module collection](https://singularityhub.github.io/singularity-hpc/) ⭐️
 
## 😁️ Contributors 😁️

We use the [all-contributors](https://github.com/all-contributors/all-contributors) 
tool to generate a contributors graphic below.

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://vsoch.github.io"><img src="https://avatars.githubusercontent.com/u/814322?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Vanessasaurus</b></sub></a><br /><a href="https://github.com/singularityhub/singularity-hpc/commits?author=vsoch" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/danielskatz"><img src="https://avatars.githubusercontent.com/u/2913845?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Daniel S. Katz</b></sub></a><br /><a href="https://github.com/singularityhub/singularity-hpc/commits?author=danielskatz" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/audreystott"><img src="https://avatars.githubusercontent.com/u/43943628?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Audrey Stott</b></sub></a><br /><a href="https://github.com/singularityhub/singularity-hpc/commits?author=audreystott" title="Code">💻</a></td>
    <td align="center"><a href="alecbcs.com"><img src="https://avatars.githubusercontent.com/u/19558067?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Alec Scott</b></sub></a><br /><a href="https://github.com/singularityhub/singularity-hpc/commits?author=alecbcs" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/manbat"><img src="https://avatars.githubusercontent.com/u/41646490?v=4?s=100" width="100px;" alt=""/><br /><sub><b>manbat</b></sub></a><br /><a href="https://github.com/singularityhub/singularity-hpc/commits?author=manbat" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/marcodelapierre"><img src="https://avatars.githubusercontent.com/u/16972180?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Marco De La Pierre</b></sub></a><br /><a href="https://github.com/singularityhub/singularity-hpc/commits?author=marcodelapierre" title="Code">💻</a></td>
    <td align="center"><a href="http://surak.wordpress.com"><img src="https://avatars.githubusercontent.com/u/878399?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Alexandre Strube</b></sub></a><br /><a href="https://github.com/singularityhub/singularity-hpc/commits?author=surak" title="Code">💻</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/xdelaruelle"><img src="https://avatars.githubusercontent.com/u/4928853?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Xavier Delaruelle</b></sub></a><br /><a href="https://github.com/singularityhub/singularity-hpc/commits?author=xdelaruelle" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/SarahBeecroft"><img src="https://avatars.githubusercontent.com/u/16343767?v=4?s=100" width="100px;" alt=""/><br /><sub><b>SarahBeecroft</b></sub></a><br /><a href="https://github.com/singularityhub/singularity-hpc/commits?author=SarahBeecroft" title="Code">💻</a></td>
    <td align="center"><a href="https://muffato.github.io"><img src="https://avatars.githubusercontent.com/u/623458?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Matthieu Muffato</b></sub></a><br /><a href="https://github.com/singularityhub/singularity-hpc/commits?author=muffato" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/georgiastuart"><img src="https://avatars.githubusercontent.com/u/8276147?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Georgia Stuart</b></sub></a><br /><a href="https://github.com/singularityhub/singularity-hpc/commits?author=georgiastuart" title="Code">💻</a></td>
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

 
## 🎨️ Previous Art 🎨️

There are other tools that you might be interested in!

 - [VA Research Computing](https://www.rc.virginia.edu/userinfo/rivanna/software/containers/) has a similar system, but I couldn't find any code.
 - [Community Collections](https://github.com/community-collections/community-collections)
 - [Spack](https://spack.readthedocs.io/en/latest/module_file_support.html) installs modules for software built from source (not containers).
 

## License

This code is licensed under the MPL 2.0 [LICENSE](LICENSE).
