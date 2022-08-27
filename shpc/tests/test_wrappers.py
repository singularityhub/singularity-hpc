#!/usr/bin/python

# Copyright (C) 2022 Vanessa Sochat.

# This Source Code Form is subject to the terms of the
# Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed
# with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

import os

import pytest

import shpc.main.container as container
import shpc.main.registry as registry
import shpc.main.wrappers.base as wrappers_base

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
    if not remote:
        assert os.path.exists(script)
    else:
        assert '{% extends "bases/shell-script-base.sh" %}' in script

    # This is not
    assert not result.find_wrapper_script("singularity", "singularity.sh")
    assert not result.load_wrapper_script("singularity", "singularity.sh")


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
