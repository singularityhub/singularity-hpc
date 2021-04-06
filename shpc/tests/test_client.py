#!/usr/bin/python

# Copyright (C) 2021 Vanessa Sochat.

# This Source Code Form is subject to the terms of the
# Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed
# with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
import shutil
import os

from shpc.main import get_client

here = os.path.dirname(os.path.abspath(__file__))
root = os.path.dirname(here)


def init_client(tmpdir):
    """Get a common client for singularity and lmod"""
    settings_file = os.path.join(root, "settings.yml")
    new_settings = os.path.join(tmpdir, "settings.yml")
    shutil.copyfile(settings_file, new_settings)
    client = get_client(
        quiet=False,
        settings_file=new_settings,
        module="lmod",
        container_tech="singularity",
    )

    # The module folder needs to be temporary too
    modules = os.path.join(tmpdir, "modules")
    client.settings.set("lmod_base", modules)
    client.settings.save()
    return client


def test_install_get(tmp_path):
    """Test install and get"""
    client = init_client(str(tmp_path))

    # Install known tag
    client.install("python:3.9.2-alpine")

    # Modules folder is created
    assert os.path.exists(client.settings.lmod_base)

    module_dir = os.path.join(client.settings.lmod_base, "python", "3.9.2-alpine")
    assert os.path.exists(module_dir)
    module_file = os.path.join(module_dir, "module.lua")
    assert os.path.exists(module_file)

    assert client.get("python/3.9.2-alpine")


def test_inspect(tmp_path):
    """Test inspect"""
    client = init_client(str(tmp_path))
    client.install("python:3.9.2-slim")

    # Install known registry item latest
    with pytest.raises(SystemExit):
        client.inspect("python")

    # Python won't have much TODO we should test a custom container
    metadata = client.inspect("python/3.9.2-slim")
    assert "attributes" in metadata


def test_check(tmp_path):
    """Test check"""
    client = init_client(str(tmp_path))
    client.install("python:3.9.2-slim")

    # Python won't have much TODO we should test a custom container
    client.check("python/3.9.2-slim")


def test_add(tmp_path):
    """Test adding a custom container"""
    client = init_client(str(tmp_path))

    # Create a copy of the latest image to add
    container = os.path.join(str(tmp_path), "salad_latest.sif")
    shutil.copyfile(os.path.join(here, "testdata", "salad_latest.sif"), container)
    client.add(container, "vanessa/salad/latest")
    assert client.get("vanessa/salad/latest")
