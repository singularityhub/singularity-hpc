#!/usr/bin/env bash

set -e

# source the right profile so we can see module
if [ -d "/usr/local/lmod/lmod/init" ]; then
    . /usr/local/lmod/lmod/init/profile
else
    . /usr/local/Modules/init/bash
fi

function main() {
    if [[ $# -eq 0 ]]; then
        /bin/bash
    else
        "$@"
    fi
}

main "$@"
