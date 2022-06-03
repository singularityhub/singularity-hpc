__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2022, Vanessa Sochat"
__license__ = "MPL 2.0"

from shpc.logger import logger
from jinja2 import Environment, FileSystemLoader
import shpc.utils
import os

here = os.path.dirname(os.path.abspath(__file__))
default_templates = os.path.join(here, "templates")


class WrapperScript:
    """
    The base class of a wrapper script provides basic wrapper script functionality,
    which can be extended for custom named wrapper scripts.
    """

    def __init__(
        self, wrapper_template, settings, image, container=None, config=None, **kwargs
    ):
        self.settings = settings
        self.container = container
        self.config = config
        self.kwargs = kwargs
        self.image = image
        self.template_type = "custom"
        if not wrapper_template:
            logger.exit("A wrapper template is required to generate a wrapper script.")
        self.wrapper_template = wrapper_template

    @property
    def container_dest_dir(self):
        return os.path.dirname(self.image)

    @property
    def container_dir(self):
        """
        Source of container.yaml
        """
        return os.path.dirname(self.config.package_file)

    @property
    def module_dir(self):
        """
        Get the module directory (should error if not provided in kwargs)
        """
        return self.kwargs["module_dir"]

    def get_template_paths(self, include_container_dir):
        """
        Establishes the list of paths in which to search the templates and their dependencies
        """

        # Where to find the template and the files it may include
        # Lowest precedence: default location shipped with shpc
        template_paths = [default_templates]

        # Optionally, (higher precedence) a user-defined global location
        if self.settings.wrapper_scripts.get("templates"):
            path = self.settings.wrapper_scripts["templates"]
            if not os.path.exists(path):
                logger.exit(
                    "%s designated as a templates directory, but it does not exist."
                    % path
                )
            template_paths = [path] + template_paths

        # Optionally, (even higher precedence) the directory of container.yaml
        if include_container_dir:
            template_paths = [self.container_dir] + template_paths

        return template_paths

    def find_wrapper_script(self, template_paths):
        """
        Finds the exact, absolute, path of the template, given a list of search directories
        """

        # If the given wrapper path is absolute, confirm it exists
        if os.path.isabs(self.wrapper_template):
            if not os.path.exists(self.wrapper_template):
                logger.exit(
                    "%s designated as a template wrapper script, but it does not exist."
                    % self.wrapper_template
                )
            return self.wrapper_template

        else:
            # Otherwise, check that the template wrapper is found in one of the
            # search paths
            for template_path in template_paths:
                template_file = os.path.join(template_path, self.wrapper_template)
                if os.path.exists(template_file):
                    return template_file
            else:
                logger.exit(
                    "%s not found in %s."
                    % (self.wrapper_template, ", ".join(template_paths))
                )

    def load_template(self, include_container_dir=False):
        """
        Load the wrapper template.
        """

        template_paths = self.get_template_paths(include_container_dir)
        template_file = self.find_wrapper_script(template_paths)
        # Once the full path of the template wrapper has been determined, add
        # its own directory to the search (highest precedence) to honour its
        # possible inclusions
        template_paths = [os.path.dirname(template_file)] + template_paths
        loader = FileSystemLoader(template_paths)
        env = Environment(loader=loader)
        self.template = env.get_template(self.wrapper_template)

    def generate(self, wrapper_name, alias_definition):
        """
        Template generation function.
        NB: alias_definition is a dictionary for command aliases, and a string
        for additional arbitrary commands
        """

        # Write scripts into container directory
        wrapper_dir = os.path.join(self.module_dir, "bin")
        shpc.utils.mkdirp([wrapper_dir])
        wrapper_path = os.path.join(wrapper_dir, wrapper_name)

        out = self.template.render(
            alias=alias_definition,
            container=self.container,
            settings=self.settings,
            image=self.image,
            config=self.config,
            # includes module_dir, features, etc
            **self.kwargs
        )
        shpc.utils.write_file(wrapper_path, out, exec=True)

        # Return the alias / script name
        return [os.path.basename(wrapper_path)]
