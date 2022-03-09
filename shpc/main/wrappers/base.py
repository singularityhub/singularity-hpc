__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2022, Vanessa Sochat"
__license__ = "MPL 2.0"

from shpc.logger import logger
from jinja2 import Environment, FileSystemLoader
import shpc.utils
import os

here = os.path.dirname(os.path.abspath(__file__))
templates = os.path.join(here, "templates")


class WrapperScript:
    """
    The base class of a wrapper script provides basic wrapper script functionality,
    which can be extended for custom named wrapper scripts.
    """

    def __init__(
        self,
        settings,
        image,
        container=None,
        config=None,
        wrapper_template=None,
        **kwargs
    ):
        """
        On init, a wrapper_template should be provided (string) OR the class
        should have an attribute.
        """
        self.settings = settings
        self.container = container
        self.config = config
        self.kwargs = kwargs
        self.image = image
        self.template_type = "custom"
        if not wrapper_template and not hasattr(self, "wrapper_template"):
            logger.exit("A wrapper template is required to generate a wrapper script.")
        if not hasattr(self, "wrapper_template") and wrapper_template:
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

    def load_template(self):
        """
        Load the wrapper template.
        """
        # Contender with the container dir
        contender = os.path.join(self.container_dir, self.wrapper_template)

        # First shot - it already exists
        template_file = None
        if os.path.exists(self.wrapper_template):
            template_file = self.wrapper_template

        # Second shot - it belongs with the container
        elif os.path.exists(contender):
            template_file = contender

        # Finally, it has to be in the template directory
        if not template_file:
            template_file = os.path.join(templates, self.wrapper_template)

        if not os.path.exists(template_file):
            logger.exit(
                "%s not found as default, container, or custom script."
                % self.wrapper_template
            )

        self.template_file = template_file

        # Default to search here in template file path, then in templates
        template_paths = [os.path.dirname(template_file), templates]

        # Do we have a custom template path directory?
        if self.settings.wrapper_scripts.get("templates"):
            path = self.settings.wrapper_scripts["templates"]
            if not os.path.exists(path):
                logger.exit(
                    "%s designated as a templates directory, but it does not exist."
                    % path
                )
            template_paths = [path] + template_paths

        loader = FileSystemLoader(template_paths)
        env = Environment(loader=loader)
        self.template = env.get_template(os.path.basename(template_file))

    def generate_aliases(self):
        """
        Generate looping over aliases
        """
        self.load_template()

        # Write scripts into container directory
        wrapper_dir = os.path.join(self.module_dir, "bin")
        shpc.utils.mkdirp([wrapper_dir])

        generated = []
        # When we get here we know we have aliases!
        for alias in self.kwargs["aliases"]:
            wrapper_path = os.path.join(wrapper_dir, alias["name"])
            self._generate(wrapper_path, alias)
            generated.append(os.path.basename(wrapper_path))

        return generated

    def _generate(self, wrapper_path, alias):
        """
        Shared generation function.
        """
        out = self.template.render(
            alias=alias,
            container=self.container,
            settings=self.settings,
            image=self.image,
            config=self.config,
            # includes module_dir, features, aliases
            **self.kwargs
        )
        shpc.utils.write_file(wrapper_path, out, exec=True)

        # Return the alias / script name
        return os.path.basename(wrapper_path)

    def generate(self, alias):
        """
        A default generation cannot know what the template wants, so we give it everything.
        """
        self.load_template()

        # Write scripts into container directory
        wrapper_dir = os.path.join(self.module_dir, "bin")
        shpc.utils.mkdirp([wrapper_dir])
        wrapper_path = os.path.join(wrapper_dir, alias)
        return [self._generate(wrapper_path, alias)]
