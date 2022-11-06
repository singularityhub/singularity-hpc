#!/usr/bin/python

# Copyright (C) 2022 Vanessa Sochat.

# This Source Code Form is subject to the terms of the
# Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed
# with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

import os

import pytest

import shpc.main.registry as registry
import shpc.utils

from .helpers import here, init_client


def test_filesystem_upgrade(tmp_path):
    """
    Test upgrade from a filesystem registry.
    """
    client = init_client(str(tmp_path), "lmod", "singularity")

    # Create temporary registry that will be empty
    registry_path = os.path.join(tmp_path, "registry")
    client.settings.registry = [registry_path]

    with pytest.raises(ValueError):
        client.reload_registry()

    # Should fail if does not exist
    os.makedirs(registry_path)
    client.reload_registry()

    local = client.registry.filesystem_registry
    assert local
    assert isinstance(local, registry.Filesystem)
    assert local.source == registry_path

    # Local filesystem registry should be empty
    assert not list(local.iter_modules())

    # Create filesystem registry with test data
    test_registry_path = os.path.join(here, "testdata", "registry")
    assert os.path.exists(test_registry_path)
    test_registry = registry.Filesystem(test_registry_path)

    # Should have one module installed
    mods = list(test_registry.iter_modules())
    assert len(mods) == 1
    module = mods[0]
    assert module == "dinosaur/salad"

    # Upgrade the current registry from the "remote" (test registry)
    assert not client.registry.exists(module)
    client.registry.sync_from_remote(test_registry, module)
    existing = client.registry.exists(module)
    assert existing is not None
    assert existing == local
    assert os.path.exists(os.path.join(local.source, module))


def test_sync_from_file(tmp_path):
    """
    Test syncing from file, from each of gitlab and github
    """
    client = init_client(str(tmp_path), "lmod", "singularity")

    cfg = {
        "sync_registry": {
            "%s/tmp/github-shpc"
            % tmp_path: "https://github.com/singularityhub/shpc-registry",
            "%s/gitlab-shpc"
            % tmp_path: "https://gitlab.com/singularityhub/shpc-registry",
        }
    }
    registry_config = os.path.join(tmp_path, "registries.yaml")
    registries = []
    for name in cfg["sync_registry"]:
        os.makedirs(name)
        registries.append(name)
    shpc.utils.write_yaml(cfg, registry_config)

    # Start out empty
    for path in registries:
        assert not os.listdir(path)

    # Dryrun should also be empty
    client.registry.sync(dryrun=True, config_file=registry_config)
    for path in registries:
        assert not os.listdir(path)

    # We should not be adding a recipe unless we already have it
    client.registry.sync(add_new=False, config_file=registry_config)
    for path in registries:
        assert not os.listdir(path)

    client.registry.sync(config_file=registry_config)
    for path in registries:
        assert os.listdir(path)


@pytest.mark.parametrize(
    "remote",
    [
        "https://github.com/singularityhub/shpc-registry",
        "https://gitlab.com/singularityhub/shpc-registry",
        # This registry does not expose a web UI
        "https://github.com/researchapps/shpc-test-registry",
    ],
)
def test_remote_upgrade(tmp_path, remote):
    """
    Test upgrade from a filesystem registry.
    """
    client = init_client(str(tmp_path), "lmod", "singularity")

    # Create temporary registry that will be empty
    registry_path = os.path.join(tmp_path, "registry")
    client.settings.registry = [registry_path]
    os.makedirs(registry_path)
    client.reload_registry()

    # Re-init registries
    client.registry = registry.Registry(client.settings)

    # Upgrade from remote
    client.registry.sync(dryrun=True, sync_registry=remote)
    assert not list(client.registry.iter_modules())

    # We should not be adding a recipe unless we already have it
    client.registry.sync(add_new=False, sync_registry=remote)
    assert not list(client.registry.iter_modules())

    client.registry.sync(sync_registry=remote)
    assert list(client.registry.iter_modules())


@pytest.mark.parametrize(
    "remote",
    [
        "https://github.com/singularityhub/shpc-registry",
        "https://gitlab.com/singularityhub/shpc-registry",
        # This registry does not expose a web UI
        "https://github.com/researchapps/shpc-test-registry",
    ],
)
def test_registry_interaction(tmp_path, remote):
    """
    Test interactions with registries of different types
    """
    client = init_client(str(tmp_path), "lmod", "singularity")
    reg = client.registry.get_registry(remote)

    assert not isinstance(reg, registry.FileSystem)

    # This will hit the underlying logic to list/show
    mods = list(reg.iter_registry())
    assert mods

    # Should use the cache
    assert reg.exists("vanessa/salad")
    assert reg.find("vanessa/salad") is not None
