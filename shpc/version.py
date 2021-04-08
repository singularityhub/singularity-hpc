__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021, Vanessa Sochat"
__license__ = "MPL 2.0"

__version__ = "0.0.14"
AUTHOR = "Vanessa Sochat"
NAME = "singularity-hpc"
PACKAGE_URL = "https://github.com/singularityhub/singularity-hpc"
KEYWORDS = "singularity, containers, hpc, lmd"
DESCRIPTION = "Local filesystem database for Singularity containers with LMOD"
LICENSE = "LICENSE"

################################################################################
# Global requirements

# Since we assume wanting Singularity and lmod, we require spython and Jinja2

INSTALL_REQUIRES = (
    ("spython", {"min_version": "0.1.13"}),
    ("Jinja2", {"min_version": None}),
    ("jsonschema", {"min_version": None}),
    ("ruamel.yaml", {"min_version": None}),
    ("sqlalchemy", {"min_version": None}),
)

TESTS_REQUIRES = (("pytest", {"min_version": "4.6.2"}),)

################################################################################
# Install basic without database (default)

INSTALL_BASIC = INSTALL_REQUIRES[:-1]

################################################################################
# Submodule Requirements (versions that include database)

INSTALL_REQUIRES_ALL = INSTALL_REQUIRES + TESTS_REQUIRES
