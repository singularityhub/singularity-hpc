#!/usr/bin/python

# Copyright (C) 2022 Vanessa Sochat.

# This Source Code Form is subject to the terms of the
# Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed
# with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

import os

import pytest

import shpc.client.view as view_client
import shpc.main.modules.views as views
import shpc.utils as utils

from .helpers import here, init_client


@pytest.mark.parametrize(
    "module_sys,module_file,container_tech,remote",
    [
        ("lmod", "module.lua", "singularity", True),
        ("lmod", "module.lua", "podman", True),
        ("tcl", "module.tcl", "singularity", True),
        ("tcl", "module.tcl", "podman", True),
        ("lmod", "module.lua", "singularity", False),
        ("lmod", "module.lua", "podman", False),
        ("tcl", "module.tcl", "singularity", False),
        ("tcl", "module.tcl", "podman", False),
    ],
)
def test_views(tmp_path, module_sys, module_file, container_tech, remote):
    """
    Test views:

    create
    install
    uninstall
    delete
    """
    client = init_client(str(tmp_path), module_sys, container_tech, remote=remote)

    # Create the view handler based on the client settings file
    view_handler = views.ViewsHandler(
        settings_file=client.settings.settings_file, module_sys=module_sys
    )

    # A view name
    view_name = "mpi"
    assert view_name not in client.views

    # Install, edit, get, or uninstall without the view should fail
    for command in ["delete", "edit"]:
        func = getattr(view_handler, command)
        with pytest.raises(SystemExit):
            func(view_name)

    # Create the view!
    view_handler.create(view_name)

    # Ensure we have the view now!
    client.detect_views()
    assert view_name in client.views

    # Get the view from the client
    view = client.views[view_name]
    assert view.path == os.path.join(tmp_path, "views", "mpi") and os.path.exists(
        view.path
    )
    assert os.path.exists(view.config_path)

    # The config is loaded already at view._config
    assert view._config["view"]["name"] == view_name
    assert not view._config["view"]["modules"]
    assert not view._config["view"]["system_modules"]

    # Now install to it via the client
    client.install("ghcr.io/autamus/emacs:27.2")
    client.view_install(view_name, "ghcr.io/autamus/emacs:27.2")

    # Ensure it was created and as a symlink
    assert view._config["view"]["modules"]
    assert "ghcr.io/autamus/emacs:27.2" in view._config["view"]["modules"][0]

    module_path = os.path.join(view.path, "emacs")
    assert os.path.exists(module_path)

    if module_sys == "lmod":
        assert ".version" in os.listdir(module_path)

    # Find the module extension installed
    module_file = [x for x in os.listdir(module_path) if x != ".version"]
    assert module_file
    module_file = os.path.join(module_path, module_file[0])
    assert os.path.islink(module_file)

    client.view_uninstall(view_name, "ghcr.io/autamus/emacs:27.2", force=True)

    # The view should be removed
    assert "emacs" not in os.listdir(os.path.join(view.path))

    # But not the module!
    assert "ghcr.io" in os.listdir(client.settings.module_base)
    assert "autamus" in os.listdir(os.path.join(client.settings.module_base, "ghcr.io"))
    assert "emacs" in os.listdir(
        os.path.join(client.settings.module_base, "ghcr.io", "autamus")
    )

    # Before adding any attributes, this file should not exist
    assert not os.path.exists(view.module_path)

    # Shared function to check view and handler
    check_view(view, view_handler)

    # Ensure we can uninstall
    view_handler.delete(view_name, force=True)
    assert not os.path.exists(view.path)

    # Test re-creating from file
    views_config = os.path.join(here, "testdata", "view.yaml")
    view_client.create_from_file(
        view_name, views_config, settings_file=client.settings.settings_file, force=True
    )


@pytest.mark.parametrize(
    "module_sys,module_file,container_tech,remote",
    [
        ("lmod", "module.lua", "singularity", True),
        ("lmod", "module.lua", "podman", True),
        ("tcl", "module.tcl", "singularity", True),
        ("tcl", "module.tcl", "podman", True),
        ("lmod", "module.lua", "singularity", False),
        ("lmod", "module.lua", "podman", False),
        ("tcl", "module.tcl", "singularity", False),
        ("tcl", "module.tcl", "podman", False),
    ],
)
def test_view_components(tmp_path, module_sys, module_file, container_tech, remote):
    """
    Test view components
    """
    client = init_client(str(tmp_path), module_sys, container_tech, remote=remote)

    # Create the view handler based on the client settings file
    view_handler = views.ViewsHandler(
        settings_file=client.settings.settings_file, module_sys=module_sys
    )

    # A view name
    view_name = "mpi"
    assert view_name not in client.views

    # Create the view!
    view_handler.create(view_name)
    client.detect_views()
    assert view_name in client.views

    # Before adding any attributes, this file should not exist
    view = client.views[view_name]
    assert not os.path.exists(view.module_path)

    check_view(view, view_handler)

    # Ensure we can uninstall
    view_handler.delete(view_name, force=True)
    assert not os.path.exists(view.path)


def check_view(view, view_handler):
    """
    Shared function for checking content of view.
    """
    # Try adding valid attributes
    for attribute, check_content in [
        ["system_modules", None],
        ["depends_on", "depends"],
    ]:
        assert not view._config["view"][attribute]
        view_handler.add_variable(view.name, attribute, "openmpi")
        assert os.path.exists(view.module_path)

        # Make sure we have openmpi in the content
        content = utils.read_file(view.module_path)
        assert "openmpi" in content
        if check_content:
            assert check_content in content

        # Reload the view config file
        view.reload()
        assert "openmpi" in view._config["view"][attribute]

        # We can't add unknown variables
        with pytest.raises(SystemExit):
            view_handler.add_variable(view.name, attribute.replace("_", "-"), [1, 2, 3])

        # Try removing now
        view_handler.remove_variable(view.name, attribute, "openmpi")
        view.reload()
        assert not view._config["view"][attribute]
        content = utils.read_file(view.module_path)
        assert "openmpi" not in content
        if check_content:
            assert check_content not in content
