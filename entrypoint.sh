#!/usr/bin/env bash

set -e

# source the lmod profile so we can see module
. /usr/local/lmod/lmod/init/profile

function main() {
    if [[ $# -eq 0 ]]; then
        /bin/bash
    else
        "$@"        
    fi
}

main "$@"
