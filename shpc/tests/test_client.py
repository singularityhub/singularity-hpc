#!/usr/bin/python

# Copyright (C) 2021-2023 Vanessa Sochat.

# This Source Code Form is subject to the terms of the
# Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed
# with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

import io
import os
import shutil

import pytest

import shpc.main.registry as registry
import shpc.utils

from .helpers import here, init_client


@pytest.mark.parametrize(
    "module_sys,module_file,container_tech,remote",
    [
        ("lmod", "module.lua", "singularity", False),
        ("lmod", "module.lua", "podman", False),
        ("tcl", "module.tcl", "singularity", False),
        ("tcl", "module.tcl", "podman", False),
        ("lmod", "module.lua", "singularity", True),
        ("lmod", "module.lua", "podman", True),
        ("tcl", "module.tcl", "singularity", True),
        ("tcl", "module.tcl", "podman", True),
    ],
)
def test_install_get(tmp_path, module_sys, module_file, container_tech, remote):
    """
    Test install and get
    """
    client = init_client(str(tmp_path), module_sys, container_tech, remote=remote)

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

    client.install("python:3.9.2-alpine")


@pytest.mark.parametrize(
    "module_sys,module_file,remote",
    [
        ("lmod", "module.lua", True),
        ("tcl", "module.tcl", True),
        ("lmod", "module.lua", False),
        ("tcl", "module.tcl", False),
    ],
)
def test_features(tmp_path, module_sys, module_file, remote):
    """
    Test adding features.
    Features are currently only supported for Singularity.
    """
    client = init_client(str(tmp_path), module_sys, "singularity", remote=remote)

    module_file_392 = os.path.join(
        client.settings.module_base, "python", "3.9.2-alpine", module_file
    )
    module_file_394 = os.path.join(
        client.settings.module_base, "python", "3.9.4-alpine", module_file
    )

    # Install known tag
    client.install("python:3.9.2-alpine")

    # Should not have nvidia flag
    content = shpc.utils.read_file(module_file_392)
    assert "--nv" not in content

    client.install("python:3.9.4-alpine")
    assert os.path.exists(module_file_392)
    assert os.path.exists(module_file_394)

    client.uninstall("python:3.9.2-alpine", force=True)
    assert not os.path.exists(module_file_392)
    assert os.path.exists(module_file_394)

    client.uninstall("python", force=True)
    assert not os.path.exists(module_file_394)

    # Now update settings
    client.settings.set("container_features", "gpu:nvidia")

    # Install known tag, add extra feature of gpu
    client.install("python:3.9.2-alpine", features=["gpu"])
    content = shpc.utils.read_file(module_file_392)
    assert "--nv" in content


@pytest.mark.parametrize(
    "default_version,remote",
    [
        (True, True),
        (False, True),
        ("module_sys", True),
        (None, True),
        ("first_installed", True),
        ("last_installed", True),
        (True, False),
        (False, False),
        ("module_sys", False),
        (None, False),
        ("first_installed", False),
        ("last_installed", False),
    ],
)
def test_tcl_default_version(tmp_path, default_version, remote):
    """
    Test tcl default versions.

    True or module_sys: no .version file
    False or None: .version file with faux number
    first_installed: we maintain first installed version number
    last_installed: version is updated to last installed
    """
    client = init_client(str(tmp_path), "tcl", "singularity", remote=remote)

    # Customize config settings
    client.settings.set("default_version", default_version)

    # Install known tag
    client.install("python:3.9.2-alpine")

    # Get paths
    module_dir = os.path.join(client.settings.module_base, "python")
    version_file = os.path.join(module_dir, ".version")

    if default_version in ["module_sys", True]:
        assert not os.path.exists(version_file)

    elif default_version in [False, None]:
        assert os.path.exists(version_file)
        content = shpc.utils.read_file(version_file)
        assert "please_specify_a_version_number" in content

    elif default_version == "first_installed":
        assert os.path.exists(version_file)
        content = shpc.utils.read_file(version_file)
        assert "3.9.2-alpine" in content
        client.install("python:3.9.5-alpine")
        content = shpc.utils.read_file(version_file)
        assert "3.9.2-alpine" in content

    elif default_version == "last_installed":
        assert os.path.exists(version_file)
        content = shpc.utils.read_file(version_file)
        assert "3.9.2-alpine" in content
        client.install("python:3.9.5-alpine")
        content = shpc.utils.read_file(version_file)
        assert "3.9.5-alpine" in content


@pytest.mark.parametrize(
    "default_version,remote",
    [
        (True, True),
        (False, True),
        ("module_sys", True),
        (None, True),
        ("first_installed", True),
        ("last_installed", True),
        (True, False),
        (False, False),
        ("module_sys", False),
        (None, False),
        ("first_installed", False),
        ("last_installed", False),
    ],
)
def test_lmod_default_version(tmp_path, default_version, remote):
    """
    Test lmod (lua) default versions.

    True or module_sys: file with non-existent version number
    False or None: no .version file
    first_installed: we maintain first installed version number
    last_installed: version is updated to last installed
    """
    client = init_client(str(tmp_path), "lmod", "singularity", remote=remote)

    # Customize config settings
    client.settings.set("default_version", default_version)

    # Install known tag
    client.install("python:3.9.2-alpine")

    # Get paths
    module_dir = os.path.join(client.settings.module_base, "python")
    version_file = os.path.join(module_dir, ".version")

    if default_version in ["module_sys", True]:
        assert os.path.exists(version_file)
        content = shpc.utils.read_file(version_file)
        assert "please_specify_a_version_number" in content

    elif default_version in [False, None]:
        assert not os.path.exists(version_file)

    elif default_version == "first_installed":
        assert os.path.exists(version_file)
        content = shpc.utils.read_file(version_file)
        assert "3.9.2-alpine" in content
        client.install("python:3.9.5-alpine")
        content = shpc.utils.read_file(version_file)
        assert "3.9.2-alpine" in content

    elif default_version == "last_installed":
        assert os.path.exists(version_file)
        content = shpc.utils.read_file(version_file)
        assert "3.9.2-alpine" in content
        client.install("python:3.9.5-alpine")
        content = shpc.utils.read_file(version_file)
        assert "3.9.5-alpine" in content


@pytest.mark.parametrize(
    "module_sys,remote",
    [("lmod", True), ("tcl", True), ("lmod", False), ("tcl", False)],
)
def test_docgen(tmp_path, module_sys, remote):
    """
    Test docgen
    """
    client = init_client(str(tmp_path), module_sys, "singularity", remote=remote)
    client.install("python:3.9.2-slim")
    out = io.StringIO()
    docs = client.docgen("python:3.9.2-slim", out=out)
    docs = docs.getvalue()
    assert "python:3.9.2-slim" in docs


@pytest.mark.parametrize(
    "module_sys,container_tech,remote",
    [
        ("lmod", "singularity", True),
        ("lmod", "podman", True),
        ("tcl", "singularity", True),
        ("tcl", "podman", True),
        ("lmod", "singularity", False),
        ("lmod", "podman", False),
        ("tcl", "singularity", False),
        ("tcl", "podman", False),
    ],
)
def test_inspect(tmp_path, module_sys, container_tech, remote):
    """
    Test inspect
    """
    client = init_client(str(tmp_path), module_sys, container_tech, remote=remote)
    client.install("python:3.9.2-slim")
    # Python won't have much TODO we should test a custom container
    metadata = client.inspect("python:3.9.2-slim")
    if container_tech == "singularity":
        assert "attributes" in metadata
    else:
        assert isinstance(metadata, list)


@pytest.mark.parametrize(
    "module_sys,remote",
    [
        ("lmod", True),
        ("tcl", True),
        ("lmod", False),
        ("tcl", False),
    ],
)
def test_namespace_and_show(tmp_path, module_sys, remote):
    """
    Test namespace and show
    """
    client = init_client(str(tmp_path), module_sys, "singularity", remote=remote)
    client.show("vanessa/salad:latest")

    with pytest.raises(SystemExit):
        client.show("salad:latest")
    client.settings.set("namespace", "vanessa")
    client.show("salad:latest")
    client.settings.set("namespace", None)


@pytest.mark.parametrize(
    "module_sys,container_tech,remote",
    [
        ("lmod", "singularity", True),
        ("lmod", "podman", True),
        ("tcl", "singularity", True),
        ("tcl", "podman", True),
        ("lmod", "singularity", False),
        ("lmod", "podman", False),
        ("tcl", "singularity", False),
        ("tcl", "podman", False),
    ],
)
def test_check(tmp_path, module_sys, container_tech, remote):
    """
    Test check
    """
    client = init_client(str(tmp_path), module_sys, container_tech, remote=remote)
    client.install("vanessa/salad:latest")
    client.check("vanessa/salad:latest")


@pytest.mark.parametrize(
    "module_sys,remote",
    [("lmod", True), ("tcl", True), ("lmod", False), ("tcl", False)],
)
def test_install_local(tmp_path, module_sys, remote):
    """
    Test adding a custom container associated with an existing recipe
    """
    client = init_client(str(tmp_path), module_sys, "singularity", remote=remote)

    # Create a copy of the latest image to add
    container = os.path.join(str(tmp_path), "salad_latest.sif")
    shutil.copyfile(os.path.join(here, "testdata", "salad_latest.sif"), container)

    # It still needs to be a known tag!
    with pytest.raises(SystemExit):
        client.install(
            "quay.io/biocontainers/samtools:1.2--0", container_image=container
        )

    # This should install our custom image using samtools metadata
    container_image = "quay.io/biocontainers/samtools:1.10--h2e538c0_3"
    client.install(container_image, container_image=container)
    assert os.path.basename(client.get(container_image)) == os.path.basename(container)


@pytest.mark.parametrize(
    "module_sys,remote",
    [("lmod", True), ("tcl", True), ("lmod", False), ("tcl", False)],
)
def test_add(tmp_path, module_sys, remote):
    """
    Test adding a custom container
    """
    client = init_client(str(tmp_path), module_sys, "singularity", remote=remote)

    # Create a copy of the latest image to add
    container = os.path.join(str(tmp_path), "salad_latest.sif")
    shutil.copyfile(os.path.join(here, "testdata", "salad_latest.sif"), container)

    # Add only works for local filesystem registry
    if remote:
        with pytest.raises(SystemExit):
            client.add(container, "dinosaur/salad:latest")
        return

    client.add(container, "dinosaur/salad:latest")

    # Ensure this creates a container.yaml in the registry
    container_yaml = os.path.join(
        client.settings.registry[0], "dinosaur", "salad", "container.yaml"
    )
    assert os.path.exists(container_yaml)

    # Add does not install!
    with pytest.raises(SystemExit):
        client.get("dinosaur/salad:latest")
    client.install("dinosaur/salad:latest")
    assert client.get("dinosaur/salad:latest")


def test_remove(tmp_path):
    """
    Test removing a container recipe
    """
    client = init_client(str(tmp_path), "lmod", "singularity")

    # Create temporary registry that will be empty
    registry_path = os.path.join(tmp_path, "registry")
    client.settings.registry = [registry_path]
    os.makedirs(registry_path)
    client.reload_registry()
    assert client.settings.filesystem_registry == registry_path

    # Wrap local test filesystem registry and add module to it
    test_registry_path = os.path.join(here, "testdata", "registry")
    test_registry = registry.Filesystem(test_registry_path)
    module = "dinosaur/salad"

    client.registry.sync_from_remote(test_registry, module)

    # It should exist in the registry
    assert client.registry.exists(module) is not None
    # Remove the module (with force)
    client.remove(module, force=True)
    assert client.registry.exists(module) is None
