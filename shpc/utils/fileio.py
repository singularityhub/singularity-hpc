__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021, Vanessa Sochat"
__license__ = "MPL 2.0"

import hashlib
import errno
import os
import pwd
import shutil
import tempfile

import json
from shpc.logger import logger


def mkdir_p(path):
    """mkdir_p attempts to get the same functionality as mkdir -p
    :param path: the path to create.
    """
    try:
        os.makedirs(path)
    except OSError as e:
        if e.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            logger.exit("Error creating path %s, exiting." % path)


def get_tmpfile(requested_tmpdir=None, prefix=""):
    """
    Get a temporary file with an optional prefix.

    Parameters
    ==========
    requested_tmpdir: an optional requested temporary directory, first
    prefix: Given a need for a sandbox (or similar), prefix the file
    with this string.
    """

    # First priority for the base goes to the user requested.
    tmpdir = get_tmpdir(requested_tmpdir)

    # If tmpdir is set, add to prefix
    if tmpdir:
        prefix = os.path.join(tmpdir, os.path.basename(prefix))

    fd, tmp_file = tempfile.mkstemp(prefix=prefix)
    os.close(fd)

    return tmp_file


def get_tmpdir(requested_tmpdir=None, prefix="", create=True):
    """Get a temporary directory for an operation.

    Parameters
    ==========
    requested_tmpdir: an optional requested temporary directory, first
    priority as is coming from calling function.
    prefix: Given a need for a sandbox (or similar), we will need to
    create a subfolder *within* the SREGISTRY_TMPDIR.
    create: boolean to determine if we should create folder (True)
    """
    from sregistry.defaults import SREGISTRY_TMPDIR

    # First priority for the base goes to the user requested.
    tmpdir = requested_tmpdir or SREGISTRY_TMPDIR

    prefix = prefix or "shpc-tmp"
    prefix = "%s.%s" % (prefix, next(tempfile._get_candidate_names()))
    tmpdir = os.path.join(tmpdir, prefix)

    if not os.path.exists(tmpdir) and create is True:
        os.mkdir(tmpdir)

    return tmpdir


def get_userhome():
    """get the user home based on the effective uid"""
    return pwd.getpwuid(os.getuid())[5]


def get_file_hash(image_path, algorithm="sha256"):
    """return an md5 hash of the file based on a criteria level. This
    is intended to give the file a reasonable version.

    Parameters
    ==========
    image_path: full path to the singularity image

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
    """copy a file from a source to its destination."""
    # Case 1: It's already there, we aren't replacing it :)
    if source == destination and force is False:
        return destination

    # Case 2: It's already there, we ARE replacing it :)
    if os.path.exists(destination) and force is True:
        os.remove(destination)

    shutil.copyfile(source, destination)
    return destination


def write_file(filename, content, mode="w"):
    """write_file will open a file, "filename" and write content, "content"
    and properly close the file
    """
    with open(filename, mode) as filey:
        filey.writelines(content)
    return filename


def write_json(json_obj, filename, mode="w", print_pretty=True):
    """write_json will (optionally,pretty print) a json object to file

    Parameters
    ==========
    json_obj: the dict to print to json
    filename: the output file to write to
    pretty_print: if True, will use nicer formatting
    """
    with open(filename, mode) as filey:
        if print_pretty:
            filey.writelines(print_json(json_obj))
        else:
            filey.writelines(json.dumps(json_obj))
    return filename


def print_json(json_obj):
    """just dump the json in a "pretty print" format"""
    return json.dumps(json_obj, indent=4, separators=(",", ": "))


def read_file(filename, mode="r", readlines=False):
    """write_file will open a file, "filename" and write content, "content"
    and properly close the file
    """
    with open(filename, mode) as filey:
        if readlines is True:
            content = filey.readlines()
        else:
            content = filey.read()
    return content


def read_json(filename, mode="r"):
    """read_json reads in a json file and returns
    the data structure as dict.
    """
    return json.load(read_file(fiename))
