#!/usr/bin/python

# Copyright (C) 2021-2022 Vanessa Sochat.

# This Source Code Form is subject to the terms of the
# Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed
# with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

import os

import shpc.main.container as container

here = os.path.dirname(os.path.abspath(__file__))
root = os.path.dirname(here)


def test_name_parsing(tmp_path):
    """Test parsing a config file"""
    with_registry = os.path.join(here, "testdata", "quay-container.yaml")
    without_registry = os.path.join(here, "testdata", "python-container.yaml")

    config = container.ContainerConfig(with_registry)
    parsed = config.name

    assert parsed.registry == "quay.io"
    assert parsed.namespace == "vgteam"
    assert parsed.tool == "vg"
    assert not parsed.tag
    assert not parsed.digest

    config = container.ContainerConfig(without_registry)
    parsed = config.name

    assert not parsed.registry
    assert not parsed.namespace == "vgteam"
    assert parsed.tool == "python"
    assert not parsed.tag
    assert not parsed.digest
