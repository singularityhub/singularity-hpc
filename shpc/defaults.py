__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021, Vanessa Sochat"
__license__ = "MPL 2.0"

import os
import shpc.utils as utils

# Replacements can currently be made for the database_file and lmod_base
reps = {"$install_dir": utils.get_installdir()}

# The default settings file in the install root
default_settings_file = os.path.join(reps["$install_dir"], "settings.yml")

# Defaults should correspond to fields in settings.yml
# Testing checks that we have a 1:1 match

# Currently only lmod is supported. To request an additional system,
# please open an issue https://github.com/singularityhub/singularity-hpc
plugins_enabled = ["lmod"]

# Lmod settings

# The install directory for modules. Defaults to the install directory/modules
lmod_base = os.path.join(reps["$install_dir"], "modules")

# disable keeping a sqlite database with metadata
database_disable = False

# default database file
database_file = os.path.join(reps["$install_dir"], "shpc.db")
