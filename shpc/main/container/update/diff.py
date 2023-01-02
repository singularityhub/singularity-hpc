__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021-2023, Vanessa Sochat"
__license__ = "MPL 2.0"

import difflib

from shpc.logger import LogColors


def print_diff(obj1: dict, obj2: dict, consider_order=False):
    """
    Given two objects print a diff. Obj1 is the previous version, obj2 updated.
    Since we don't ever delete anything (just change) we remove those that
    are unchanged first, and print them at the bottom (in white). Deletions
    are printed in red, and additions in green. If consider_order is True, a
    tag that is the same (but in a different location) can show up as added.
    If consider_order is False, we remove them first and print at the bottom
    in white to indicate not changed.
    """
    unchanged = {}

    # First look for tags in the first that aren't in the second - we aren't deleting them
    if not consider_order:
        unchanged = set(obj1.keys()).difference(obj2.keys())
        unchanged = {k: obj1[k] for k in unchanged}
        obj1 = {k: v for k, v in obj1.items() if k not in unchanged}

    obj1_content = ["%s:%s" % (k, v) for k, v in obj1.items()]
    obj2_content = ["%s:%s" % (k, v) for k, v in obj2.items()]

    # Since the sorting can be weird (and we don't want to show up as deletion)
    # just remove from both if no change!
    intersect = set(obj1_content).intersection(obj2_content)
    obj2_content = [x for x in obj2_content if x not in intersect]
    obj1_content = [x for x in obj1_content if x not in intersect]

    for line in difflib.ndiff(obj1_content, obj2_content):

        # What looks like a new tag or addition
        if line.startswith("+"):
            print(f"{LogColors.OKGREEN}{line}{LogColors.ENDC}")

        # Deleted (the replaced digests)
        elif line.startswith("-"):
            print(f"{LogColors.RED}{line}{LogColors.ENDC}")

    # No change!
    for line in intersect:
        print(line)
    for name, digest in unchanged.items():
        print("%s:%s" % (name, digest))
