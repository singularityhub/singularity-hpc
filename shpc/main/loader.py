__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021-2022, Vanessa Sochat"
__license__ = "MPL 2.0"

from jinja2.exceptions import TemplateNotFound
from jinja2 import FileSystemLoader
from jinja2.loaders import split_template_path
from jinja2.utils import open_if_exists
import posixpath
import os


class CustomLoader(FileSystemLoader):
    """
    A custom loader will support providing a custom string, but also
    includes within that. We do that by subclassing a FileSystemLoader,
    which allows you to create a Jinja2 environment to load from a path.
    E.g.,:

    Example
    -------
    from jinja2 import Environment

    # Allow includes from this directory OR providing strings
    template_dir = os.path.join(root, "templates")
    env = Environment(loader=loader.CustomLoader(template_dir))

    # Load from a string
    with open(template_file, "r") as temp:
        template = env.get_template(self.substitute(temp.read()))

    # Load from a filepath
    template = env.get_template("includes/snippet.html")
    """

    def get_source(self, environment, template):
        """
        get_source first assumes looking for a file. If we get to the bottom
        and cannot find it, assume a template and return the loaded template.
        """
        pieces = split_template_path(template)
        for searchpath in self.searchpath:
            # Use posixpath even on Windows to avoid "drive:" or UNC
            # segments breaking out of the search directory.
            filename = posixpath.join(searchpath, *pieces)
            f = open_if_exists(filename)
            if f is None:
                continue
            try:
                contents = f.read().decode(self.encoding)
            finally:
                f.close()

            mtime = os.path.getmtime(filename)

            def uptodate() -> bool:
                try:
                    return os.path.getmtime(filename) == mtime
                except OSError:
                    return False

            # Use normpath to convert Windows altsep to sep.
            return contents, os.path.normpath(filename), uptodate

        # Not perfect, but a way to guess it's not a template!
        if "{%" not in template and "{{" not in template:
            raise TemplateNotFound(template)
        return template, None, None
