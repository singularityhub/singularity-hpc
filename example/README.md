# Examples

This set of examples includes the following:

## Biocontainers Update

The intention of this script is to instantiate a client, and then match
containers you have in some root from [Galaxy Project Depot](https://depot.galaxyproject.org/singularity/)
on your local filesytem to install to an shpc registry (as modules). The script
tries to be efficient and instantiate one remote registry that has all the containers.
See the script header for usage examples.

## Google Cloud Storage

This example walks through installing containers to Google Cloud Storage,
which we do by way of running a virtual machine to pull and then save
the containers there. It would be up to you to then mount the storage in
some respect to interact with your containers.
