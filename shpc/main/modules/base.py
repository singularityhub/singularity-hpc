__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021-2022, Vanessa Sochat"
__license__ = "MPL 2.0"

from shpc.main.client import Client as BaseClient
from shpc.logger import logger
import shpc.utils as utils
import shpc.defaults as defaults
import shpc.main.container as container
import shpc.main.modules.template as templatectl
import shpc.main.modules.views as views
import shpc.main.modules.versions as versionfile

from datetime import datetime
import os
import shutil
import subprocess
import sys
import inspect


class ModuleBase(BaseClient):
    def __init__(self, **kwargs):

        # Files for module software to generate depending on user setting
        super(ModuleBase, self).__init__(**kwargs)
        self.here = os.path.dirname(inspect.getfile(self.__class__))
        self.template = templatectl.Template(self.settings)
        self.versionfile = versionfile.VersionFile(self.settings, self.module_extension)
        self.detect_views()

    def detect_views(self):
        """
        Detect and load existing views into the module for easy interaction.
        """
        # Lookup of named views in the views base
        self.views = {}
        if not self.settings.views_base or not os.path.exists(self.settings.views_base):
            return

        # Load existing views
        for view_name in os.listdir(self.settings.views_base):
            self.views[view_name] = views.View(
                name=view_name,
                settings=self.settings,
                symlink_extension=self.symlink_extension,
                module_extension=self.module_extension,
                modulefile=self.modulefile,
            )

    @property
    def container_base(self):
        """
        Quickly return what is being used for the container base
        """
        if not self.settings.container_base:
            return self.settings.module_base
        return self.settings.container_base

    @property
    def modulefile(self):
        return "%s.%s" % (self.container.modulefile, self.module_extension)

    @property
    def templatefile(self):
        return "%s.%s" % (self.container.templatefile, self.module_extension)

    def uninstall(self, name, view=None, force=False):
        """
        Given a unique resource identifier, uninstall a module. If a view
        name is provided, assume we only want to uninstall from the view
        """
        # The name can either be a folder or an install directory
        name = self.add_namespace(name)

        # folder paths do not have :
        name = name.replace(":", os.sep)
        module_dir = os.path.join(self.settings.module_base, name)
        container_dir = self.container.container_dir(name)

        # We need to look for the module in all views and show to the user first
        views_with_module = set()

        # Only populate if the command is not directed to a view
        if not view:

            # If uninstalling the entire module, clean up symbolic links in all views
            for view_name, entry in self.views.items():
                if entry.exists(module_dir):
                    views_with_module.add(view_name)

        # Ask before deleting anything!
        if not force:
            msg = name + "?"
            if views_with_module:
                msg += (
                    "\nThis will uninstall the module from views:\n  %s\nAre you sure?"
                    % "\n  ".join(views_with_module)
                )
            if not utils.confirm_uninstall(msg, force):
                return

        # Only uninstall from the view
        if view:
            if view not in self.views:
                logger.exit("View %s does not exist, cannot uninstall." % view)
            return self.views[view].uninstall(module_dir)

        # Podman needs image deletion
        self.container.delete(name)

        if container_dir != module_dir:
            self._uninstall(
                container_dir, self.container_base, "$container_base/%s" % name
            )
            self._uninstall(
                module_dir, self.settings.module_base, "$module_base/%s" % name
            )
        else:
            self._uninstall(
                module_dir, self.settings.module_base, "$module_base/%s" % name
            )

        # If uninstalling the entire module, clean up symbolic links in all views
        for view_name, view in self.views.items():
            view.uninstall(module_dir)

        # parent of versioned directory has module .version
        module_dir = os.path.dirname(module_dir)

        # update the default version file, if other versions still present
        if os.path.exists(module_dir):
            self.versionfile.write(module_dir)

    def _uninstall(self, path, base_path, name):
        """
        Sub function, so we can pass more than one folder from uninstall
        """
        if os.path.exists(path):
            utils.remove_to_base(path, base_path)
            logger.info("%s and all subdirectories have been removed." % name)
        else:
            logger.warning("%s does not exist." % name)

    def _test_setup(self, tmpdir):
        """
        Setup tests, including changes to settings or test directory
        """
        self.settings.set("module_base", tmpdir)

    def _test(self, module_name, module_dir, tag, template="test.sh"):
        """
        Run specific tests for this module
        """
        # Generate a test template
        template = self.template.load(template or "test.sh")
        test_file = os.path.join(module_dir, "test.sh")

        # Generate the test script
        out = template.render(
            module_dir=module_dir,
            shell=self.settings.test_shell,
            version=tag,
            module_name=module_name,
        )
        utils.write_file(test_file, out)
        return subprocess.call(["/bin/bash", test_file])

    def add(self, image, module_name=None, **kwargs):
        """
        Add a container to the registry to enable install.
        """
        # Docker module name is always the same namespace as the image
        if image.startswith("docker"):
            module_name = image.replace("docker://", "")

        # If we still dont' have a module name and not docker, no go
        if not module_name:
            logger.exit("A module name is required to add an image.")
        module_name = self.add_namespace(module_name)

        # Assume adding to default registry
        dest = os.path.join(
            self.settings.registry[0], module_name.split(":")[0], "container.yaml"
        )

        # if the container.yaml already exists, use it
        template = container.ContainerConfig.get_config_template("container.yaml")
        if os.path.exists(dest):
            logger.warning("%s already exists and will be updated!" % module_name)
            template = dest

        # Load config (but don't validate yet!)
        config = container.ContainerConfig(template, validate=False)
        self.container.add(module_name, image, config, container_yaml=dest, **kwargs)

    def get(self, module_name, env_file=False):
        """
        Get an image path or uri specific to a container.
        """
        if env_file:
            return self.container.get_environment_file(module_name)
        return self.container.get(module_name)

    def list(self, pattern=None, names_only=False, out=None, short=False):
        """
        List installed modules.
        """
        self._list_modules(
            self.settings.module_base,
            self.modulefile,
            pattern,
            names_only,
            out,
            short=short,
        )

    def docgen(self, module_name, out=None):
        """
        Render documentation for a module.
        """
        config = self._load_container(module_name)
        out = out or sys.stdout
        aliases = config.get_aliases()
        template = self.template.load("docs.md")
        github_url = "%s/blob/main/registry/%s/container.yaml" % (
            defaults.github_url,
            module_name,
        )

        # Currently one doc is rendered for all containers
        result = template.render(
            parsed_name=config.name,
            settings=self.settings,
            description=config.description,
            aliases=aliases,
            versions=config.tags.keys(),
            github_url=github_url,
            container_url=config.url,
            creation_date=datetime.now(),
            name=module_name,
            flatname=module_name.replace(os.sep, "-"),
        )
        out.write(result)
        return out

    def shell(self, module_name):
        """Shell into an installed module container"""
        image = self.container.get(module_name)
        if not image:
            logger.exit("%s does not exist." % module_name)
        self.container.shell(image)

    def inspect(self, module_name):
        """
        Return complete metadata for the user from a container.
        """
        if not os.path.exists(self.container_base):
            logger.exit("%s does not exist." % self.container_base)

        image = self.container.get(module_name)
        return self.container.inspect(image)

    def _list_modules(
        self, base, filename, pattern=None, names_only=False, out=None, short=False
    ):
        """A shared function to list modules or registry entries."""
        out = out or sys.stdout
        modules = self._get_module_lookup(base, filename, pattern)

        # If we don't have modules, exit early
        if not modules:
            logger.exit("You don't have any install modules. Try shpc show.", 0)

        # The user can request to list only names, which is useful to find modules
        for module_name, versions in modules.items():
            if names_only:
                out.write("%s\n" % module_name)
            elif short:
                out.write("%s: %s\n" % (module_name.rjust(30), ", ".join(versions)))
            else:
                for version in versions:
                    out.write("%s:%s\n" % (module_name.rjust(30), version))

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
        module_name = self.add_namespace(module_name)

        # If a tag is provided, convert to directory
        module_dir = module_name.replace(":", os.sep)

        # We derive the current version installed from the container
        # We assume the user has provided the correct prefix
        module_dir = os.path.join(self.settings.module_base, module_dir)
        if not os.path.exists(module_dir):
            logger.exit(
                "%s does not exist. Is this a known registry entry?" % module_dir
            )

        config = self._load_container(module_name.rsplit(":", 1)[0])
        return self.container.check(module_name, config)

    def install(
        self, name, tag=None, view=None, disable_view=False, force=False, **kwargs
    ):
        """
        Given a unique resource identifier, install a recipe.

        For lmod, this means creating a subfolder in modules, pulling the
        container to it, and writing a module file there. We've already
        grabbed the name from docker (which is currently the only supported).
        """
        name = self.add_namespace(name)
        config = self._load_container(name, tag)

        # The chosen tag is set for the config (or defaults to latest)
        if not config.tag:
            logger.exit(
                "%s is not a known identifier. Choices are:\n%s"
                % (name, "\n".join(config.tags.keys()))
            )

        # We currently support gh, docker, path, or oras
        uri = config.get_uri()

        # If we have a path, the URI comes from the name
        if ".sif" in uri:
            uri = name.split(":", 1)[0]

        # This is a tag object with name and digest
        tag = config.tag

        # Pull the container to the module directory OR container base
        module_dir = os.path.join(self.settings.module_base, uri, tag.name)
        subfolder = os.path.join(uri, tag.name)
        container_dir = self.container.container_dir(subfolder)

        # Are we also installing to a named view?
        if view is None and not disable_view:
            view = self.settings.default_view

        # A view is a symlink under views_base/$view/$module
        if view:
            if view not in self.views:
                logger.exit(
                    "View %s does not exist, shpc view create %s." % (view, view)
                )

            # Update view from name to be View to interact with
            view = self.views[view]

            # Don't continue if it exists, unless force is True
            view.confirm_install(module_dir, force=force)

        # Create the module and container directory
        utils.mkdirp([module_dir, container_dir])

        # If we have a sif URI provided by path, the container needs to exist
        container_path = None
        if config.path:
            container_path = os.path.join(config.package_dir, config.path)
            if not os.path.exists(container_path):
                logger.exit(
                    "Expected container defined by path %s not found in %s."
                    % (config.path, config.package_dir)
                )
            container_dest = os.path.join(container_dir, config.path)

            # Note that here we are *duplicating* the container, assuming we
            # cannot use a link, and the registry won't be deleted but the
            # module container might!
            if not os.path.exists(container_dest):
                shutil.copyfile(container_path, container_dest)
            container_path = container_dest

        # Add a .version file to indicate the level of versioning
        self.versionfile.write(os.path.join(self.settings.module_base, uri), tag.name)

        # For Singularity this is a path, podman is a uri. If None is returned
        # there was an error and we cleanup
        if not container_path:
            container_path = self.container.registry_pull(
                module_dir, container_dir, config, tag
            )
        if not container_path:
            utils.remove_to_base(container_dir, self.container_base)
            logger.exit("There was an issue pulling %s" % container_path)

        # Get the template based on the module and container type
        template = self.template.load(self.templatefile)
        module_path = os.path.join(module_dir, self.modulefile)

        # If the module has a version, overrides version
        version = tag.name
        if ":" in name:
            name, version = name.split(":", 1)

        # Install the container
        self.container.install(
            module_path,
            container_path,
            name,
            template,
            aliases=config.get_aliases(),
            config=config,
            parsed_name=config.name,
            url=config.url,
            description=config.description,
            version=version,
            config_features=config.features,
            features=kwargs.get("features"),
        )

        # If the container tech does not need storage, clean up
        if not os.listdir(container_dir):
            utils.remove_to_base(container_dir, self.container_base)

        # Write the environment file to be bound to the container
        self.container.add_environment(
            module_dir,
            envars=config.get_envars(),
            environment_file=self.settings.environment_file,
        )

        if ":" not in name:
            name = "%s:%s" % (name, tag.name)
        logger.info("Module %s was created." % name)

        # Install the module (symlink) to the view and create version file
        if view:
            view.install(module_dir)

        return container_path
