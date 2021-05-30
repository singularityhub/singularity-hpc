__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021, Vanessa Sochat"
__license__ = "MPL 2.0"


from shpc.logger import logger
from .base import ContainerTechnology
import shpc.main.templates
import shpc.utils

from datetime import datetime
import json
import os
import sys


class PodmanContainer(ContainerTechnology):
    """
    A Podman container controleer.
    """

    # The module technology adds extensions here
    templatefile = "podman"

    # Podman doesn't have flags for gpu, requires
    # https://www.redhat.com/en/blog/how-use-gpus-containers-bare-metal-rhel-8
    features = {}

    def __init__(self):
        if shpc.utils.which("podman")["return_code"] != 0:
            logger.exit("podman is required to use the podman base.")
        super(PodmanContainer, self).__init__()

    def shell(self, image):
        """
        Interactive shell into a container image.
        """
        os.system(
            "podman run -it --rm --entrypoint %s %s"
            % (self.settings.podman_shell, image)
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
        Pull a container to the podman library
        """
        pull_type = "docker" if getattr(config, "docker") else "gh"
        if pull_type != "docker":
            logger.exit("podman only supports Docker (oci registry) pulls.")

        # Podman doesn't keep a record of digest->tag, so we use tag
        uri = "%s:%s" % (self.add_registry(config.docker), tag.name)
        return self.pull(uri)

    def pull(self, uri):
        """
        Pull a unique resource identifier.
        """
        res = shpc.utils.run_command(["podman", "pull", uri], stream=True)
        if res["return_code"] != 0:
            logger.exit("There was an issue pulling %s" % uri)
        return uri

    def inspect(self, image):
        """
        Inspect an image
        """
        res = shpc.utils.run_command(["podman", "inspect", image])
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
        res = shpc.utils.run_command(["podman", "inspect", image])
        if res["return_code"] != 0:
            return False
        return True

    def get(self, module_name):
        """
        Determine if a container uri exists.
        """
        # If no module tag provided, try to deduce from install tree
        module_name = self.guess_tag(module_name)

        uri = self.add_registry(module_name)
        # If there isn't a tag in the name, add it back
        if ":" not in uri:
            uri = ":".join(uri.rsplit("/", 1))
        if uri and self.exists(uri):
            return uri

    def delete(self, image):
        """
        Delete a container when a module is deleted.
        """
        image = self.get(image)
        if self.exists(image):
            shpc.utils.run_command(["podman", "rmi", image])

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

    def install(
        self,
        module_path,
        container_path,
        name,
        template,
        parsed_name,
        aliases=None,
        url=None,
        description=None,
        version=None,
        config_features=None,
        features=None,
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

        # Ensure that the container exists
        # Do we want to clean up other versions here too?
        manifest = self.inspect(container_path)
        if not manifest:
            sys.exit("Container %s was not found. Was it pulled?" % container_path)

        labels = manifest[0].get("Labels", {})

        # If there's a tag in the name, don't use it
        name = name.split(":", 1)[0]

        # Make sure to render all values!
        out = template.render(
            podman_module=self.settings.podman_module,
            bindpaths=self.settings.bindpaths,
            shell=self.settings.podman_shell,
            image=container_path,
            description=description,
            module_dir=os.path.dirname(module_path),
            aliases=aliases,
            url=url,
            features=features,
            version=version,
            labels=labels,
            prefix=self.settings.module_exc_prefix,
            creation_date=datetime.now(),
            name=name,
            tool=parsed_name.tool,
            registry=parsed_name.registry,
            namespace=parsed_name.namespace,
            envfile=self.settings.environment_file,
        )
        shpc.utils.write_file(module_path, out)
