#!/usr/bin/python

# Copyright (C) 2021 Vanessa Sochat.

# This Source Code Form is subject to the terms of the
# Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed
# with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
import shutil
import os

import shpc.main.container as container

here = os.path.dirname(os.path.abspath(__file__))
root = os.path.dirname(here)


def test_pull_gh(tmp_path):
    """Test a singularity container command"""
    cli = container.SingularityContainer()

    # Test default Singularity pull
    image = os.path.join(str(tmp_path), "busybox.sif")
    result = cli.pull("docker://busybox", image)
    assert os.path.exists(result)

    # Test singularity pull from GitHub
    image = os.path.join(str(tmp_path), "latest.sif")
    result = cli.pull("gh://singularityhub/singularity-deploy/0.0.1:latest", image)
    assert os.path.exists(result)
