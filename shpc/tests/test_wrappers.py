#!/usr/bin/python

# Copyright (C) 2021-2023 Vanessa Sochat.

# This Source Code Form is subject to the terms of the
# Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed
# with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

import os

import pytest

import shpc.main.container as container
import shpc.main.registry as registry
import shpc.main.wrappers.base as wrappers_base
import shpc.utils as utils

from .helpers import here, init_client


@pytest.mark.parametrize(
    "with_custom_wrapper_template_path",
    [
        (False, False),
        (False, True),
        (True, False),
        (True, True),
    ],
)
def test_get_local_template_paths(tmp_path, with_custom_wrapper_template_path):
    """
    Test the shpc.main.wrappers.base.WrapperScript.get_template_paths function
    """
    # Note: the module_sys and container_tech parameters are actually not used in the test
    client = init_client(str(tmp_path), "tcl", "singularity", remote=False)
    # The file name is actually not used in the test, only its enclosing directory
    testdata_dir = os.path.join(here, "testdata")
    container_yaml = os.path.join(testdata_dir, "quay-container.yaml")
    config = container.ContainerConfig(
        registry.FilesystemResult("quay.io/vgteam/vg", container_yaml)
    )
    ws = wrappers_base.WrapperScript(
        "dummy.sh",
        client.settings,
        config=config,
        image=None,  # Not used in this test
    )
    client.settings.set(
        "wrapper_scripts",
        "templates:" + (str(tmp_path) if with_custom_wrapper_template_path else "None"),
    )

    # get_template_paths
    # - always default template path
    # - optional wrapper path from settings
    tp = ws.get_template_paths()
    expected_len = 2 if with_custom_wrapper_template_path else 1
    assert len(tp) == expected_len
    if with_custom_wrapper_template_path:
        assert str(tmp_path) in tp
    else:
        assert str(tmp_path) not in tp
    assert testdata_dir not in tp


@pytest.mark.parametrize(
    "remote",
    [False, True],
)
def test_get_registry_wrapper_script(tmp_path, remote):
    """
    Test getting a wrapper script from a remote and local registry.
    """
    client = init_client(str(tmp_path), "tcl", "singularity", remote=remote)

    # This container has wrappers both local/remote
    result = client.registry.find("vanessa/salad")
    assert result

    # This is an existing one
    assert result.find_wrapper_script("singularity", "singularity_fork.sh")
    script = result.load_wrapper_script("singularity", "singularity_fork.sh")

    # Regardless of source, we should get the correct content
    assert '{% extends "bases/shell-script-base.sh" %}' in script

    # This is not
    assert not result.find_wrapper_script("singularity", "singularity.sh")
    assert not result.load_wrapper_script("singularity", "singularity.sh")


@pytest.mark.parametrize(
    "module_sys,module_file,container_tech",
    [
        ("lmod", "module.lua", "singularity"),
        ("lmod", "module.lua", "podman"),
        ("tcl", "module.tcl", "singularity"),
        ("tcl", "module.tcl", "podman"),
    ],
)
def test_wrapper_install(tmp_path, module_sys, module_file, container_tech):
    """
    Test that install of wrapper scripts produces expected files in bin
    """
    client = init_client(str(tmp_path), module_sys, container_tech)

    assert client.settings.get("wrapper_scripts:enabled") is True

    # Install known tag
    client.install("python:3.9.2-alpine")
    module_dir = os.path.join(client.settings.module_base, "python", "3.9.2-alpine")
    assert os.path.exists(module_dir)
    assert "bin" in os.listdir(module_dir)
    module_bin = os.path.join(module_dir, "bin")
    assert os.path.exists(module_bin)

    requireds = [
        "python-container",
        "python-run",
        "python-exec",
        "python",
        "python-shell",
    ]
    if container_tech == "singularity":
        requireds += ["python-inspect-runscript", "python-inspect-deffile"]
    else:
        requireds += ["python-inspect"]
    binaries = os.listdir(module_bin)
    for required in requireds:
        assert required in binaries


@pytest.mark.parametrize(
    "module_sys,module_file,container_tech",
    [
        ("lmod", "module.lua", "singularity"),
        ("lmod", "module.lua", "podman"),
        ("tcl", "module.tcl", "singularity"),
        ("tcl", "module.tcl", "podman"),
    ],
)
def test_disabled_wrapper_install(tmp_path, module_sys, module_file, container_tech):
    """
    Test that install of wrapper scripts produces expected files in bin
    """
    client = init_client(str(tmp_path), module_sys, container_tech)

    client.settings.set("wrapper_scripts:enabled", False)
    assert client.settings.get("wrapper_scripts:enabled") is False

    # Install known tag
    client.install("python:3.9.2-alpine")
    module_dir = os.path.join(client.settings.module_base, "python", "3.9.2-alpine")
    assert os.path.exists(module_dir)
    assert "bin" not in os.listdir(module_dir)


@pytest.mark.parametrize(
    "module_sys,module_file,container_tech,with_custom_wrapper_dir",
    [
        ("lmod", "module.lua", "singularity", True),
        ("lmod", "module.lua", "singularity", False),
        ("lmod", "module.lua", "podman", True),
        ("lmod", "module.lua", "podman", False),
        ("tcl", "module.tcl", "singularity", True),
        ("tcl", "module.tcl", "singularity", False),
        ("tcl", "module.tcl", "podman", True),
        ("tcl", "module.tcl", "podman", False),
    ],
)
def test_custom_wrapper_dir(
    tmp_path, module_sys, module_file, container_tech, with_custom_wrapper_dir
):
    """
    Test that we can customize the install location of wrapper scripts
    """

    client = init_client(str(tmp_path), module_sys, container_tech)

    if with_custom_wrapper_dir:
        wrapper_dir = os.path.join(str(tmp_path), "wrappers")
        client.settings.set("wrapper_base", wrapper_dir)

    # A custom wrapper directory should not have a bin in the module base
    client.install("python:3.9.2-alpine")
    module_dir = os.path.join(client.settings.module_base, "python", "3.9.2-alpine")
    module_filepath = os.path.join(module_dir, module_file)

    assert os.path.exists(module_dir)
    assert os.path.exists(module_filepath)

    # The content of the file
    content = utils.read_file(module_filepath)
    if module_file.endswith("lua") and with_custom_wrapper_dir:
        assert f'local wrapperDir = "{wrapper_dir}/python/3.9.2-alpine"' in content
    elif module_file.endswith("tcl") and with_custom_wrapper_dir:
        assert f'set wrapperDir "{wrapper_dir}/python/3.9.2-alpine"' in content
    elif module_file.endswith("module.lua"):
        assert 'local wrapperDir = "$moduleDir"'
    else:
        assert (
            "set wrapperDir ${moduleDir}" in content
            or "set wrapperDir $moduleDir" in content
        )

    # By default wrappers are generated in the module directory
    if not with_custom_wrapper_dir:
        assert "bin" in os.listdir(module_dir)

    # A custom wrapper directory means we have the wrappers generated there
    else:
        wrapper_dir = os.path.join(
            client.settings.wrapper_base, "python", "3.9.2-alpine"
        )
        assert "bin" not in os.listdir(module_dir)
        assert os.listdir(os.path.join(wrapper_dir, "bin"))


@pytest.mark.parametrize(
    "make_absolute,exists",
    [
        (False, False),
        (False, True),
        (True, False),
        (True, True),
    ],
)
def test_find_wrapper_script(tmp_path, make_absolute, exists):
    """
    Test the shpc.main.wrappers.base.WrapperScript.find_wrapper_script function
    """
    # Note: the module_sys and container_tech parameters are actually not used in the test
    client = init_client(str(tmp_path), "tcl", "singularity", remote=False)
    # The file name is actually not used in the test, only its enclosing directory
    testdata_dir = os.path.join(here, "testdata")
    container_yaml = os.path.join(testdata_dir, "quay-container.yaml")
    config = container.ContainerConfig(
        registry.FilesystemResult("quay.io/vgteam/vg", container_yaml)
    )

    if exists:
        # Using "empty_singularity.sh" to avoid potential false positives in the default wrapper template directory
        wrapper_template = "empty_singularity.sh"
    else:
        # Using "singularity.sh" to avoid potential false positives in the default wrapper template directory
        wrapper_template = "singularity.sh"

    if make_absolute:
        wrapper_template = os.path.join(testdata_dir, wrapper_template)
        template_paths = None
    else:
        template_paths = [testdata_dir]

    ws = wrappers_base.WrapperScript(
        wrapper_template,
        client.settings,
        image=None,
        config=config,
    )

    if exists:
        p = ws.find_wrapper_script(template_paths)
        assert "path" in p
        if make_absolute:
            assert wrapper_template == p["path"]
        assert os.path.isabs(p["path"])
    else:
        with pytest.raises(SystemExit):
            ws.find_wrapper_script(template_paths)
