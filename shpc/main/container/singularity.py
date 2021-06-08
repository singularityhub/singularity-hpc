__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021, Vanessa Sochat"
__license__ = "MPL 2.0"


from shpc.logger import logger
import shpc.utils
from .base import ContainerTechnology, ContainerName

from datetime import datetime
from glob import glob
import re
import os
import shutil


class SingularityContainer(ContainerTechnology):
    """
    A Singularity container controller.

    All container controllers should have the same general interface.
    """

    # The module technology adds extensions here
    templatefile = "singularity"

    # Singularity container features
    features = {"gpu": {"nvidia": "--nv", "amd": "--rocm"}}

    def __init__(self):
        try:
            from spython.main import Client

            self.client = Client
        except:
            logger.exit("singularity python (spython) is required to use singularity.")
        super(SingularityContainer, self).__init__()

    def exists(self, module_name):
        """
        A derivate of get to return boolean about container existence.
        """
        # This can be the module or container directory
        container_dir = self.container_dir(module_name)

        # A container must be present
        return True if glob("%s%s*.sif" % (container_dir, os.sep)) else False

    def get(self, module_name, env_file=False):
        """
        Get the path to a container for a module
        """
        module_name = self.guess_tag(module_name)

        # This can be the module or container directory
        container_dir = self.container_dir(module_name)

        # A container must be present
        sif = glob("%s%s*.sif" % (container_dir, os.sep))
        if not sif:
            logger.exit(
                "%s is not a known tag, or does not have a sif binary." % module_name
            )

        # Currently we only allow one container per module folder
        if len(sif) > 1:
            logger.exit("Found more than one sif in module folder.")
        return sif[0]

    def add(self, sif, module_name, modulefile, template, **kwargs):
        """
        Manually add a registry container.
        """
        # Ensure the container exists
        sif = os.path.abspath(sif)
        if not os.path.exists(sif):
            logger.exit("%s does not exist." % sif)

        # First ensure that we aren't using a known namespace
        for registry_dir, _ in self.iter_registry():
            for subfolder in module_name.split("/"):
                registry_dir = os.path.join(registry_dir, subfolder)
                if os.path.exists(registry_dir):
                    logger.exit(
                        "%s is a known registry namespace, choose another for a custom addition."
                        % subfolder
                    )

        # The user can have a different container directory defined
        container_dir = self.container_dir(module_name)
        module_path = os.path.join(container_dir, modulefile)
        shpc.utils.mkdirp([container_dir])

        # Name the container appropriately
        name = module_name.replace("/", "-")
        digest = shpc.utils.get_file_hash(sif)
        dest = os.path.join(container_dir, "%s-sha256:%s.sif" % (name, digest))
        shutil.copyfile(sif, dest)

        # Parse the module name for the user
        parsed_name = ContainerName(module_name)

        self.install(
            module_path,
            dest,
            module_name,
            template,
            parsed_name=parsed_name,
            features=kwargs.get("features"),
        )
        self.add_environment(container_dir, {}, self.settings.environment_file)
        logger.info("Module %s was created." % (module_name))

    def install(
        self,
        module_path,
        container_path,
        name,
        template,
        parsed_name,
        aliases=None,
        template_name=None,
        url=None,
        description=None,
        config_features=None,
        features=None,
        version=None,
    ):
        """Install a general container path to a module

        The module_dir should be created by the calling function, and
        the container should already be added to the module directory. In
        the case of install this means we did a pull from a registry,
        and for add we moved the container there explicitly.
        """
        # Container features are defined in container.yaml and the settings
        # and specific values are determined by the container technology
        features = self.get_features(
            config_features, self.settings.container_features, features
        )

        # Remove any previous containers
        for older in glob("%s%s*.sif" % (module_path, os.sep)):
            if older == container_path:
                continue
            os.remove(older)

        # Get inspect metadata from the container (only if singularity installed
        try:
            metadata = self.inspect(container_path)

            # Add labels, and deffile
            labels = metadata.get("attributes", {}).get("labels")
            deffile = (
                metadata.get("attributes", {}).get("deffile", "").replace("\n", "\\n")
            )
        except:
            metadata = None
            deffile = None
            labels = {}
            logger.warning("Singularity is not installed, skipping metadata.")

        # Make sure to render all values!
        out = template.render(
            singularity_module=self.settings.singularity_module,
            singularity_shell=self.settings.singularity_shell,
            bindpaths=self.settings.bindpaths,
            container_sif=container_path,
            description=description,
            aliases=aliases,
            url=url,
            features=features,
            version=version,
            module_dir=os.path.dirname(module_path),
            labels=labels,
            deffile=deffile,
            creation_date=datetime.now(),
            name=name,
            tool=parsed_name.tool,
            registry=parsed_name.registry,
            repository=parsed_name.repository,
            envfile=self.settings.environment_file,
        )
        shpc.utils.write_file(module_path, out)

    def registry_pull(self, module_dir, container_dir, config, tag):
        """
        Given a module directory, container config, and tag, pull the container
        """
        pull_type = "docker" if getattr(config, "docker") else "gh"

        # Preserve name and version of container if it's ever moved
        container_path = os.path.join(
            container_dir, "%s-%s-%s.sif" % (config.flatname, tag.name, tag.digest)
        )

        # We pull by the digest
        if pull_type == "docker":
            container_uri = "docker://%s@%s" % (config.docker, tag.digest)
        elif pull_type == "gh":
            container_uri = "gh://%s/%s:%s" % (config.gh, tag.digest, tag.name)

        # Pull new containers
        if not os.path.exists(container_path):
            self.pull(container_uri, container_path)

        # Exit early if there is an issue
        if not os.path.exists(container_path):
            container_path = None
        return container_path

    def check(self, module_name, config):
        """
        Given a module name, check if it's the latest version
        """
        # Case 1: a specific tag is selected
        if self.exists(module_name):
            image = self.get(module_name)
            return self._check_digest(module_name, image, config)
        return self._check_tags(module_name, config)

    def _check_tags(self, module_name, config):
        """
        Check if the installed tag is the latest.
        """
        # Derive the registry entry from the module_name
        dirname = os.path.join(self.settings.module_base, module_name)

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

    def _check_digest(self, module_name, image, config):
        """
        Check if there is an updated digest for a tag.

        At this point we assume only one container per install, as older containers
        are cleaned up to save filesystem space. If this is changed, we would
        need another way to deduce what version of the container is installed.
        """
        sif = os.path.basename(image)

        # The prefix of the image is the module_name (which includes version here)
        prefix = re.sub("(:|[/])", "-", module_name) + "-"
        digest = sif.replace(prefix, "").replace(".sif", "")

        # Get the latest version digest, remove the tag first
        tag = module_name.split(":")[-1]

        # Get the tag
        tag = config.tags.get(tag)
        if not tag:
            logger.exit("Tag %s is not present in the registry entry." % tag)

        if tag.digest == digest:
            logger.info("⭐️ tag %s is up to date. ⭐️" % tag.name)
        else:
            logger.exit("👉️ tag %s requires an update! 👈️" % tag.name)

    def shell(self, image):
        """
        Interactive shell into a container image.
        """
        self.client.shell(image)

    def pull(self, uri, dest):
        """
        Pull a container to a destination
        """
        if re.search("^(docker|shub|https)", uri):
            return self._pull_regular(uri, dest)
        elif uri.startswith("gh://"):
            return self._pull_github(uri, dest)

    def _pull_regular(self, uri, dest):
        """
        Pull a URI that Singularity recognizes
        """
        pull_folder = os.path.dirname(dest)
        name = os.path.basename(dest)
        return self.client.pull(uri, name=name, pull_folder=pull_folder)

    def inspect(self, image):
        """
        Inspect an image and return metadata.
        """
        return self.client.inspect(image)

    def _pull_github(self, uri, dest=None):
        """
        Pull a singularity-deploy container to a destination
        """
        # Assemble the url based on the container uri
        uri = uri.replace("gh://", "", 1)

        # repository name and image prefix
        repo = "/".join(uri.split("/")[0:2])
        prefix = repo.replace("/", "-")

        # The tag includes release and contianer tag (e.g., 0.0.1:latest)
        tag = uri.replace(repo, "", 1).strip("/")
        github_tag, container_tag = tag.split(":", 1)

        # Assemble the artifact url
        url = "https://github.com/%s/releases/download/%s/%s.%s.sif" % (
            repo,
            github_tag,
            prefix,
            container_tag,
        )

        # If no destination, default to present working directory
        if not dest:
            dest = os.path.basename(url)
        name = os.path.basename(dest)
        return self.client.pull(url, name=name, pull_folder=os.path.dirname(dest))

    def test_script(self, image, test_script):
        """
        Given a test file, run it and respond accordingly.
        """
        command = ["singularity", "exec", image, "/bin/bash", test_script]
        result = shpc.utils.run_command(command)

        # We can't run on incompatible hosts
        if (
            "the image's architecture" in result["message"]
            and result["return_code"] != 0
        ):
            logger.warning(
                "Cannot run test for incompatible architecture: %s" % result["message"]
            )
            return 0

        # Return code
        return result["return_code"]
