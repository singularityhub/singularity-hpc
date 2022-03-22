#!/bin/bash

echo
echo "************** START: test_client.sh **********************"

# Create temporary testing directory
echo "Creating temporary directory to work in."
here="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
shpc_root="$( dirname "${here}" )"

. $here/helpers.sh

# Create temporary testing directory
tmpdir=$(mktemp -d)
output=$(mktemp ${tmpdir:-/tmp}/shpc_test.XXXXXX)
printf "Created temporary directory to work in. ${tmpdir}\n"

# Make sure it's installed
if ! command -v shpc &> /dev/null
then
    printf "shpc is not installed\n"
    exit 1
else
    printf "shpc is installed\n"
fi

# Create a temporary config file, module folder, etc.
settings=$tmpdir/settings.yaml
modules=$tmpdir/modules
cp $shpc_root/settings.yml $settings

# Prepare a container to install
container=$tmpdir/salad_latest.sif
cp $here/testdata/salad_latest.sif $container

echo
echo "#### Testing base client "
runTest 0 $output shpc --settings-file $settings --version

echo
echo "#### Testing config "
runTest 0 $output shpc --settings-file $settings config --help
runTest 0 $output shpc --settings-file $settings config set "module_base:${modules}"
runTest 0 $output shpc --settings-file $settings config get "module_base"

echo
echo "#### Testing show "
runTest 0 $output shpc --settings-file $settings show --help
runTest 0 $output shpc --settings-file $settings show
runTest 0 $output shpc --settings-file $settings show python

echo
echo "#### Testing add local "
runTest 0 $output shpc --settings-file $settings add --help
runTest 0 $output shpc --settings-file $settings add "$container" salad/latest
runTest 0 $output shpc --settings-file $settings install salad/latest

echo
echo "#### Testing add docker "
runTest 0 $output shpc --settings-file $settings add docker://vanessa/pokemon
runTest 0 $output shpc --settings-file $settings install vanessa/pokemon

echo
echo "#### Testing install "
runTest 0 $output shpc --settings-file $settings install --help
runTest 0 $output shpc --settings-file $settings install python:3.9.2-slim
runTest 0 $output shpc --settings-file $settings install vanessa/salad:latest
runTest 0 $output shpc --settings-file $settings install --container_tech podman python

echo
echo "#### Testing get "
runTest 0 $output shpc --settings-file $settings get --help
runTest 1 $output shpc --settings-file $settings get vanessa/fork:latest
runTest 0 $output shpc --settings-file $settings get salad:latest

echo
echo "#### Testing list "
runTest 0 $output shpc --settings-file $settings list --help
runTest 0 $output shpc --settings-file $settings list
runTest 0 $output shpc --settings-file $settings list --short
runTest 0 $output shpc --settings-file $settings list salad

echo
echo "#### Testing inspect "
runTest 0 $output shpc --settings-file $settings inspect --help
runTest 0 $output shpc --settings-file $settings inspect python:3.9.2-slim
runTest 0 $output shpc --settings-file $settings inspect vanessa/salad:latest

echo
echo "#### Testing namespace "
runTest 0 $output shpc --settings-file $settings namespace use vanessa
runTest 0 $output shpc --settings-file $settings show salad
runTest 0 $output shpc --settings-file $settings namespace unset

echo
echo "#### Testing check "
runTest 0 $output shpc --settings-file $settings check --help
# This test will succeed if this version is latest!
runTest 0 $output shpc --settings-file $settings check python:3.9.2-slim
# This test will fail if this is not latest
runTest 0 $output shpc --settings-file $settings check vanessa/salad:latest

echo
echo "#### Testing uninstall "
runTest 0 $output shpc --settings-file $settings uninstall --help
runTest 0 $output shpc --settings-file $settings uninstall --force vanessa/salad:latest


rm -rf ${tmpdir}
