__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021-2022, Vanessa Sochat"
__license__ = "MPL 2.0"


import os

from jinja2 import Environment, FileSystemLoader

here = os.path.dirname(os.path.abspath(__file__))

# Allow includes from this directory OR providing strings
template_dir = os.path.join(here, "templates")
env = Environment(loader=FileSystemLoader(template_dir))


class Template:
    """
    Supporting functions for loading any kind of module template
    """

    def __init__(self, settings):
        self.settings = settings

    def get(self, template_name):
        """
        Get a template from templates
        """
        template_file = os.path.join(here, "templates", template_name)
        if not os.path.exists(template_file):
            template_file = os.path.abspath(template_name)
        return template_file

    def load(self, template_name):
        """
        Load the default module template.
        """
        template_file = self.get(template_name)

        with open(template_file, "r") as temp:
            template = env.from_string(self.substitute(temp.read()))
        return template

    def substitute(self, template):
        """
        For all known identifiers, substitute user specified format strings.
        """
        subs = {
            "{|module_name|}": self.settings.module_name or "{{ parsed_name.tool }}"
        }
        for key, replacewith in subs.items():
            template = template.replace(key, replacewith)
        return template
