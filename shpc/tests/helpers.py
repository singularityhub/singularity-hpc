#!/usr/bin/python

# Copyright (C) 2022 Vanessa Sochat.

# This Source Code Form is subject to the terms of the
# Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed
# with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

import os
import shutil

from shpc.main import get_client
from shpc.main.registry import GitHub

here = os.path.dirname(os.path.abspath(__file__))
root = os.path.dirname(here)


def init_client(tmpdir, module_sys, container_tech, remote=True):
    """
    Get a common client for some container technology and module system
    """
    settings_file = os.path.join(root, "settings.yml")
    new_settings = os.path.join(tmpdir, "settings.yml")
    shutil.copyfile(settings_file, new_settings)
    client = get_client(
        quiet=False,
        settings_file=new_settings,
        module_sys=module_sys,
        container_tech=container_tech,
    )

    # The module and views folders need to be temporary too
    modules = os.path.join(tmpdir, "modules")
    containers = os.path.join(tmpdir, "containers")
    views = os.path.join(tmpdir, "views")
    client.settings.set("module_base", modules)
    client.settings.set("container_base", containers)
    client.settings.set("views_base", views)

    # If it's not remote, create a temporary filesystem registry
    if not remote:
        clone_dir = os.path.join(tmpdir, "registry")
        reg = GitHub("https://github.com/singularityhub/shpc-registry")
        reg.clone(clone_dir)
        client.settings.registry = [clone_dir]
        client.reload_registry()
    client.settings.save()

    # Reinit views so they are detected in the temporary location
    client.detect_views()
    return client
