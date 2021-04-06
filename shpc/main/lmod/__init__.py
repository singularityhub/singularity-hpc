__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021, Vanessa Sochat"
__license__ = "MPL 2.0"

from shpc.main.client import Client as BaseClient
from shpc.logger import logger
from datetime import datetime
import shpc.utils as utils
from jinja2 import Template

from glob import glob
import os
import shutil

here = os.path.dirname(os.path.abspath(__file__))


class Client(BaseClient):
    def __init__(self, **kwargs):
        """
        An Lmod client generates an lmod recipe for install
        """
        super(Client, self).__init__(**kwargs)

    @staticmethod
    def _load_template(template_name="template.lua"):
        """
        Load the default lmod template
        """
        template_file = os.path.join(here, template_name)
        with open(template_file, "r") as temp:
            template = Template(temp.read())
        return template

    def uninstall(self, name, force=False):
        """
        Given a unique resource identifier, uninstall a module
        """
        # The name can either be a folder or an install directory
        module_dir = os.path.join(self.settings.lmod_base, name)

        if os.path.exists(module_dir) and not force:
            msg = "%s, and all content below it? " % name
            if utils.confirm_uninstall(msg, force):
                shutil.rmtree(module_dir)
        elif os.path.exists(module_dir) and force:
            shutil.rmtree(module_dir)
        logger.info("%s and all subdirectories have been removed," % name)

    def add(self, sif, module_name):
        """
        Add a container directly as a module
        """
        registry_dir = self.settings.registry

        # Ensure the container exists
        sif = os.path.abspath(sif)
        if not os.path.exists(sif):
            logger.exit("%s does not exist." % sif)

        # First ensure that we aren't using a known namespace
        for subfolder in module_name.split("/"):
            registry_dir = os.path.join(registry_dir, subfolder)
            if os.path.exists(registry_dir):
                logger.exit(
                    "%s is a known registry namespace, choose another for a custom addition."
                    % subfolder
                )

        module_dir = os.path.join(self.settings.lmod_base, module_name)
        if not os.path.exists(module_dir):
            os.makedirs(module_dir)

        # Name the container appropriately
        name = module_name.replace("/", "-")
        digest = utils.get_file_hash(sif)
        dest = os.path.join(module_dir, "%s-sha256:%s.sif" % (name, digest))
        shutil.move(sif, dest)
        self._install(module_dir, dest, name)
        logger.info("Module %s was created." % (module_name))

    def install(self, name, tag=None):
        """
        Given a unique resource identifier, install a recipe.

        For lmod, this means creating a subfolder in modules, pulling the
        container to it, and writing a module file there. We've already
        grabbed the name from docker (which is currently the only supported).
        """
        config = self._load_container(name, tag)

        # The chosen tag is set for the config (or defaults to latest)
        if not config.tag:
            logger.exit(
                "%s is not a known identifier. Choices are:\n%s"
                % (name, "\n".join(config.tags.keys()))
            )

        # We currently support gh or docker
        uri = getattr(config, "docker") or getattr(config, "gh")
        pull_type = "docker" if getattr(config, "docker") else "gh"

        # This is a tag object with name and digest
        tag = config.tag

        # Pull the container to the module directory
        module_dir = os.path.join(self.settings.lmod_base, uri, tag.name)

        if not os.path.exists(module_dir):
            os.makedirs(module_dir)

        # Preserve name and version of container if it's ever moved
        container_path = os.path.join(
            module_dir, "%s-%s-%s.sif" % (config.name, tag.name, tag.digest)
        )

        # We pull by the digest
        if pull_type == "docker":
            container_uri = "docker://%s@%s" % (config.docker, tag.digest)
            pull = self._container.pull
        elif pull_type == "gh":
            container_uri = "gh://%s/%s:%s" % (config.gh, tag.digest, tag.name)
            pull = self._container.pull_gh

        # Pull new containers (this doesn't clean up old ones, which we might want to do)
        if not os.path.exists(container_path):
            pull(container_uri, container_path)

        # Exit early if there is an issue
        if not os.path.exists(container_path):
            logger.exit("There was an issue pulling %s" % container_path)

        # prepare aliases
        aliases = config.get_aliases()

        self._install(
            module_dir,
            container_path,
            name,
            aliases,
            url=config.url,
            description=config.description,
            version=tag.name,
        )
        logger.info("Module %s/%s was created." % (config.name, tag.name))

    def _install(
        self,
        module_dir,
        container_path,
        name,
        aliases=None,
        template_name="template.lua",
        url=None,
        description=None,
        version=None,
    ):
        """Install a general container path to a module

        The module_dir should be created by the calling function, and
        the container should already be added to the module directory. In
        the case of install this means we did a pull from a registry,
        and for add we moved the container there explicitly.
        """
        module_path = os.path.join(module_dir, "module.lua")

        # Remove any previous containers
        for older in glob("%s%s*.sif" % (module_path, os.sep)):
            if older == container_path:
                continue
            os.remove(older)

        # Get inspect metadata from the container (only if singularity installed
        try:
            metadata = self._container.inspect(container_path)

            # Add labels, and deffile
            labels = metadata.get("attributes", {}).get("labels")
            deffile = (
                metadata.get("attributes", {}).get("deffile", "").replace("\n", "\\n")
            )
        except:
            metadata = None
            logger.warning("Singularity is not installed, skipping metadata.")

        # Get the template
        template = self._load_template(template_name)

        # Make sure to render all values!
        out = template.render(
            singularity_module=self.settings.singularity_module,
            singularity_shell=self.settings.singularity_shell,
            bindpaths=self.settings.bindpaths,
            container_sif=container_path,
            description=description,
            aliases=aliases,
            url=url,
            version=version,
            module_dir=module_dir,
            labels=labels,
            deffile=deffile,
            prefix=self.settings.lmod_exc_prefix,
            creation_date=datetime.now(),
            name=name,
            flatname=name.replace("/", "-"),
        )
        utils.write_file(module_path, out)
