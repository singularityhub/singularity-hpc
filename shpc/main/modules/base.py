__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021-2022, Vanessa Sochat"
__license__ = "MPL 2.0"

import inspect
import json
import os
import subprocess
import sys
from datetime import datetime

import shpc.defaults as defaults
import shpc.main.container as container
import shpc.main.modules.template as templatectl
import shpc.main.modules.versions as versionfile
import shpc.main.modules.views as views
import shpc.main.registry as registry
import shpc.utils as utils
from shpc.logger import logger
from shpc.main.client import Client as BaseClient
from .module import Module


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

    def view_uninstall(self, view, name, force=False):
        """
        Uninstall a module from a view.
        Set "force" to True to bypass the confirmation prompt.
        """
        module = self.new_module(name)

        # Ask before deleting anything!
        if not force:
            if not utils.confirm_uninstall(name + "?", force):
                return

        # Only uninstall from the view
        if view not in self.views:
            logger.exit("View %s does not exist, cannot uninstall." % view)
        return self.views[view].uninstall(module.module_dir)

    def uninstall(self, name, force=False):
        """
        Given a unique resource identifier, uninstall a module.
        Set "force" to True to bypass the confirmation prompt.
        """
        module = self.new_module(name)

        # We need to look for the module in all views and show to the user first
        views_with_module = set()
        for view_name, entry in self.views.items():
            if entry.exists(module.module_dir):
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

        # Podman needs image deletion
        self.container.delete(module.name)

        if module.container_dir != module.module_dir:
            self._uninstall(
                module.container_dir,
                self.container_base,
                "$container_base/%s" % module.name,
            )
            self._uninstall(
                module.module_dir,
                self.settings.module_base,
                "$module_base/%s" % module.name,
            )
        else:
            self._uninstall(
                module.module_dir,
                self.settings.module_base,
                "$module_base/%s" % module.name,
            )

        # If uninstalling the entire module, clean up symbolic links in all views
        for view_name in views_with_module:
            self.views[view_name].uninstall(module.module_dir)

        # parent of versioned directory has module .version
        module_dir = os.path.dirname(module.module_dir)

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
        self.settings.ensure_filesystem_registry()

        # Docker module name is always the same namespace as the image
        if image.startswith("docker"):
            module_name = image.replace("docker://", "")

        # If we still dont' have a module name and not docker, no go
        if not module_name:
            logger.exit("A module name is required to add an image.")
        module_name = self.add_namespace(module_name)

        # Assume adding to default registry
        dest = os.path.join(
            self.settings.filesystem_registry,
            module_name.split(":")[0],
            "container.yaml",
        )
        template = container.ContainerConfig.get_config_template("container.yaml")

        # if the container.yaml already exists, use it
        if os.path.exists(dest):
            logger.warning("%s already exists and will be updated!" % module_name)
            template = dest

        # Load config (but don't validate yet!)
        config = container.ContainerConfig(
            registry.FilesystemResult(module_name, template), validate=False
        )
        return self.container.add(
            module_name, image, config, container_yaml=dest, **kwargs
        )

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

    def docgen(self, module_name, registry=None, out=None, branch="main"):
        """
        Render documentation for a module within a local registry.
        """
        config = self._load_container(module_name)

        out = out or sys.stdout
        aliases = config.get_aliases()
        template = self.template.load("docs.md")
        registry = registry or defaults.github_url
        github_url = "%s/blob/%s/%s/container.yaml" % (registry, branch, module_name)
        registry_bare = registry.split(".com")[-1]
        raw = (
            "https://gitlab.com/%s/-/raw/%s/%s/container.yaml"
            if "gitlab" in registry
            else "https://raw.githubusercontent.com/%s/%s/%s/container.yaml"
        )
        raw_github_url = raw % (
            registry_bare,
            branch,
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
            config_url=raw_github_url,
            creation_date=datetime.now(),
            name=module_name,
            latest=config.latest.name,
            flatname=module_name.replace(os.sep, "-"),
            config=json.dumps(config.entry._config),
        )
        out.write(result)
        return out

    def shell(self, module_name):
        """
        Shell into an installed module container
        """
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
        """
        A shared function to list modules or registry entries.
        """
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
        """
        A shared function to get a lookup of installed modules or registry entries
        """
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
        module = self.new_module(module_name)
        if not os.path.exists(module.module_dir):
            logger.exit(
                "%s does not exist. Is this a known registry entry?" % module.module_dir
            )

        return module.check()

    def new_module(self, name, tag=None, tag_exists=True):
        """
        Create a new module
        """
        name = self.add_namespace(name)

        # If the module has a version, overrides provided tag
        if ":" in name:
            name, tag = name.split(":", 1)

        module = Module(name)
        module.config = self._load_container(module.name, tag)

        # Ensure the tag exists, if required, uses config.tag
        if tag_exists:
            module.validate_tag_exists()

        # Pass on container and settings
        module.container = self.container
        module.settings = self.settings
        return module

    def install(self, name, tag=None, force=False, **kwargs):
        """
        Given a unique resource identifier, install a recipe.

        For lmod, this means creating a subfolder in modules, pulling the
        container to it, and writing a module file there. We've already
        grabbed the name from docker (which is currently the only supported).
        "force" is currently not used.
        """
        # Create a new module
        module = self.new_module(name, tag=tag, tag_exists=True)

        # We always load overrides for an install
        module.load_override_file()

        # Create the module and container directory
        utils.mkdirp([module.module_dir, module.container_dir])

        # Add a .version file to indicate the level of versioning
        self.versionfile.write(
            os.path.join(self.settings.module_base, module.uri), module.tag.name
        )
        if not module.container_path:
            utils.remove_to_base(module.container_dir, self.container_base)
            logger.exit("There was an issue pulling the container for %s" % module.name)

        # Get the template based on the module and container type
        template = self.template.load(self.templatefile)
        module_path = os.path.join(module.module_dir, self.modulefile)

        # Install the container
        # This could be simplified to take the module
        self.container.install(module_path, template, module, kwargs.get("features"))

        # If the container tech does not need storage, clean up
        if not os.listdir(module.container_dir):
            utils.remove_to_base(module.container_dir, self.container_base)

        # Write the environment file to be bound to the container
        module.add_environment()
        logger.info("Module %s was created." % module.tagged_name)
        return module.container_path

    def view_install(self, view_name, name, tag=None, force=False):
        """
        Install a module in a view. The module must already be installed.
        Set "force" to True to allow overwriting existing symlinks.
        """
        module = self.new_module(name, tag=tag, tag_exists=True)

        # A view is a symlink under views_base/$view/$module
        if view_name not in self.views:
            logger.exit(
                "View %s does not exist, shpc view create %s." % (view_name, view_name)
            )

        # Update view from name to be View to interact with
        view = self.views[view_name]

        # Don't continue if it exists, unless force is True
        view.confirm_install(module.module_dir, force=force)
        view.install(module.module_dir)
