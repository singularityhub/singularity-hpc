#!/usr/bin/python

# Copyright (C) 2022 Vanessa Sochat.

# This Source Code Form is subject to the terms of the
# Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed
# with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
import shutil
import os
import io

import shpc.utils
import shpc.main.registry as registry
from .helpers import here, init_client


def test_filesystem_upgrade(tmp_path):
    """
    Test upgrade from a filesystem registry.
    """
    client = init_client(str(tmp_path), "lmod", "singularity")

    # Create temporary registry that will be empty
    registry_path = os.path.join(tmp_path, "registry")
    client.settings.remove("registry", os.path.join("$root_dir", "registry"))
    client.settings.add("registry", registry_path)
    assert registry_path in client.settings.get("registry")

    # Test interacting with local filesystem registry
    with pytest.raises(ValueError):
        local = registry.Filesystem(registry_path)
    os.makedirs(registry_path)
    local = registry.Filesystem(registry_path)

    # It should be empty
    assert not list(local.iter_modules())

    # Create filesystem registry with test data
    test_registry_path = os.path.join(here, "testdata", "registry")
    assert os.path.exists(test_registry_path)
    test_registry = registry.Filesystem(test_registry_path)

    # Should have one module installed
    mods = list(test_registry.iter_modules())
    assert len(mods) == 1
    module = mods[0][1]
    assert mods[0][0] == test_registry_path
    assert module == "dinosaur/salad"

    assert not local.exists(module)
    from_path = os.path.join(test_registry_path, module)
    to_path = os.path.join(registry_path, module)
    assert os.path.exists(from_path)

    # Update container module from test to tmp registry
    registry.update_container_module(module, from_path, to_path)
    assert local.exists(module)
    # TODO eventually want to create dummy remote registry to test

    local.cleanup()
    assert not os.path.exists(registry_path)
