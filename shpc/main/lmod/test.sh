#!/usr/bin/env bash

# This is a testing script that can be populated by a module to ensure that
# it loads. We likely can add additional tests to registry files to run too.

set -e

# This script assumes lmod is setup, and module on the path

export MODULEPATH="{{ module_dir }}"
module use "{{ module_dir }}"

printf "Testing load of {{ module_name }}:{{ version }}\n"
module load "{{ module_name }}/{{ version }}"

# TODO add test commands here
