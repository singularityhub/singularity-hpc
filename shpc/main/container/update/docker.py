__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021-2022, Vanessa Sochat"
__license__ = "MPL 2.0"

from shpc.logger import logger
import requests


class DockerImage:

    """
    A thin client for getting metadata about an image.
    """

    def __init__(self, container_name):
        self.container_name = container_name

        # might not last forever, but we can use it for now
        self.apiroot = "https://crane.ggcr.dev"

    def get_request(self, url):
        """
        Perform a get request, expecting status code 200.
        """
        response = requests.get(url)
        if response.status_code != 200:
            logger.exit("Issue with request %s" % url)
        return response

    def tags(self):
        """
        Get image tags.
        """
        url = "%s/ls/%s" % (self.apiroot, self.container_name)
        response = self.get_request(url)
        return [x for x in response.text.split("\n") if x]

    def manifest(self, tag):
        url = "%s/manifest/%s:%s" % (self.apiroot, self.container_name, tag)
        return self.get_request(url).json()

    def digest(self, tag):
        url = "%s/digest/%s:%s" % (self.apiroot, self.container_name, tag)
        response = self.get_request(url).text
        if "could not parse reference" in response:
            logger.exit("Issue getting digest: %s" % response)
        return self.get_request(url).text

    def config(self):
        url = "%s/config/%s" % (self.apiroot, self.container_name)
        return self.get_request(url).json()
