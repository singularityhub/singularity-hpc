#!/usr/bin/python

# Copyright (C) 2021 Vanessa Sochat.

# This Source Code Form is subject to the terms of the
# Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed
# with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

import os
import shutil
import pytest


def test_write_read_files(tmp_path):
    """test_write_read_files will test the functions write_file and read_file"""
    print("Testing utils.write_file...")
    from shpc.utils import write_file

    tmpfile = str(tmp_path / "written_file.txt")
    assert not os.path.exists(tmpfile)
    write_file(tmpfile, "hello!")
    assert os.path.exists(tmpfile)

    print("Testing utils.read_file...")
    from shpc.utils import read_file

    content = read_file(tmpfile)
    assert content == "hello!"


def test_write_bad_json(tmp_path):
    from shpc.utils import write_json

    bad_json = {"Wakkawakkawakka'}": [{True}, "2", 3]}
    tmpfile = str(tmp_path / "json_file.txt")
    assert not os.path.exists(tmpfile)
    with pytest.raises(TypeError):
        write_json(bad_json, tmpfile)


def test_write_json(tmp_path):
    import json
    from shpc.utils import write_json, read_json

    good_json = {"Wakkawakkawakka": [True, "2", 3]}
    tmpfile = str(tmp_path / "good_json_file.txt")

    assert not os.path.exists(tmpfile)
    write_json(good_json, tmpfile)
    with open(tmpfile, "r") as f:
        content = json.loads(f.read())
    assert isinstance(content, dict)
    assert "Wakkawakkawakka" in content
    content = read_json(tmpfile)
    assert "Wakkawakkawakka" in content


def test_check_install():
    """check install is used to check if a particular software is installed.
    If no command is provided, singularity is assumed to be the test case"""
    print("Testing utils.check_install")
    from shpc.utils import check_install

    is_installed = check_install("echo")
    assert is_installed
    is_not_installed = check_install("fakesoftwarename")
    assert not is_not_installed


def test_get_installdir():
    """get install directory should return the base of where shpc
    is installed
    """
    print("Testing utils.get_installdir")
    from shpc.utils import get_installdir

    whereami = get_installdir()
    print(whereami)
    assert whereami.endswith("shpc")


def test_run_command():
    print("Testing utils.run_command")
    from shpc.utils import run_command

    result = run_command(["echo", "hello"])
    assert result["message"] == "hello\n"
    assert result["return_code"] == 0


def test_which():
    print("Testing utils.which")
    from shpc.utils import which

    result = which("echo")
    assert result["message"].endswith("echo")
    assert result["return_code"] == 0
    result = which("singularityaaaa")
    assert result["message"] == ""
    assert result["return_code"] == 1


def test_get_file_hash():
    print("Testing utils.get_file_hash")
    from shpc.utils import get_file_hash

    here = os.path.dirname(os.path.abspath(__file__))
    testdata = os.path.join(here, "testdata", "hashtest.txt")
    assert (
        get_file_hash(testdata)
        == "6bb92117bded3da774363713657a629a9f38eac2e57cd47e1dcda21d3445c67d"
    )
    assert get_file_hash(testdata, "md5") == "e5d376ca96081dd561ff303c3a631fd5"


def test_copyfile(tmp_path):
    print("Testing utils.copyfile")
    from shpc.utils import copyfile, write_file

    original = str(tmp_path / "location1.txt")
    dest = str(tmp_path / "location2.txt")
    print(original)
    print(dest)
    write_file(original, "CONTENT IN FILE")
    copyfile(original, dest)
    assert os.path.exists(original)
    assert os.path.exists(dest)


def test_get_tmpdir_tmpfile():
    print("Testing utils.get_tmpdir, get_tmpfile")
    from shpc.utils import get_tmpdir, get_tmpfile

    tmpdir = get_tmpdir()
    assert os.path.exists(tmpdir)
    assert os.path.basename(tmpdir).startswith("shpc")
    shutil.rmtree(tmpdir)
    tmpdir = get_tmpdir(prefix="name")
    assert os.path.basename(tmpdir).startswith("name")
    shutil.rmtree(tmpdir)
    tmpfile = get_tmpfile()
    assert "shpc" in tmpfile
    os.remove(tmpfile)
    tmpfile = get_tmpfile(prefix="pancakes")
    assert "pancakes" in tmpfile
    os.remove(tmpfile)


def test_mkdir_p(tmp_path):
    print("Testing utils.mkdir_p")
    from shpc.utils import mkdir_p

    dirname = str(tmp_path / "input")
    result = os.path.join(dirname, "level1", "level2", "level3")
    mkdir_p(result)
    assert os.path.exists(result)


def test_print_json():
    print("Testing utils.print_json")
    from shpc.utils import print_json

    result = print_json({1: 1})
    assert result == '{\n    "1": 1\n}'
