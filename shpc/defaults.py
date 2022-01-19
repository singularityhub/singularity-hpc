__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021-2022, Vanessa Sochat"
__license__ = "MPL 2.0"

import os
import shpc.utils as utils

install_dir = utils.get_installdir()
reps = {"$install_dir": install_dir, "$root_dir": os.path.dirname(install_dir)}

# The default settings file in the install root
default_settings_file = os.path.join(reps["$install_dir"], "settings.yml")

# The user settings file can be created to over-ride default
user_settings_file = os.path.join(
    os.path.expanduser("~/.singularity-hpc"), "settings.yml"
)

# variables in settings that allow environment variable expansion
allowed_envars = ["container_base", "module_base", "registry"]

# The GitHub repository with recipes
github_url = "https://github.com/singularityhub/singularity-hpc"
