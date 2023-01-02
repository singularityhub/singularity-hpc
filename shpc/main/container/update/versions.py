__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021-2023, Vanessa Sochat"
__license__ = "MPL 2.0"

import re
from distutils.version import LooseVersion


def not_all_letters(version):
    """
    Helper function to determine if a string is all lowercase letters.
    This is unlikely to be a commit.
    """
    return re.sub("([a-z])+", "", version) != ""


def only_lowercase_letters_numbers(version):
    """
    Return True if the string is only lowercase letters and numbers.
    """
    return re.sub("([0-9]|[a-z])+", "", version) == ""


def filter_versions(tags, filters=None, max_length=5):
    """
    Given a list of tags, filter down to the latest up to a max length.

    Parameters
    ----------
    tags (list)      : a listing of string tags
    filters (list)   : an optional list of string filters
    max_length (int) : the max number to return (latest)
    """
    filters = filters or []
    if tags and filters:
        for pattern in filters:
            tags = [x for x in tags if re.search(pattern, x)]

    # Convert to TaggedLooseVersion
    versions = [TaggedLooseVersion(x) for x in tags]

    # The sorting will tag a subset with "remove" that aren't sortable
    # This has latest at the top
    versions.sort(reverse=True)

    # Now only take the top major / minor of each
    filtered = []
    seen = set()

    for version in versions:

        # Do not allow any raw strings that look like commits
        # We check for length, and replacing lowercase letters / numbers is empty
        if (
            len(version.vstring) >= 10
            and not_all_letters(version.vstring)
            and only_lowercase_letters_numbers(version.vstring)
        ):
            continue

        # Keep all that don't have major or minor
        if not version.major_minor and not version.major:
            filtered.append(version)

        # if we have a version major minor, only add if we haven't seen it
        if version.major_minor is not None and version.major_minor not in seen:
            filtered.append(version)
            seen.add(version.major_minor)
            seen.add(version.major)

        elif version.major is not None and version.major not in seen:
            filtered.append(version)
            seen.add(version.major)

    # these are sorted with newest at top, so we cut off top
    if len(filtered) > max_length:
        filtered = filtered[0:max_length]
    return filtered


class TaggedLooseVersion(LooseVersion):
    """
    A tagged loose version allows for version comparison without failure.
    Given that a comparison fails, we simply tag it for removal. We also
    do custom parsing of the version string for common patterns of container
    tags to derive a more meaningful version.
    """

    def __init__(self, vstring=None):

        # Additional set of tags for labeling
        self.tags = set()
        self.version = []
        if vstring:
            self.parse(vstring)

    @property
    def major_minor(self):
        if self._major_minor:
            return ".".join(str(x) for x in self._major_minor)

    @property
    def major(self):
        if self._major:
            return ".".join(str(x) for x in self._major)

    def parse(self, vstring):
        """
        Parse a version string (vstring) into pieces. Strings are added as tags.
        """
        self.vstring = vstring

        # Do a custom parsing for weird biocontainers versions
        if "--" in vstring and "_" in vstring:
            start, rest = vstring.split("--", 1)
            ending = rest.split("_", 1)[-1]

            # '0.1.19.10'
            vstring = "%s.%s" % (start, ending)

        # If we get here and still have -- replace with .
        if "--" in vstring:
            vstring = vstring.replace("--", ".")
        if "-" in vstring:
            vstring = vstring.replace("-", ".")

        contenders = [x for x in self.component_re.split(vstring) if x and x != "."]
        components = []

        # Add non-numerical components as tags
        for obj in contenders:
            try:
                components.append(int(obj))
            except ValueError:
                self.tags.add(obj)
                pass

        # If we have > 2 components, try to save a major/minor
        self._major_minor = None
        self._major = None

        # more strict considers duplicate of major "the same"
        if len(components) >= 1:
            self._major = components[0:1]
        if len(components) >= 2:
            self._major_minor = components[0:2]
        self.version = components

    def _cmp(self, other):
        if isinstance(other, str):
            other = LooseVersion(other)

        # We can only compare matching types
        shortest = min(len(other.version), len(self.version))

        for i in range(shortest):
            this_version = self.version[i]
            other_version = other.version[i]

            if type(this_version) != type(other_version):
                continue

            if this_version == other_version:
                continue
            elif this_version < other_version:
                return -1
            elif this_version > other_version:
                return 1

        # If we get to the bottom, consider equal
        return 0
