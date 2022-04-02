__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021-2022, Vanessa Sochat"
__license__ = "MPL 2.0"

import difflib
from shpc.logger import LogColors


def print_diff(obj1: dict, obj2: dict):
    """
    Given two objects print a diff. Obj1 is the previous version, obj2 updated.
    Since we don't ever delete anything (just change) we print changed as
    yellow,
    """
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
