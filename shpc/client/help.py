shell_description = """Shell into a Python session with a client.

  # Install python, and shell directly into container
  $ shpc install python
  $ shpc shell python:3.12-rc
  Singularity>

  # Shell into a Python client interaction
  $ shpc shell
  > client
  Out[1]: [shpc-client]

  # Shell into a client with a different interpeter
  $ shpc shell -i python
  $ shpc shell -i ipython
  $ shpc shell -i bpython"""


config_params = """"Customize a settings.yaml config value on the fly to ADD/SET/REMOVE for a command

  # Set a single key to be value
  $ shpc -c set:key:value <command> <args>

  # Add "/tmp/registry' to the "registry" attribute list
  $ shpc -c add:registry:/tmp/registry <command> <args>

  # Remove from the list
  $ shpc -c rm:registry:/tmp/registry"""

install_description = """Install a registry recipe.

  $ Install latest version
  $ shpc install python

  # Show all versions available in config under "tags"
  $ shpc show python

  # Install a specific version from that set
  $ shpc install python:3.9.5-alpine
"""

listing_description = """List installed modules.

  # Show installed modules
  $ shpc list

  # Search for those with "python" in the name
  $ shpc list python

  # Show modules names without tags (versions)
  $ shpc list --names-only

  # Show organized by module, with tags (versions) underneath
  $ shpc show --short
"""

inspect_description = """Inspect an installed module image."

  # Show modules installed (we will need a version)
  $ shpc list

  # Inpect python, for all attributes
  $ shpc inspect python:3.12-rc

  # Inpect python runscript
  $ shpc inspect python:3.12-rc --runscript

  # Same, but output in json (this works for any of the above commands)
  $ shpc inspect python:3.12-rc --json
"""

get_description = """Get an image path for a module

  # Get the container path of the installed module python:3.12-rc
  $ shpc get python:3.12-rc

  # Get the path of the environment file
  $ shpc get python:3.12-rc --env-file
"""

add_description = """Add an image to modules manually. This command requires a local registry.

  # Add a docker URI to your registry under the same namespace
  $ shpc add docker://vanessa/salad:latest

  # Add a SIF container to the registry namespace
  # After adding, you would edit the container.yaml
  $ shpc add salad_latest.sif dinosaur/salad:latest

  # Install the newly created container.yaml
  $ shpc install dinosaur/salad:latest
"""

check_description = """Check if you have latest installed.

  # Check to see if we have the latest tag installed for python
  $ shpc check python
"""

view_description = """View control to create, install, and uninstall A view name is always required.

  # Create a new view
  $ shpc view create <name>

  # Delete an existing view
  $ shpc view delete <name>

  # Get the path to an existing view
  $ shpc view get <name>

  # List existing views
  $ shpc view list <name>

  # Install a registry module to a named view
  $ shpc view install <name> <module>

  # Uninstall a registry module from a view
  $ shpc view uninstall <name> <module>

  # Open up an editor to edit the config for a view
  $ shpc view edit <name>
"""

config_description = """Set or get a config value, edit the config, add or remove a list variable, or create a user-specific config.

  # Set a key in settings.yml to "value"
  $ shpc config set key value
  $ shpc config set key:subkey value

  # Get the currently set value for "key"
  $ shpc config get key

  # Open the settings.yml to manually edit
  $ shpc config edit

  # Create a user-space config in ~/.singularity-hpc/settings.yml
  $ shpc config inituser

  # Add "/tmp/registry" to the list "registry"
  $ shpc config add registry /tmp/registry

  # Remove the entry from the list
  $ shpc config remove registry /tmp/registry
"""

docgen_description = """Generate a markdown document for a container registry entry

  # Generate an entry from the default remote shpc-registry
  $ shpc docgen python

  # Generate an entry from a custom registry URL
  $ shpc docgen --registry-url https://github.com/singularityhub/shpc-registry python

  # Customize the branch
  $ shpc docgen --registry-url https://github.com/singularityhub/shpc-registry --branch main python
"""

pull_description = """Pull a container built with singularityhub/singularity-deploy.

This command is considered deprecated. If you want to use a SIF in GitHub packages, simply
push with oras and define the container URI as oras: ghcr.io/singularityhub/github-ci.
"""

test_description = """Test a registry entry. This is considered a developer command.

  # Test the pull, install, and module command for python
  # This command requires your module software.
  $ shpc test python

  # Use a custom test.sh template
  $ shpc test python --template ./test.sh
"""

uninstall_description = """Uninstall a module"

  # Uninstall a specific python version
  $ shpc uninstall python:3.12-rc1

  # Uninstall all Python versions
  $ shpc uninstall python

  # Uninstall all modules
  $ shpc uninstall --all
"""

update_description = """Update a container recipe with new versions. The actual update is supported only for local registries.

  # Look for updates for a remote container
  $ shpc update quay.io/biocontainers/samtools --dry-run

  # Update a local container recipe
  $ shpc update quay.io/biocontainers/samtools

  # Update all local container yaml recipes
  $ shpc update
"""

sync_description = """Get latest files and containers from an upstream shpc. This is only supported to run against a filesystem (local) registry.

  # Make a temporary local filesystem registry
  $ mkdir -p ./registry

  # Sync the default remote registry to it!
  $ shpc sync-registry --registry ./registry

  # Ask to update from a specific reference (tag or branch):
  $ shpc sync-registry --registry ./registry --tag 0.0.58

  # Ask to add just a specific container:
  $ shpc sync-registry --registry ./registry quay.io/not-local/container

  # Add new containers and completely update container.yaml files.
  $ shpc sync-registry --registry ./registry --all

  # Always do a dry run first!
  $ shpc sync-registry --registry ./registry --dry-run
"""

namespace_description = """Set or unset the install namespace.

  # Use the ghcr.io/autamus namespace
  shpc namespace use ghcr.io/autamus

  # Install ghcr.io/autamus/clingo
  $ shpc install clingo

  # Unset the namespace when you are done
  $ shpc namespace unset
"""

show_description = """Show the config for a registry entry

  # Show all modules available for the remote registry (or targeted from your settings.yml config)
  $ shpc show

  # Show complete list, adding tags or versions
  $ shpc show --versions

  # Show container.yaml metadata for module "python"
  $ shpc show python

  # Filter all modules to those with "python"
  $ shpc show --filter python
"""
