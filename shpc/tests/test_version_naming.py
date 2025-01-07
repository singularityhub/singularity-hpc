#!/usr/bin/python

# Copyright (C) 2021-2023 Vanessa Sochat.

# This Source Code Form is subject to the terms of the
# Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed
# with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

import io
import os
import shutil

import pytest

import shpc.main.registry as registry
import shpc.utils

from .helpers import here, init_client


@pytest.mark.parametrize(
    "module_sys,module_file,container_tech",
    [
        ("lmod", "module.lua", "singularity"),
        ("lmod", "module.lua", "podman"),
        ("tcl", "module.tcl", "singularity"),
        ("tcl", "module.tcl", "podman"),
        ("lmod", "module.lua", "singularity"),
        ("lmod", "module.lua", "podman"),
        ("tcl", "module.tcl", "singularity"),
        (
            "tcl",
            "module.tcl",
            "podman",
        ),
    ],
)
def test_version_naming_install(tmp_path, module_sys, module_file, container_tech):

    """
    Test that version naming install makes module file as version number
    """
    client = init_client(str(tmp_path), module_sys, container_tech)

    client.settings.set("version_naming", True)
    assert client.settings.get("version_naming") == True
    # Install known tag
    client.install("python:3.9.2-alpine")

    # Modules folder is created
    assert os.path.exists(client.settings.module_base)

    module_dir = os.path.join(client.settings.module_base, "python")

    assert os.path.exists(module_dir)

    module_file = os.path.join(module_dir, "3.9.2-alpine")

    assert os.path.exists(module_file)

@pytest.mark.parametrize(
    "module_sys,module_file,container_tech",
    [
        ("lmod", "module.lua", "singularity"),
        ("lmod", "module.lua", "podman"),
        ("tcl", "module.tcl", "singularity"),
        ("tcl", "module.tcl", "podman"),
        ("lmod", "module.lua", "singularity"),
        ("lmod", "module.lua", "podman"),
        ("tcl", "module.tcl", "singularity"),
        (
            "tcl",
            "module.tcl",
            "podman",
        ),
    ],
)

def test_disabled_version_naming_install(
    tmp_path, module_sys, module_file, container_tech
):

    """
    Test that version naming install makes module file as version number
    """
    client = init_client(str(tmp_path), module_sys, container_tech)

    client.settings.set("version_naming", False)
    assert client.settings.get("version_naming") == False
    # Install known tag
    client.install("python:3.9.2-alpine")

    # Modules folder is created
    assert os.path.exists(client.settings.module_base)

    module_dir = os.path.join(client.settings.module_base, "python", "3.9.2-alpine")

    assert os.path.exists(module_dir)
    module_file = os.path.join(module_dir, module_file)
    assert os.path.exists(module_file)
