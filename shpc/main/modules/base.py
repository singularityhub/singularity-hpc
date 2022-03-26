__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021-2022, Vanessa Sochat"
__license__ = "MPL 2.0"

from shpc.main.client import Client as BaseClient
from shpc.logger import logger
import shpc.utils as utils
import shpc.defaults as defaults
import shpc.main.templates
import shpc.main.container as container
from jinja2 import Template

from datetime import datetime
import os
import shutil
import subprocess
import sys
import inspect

here = os.path.abspath(os.path.dirname(__file__))


class ModuleBase(BaseClient):
    def __init__(self, **kwargs):

        # Files for module software to generate depending on user setting
        super(ModuleBase, self).__init__(**kwargs)
        self.here = os.path.dirname(inspect.getfile(self.__class__))

    def _get_template(self, template_name):
        """
        Get a template from templates
        """
        template_file = os.path.join(here, "templates", template_name)
        if not os.path.exists(template_file):
            template_file = os.path.abspath(template_name)
        return template_file

    def _load_template(self, template_name):
        """
        Load the default module template.
        """
        template_file = self._get_template(template_name)

        # Make all substitutions here
        with open(template_file, "r") as temp:
            template = Template(self.substitute(temp.read()))
        return template

    def substitute(self, template):
        """
        For all known identifiers, substitute user specified format strings.
        """
        subs = {
            "{|module_name|}": self.settings.module_name or "{{ parsed_name.tool }}"
        }
        for key, replacewith in subs.items():
            template = template.replace(key, replacewith)
        return template

    def _cleanup(self, module_dir):
        """
        Given a module directory, delete up to module base
        """
        # Exit early if the module directory for some reason was removed
        if not os.path.exists(module_dir):
            return
        shutil.rmtree(module_dir)

        # If directories above it are empty, remove
        while module_dir != self.settings.module_base:
            if not utils.can_be_deleted(module_dir, [".version"]):
                break
            shutil.rmtree(module_dir)
            module_dir = os.path.dirname(module_dir)

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

    def uninstall(self, name, force=False):
        """
        Given a unique resource identifier, uninstall a module
        """
        # The name can either be a folder or an install directory
        name = self.add_namespace(name)

        # folder paths do not have :
        name = name.replace(":", os.sep)
        module_dir = os.path.join(self.settings.module_base, name)
        container_dir = self.container.container_dir(name)

        # Podman needs image deletion
        self.container.delete(name)

        if container_dir != module_dir:
            self._uninstall(container_dir, "$container_base/%s" % name, force)
            self._uninstall(module_dir, "$module_base/%s" % name, force)
        else:
            self._uninstall(module_dir, "$module_base/%s" % name, force)

    def _uninstall(self, module_dir, name, force=False):
        """
        Sub function, so we can pass more than one folder from uninstall
        """
        if os.path.exists(module_dir):
            if not force:
                msg = "%s, and all content below it? " % name
                if not utils.confirm_uninstall(msg, force):
                    return
            self._cleanup(module_dir)
            logger.info("%s and all subdirectories have been removed." % name)
        else:
            logger.warning("%s does not exist." % name)

        # parent of versioned directory has module .version
        module_dir = os.path.dirname(module_dir)

        # update the default version file, if other versions still present
        if os.path.exists(module_dir):
            self.write_version_file(module_dir)

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
        template = self._load_template(template or "test.sh")
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
        template = self._load_template("docs.md")
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

    def install(self, name, tag=None, **kwargs):
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
        shpc.utils.mkdirp([module_dir, container_dir])

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
        self.write_version_file(uri, tag.name)

        # For Singularity this is a path, podman is a uri. If None is returned
        # there was an error and we cleanup
        if not container_path:
            container_path = self.container.registry_pull(
                module_dir, container_dir, config, tag
            )
        if not container_path:
            self._cleanup(container_dir)
            logger.exit("There was an issue pulling %s" % container_path)

        # Get the template based on the module and container type
        template = self._load_template(self.templatefile)
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
            self._cleanup(container_dir)

        # Write the environment file to be bound to the container
        self.container.add_environment(
            module_dir,
            envars=config.get_envars(),
            environment_file=self.settings.environment_file,
        )

        if ":" not in name:
            name = "%s:%s" % (name, tag.name)
        logger.info("Module %s was created." % name)
        return container_path

    # Module software can choose how to handle each of these cases
    def _no_default_version(self, version_file, tag):
        return

    def _module_sys_default_version(self, version_file, tag):
        return

    def _set_default_version(self, version_file, tag):
        """
        Set the default version to the given tag
        """
        template = self._load_template("default_version")
        utils.write_file(version_file, template.render(version=tag))

    def write_version_file(self, uri, latest_tag_installed=None):
        """
        Create the .version file, if there is a template for it.
        """
        version_dir = os.path.join(self.settings.module_base, uri)
        version_file = os.path.join(version_dir, ".version")

        # No default versions
        if self.settings.default_version in [False, None]:
            return self._no_default_version(version_file, latest_tag_installed)

        # allow the module software to control versions
        if self.settings.default_version in [True, "module_sys"]:
            return self._module_sys_default_version(version_file, latest_tag_installed)

        # First or last installed
        if latest_tag_installed and (self.settings.default_version == "last_installed"):
            tag = latest_tag_installed
        else:
            # The versions we actually have
            found = [x for x in os.listdir(version_dir) if x != ".version"]
            if len(found) == 1:
                tag = found[0]
            else:
                if self.settings.default_version == "first_installed":
                    selector = min
                else:
                    selector = max
                tag = selector(
                    found,
                    key=lambda x: utils.creation_date(os.path.join(version_dir, x)),
                )

        # Write the .version file
        return self._set_default_version(version_file, tag)
