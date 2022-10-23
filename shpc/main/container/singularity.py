__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021-2022, Vanessa Sochat"
__license__ = "MPL 2.0"


import os
import re
import shutil
from datetime import datetime
from glob import glob

import shpc.main.container.update as update
import shpc.main.wrappers
import shpc.utils as utils
from shpc.logger import logger

from .base import ContainerTechnology


class SingularityContainer(ContainerTechnology):
    """
    A Singularity container controller.

    All container controllers should have the same general interface.
    """

    # The module technology adds extensions here
    templatefile = "singularity"
    command = "singularity"

    # Singularity container features
    features = {
        "gpu": {"nvidia": "--nv", "amd": "--rocm"},
        "x11": {True: "~/.Xauthority", str: "[use-self]"},
        "home": {str: "[use-self]"},
    }

    def __init__(self):
        try:
            from spython.main import Client

            self.client = Client
        except Exception:
            logger.exit("singularity python (spython) is required to use singularity.")
        super(SingularityContainer, self).__init__()

    def exists(self, module_name):
        """
        A derivative of get to return boolean about container existence.
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

    def add(self, module_name, image, config, container_yaml, **kwargs):
        """
        Manually add a registry container, e.g., generating a container.yaml
        for an existing container file. container_yaml is the destination file.
        If it's already existing, it's loaded into config. Otherwise we are
        using a template config.
        """
        if ":" not in module_name:
            tag = "latest"
        else:
            module_name, tag = module_name.split(":", 1)

        # Cut out early if the tag isn't latest, and we already have it
        # DO NOT call config.tags here, it will add an empty latest
        if tag != "latest" and config._config and tag in config._config["tags"]:
            if not utils.confirm_action(
                "Tag %s already is defined, are you sure you want to overwrite it? "
                % tag
            ):
                return

        # Destination for container in registry
        dest_dir = os.path.dirname(container_yaml)
        utils.mkdir_p(dest_dir)

        # Add a docker (or local image) and return the config
        if image.startswith("docker://"):
            config = self._add_docker_image(
                module_name, tag, image, config, container_yaml, **kwargs
            )
        else:
            config = self._add_local_image(
                module_name, tag, image, config, container_yaml, **kwargs
            )

        # Final save of config, and tell the user we're done!
        config.save(container_yaml)
        logger.info(
            "Registry entry %s was added! Before shpc install, edit:" % module_name
        )
        print(container_yaml)
        return container_yaml

    def _add_local_image(self, name, tag, image, config, container_yaml, **kwargs):
        """
        A subtype of "add" that adds a local image, e.g.,:

        shpc add <container.sif> <uri>
        """
        if not os.path.exists(image):
            logger.exit(f"{image} does not exist.")

        digest = utils.get_file_hash(image)

        # Destination for container in registry
        dest_dir = os.path.dirname(container_yaml)

        # The destination container in the registry folder
        container_digest = "sha256:%s" % digest
        container_name = "%s.sif" % container_digest
        dest_container = os.path.join(dest_dir, container_name)

        # Update the config path and latest
        config.set("path", container_name)
        config.set("latest", {tag: container_digest})
        config.add_tag(tag, container_digest)

        # Only copy if it's not there yet (enforces naming by hash)
        if not os.path.exists(dest_container):
            shutil.copyfile(image, dest_container)
        return config

    def _add_docker_image(self, name, tag, image, config, container_yaml, **kwargs):
        """
        A subtype of "add" that adds a docker URI, e.g.,:

        shpc add docker://vanessa/salad
        shpc add docker://vanessa/salad dinosaur/salad
        TODO need to test if different URI will work
        """
        # Container name should not have tag
        container_name = image.replace("docker://", "").split(":", 1)[0]
        tags = update.get_container_tag(container_name, tag)

        # Update the config path and latest
        config.set("docker", container_name)
        config.set("latest", tags)
        config.add_tag(tag, tags[tag])
        return config

    def install(self, module_path, template, module, features=None):
        """Install a general container path to a module

        The module_dir should be created by the calling function, and
        the container should already be added to the module directory. In
        the case of install this means we did a pull from a registry,
        and for add we moved the container there explicitly.
        """
        # Container features are defined in container.yaml and the settings
        # and specific values are determined by the container technology
        features = self.get_features(
            module.config.features, self.settings.container_features, features
        )

        # Remove any previous containers
        container_dir = os.path.dirname(module.container_path)
        for older in glob("%s%s*.sif" % (container_dir, os.sep)):
            if older == module.container_path:
                continue
            os.remove(older)

        # Get inspect metadata from the container (only if singularity installed
        try:
            metadata = self.inspect(module.container_path)

            # Add labels, and deffile
            labels = metadata.get("attributes", {}).get("labels")
            deffile = (
                metadata.get("attributes", {}).get("deffile", "").replace("\n", "\\n")
            )
        except Exception:
            metadata = None
            deffile = None
            labels = {}

        # Option to create wrapper scripts for commands
        aliases = module.config.get_aliases()

        # Wrapper scripts can be global (for aliases) or container specific
        wrapper_scripts = []
        if self.settings.wrapper_scripts["enabled"] is True:
            wrapper_scripts = shpc.main.wrappers.generate(
                aliases=aliases,
                module_dir=module.module_dir,
                features=features,
                container=self,
                image=module.container_path,
                config=module.config,
            )

        # Make sure to render all values!
        out = template.render(
            settings=self.settings,
            aliases=aliases,
            features=features,
            labels=labels,
            deffile=deffile,
            creation_date=datetime.now(),
            module=module,
            parsed_name=module.config.name,
            wrapper_scripts=wrapper_scripts,
        )
        utils.write_file(module_path, out)

    def registry_pull(self, module_dir, container_dir, config, tag):
        """
        Given a module directory, container config, and tag, pull the container
        """
        pull_type = config.get_pull_type()

        # Preserve name and version of container if it's ever moved
        container_path = os.path.join(
            container_dir, "%s-%s-%s.sif" % (config.flatname, tag.name, tag.digest)
        )

        # We pull by the digest
        if pull_type in ["docker", "oras"]:
            container_uri = "%s://%s@%s" % (
                pull_type,
                config.docker or config.oras,
                tag.digest,
            )
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
        if re.search("^(docker|shub|https|oras)", uri):
            return self._pull_regular(uri, dest)
        elif uri.startswith("gh://"):
            return self._pull_github(uri, dest)

    def _pull_regular(self, uri, dest):
        """
        Pull a URI that Singularity recognizes
        """
        pull_folder = os.path.dirname(dest)
        name = os.path.basename(dest)
        image, lines = self.client.pull(
            uri, name=name, pull_folder=pull_folder, stream=True
        )
        for line in lines:
            print(line, end="")
        return image

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

        # The tag includes release and container tag (e.g., 0.0.1:latest)
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
        command = [self.command, "exec", image, "/bin/bash", test_script]
        result = utils.run_command(command)

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
