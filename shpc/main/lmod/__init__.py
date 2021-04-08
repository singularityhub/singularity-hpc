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
import subprocess
import sys

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
        if not os.path.exists(template_file):
            template_file = os.path.abspath(template_name)
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

    def _test_setup(self, tmpdir):
        """
        Setup tests, including changes to settings or test directory
        """
        self.settings.set("lmod_base", tmpdir)

    def _test(self, module_name, module_dir, tag, template="test.sh"):
        """
        Run specific tests for this module
        """
        # Generate a test template
        template = self._load_template(template)
        test_file = os.path.join(module_dir, "test.sh")

        # Generate the test script
        out = template.render(
            module_dir=module_dir,
            version=tag,
            module_name=module_name,
        )
        utils.write_file(test_file, out)
        return subprocess.call(["/bin/bash", test_file])

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

    def get(self, module_name):
        """
        Get the path to a container for a module
        """
        module_dir = os.path.join(self.settings.lmod_base, module_name)

        # A container must be present
        sif = glob("%s%s*.sif" % (module_dir, os.sep))
        if not sif:
            logger.exit(
                "%s is not a module tag folder, or does not have a sif binary."
                % module_name
            )

        # Currently we only allow one container per module folder
        if len(sif) > 1:
            logger.exit("Found more than one sif in module folder.")
        return sif[0]

    def list(self, pattern=None, names_only=False, out=None):
        """
        List installed modules.
        """
        self._list_modules(
            self.settings.lmod_base, "module.lua", pattern, names_only, out
        )

    def inspect(self, module_name):
        """
        Return complete metadata for the user from a container.
        """
        module_dir = os.path.join(self.settings.lmod_base, module_name)
        if not os.path.exists(module_dir):
            logger.exit("%s does not exist." % module_dir)

        sif = self.get(module_name)
        return self._container.inspect(sif[0])

    def _list_modules(self, base, filename, pattern=None, names_only=False, out=None):
        """A shared function to list modules or registry entries."""
        out = out or sys.stdout
        modules = self._get_module_lookup(base, filename, pattern)

        # The user can request to list only names, which is useful to find modules
        for module_name, versions in modules.items():
            if names_only:
                out.write("%s\n" % module_name)
            else:
                out.write("%s: %s\n" % (module_name, ", ".join(versions)))

    def _get_module_lookup(self, base, filename, pattern=None):
        """A shared function to get a lookup of installed modules or registry entries"""
        modules = {}
        for fullpath in utils.recursive_find(base, pattern):
            if fullpath.endswith(filename):
                module_name, version = os.path.dirname(fullpath).rsplit(os.sep, 1)
                module_name = module_name.replace(base, "").strip(os.sep)
                if module_name not in modules:
                    modules[module_name] = set()
                modules[module_name].add(version)
        return modules

    def check(self, module_name):
        """
        Given a module name, check if the latest is installed.

        If the user provides a top level folder, assume we want to look
        at updates for entire tags. If a specific folder is provided with
        a container, check the digest.
        """
        # If a tag is provided, convert to directory
        module_name = module_name.replace(":", os.sep)

        # We derive the current version installed from the container
        # We assume the user has provided the correct prefix
        module_dir = os.path.join(self.settings.lmod_base, module_name)
        if not os.path.exists(module_dir):
            logger.exit(
                "%s does not exist. Is this a known registry entry?" % module_dir
            )

        # Case 1: a specific tag is selected
        sif = self.get(module_name)
        if sif:
            return self._check_digest(module_name, sif)

        return self._check_tags(module_name)

    def _check_tags(self, module_name):
        """
        Check if the installed tag is the latest.
        """
        # Derive the registry entry from the module_name
        config = self._load_container(module_name)
        dirname = os.path.join(self.settings.lmod_base, module_name)

        # Does the user have the modules installed?
        if not os.path.exists(dirname):
            logger.exit("%s is not installed." % module_name)

        # Compare the latest name to the version folders
        versions = os.listdir(dirname)
        if config.latest.name not in versions:
            logger.exit(
                "The latest tag is %s, but you have: %s."
                % (config.latest.name, ", ".join(versions))
            )
        else:
            logger.info("⭐️ latest tag %s is up to date. ⭐️" % config.latest.name)

    def _check_digest(self, module_name, sif):
        """
        Check if there is an updated digest for a tag.

        At this point we assume only one container per install, as older containers
        are cleaned up to save filesystem space. If this is changed, we would
        need another way to deduce what version of the container is installed.
        """
        sif = os.path.basename(sif)

        # The prefix of the image is the module_name (which includes version here)
        prefix = module_name.replace(os.sep, "-") + "-"
        digest = sif.replace(prefix, "").replace(".sif", "")

        # Get the latest version digest, remove the tag first
        docker = os.sep.join(module_name.split(os.sep)[:-1])
        tag = module_name.split(os.sep)[-1]
        config = self._load_container(docker)

        # Get the tag
        tag = config.tags.get(tag)
        if not tag:
            logger.exit("Tag %s is not present in the registry entry." % tag)

        if tag.digest == digest:
            logger.info("⭐️ tag %s is up to date. ⭐️" % tag.name)
        else:
            logger.exit("👉️ tag %s requires an update! 👈️" % tag.name)

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
        elif pull_type == "gh":
            container_uri = "gh://%s/%s:%s" % (config.gh, tag.digest, tag.name)

        # Pull new containers (this doesn't clean up old ones, which we might want to do)
        if not os.path.exists(container_path):
            self._container.pull(container_uri, container_path)

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
        return container_path

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
