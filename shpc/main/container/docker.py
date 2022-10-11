__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021-2022, Vanessa Sochat"
__license__ = "MPL 2.0"


import json
import os
import sys
from datetime import datetime

import shpc.main.templates
import shpc.main.wrappers
import shpc.utils
from shpc.logger import logger

from .base import ContainerTechnology


class DockerContainer(ContainerTechnology):
    """
    A Docker container controller.
    """

    # The module technology adds extensions here
    templatefile = "docker"
    command = "docker"
    features = {"home": {str: "[use-self]"}}

    def __init__(self):
        if shpc.utils.which(self.command)["return_code"] != 0:
            logger.exit(
                "%s is required to use the '%s' base."
                % (self.command.capitalize(), self.command)
            )
        super(DockerContainer, self).__init__()

    @property
    def shell_path(self):
        """
        Return the path of the shell to use with this container.
        """
        return self.settings.docker_shell

    def shell(self, image):
        """
        Interactive shell into a container image.
        """
        os.system(
            "%s run -it --rm --entrypoint %s %s"
            % (self.command, self.shell_path, image)
        )

    def add_registry(self, uri):
        """
        Given a "naked" name, add the registry if it's Docker Hub
        """
        # Is this a core library container, or Docker Hub without prefix?
        if uri.count("/") == 0:
            uri = "docker.io/library/%s" % uri
        elif uri.count("/") == 1:
            uri = "docker.io/%s" % uri
        return uri

    def registry_pull(self, module_dir, container_dir, config, tag):
        """
        Pull a container to the library.
        """
        pull_type = config.get_pull_type()
        if pull_type != "docker":
            logger.exit("%s only supports Docker (oci registry) pulls." % self.command)

        tag_uri = "%s:%s" % (self.add_registry(config.docker), tag.name)
        tag_digest = "%s@%s" % (self.add_registry(config.docker), tag.digest)
        self.pull(tag_digest)
        # Podman doesn't keep a record of digest->tag, so we tag after
        return self.tag(tag_digest, tag_uri)

    def pull(self, uri):
        """
        Pull a unique resource identifier.
        """
        res = shpc.utils.run_command([self.command, "pull", uri], stream=True)
        if res["return_code"] != 0:
            logger.exit("There was an issue pulling %s" % uri)
        return uri

    def tag(self, image, tag_as):
        """
        Given a container URI, tag as something else.
        """
        res = shpc.utils.run_command([self.command, "tag", image, tag_as])
        if res["return_code"] != 0:
            logger.exit("There was an issue tagging %s as %s" % (image, tag_as))
        return tag_as

    def inspect(self, image):
        """
        Inspect an image
        """
        res = shpc.utils.run_command([self.command, "inspect", image])
        if res["return_code"] != 0:
            logger.exit("There was an issue getting the manifest for %s" % image)
        raw = res["message"]
        return json.loads(raw)

    def exists(self, image):
        """
        Exists is a derivative of inspect that just determines existence.
        """
        if not image:
            return False
        res = shpc.utils.run_command([self.command, "inspect", image])
        if res["return_code"] != 0:
            return False
        return True

    def get(self, module_name):
        """
        Determine if a container uri exists.
        """
        # If no module tag provided, try to deduce from install tree
        full_name = self.guess_tag(module_name, allow_fail=True)

        # The user already provided a tag
        if not full_name:
            full_name = module_name

        uri = self.add_registry(full_name)
        # If there isn't a tag in the name, add it back
        if ":" not in uri:
            uri = ":".join(uri.rsplit("/", 1))
        if uri and self.exists(uri):
            return uri

    def delete(self, image):
        """
        Delete a container when a module is deleted.
        """
        container = self.get(image)

        # If we can't get a specific image, the user wants to delete all tags
        # and we have more than one tag!
        if not container:
            tags = self.installed_tags(image)
            containers = ["%s:%s" % (image, tag) for tag in tags]
        else:
            containers = [container]

        for container in containers:
            if self.exists(container):
                shpc.utils.run_command([self.command, "rmi", "--force", container])

    def check(self, module_name, config):
        """
        Given a module name, check if it's the latest version.
        """
        # Case 1: a specific tag is selected
        image = self.get(module_name)
        if self.exists(image):
            tag = image.split(":")[-1]
            if tag == config.latest.name:
                logger.info("⭐️ tag %s is up to date. ⭐️" % config.tag.name)
            else:
                logger.exit(
                    "👉️ tag %s can be updated to %s! 👈️"
                    % (module_name, config.latest.name)
                )

    def test_script(self, image, test_script):
        """
        Given a test file, run it and respond accordingly.
        """
        command = [
            "docker",
            "run",
            "-i",
            "--entrypoint",
            "/bin/bash",
            "-t",
            image,
            test_script,
        ]
        result = shpc.utils.run_command(command)

        # Return code
        return result["return_code"]

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

        # Ensure that the container exists
        # Do we want to clean up other versions here too?
        manifest = self.inspect(module.container_path)
        if not manifest:
            sys.exit(
                "Container %s was not found. Was it pulled?" % module.container_path
            )

        labels = manifest[0].get("Labels", {})

        # Option to create wrapper scripts for commands
        aliases = module.config.get_aliases()
        wrapper_scripts = []

        # Wrapper scripts can be global (for aliases) or container specific
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
            shell=self.shell_path,
            aliases=aliases,
            features=features,
            labels=labels,
            creation_date=datetime.now(),
            command=self.command,
            module=module,
            parsed_name=module.config.name,
            wrapper_scripts=wrapper_scripts,
        )
        shpc.utils.write_file(module_path, out)
