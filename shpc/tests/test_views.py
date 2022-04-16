#!/usr/bin/python

# Copyright (C) 2022 Vanessa Sochat.

# This Source Code Form is subject to the terms of the
# Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed
# with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
import os

import shpc.main.modules.views as views

from .helpers import init_client


@pytest.mark.parametrize(
    "module_sys,module_file,container_tech",
    [
        ("lmod", "module.lua", "singularity"),
        ("lmod", "module.lua", "podman"),
        ("tcl", "module.tcl", "singularity"),
        ("tcl", "module.tcl", "podman"),
    ],
)
def test_views(tmp_path, module_sys, module_file, container_tech):
    """
    Test views:

    create
    install
    uninstall
    delete
    """
    client = init_client(str(tmp_path), module_sys, container_tech)

    # Create the view handler based on the client settings file
    view_handler = views.ViewsHandler(settings_file=client.settings.settings_file)

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
    client.install("ghcr.io/autamus/emacs:27.2", view=view_name)

    # Ensure it was created and as a symlink
    assert view._config["view"]["modules"]
    assert "ghcr.io/autamus/emacs:27.2" in view._config["view"]["modules"][0]

    module_path = os.path.join(view.path, "emacs")
    assert os.path.exists(module_path)
    assert ".version" in os.listdir(module_path)

    # Find the module extension installed
    module_file = [x for x in os.listdir(module_path) if x != ".version"]
    assert module_file
    module_file = os.path.join(module_path, module_file[0])
    assert os.path.islink(module_file)

    client.uninstall("ghcr.io/autamus/emacs:27.2", view=view_name, force=True)

    # The view should be removed
    assert "emacs" not in os.listdir(os.path.join(view.path))

    # But not the module!
    assert "ghcr.io" in os.listdir(client.settings.module_base)
    assert "autamus" in os.listdir(os.path.join(client.settings.module_base, "ghcr.io"))
    assert "emacs" in os.listdir(
        os.path.join(client.settings.module_base, "ghcr.io", "autamus")
    )

    # Ensure we can uninstall
    view_handler.delete(view_name, force=True)
    assert not os.path.exists(view.path)
