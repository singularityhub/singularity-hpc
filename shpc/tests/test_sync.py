#!/usr/bin/python

# Copyright (C) 2022 Vanessa Sochat.

# This Source Code Form is subject to the terms of the
# Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed
# with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
import os

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

    # Re-init registries
    client.registry = registry.Registry(client.settings)

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

    # Upgrade the current registry from the "remote" (test registry)
    assert not client.registry.exists(module)
    client.registry.sync_from_remote(test_registry, module)
    existing = client.registry.exists(module)
    assert existing is not None
    assert os.path.exists(existing)


def test_github_upgrade(tmp_path):
    """
    Test upgrade from a filesystem registry.
    """
    client = init_client(str(tmp_path), "lmod", "singularity")

    # Create temporary registry that will be empty
    registry_path = os.path.join(tmp_path, "registry")
    client.settings.remove("registry", os.path.join("$root_dir", "registry"))
    client.settings.add("registry", registry_path)
    os.makedirs(registry_path)

    # Re-init registries
    client.registry = registry.Registry(client.settings)

    # Upgrade from remote
    client.registry.sync(dryrun=True)
    assert not list(client.registry.iter_modules())

    # We should not be adding a recipe unless we already have it
    client.registry.sync(add_new=False)
    assert not list(client.registry.iter_modules())

    client.registry.sync()
    assert list(client.registry.iter_modules())
