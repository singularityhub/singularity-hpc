__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021-2022, Vanessa Sochat"
__license__ = "MPL 2.0"

import errno
import hashlib
import json
import os
import re
import shutil
import stat
import tempfile

from shpc.logger import logger

try:
    from ruamel_yaml import YAML
except:
    from ruamel.yaml import YAML


def can_be_deleted(path, ignore_files=None):
    """
    A path can be deleted if it contains no entries, *or*
    if the only files are in ignore_files
    """
    ignore_files = ignore_files or []
    if os.path.exists(path):
        entries = os.listdir(path)
        if not entries:
            return True
        if set(ignore_files).issuperset(entries):
            return True
    return False


def creation_date(filename):
    """
    Get the creation date, and fallback to modified date.
    """
    stat = os.stat(filename)
    try:
        return stat.st_birthtime
    except AttributeError:
        return stat.st_mtime


def mkdirp(dirnames):
    """
    Create one or more directories
    """
    for dirname in dirnames:
        mkdir_p(dirname)


def mkdir_p(path):
    """
    Make a directory path if it does not exist, akin to mkdir -p
    """
    try:
        os.makedirs(path)
    except OSError as e:
        if e.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            logger.exit("Error creating path %s, exiting." % path)


def remove_to_base(path, base_path):
    """
    Delete the tree under $path and all the parents
    up to $base_path as long as they are empty
    """
    if not os.path.isdir(base_path):
        logger.exit("Error: %s is not a directory" % base_path)
    if not path.startswith(base_path):
        logger.exit("Error: %s is not a parent of %s" % (base_path, path))

    if os.path.islink(path) or os.path.isfile(path):
        os.unlink(path)
    elif os.path.isdir(path):
        shutil.rmtree(path)

    # If directories above it are empty, remove
    while path != base_path:
        if os.path.exists(path):
            if not can_be_deleted(path, [".version"]):
                break
            shutil.rmtree(path)
        path = os.path.dirname(path)


def get_tmpfile(tmpdir=None, prefix=""):
    """
    Get a temporary file with an optional prefix.
    """

    # First priority for the base goes to the user requested.
    tmpdir = get_tmpdir(tmpdir)

    # If tmpdir is set, add to prefix
    if tmpdir:
        prefix = os.path.join(tmpdir, os.path.basename(prefix))

    fd, tmp_file = tempfile.mkstemp(prefix=prefix)
    os.close(fd)

    return tmp_file


def get_tmpdir(tmpdir=None, prefix="", create=True):
    """
    Get a temporary directory for an operation.
    """
    tmpdir = tmpdir or tempfile.gettempdir()
    prefix = prefix or "shpc-tmp"
    prefix = "%s.%s" % (prefix, next(tempfile._get_candidate_names()))
    tmpdir = os.path.join(tmpdir, prefix)

    if not os.path.exists(tmpdir) and create is True:
        os.mkdir(tmpdir)

    return tmpdir


def recursive_find(base, pattern=None):
    """
    Find filenames that match a particular pattern, and yield them.
    """
    # We can identify modules by finding module.lua
    for root, folders, files in os.walk(base):
        for file in files:
            fullpath = os.path.abspath(os.path.join(root, file))

            if pattern and not re.search(pattern, fullpath):
                continue
            yield fullpath


def get_file_hash(image_path, algorithm="sha256"):
    """
    Return an sha256 hash of the file based on a criteria level.
    """
    try:
        hasher = getattr(hashlib, algorithm)()
    except AttributeError:
        logger.error("%s is an invalid algorithm.")
        logger.exit(" ".join(hashlib.algorithms_guaranteed))

    with open(image_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def copyfile(source, destination, force=True):
    """
    Copy a file from a source to its destination.
    """
    # Case 1: It's already there, we aren't replacing it :)
    if source == destination and force is False:
        return destination

    # Case 2: It's already there, we ARE replacing it :)
    if os.path.exists(destination) and force is True:
        os.remove(destination)

    shutil.copyfile(source, destination)
    return destination


def write_file(filename, content, mode="w", exec=False):
    """
    Write content to a filename
    """
    with open(filename, mode) as filey:
        filey.writelines(content)
    if exec:
        st = os.stat(filename)

        # Execute / search permissions for the user and others
        os.chmod(filename, st.st_mode | stat.S_IEXEC | stat.S_IXGRP | stat.S_IXOTH)
    return filename


def write_json(json_obj, filename, mode="w"):
    """
    Write json to a filename
    """
    with open(filename, mode) as filey:
        filey.writelines(print_json(json_obj))
    return filename


def print_json(json_obj):
    """
    Print json pretty
    """
    return json.dumps(json_obj, indent=4, separators=(",", ": "))


def write_yaml(obj, filename):
    """
    Save yaml to file, also preserving comments.
    """
    yaml = YAML()
    yaml.preserve_quotes = True

    with open(filename, "w") as fd:
        yaml.dump(obj, fd)


def read_yaml(filename):
    """
    Load a yaml from file, roundtrip to preserve comments
    """
    yaml = YAML()
    with open(filename, "r") as fd:
        content = yaml.load(fd.read())
    return content


def read_file(filename, mode="r"):
    """
    Read a file.
    """
    with open(filename, mode) as filey:
        content = filey.read()
    return content


def read_json(filename, mode="r"):
    """
    Read a json file to a dictionary.
    """
    return json.loads(read_file(filename))
