#!/usr/bin/python

# Copyright (C) 2022 Vanessa Sochat.

# This Source Code Form is subject to the terms of the
# Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed
# with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
import os

import shpc.main.container as container
import shpc.main.wrappers.base as wrappers_base

from .helpers import init_client, here


@pytest.mark.parametrize(
    "with_custom_wrapper_template_path,include_container_dir",
    [
        (False, False),
        (False, True),
        (True, False),
        (True, True),
    ],
)
def test_get_template_paths(
    tmp_path, with_custom_wrapper_template_path, include_container_dir
):
    """
    Test the shpc.main.wrappers.base.WrapperScript.get_template_paths function
    """
    # Note: the module_sys and container_tech parameters are actually not used in the test
    client = init_client(str(tmp_path), "tcl", "singularity")
    # The file name is actually not used in the test, only its enclosing directory
    testdata_dir = os.path.join(here, "testdata")
    container_yaml = os.path.join(testdata_dir, "quay-container.yaml")
    config = container.ContainerConfig(container_yaml)
    ws = wrappers_base.WrapperScript(
        "dummy.sh",  # Not used in this test
        client.settings,
        None,  # image
        config=config,
    )
    client.settings.set(
        "wrapper_scripts",
        "templates:" + (str(tmp_path) if with_custom_wrapper_template_path else "None"),
    )

    # get_template_paths
    # - always default template path
    # - optional wrapper path from settings
    # - optional cf include_container_dir
    tp = ws.get_template_paths(include_container_dir)
    expected_len = (
        1 + int(with_custom_wrapper_template_path) + int(include_container_dir)
    )
    assert len(tp) == expected_len
    if with_custom_wrapper_template_path:
        assert str(tmp_path) in tp
    else:
        assert str(tmp_path) not in tp
    if include_container_dir:
        assert testdata_dir in tp
    else:
        assert testdata_dir not in tp


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
    client = init_client(str(tmp_path), "tcl", "singularity")
    # The file name is actually not used in the test, only its enclosing directory
    testdata_dir = os.path.join(here, "testdata")
    container_yaml = os.path.join(testdata_dir, "quay-container.yaml")
    config = container.ContainerConfig(container_yaml)

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
        None,  # image
        config=config,
    )

    if exists:
        p = ws.find_wrapper_script(template_paths)
        if make_absolute:
            assert wrapper_template == p
        assert os.path.isabs(p)
    else:
        with pytest.raises(SystemExit):
            ws.find_wrapper_script(template_paths)
