__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021, Vanessa Sochat"
__license__ = "MPL 2.0"

from shpc.main.client import Client as BaseClient
from shpc.logger import logger
from datetime import datetime
import shpc.utils as utils
from jinja2 import Template
import json
import os

here = os.path.dirname(os.path.abspath(__file__))


class Client(BaseClient):
    def __init__(self, **kwargs):
        """
        An Lmod client generates an lmod recipe for install
        """
        super(Client, self).__init__(**kwargs)

    @staticmethod
    def _load_template():
        """
        Load the default lmod template
        """
        template_file = os.path.join(here, "template.lua")
        with open(template_file, "r") as temp:
            template = Template(temp.read())
        return template

    def install(self, name, tag=None):
        """
        Given a unique resource identifier, install a recipe.

        For lmod, this means creating a subfolder in modules, pulling the
        container to it, and writing a module file there. We've already
        grabbed the name from docker (which is currently the only supported).
        """
        config = self._load_container(name, tag)

        # If a tag is not defined, use latest. This is a dict with name/hash
        tag = tag or config.latest.name

        # The tag must be defined in the config
        if tag not in config.tags:
            logger.exit("%s is not a known tag." % tag)

        # A tag object with a name and digest
        tag = config.tags.get(tag)

        # Pull the container to the module directory
        module_dir = os.path.join(self.settings.lmod_base, name, tag.name)
        if not os.path.exists(module_dir):
            os.makedirs(module_dir)

        # Preserve name and version of container if it's ever moved
        container_path = os.path.join(
            module_dir, "%s-%s-%s.sif" % (name, tag.name, tag.digest)
        )
        module_path = os.path.join(module_dir, "module.lua")

        # We pull by the digest
        container_uri = "docker://%s@%s" % (name, tag.digest)

        # Pull new containers (this doesn't clean up old ones, which we might want to do)
        if not os.path.exists(container_path):
            self._container.pull(container_uri, container_path)

        # Get the template
        template = self._load_template()

        # Make sure to render all values!
        out = template.render(
            singularity_module=self.settings.singularity_module,
            singularity_shell=self.settings.singularity_shell,
            bindpaths=self.settings.bindpaths,
            container_sif=container_path,
            description=config.description,
            aliases=dict(config.aliases),
            url=config.url,
            version=tag.name,
            module_dir=module_dir,
            creation_date=datetime.now(),
            name=name,
        )
        utils.write_file(module_path, out)
        logger.info("Module %s/%s is created." % (name, tag.name))
