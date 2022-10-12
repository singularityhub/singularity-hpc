__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2022, Vanessa Sochat"
__license__ = "MPL 2.0"

import os
import shutil
from shpc.logger import logger


class Module:
    def __init__(self, name):
        """
        New module metadata and shared functions.

        This should be created by base.py new_module to ensure the same
        container and settings are carried forward here.
        """
        self.name = name

        # Cache variable properties
        self._uri = None
        self._container_dir = None
        self._container_path = None

    @property
    def tagged_name(self):
        name = self.name
        if ":" not in name:
            name = "%s:%s" % (name, self.tag.name)
        return name

    def add_environment(self):
        """
        Write the environment to the module directory.
        """
        self.container.add_environment(
            self.module_dir,
            envars=self.config.get_envars(),
            environment_file=self.settings.environment_file,
        )

    def validate_tag_exists(self):
        """
        Ensure that a provided module name (and tag) exists.
        """
        if not self.config.tag:
            logger.exit(
                "%s is not a known identifier. Choices are:\n%s"
                % (self.name, "\n".join(self.config.tags.keys()))
            )

    def load_override_file(self):
        self.config.load_override_file(self.tag.name)

    @property
    def container_dir(self):
        """
        Derive the module container directory.
        """
        if not self._container_dir:
            # Pull the container to the module directory OR container base
            self._container_dir = self.container.container_dir(self.module_basepath)
        return self._container_dir

    @property
    def container_path(self):
        """
        Derive the container path, if possible.
        """
        if self._container_path:
            return self._container_path

        # If we have a sif URI provided by path, the container needs to exist
        if self.config.path:
            self._container_path = os.path.join(
                self.config.entry.dirname, self.config.path
            )
            if not os.path.exists(self._container_path):
                logger.exit(
                    "Expected container defined by path %s not found in %s."
                    % (self.config.path, self.config.entry.dirname)
                )
            container_dest = os.path.join(self.container_dir, self.config.path)

            # Note that here we are *duplicating* the container, assuming we
            # cannot use a link, and the registry won't be deleted but the
            # module container might!
            if not os.path.exists(container_dest):
                shutil.copyfile(self._container_path, container_dest)
            self._container_path = container_dest

        # For Singularity this is a path, podman is a uri. If None is returned
        # there was an error and we cleanup
        if not self._container_path:
            self._container_path = self.container.registry_pull(
                self.module_dir, self.container_dir, self.config, self.tag
            )
        return self._container_path

    @property
    def tag(self):
        """
        Pass forward the tag defined in the config.
        """
        return self.config.tag

    def check(self):
        """
        Check to see if the module version installed is up to date.
        """
        return self.container.check(self.name, self.config)

    @property
    def uri(self):
        """
        Get the uri for the module, docker / path / oras / gh
        """
        if self._uri:
            return self._uri

        # We currently support gh, docker, path, or oras
        uri = self.config.get_uri()

        # If we have a path, the URI comes from the name
        if ".sif" in uri:
            uri = self.name.split(":", 1)[0]
        self._uri = uri
        return uri

    @property
    def module_dir(self):
        """
        Full path to the module directory.
        """
        return os.path.join(self.settings.module_base, self.module_basepath)

    @property
    def module_basepath(self):
        """
        Path of only the module name and tag.
        """
        return os.path.join(self.uri, self.tag.name)
