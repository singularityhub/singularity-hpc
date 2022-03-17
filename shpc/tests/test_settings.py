#!/usr/bin/python

# Copyright (C) 2021-2022 Vanessa Sochat.

# This Source Code Form is subject to the terms of the
# Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed
# with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
import os

from shpc.main.settings import Settings

here = os.path.dirname(os.path.abspath(__file__))
root = os.path.dirname(here)


def test_environment_substitution(tmp_path):
    """Test variable substitution"""
    settings_file = os.path.join(root, "settings.yml")
    settings = Settings(settings_file)

    assert "/tmp" not in settings.module_base
    os.environ["SOME_PATH"] = "/tmp"
    os.putenv("SOME_PATH", "/tmp")
    settings.set("module_base", "$SOME_PATH/modules")
    assert settings.module_base == "/tmp/modules"


def test_set_get(tmp_path):
    """Test variable set/get"""
    settings_file = os.path.join(root, "settings.yml")
    settings = Settings(settings_file)
    assert settings.container_base.endswith("containers")
    settings.set("container_base", "/tmp/containers")
    settings.set("container_features", "gpu:amd")
    assert settings.container_base == "/tmp/containers"
    assert settings.container_features["gpu"] == "amd"
    assert settings.get("container_features:gpu") == "amd"
    assert settings.get("container_features")["gpu"] == "amd"


def test_add_remove(tmp_path):
    """Test variable add/remove"""
    settings_file = os.path.join(root, "settings.yml")
    settings = Settings(settings_file)
    assert len(settings.registry) == 1
    settings.add("registry", "/tmp/containers")
    assert len(settings.registry) == 2
    settings.remove("registry", "/tmp/containers")
    assert len(settings.registry) == 1
    with pytest.raises(SystemExit):
        settings.remove("registry", "/does/not/exist")
