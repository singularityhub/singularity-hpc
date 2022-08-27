#!/usr/bin/python

# Copyright (C) 2022 Vanessa Sochat.
# This Source Code Form is subject to the terms of the
# Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed
# with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest

from .helpers import init_client


def test_config(tmp_path):
    """
    Test config get, set, etc.
    """
    client = init_client(str(tmp_path), "lmod", "singularity")

    # Set/get one level
    assert not client.settings.get("container_features:gpu")
    client.settings.set("container_features", "gpu:nvidia")
    assert client.settings.get("container_features:gpu") == "nvidia"

    # Set null
    client.settings.set("container_features:gpu", None)
    assert not client.settings.get("container_features:gpu")

    client.settings.set("container_features:gpu", "null")
    assert not client.settings.get("container_features:gpu")

    client.settings.set("container_features:gpu", "none")
    assert not client.settings.get("container_features:gpu")

    # Boolean
    assert client.settings.get("wrapper_scripts:enabled") == True
    client.settings.set("wrapper_scripts:enabled", False)
    assert client.settings.get("wrapper_scripts:enabled") == False
    client.settings.set("wrapper_scripts:enabled", "false")
    assert client.settings.get("wrapper_scripts:enabled") == False
    client.settings.set("wrapper_scripts:enabled", "TRUE")
    assert client.settings.get("wrapper_scripts:enabled") == True


@pytest.mark.parametrize(
    "command,name,param,default,result",
    [
        (
            "set",
            "container_features:gpu",
            "container_features:gpu:nvidia",
            None,
            "nvidia",
        ),
        (
            "set",
            "container_features:gpu",
            ["container_features:gpu", "nvidia"],
            None,
            "nvidia",
        ),
        (
            "set",
            "wrapper_scripts:templates",
            "wrapper_scripts:templates:value",
            None,
            "value",
        ),
        (
            "set",
            "wrapper_scripts:templates",
            ["wrapper_scripts:templates", "value"],
            None,
            "value",
        ),
    ],
)
def test_update_param(tmp_path, command, name, param, default, result):
    """
    Test general update_param used by client
    """
    client = init_client(str(tmp_path), "lmod", "singularity")

    # Set/get one level
    assert client.settings.get(name) == default
    client.settings.update_param(command, param)
    assert client.settings.get(name) == result


def test_add_remove(tmp_path):
    """
    Test add/remove (from list)
    """
    client = init_client(str(tmp_path), "lmod", "singularity")

    # Default is a single list
    registry = client.settings.get("registry")
    assert isinstance(registry, list)
    assert len(registry) == 1
    assert registry[0].endswith("registry")

    # Add a registry location
    client.settings.update_param("add", ["registry", "/tmp/registry"])
    registry = client.settings.get("registry")
    assert len(registry) == 2
    assert "/tmp/registry" in registry

    # Remove from list
    client.settings.update_param("remove", ["registry", "/tmp/registry"])
    registry = client.settings.get("registry")
    assert len(registry) == 1
    assert "/tmp/registry" not in registry

    # Add a registry location (old format)
    client.settings.update_param("add", "registry:/tmp/registry")
    registry = client.settings.get("registry")
    assert len(registry) == 2
    assert "/tmp/registry" in registry

    # Remove a registry location (old format)
    client.settings.update_param("remove", "registry:/tmp/registry")
    registry = client.settings.get("registry")
    assert len(registry) == 1
    assert "/tmp/registry" not in registry
