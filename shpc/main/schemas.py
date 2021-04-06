__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021, Vanessa Sochat"
__license__ = "MPL 2.0"


## ContainerConfig Schema

schema_url = "https://json-schema.org/draft-07/schema/#"

# This is also for latest, and a list of tags

# The simplest form of aliases is key/value pairs
aliases = {
    "type": "object",
    "patternProperties": {
        "\\w[\\w-]*": {"type": "string"},
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
            "options": {"type": "string"},
        },
    },
}


latest = {
    "type": "object",
    "minProperties": 1,
    "maxProperties": 1,
    "patternProperties": {
        "\\w[\\w-]*": {"type": "string"},
    },
}

containerConfigProperties = {
    "latest": aliases,
    "docker": {"type": "string"},
    "gh": {"type": "string"},
    "url": {"type": "string"},
    "maintainer": {"type": "string"},
    "description": {"type": "string"},
    "tags": aliases,
    "filter": {
        "type": "array",
        "items": {"type": "string"},
    },
    "aliases": {
        "oneOf": [
            aliases,
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
        "aliases",
    ],
    "properties": containerConfigProperties,
}


## Settings.yml (loads as json)

# Since we only support lmod, currently all of these are required

settingsProperties = {
    "registry": {"type": "string"},
    "lmod_base": {"type": "string"},
    "database_disable": {"type": "boolean"},
    "database_file": {"type": "string"},
    "singularity_module": {"type": ["string", "null"]},
    "bindpaths": {"type": ["string", "null"]},
    "updated_at": {"type": "string"},
    "singularity_shell": {"type": "string", "enum": ["/bin/bash", "/bin/sh"]},
    "plugins_enabled": {
        "type": "array",
        "items": {"type": "string", "enum": ["lmod"]},
    },
}


settings = {
    "$schema": schema_url,
    "title": "Settings Schema",
    "type": "object",
    "required": [
        "plugins_enabled",
        "registry",
        "lmod_base",
        "database_disable",
        "database_file",
        "singularity_module",
        "bindpaths",
        "singularity_shell",
    ],
    "properties": settingsProperties,
}
