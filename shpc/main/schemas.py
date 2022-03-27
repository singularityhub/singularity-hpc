__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021-2022, Vanessa Sochat"
__license__ = "MPL 2.0"


## ContainerConfig Schema

schema_url = "http://json-schema.org/draft-07/schema"

# This is also for latest, and a list of tags

# The simplest form of aliases is key/value pairs
keyvals = {
    "type": "object",
    "patternProperties": {
        "\\w[\\w-]*": {"type": "string"},
    },
}


# Features in container.yaml can be boolean or null, as they need to be
# container technology agnostic
features = {
    "type": "object",
    "patternProperties": {"\\w[\\w-]*": {"type": ["boolean", "null"]}},
}

# container features can be null or a known string
container_features = {
    "type": "object",
    "properties": {
        "gpu": {
            "oneOf": [{"type": "null"}, {"type": "string", "enum": ["nvidia", "amd"]}]
        },
        "x11": {"oneOf": [{"type": "null"}, {"type": "string"}, {"type": "boolean"}]},
        "home": {"oneOf": [{"type": "null"}, {"type": "string"}]},
    },
}


# Or a list
aliases_list = {
    "type": "array",
    "items": {
        "type": "object",
        "required": [
            "name",
            "command",
        ],
        "properties": {
            "name": {"type": "string"},
            "command": {"type": "string"},
            "singularity_options": {"type": "string"},
            "docker_options": {"type": "string"},
        },
    },
}


containerConfigProperties = {
    "latest": keyvals,
    "docker": {"type": "string"},
    "path": {"type": "string"},
    "oras": {"type": "string"},
    "gh": {"type": "string"},
    "url": {"type": "string"},
    "test": {"type": "string"},
    "maintainer": {"type": "string"},
    "description": {"type": "string"},
    "docker_scripts": keyvals,
    "singularity_scripts": keyvals,
    "tags": keyvals,
    "filter": {
        "type": "array",
        "items": {"type": "string"},
    },
    "env": keyvals,
    "features": features,
    "aliases": {
        "oneOf": [
            keyvals,
            aliases_list,
        ]
    },
}


containerConfig = {
    "$schema": schema_url,
    "title": "ContainerConfig Schema",
    "type": "object",
    "required": [
        "latest",
        "tags",
        "maintainer",
        "description",
    ],
    "properties": containerConfigProperties,
    "additionalProperties": False,
}

# Wrapper scripts for global (aliases) and container.yaml
wrapper_scripts = {
    "type": "object",
    "properties": {
        "enabled": {"type": "boolean"},
        "docker": {"type": ["string", "null"]},
        "podman": {"type": ["string", "null"]},
        "templates": {"type": ["string", "null"]},
        "singularity": {"type": ["string", "null"]},
    },
}


## Settings.yml (loads as json)

shells = ["/bin/bash", "/bin/sh", "/bin/csh"]

# Currently all of these are required
settingsProperties = {
    "registry": {"type": "array", "items": {"type": "string"}},
    "module_base": {"type": "string"},
    "container_base": {"type": ["string", "null"]},
    "namespace": {"type": ["string", "null"]},
    "singularity_module": {"type": ["string", "null"]},
    "podman_module": {"type": ["string", "null"]},
    "bindpaths": {"type": ["string", "null"]},
    "updated_at": {"type": "string"},
    "module_name": {"type": "string"},
    "config_editor": {"type": "string"},
    "environment_file": {"type": "string"},
    "default_version": {
        "oneOf": [
            {"type": ["null", "boolean"]},
            {
                "type": "string",
                "enum": ["module_sys", "last_installed", "first_installed"],
            },
        ]
    },
    "enable_tty": {"type": "boolean"},
    "wrapper_scripts": wrapper_scripts,
    "container_tech": {"type": "string", "enum": ["singularity", "podman", "docker"]},
    "singularity_shell": {"type": "string", "enum": shells},
    "podman_shell": {"type": "string", "enum": shells},
    "docker_shell": {"type": "string", "enum": shells},
    "test_shell": {"type": "string", "enum": shells},
    "wrapper_shell": {"type": "string", "enum": shells},
    "module_sys": {"type": "string", "enum": ["lmod", "tcl", None]},
    "container_features": container_features,
}

settings = {
    "$schema": schema_url,
    "title": "Settings Schema",
    "type": "object",
    "required": [
        "module_sys",
        "registry",
        "module_base",
        "singularity_module",
        "environment_file",
        "container_tech",
        "bindpaths",
        "singularity_shell",
        "container_features",
    ],
    "properties": settingsProperties,
    "additionalProperties": False,
}
