__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2022, Vanessa Sochat"
__license__ = "MPL 2.0"


from .base import WrapperScript


def get_wrapper_script(name):
    return (
        {
            "docker.sh": DockerWrapper,
            "singularity.sh": SingularityWrapper,
            "podman.sh": DockerWrapper,
        }
    ).get(name) or WrapperScript


class DockerWrapper(WrapperScript):
    wrapper_template = "docker.sh"


class SingularityWrapper(WrapperScript):
    wrapper_template = "singularity.sh"
