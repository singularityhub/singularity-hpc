#!/usr/bin/python

# Copyright (C) 2021-2022 Vanessa Sochat.

# This Source Code Form is subject to the terms of the
# Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed
# with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

import os

import jsonschema
import pytest

import shpc.main.container as container
import shpc.main.registry as registry

here = os.path.dirname(os.path.abspath(__file__))
root = os.path.dirname(here)


def test_name_parsing(tmp_path):
    """
    Test name parsing in a config file
    """
    with_registry = os.path.join(here, "testdata", "quay-container.yaml")
    without_registry = os.path.join(here, "testdata", "python-container.yaml")

    config = container.ContainerConfig(
        registry.FilesystemResult("quay.io/vgteam/vg", with_registry)
    )
    parsed = config.name

    assert parsed.registry == "quay.io"
    assert parsed.namespace == "vgteam"
    assert parsed.tool == "vg"
    assert not parsed.tag
    assert not parsed.digest

    config = container.ContainerConfig(
        registry.FilesystemResult("quay.io/vgteam/vg", without_registry)
    )
    parsed = config.name

    assert not parsed.registry
    assert not parsed.namespace == "vgteam"
    assert parsed.tool == "python"
    assert not parsed.tag
    assert not parsed.digest


# TODO we don't have any remote overrides to test!
def test_filesystem_overrides(tmp_path):
    """
    Test custom override files
    """
    alias_container = os.path.join(here, "testdata", "alias-container.yaml")
    config = container.ContainerConfig(
        registry.FilesystemResult("python", alias_container)
    )

    # Trying to load over-rides for a tag that doesn't have any should skip
    config.load_override_file("3.9.2-slim")
    aliases = config.get_aliases()
    assert len(aliases) == 1
    assert aliases[0]["name"] == "python"
    assert aliases[0]["command"] == "/usr/local/bin/python"

    # Not loading any overrides should provide default in container.yaml
    aliases = config.get_aliases()
    assert len(aliases) == 1
    assert aliases[0]["name"] == "python"
    assert aliases[0]["command"] == "/usr/local/bin/python"

    # Load a known overrides file should work
    config.load_override_file("3.10.0a7-alpine")
    aliases = config.get_aliases()
    assert len(aliases) == 1
    assert aliases[0]["name"] == "python"
    assert aliases[0]["command"] == "/alias/path/to/python"

    samtools_container = os.path.join(here, "testdata", "samtools", "container.yaml")

    config = container.ContainerConfig(
        registry.FilesystemResult("samtools", samtools_container)
    )
    assert len(config.get_aliases()) == 14
    assert not config.env

    config.load_override_file("1.14--hb421002_0")
    assert len(config.get_aliases()) == 27
    assert not config.env

    config = container.ContainerConfig(
        registry.FilesystemResult("samtools", samtools_container)
    )
    config.load_override_file("1.15--h3843a85_0")
    assert len(config.get_aliases()) == 14
    assert "REF_PATH" in config.env
    assert config.env["REF_PATH"] == "/shared/cram_cache/%2s/%2s/%s"


def test_invalid_overrides(tmp_path):
    """
    Test custom invalid override files
    """
    alias_container = os.path.join(here, "testdata", "alias-container.yaml")
    config = container.ContainerConfig(
        registry.FilesystemResult("python", alias_container)
    )
    with pytest.raises(jsonschema.exceptions.ValidationError):
        config.load_override_file("3.9.4-alpine")
