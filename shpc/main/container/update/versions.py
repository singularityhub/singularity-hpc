__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021-2022, Vanessa Sochat"
__license__ = "MPL 2.0"

from distutils.version import LooseVersion
import re


class TaggedLooseVersion(LooseVersion):
    """
    A tagged loose version allows for version comparison without failure.
    Given that a comparison fails, we simply tag it for removal. We also
    do custom parsing of the version string for common patterns of container
    tags to derive a more meaningful version.
    """

    def __init__(self, vstring=None):
        if vstring:
            self.parse(vstring)

        # Additional set of tags for labeling
        self.tags = set()

    @property
    def major_minor(self):
        if self._major_minor:
            return ".".join(str(x) for x in self._major_minor)

    def parse(self, vstring):
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

        components = [x for x in self.component_re.split(vstring) if x and x != "."]
        for i, obj in enumerate(components):
            try:
                components[i] = int(obj)
            except ValueError:
                pass

        # If we have > 2 components, try to save a major/minor
        self._major_minor = None
        if len(components) >= 2:
            self._major_minor = components[0:2]
        self.version = components

    def is_comparable(self):
        """
        An item is comparable if it's not all string. We don't have a meaningufl
        way to compare things that are all strings.
        """
        all_string = True
        for comp in self.version:
            if not isinstance(comp, str):
                all_string = False
        return not all_string

    def _cmp(self, other):
        if isinstance(other, str):
            other = LooseVersion(other)

        # Figure out if either version cannot be compared
        if not self.is_comparable():
            self.tags.add("remove")
            return -1
        if not other.is_comparable():
            other.tags.add("remove")
            return -1

        # When we get here, we assume comparable!
        if self.version == other.version:
            return 0
        if self.version < other.version:
            return -1
        if self.version > other.version:
            return 1


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

    # Remove any tagged to remove or known tags
    versions = [x for x in versions if "remove" not in x.tags]

    # Now only take the top major / minor of each
    filtered = []
    seen = set()
    for version in versions:
        # Keep all that don't have major or minor
        if not version.major_minor:
            filtered.append(version)

        # if we have a version major minor, only add if we haven't seen it
        if version.major_minor is not None and version.major_minor not in seen:
            filtered.append(version)
            seen.add(version.major_minor)

    # these are sorted with newest at top, so we cut off top
    if len(filtered) > max_length:
        filtered = filtered[0:max_length]
    return filtered
