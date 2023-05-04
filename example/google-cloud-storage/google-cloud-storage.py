#!/usr/bin/env python3

# Run this script on a VM (or a machine with your Google Cloud credentials)
# to upload to storage. You should target a containers.txt file, a single
# line listing of the containers you want to build / install. A container
# that already is at the path will not be replaced.

import argparse
import multiprocessing
import os
import shutil
import sys
import time

from google.cloud import storage

import shpc.utils
from shpc.main import get_client

# Global shpc and storage clients
cli = get_client()
storage_client = storage.Client()


def get_parser():
    parser = argparse.ArgumentParser(
        description="SHPC Google Cloud Storage Adder",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument(
        "--force", help="Force reinstall of module", default=False, action="store_true"
    )
    parser.add_argument("containers", help="Path to containers.txt file")
    parser.add_argument("--bucket", help="Bucket name and prefix", required=True)
    parser.add_argument(
        "--root",
        help="Install root for modules and containers",
        default=os.path.expanduser("~/shpc-cache"),
    )
    parser.add_argument(
        "--keep",
        help="Don't clean up as we go (only recommended if you have a large filesystem)",
        default=False,
        action="store_true",
    )
    parser.add_argument(
        "--workers",
        help="Number of workers to use",
        default=os.cpu_count(),
        type=int,
    )
    parser.add_argument(
        "--group-size",
        help="Number containers to pull at once (before clearing cache)",
        default=1,
        type=int,
    )
    return parser


def recursive_list(base):
    """
    Get all files in a root
    """
    for root, _, filenames in os.walk(base):
        for filename in filenames:
            yield os.path.join(root, filename)


class Task:
    """
    Task to pull a Singularity container
    """

    def __init__(self, module, bucket, keep=False, force=False):
        self.module = module
        self.keep = keep
        self.bucket = bucket
        self.force = force

    def run(self):
        """
        Run the repo task, uploading the data and taking a pause if needed.
        """
        global cli

        # First check that it doesn't already exist
        bucket_name = self.bucket.replace("gs://", "")
        bucket_name, bucket_subdir = bucket_name.split("/", 1)
        bucket = storage_client.bucket(bucket_name)

        # This will have the name and latest
        module = cli.get_module(self.module)
        blob_path = os.path.join(
            bucket_subdir, self.module, module.tag.name, "module.lua"
        )
        blob = bucket.blob(blob_path)

        # Cut out early if the module exists and we don't force re-install
        if blob.exists() and not self.force:
            return f"Module {self.module} already exists and force is false, not re-installing."

        container_path = cli.install(self.module)

        # Upload to Google Cloud Storage
        container_base = cli.settings.get("container_base")
        relpath = os.path.relpath(container_path, container_base)
        module, version, _ = relpath.split(os.sep, 2)

        # The module files and container are here
        root = os.path.join(container_base, module, version)
        for path in recursive_list(root):
            # Get path relative to storage
            relpath = os.path.relpath(path, container_base)

            # Assemble relative path
            blob = bucket.blob(os.path.join(bucket_subdir, relpath))
            if not blob.exists():
                generation_match_precondition = 0
                blob.upload_from_filename(
                    path, if_generation_match=generation_match_precondition
                )

        # Clean up the root if we don't intend to keep
        if not self.keep:
            shutil.rmtree(root)


def chunks(listing, size):
    """
    Yield sized chunks of a list
    """
    assert type(listing) is list, "L is not a list"
    for i in range(0, len(listing), size):
        yield listing[i : i + size]


class TaskRunner:
    """
    A task runner knows how run tasks!
    """

    def __init__(self, workers=4):
        self.workers = workers
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def run(self):
        """
        Run the tasks!
        """
        items = []
        with multiprocessing.Pool(processes=self.workers) as pool:
            for result in pool.map(run_task, self.tasks):
                # This is a smaller list of packages/repo metadata pushes
                print(f"Installed {result}")
                items.append(result)

        # Return all results from running the task
        return items


def run_task(t):
    """
    Anything with a run function can be provided as a task.
    """
    return t.run()


def main():
    parser = get_parser()

    # If an error occurs while parsing the arguments, the interpreter will exit with value 2
    args, extra = parser.parse_known_args()

    if not args.bucket:
        sys.exit("A --bucket is required, name and desired path prefix.")

    # Show args to the user
    print("     containers: %s" % args.containers)
    print("         bucket: %s" % args.bucket)
    print("        workers: %s" % args.workers)
    print("           root: %s" % args.root)
    print("  force install: %s" % args.force)
    print("keep containers: %s" % args.keep)
    time.sleep(3)

    if not os.path.exists(args.containers):
        sys.exit(f"Path {args.containers} does not exist.")

    global cli

    # Create the root to install to
    print(f"Containers and modules will install to {args.root}")
    if not os.path.exists(args.root):
        os.makedirs(args.root)

    cli.settings.set("module_base", args.root)
    cli.settings.set("container_base", args.root)

    # Ensure we start with the populated modules
    cli.registry.iter_modules()

    # We break into groups of 5 so we can clear the cache in-between runs
    containers = shpc.utils.read_file(args.containers).split("\n")

    # For each container, install
    for group in chunks(containers, args.group_size):
        # When we start a group, clean up cache from last
        os.system("singularity cache clean --force")

        # Create a task runner to do the installs
        runner = TaskRunner(args.workers)
        for container in group:
            container = container.strip()
            if not container:
                continue
            task = Task(container, args.bucket, args.keep, args.force)
            runner.add_task(task)

        # Run all tasks to install containers
        runner.run()


if __name__ == "__main__":
    main()
