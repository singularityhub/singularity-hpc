__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021-2022, Vanessa Sochat"
__license__ = "MPL 2.0"

__version__ = "0.0.51"
AUTHOR = "Vanessa Sochat"
NAME = "singularity-hpc"
PACKAGE_URL = "https://github.com/singularityhub/singularity-hpc"
KEYWORDS = "singularity, containers, hpc, lmd"
DESCRIPTION = "Local registry intended for HPC using containers and system modules."
LICENSE = "LICENSE"

################################################################################
# Global requirements

# Since we assume wanting Singularity and lmod, we require spython and Jinja2

INSTALL_REQUIRES = (
    # 0.1.18 added support for oras
    ("spython", {"min_version": "0.2.0"}),
    ("Jinja2", {"min_version": None}),
    ("jsonschema", {"min_version": None}),
    ("ruamel.yaml", {"min_version": None}),
    ("requests", {"min_version": None}),
)

TESTS_REQUIRES = (("pytest", {"min_version": "4.6.2"}),)

################################################################################
# Submodule Requirements (versions that include database)

INSTALL_REQUIRES_ALL = INSTALL_REQUIRES + TESTS_REQUIRES
