#!/usr/bin/python

# Copyright (C) 2021 Vanessa Sochat.

# This Source Code Form is subject to the terms of the
# Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed
# with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
import shutil
import os
import io

import shpc.utils
from shpc.main import get_client

here = os.path.dirname(os.path.abspath(__file__))
root = os.path.dirname(here)


def init_client(tmpdir, module_sys, container_tech):
    """Get a common client for singularity and lmod"""
    settings_file = os.path.join(root, "settings.yml")
    new_settings = os.path.join(tmpdir, "settings.yml")
    shutil.copyfile(settings_file, new_settings)
    client = get_client(
        quiet=False,
        settings_file=new_settings,
        module=module_sys,
        container_tech=container_tech,
    )

    # The module folder needs to be temporary too
    modules = os.path.join(tmpdir, "modules")
    modules = os.path.join(tmpdir, "containers")
    client.settings.set("module_base", modules)
    client.settings.set("container_base", modules)
    client.settings.save()
    return client


@pytest.mark.parametrize(
    "module_sys,module_file,container_tech",
    [
        ("lmod", "module.lua", "singularity"),
        ("lmod", "module.lua", "podman"),
        ("tcl", "module.tcl", "singularity"),
        ("tcl", "module.tcl", "podman"),
    ],
)
def test_install_get(tmp_path, module_sys, module_file, container_tech):
    """Test install and get"""
    client = init_client(str(tmp_path), module_sys, container_tech)

    # Install known tag
    client.install("python:3.9.2-alpine")

    # Modules folder is created
    assert os.path.exists(client.settings.module_base)

    module_dir = os.path.join(client.settings.module_base, "python", "3.9.2-alpine")
    assert os.path.exists(module_dir)
    module_file = os.path.join(module_dir, module_file)
    assert os.path.exists(module_file)
    env_file = os.path.join(module_dir, client.settings.environment_file)
    assert os.path.exists(env_file)

    assert client.get("python:3.9.2-alpine")


@pytest.mark.parametrize(
    "module_sys,module_file", [("lmod", "module.lua"), ("tcl", "module.tcl")]
)
def test_features(tmp_path, module_sys, module_file):
    """
    Test adding features.
    Features are currently only supported for Singularity.
    """
    client = init_client(str(tmp_path), module_sys, "singularity")

    # Install known tag
    client.install("python:3.9.2-alpine")

    module_dir = os.path.join(client.settings.module_base, "python", "3.9.2-alpine")
    module_file = os.path.join(module_dir, module_file)

    # Should not have nvidia flag
    content = shpc.utils.read_file(module_file)
    assert "--nv" not in content

    client.uninstall("python:3.9.2-alpine", force=True)

    # Now update settings
    client.settings.set("container_features:gpu", "nvidia")

    # Install known tag, add extra feature of gpu
    client.install("python:3.9.2-alpine", features=["gpu"])
    content = shpc.utils.read_file(module_file)
    assert "--nv" in content


@pytest.mark.parametrize("module_sys", [("lmod"), ("tcl")])
def test_docgen(tmp_path, module_sys):
    """Test docgen"""
    client = init_client(str(tmp_path), module_sys, "singularity")
    client.install("python:3.9.2-slim")
    out = io.StringIO()
    docs = client.docgen("python:3.9.2-slim", out)
    docs = docs.getvalue()
    assert "python:3.9.2-slim" in docs


@pytest.mark.parametrize(
    "module_sys,container_tech",
    [
        ("lmod", "singularity"),
        ("lmod", "podman"),
        ("tcl", "singularity"),
        ("tcl", "podman"),
    ],
)
def test_inspect(tmp_path, module_sys, container_tech):
    """Test inspect"""
    client = init_client(str(tmp_path), module_sys, container_tech)
    client.install("python:3.9.2-slim")
    # Python won't have much TODO we should test a custom container
    metadata = client.inspect("python:3.9.2-slim")
    if container_tech == "singularity":
        assert "attributes" in metadata
    else:
        assert isinstance(metadata, list)


@pytest.mark.parametrize("module_sys", [("lmod"), ("tcl")])
def test_namespace_and_show(tmp_path, module_sys):
    """Test namespace and show"""
    client = init_client(str(tmp_path), module_sys, "singularity")
    client.show("vanessa/salad:latest")

    with pytest.raises(SystemExit):
        client.show("salad:latest")
    client.settings.set("namespace", "vanessa")
    client.show("salad:latest")
    client.settings.set("namespace", None)


@pytest.mark.parametrize(
    "module_sys,container_tech",
    [
        ("lmod", "singularity"),
        ("lmod", "podman"),
        ("tcl", "singularity"),
        ("tcl", "podman"),
    ],
)
def test_check(tmp_path, module_sys, container_tech):
    """Test check"""
    client = init_client(str(tmp_path), module_sys, container_tech)
    client.install("vanessa/salad:latest")
    client.check("vanessa/salad:latest")


@pytest.mark.parametrize("module_sys", [("lmod"), ("tcl")])
def test_add(tmp_path, module_sys):
    """Test adding a custom container"""
    client = init_client(str(tmp_path), module_sys, "singularity")

    # Create a copy of the latest image to add
    container = os.path.join(str(tmp_path), "salad_latest.sif")
    shutil.copyfile(os.path.join(here, "testdata", "salad_latest.sif"), container)
    client.add(container, "dinosaur/salad/latest")
    assert client.get("dinosaur/salad:latest")
