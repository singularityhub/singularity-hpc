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
from .helpers import here, init_client


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

    # Boolean
    assert client.settings.get("wrapper_scripts:enabled") == True
    client.settings.set("wrapper_scripts:enabled", False)
    assert client.settings.get("wrapper_scripts:enabled") == False
