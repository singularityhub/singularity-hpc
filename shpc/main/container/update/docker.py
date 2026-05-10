__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021-2025, Vanessa Sochat"
__license__ = "MPL 2.0"

import os
import re
import time

import requests

from shpc.logger import logger


class DockerImage:

    """
    A thin client for getting metadata about an image.
    """

    def __init__(self, container_name):
        self.container_name = container_name

        # might not last forever, but we can use it for now
        self.apiroot = "https://crane.ggcr.dev"
        self.tag_response = None

    def get_request(self, url, attempt=0):
        """
        Perform a get request, expecting status code 200.
        """
        try:
            response = requests.get(url)
            response.raise_for_status()

        except requests.exceptions.HTTPError as e:
            # Try to retry if rate limited
            if e.response.status_code == 429:
                retry_seconds = e.response.headers.get("Retry-After", "unknown")
                logger.warning(
                    "Rate limit hit for %s, retrying after %s seconds"
                    % (url, retry_seconds)
                )
                time.sleep(int(retry_seconds) + 1)
                if attempt < 5:
                    return self.get_request(url, attempt + 1)

            if e.response.status_code == 404:
                raise ValueError(f"Request to {url} returned 404, not found.")

            if e.response.status_code == 401:
                logger.exit(
                    f"Unauthorized access to {url}. This image may be in a private repository. If this is expected, check your credentials."
                )

            # Pass along things that aren't handled otherwise
            raise e

        return response

    # This should always return a dicts with tag name keys and digest values.
    # For some registries, the digest query is separate.
    # Return "unknown" in this case.
    def _query_tag_api(self, tag=None):
        tag_string = f":{tag}" if tag else ""
        operation = "digest" if tag else "ls"

        url = "%s/%s/%s%s" % (self.apiroot, operation, self.container_name, tag_string)
        response = self.get_request(url)

        if "could not parse reference" in response:
            logger.exit("Issue getting digest: %s" % response)
        if "unsupported status" in response:
            logger.exit("Issue getting digest: %s" % response)
        if "MANIFEST_UNKNOWN" in response.text:
            raise ValueError(
                f"The image {'%s%s' % (self.container_name, tag_string)} you provided is not known. Check that it and the container both exist."
            )

        if tag is not None:
            return {tag: response.text}
        return {x.strip(): "unknown" for x in response.text.split("\n") if x.strip()}

    def tags(self):
        """
        Get image tags.
        """
        if self.tag_response is None:
            self.tag_response = self._query_tag_api()

        # Don't include tags for vex or sbom
        tags = [
            x for x in self.tag_response.keys() if not re.search("[.](sbom|vex)$", x)
        ]
        return tags

    def manifest(self, tag):
        url = "%s/manifest/%s:%s" % (self.apiroot, self.container_name, tag)
        response = self.get_request(url)
        return response.json()

    def digest(self, tag):
        if (
            self.tag_response is None
            or self.tag_response.get(tag, "unknown") == "unknown"
        ):
            self.tag_response[tag] = self._query_tag_api(tag=tag)[tag]
        return self.tag_response.get(tag, "unknown")

    def config(self):
        url = "%s/config/%s" % (self.apiroot, self.container_name)
        return self.get_request(url).json()


class QuayDockerImage(DockerImage):

    """
    A thin client for getting metadata about an image on Quay.
    """

    def __init__(self, container_name):
        super().__init__(container_name)
        self.apiroot = "https://quay.io/api/v1/repository"

    def _query_tag_api(self, tag=None):
        """
        Custom endpoint to handle quay and pagination.
        """
        repository = self.container_name.replace("quay.io/", "", 1)
        page = 1
        tags = []
        has_more = True
        specific_tag = "&specificTag=%s" % tag if tag else ""
        while has_more:
            url = "%s/%s/tag/?limit=100&page=%s%s" % (
                self.apiroot,
                repository,
                page,
                specific_tag,
            )
            response = self.get_request(url).json()
            tags = response.get("tags", {})

            if len(tags) == 0:
                raise ValueError(
                    f"The tag {tag} you provided is not known. "
                    f"Check that it and the container both exist."
                )
            new_tags = [x for x in tags if x.get("name")]
            tags.extend(new_tags)
            has_more = response.get("has_additional") is True
            page += 1
        return {
            tag.get("name"): tag.get("manifest_digest", "unknown")
            for tag in tags
            if tag.get("name") is not None
        }

    def manifest(self, tag):
        raise NotImplementedError(
            "Manifest retrieval for QuayDockerImage has not been implemented."
        )

    def config(self):
        raise NotImplementedError(
            "Config retrieval for QuayDockerImage has not been implemented."
        )


class DockerHubImage(DockerImage):

    """
    A thin client for getting metadata about an image on DockerHub.
    """

    def __init__(self, container_name):
        super().__init__(container_name)
        container_name_array = container_name.replace("docker.io/", "", 1).split("/")
        if len(container_name_array) == 1:
            self.container_name = "library/%s" % container_name_array[0]
        elif len(container_name_array) == 2:
            self.container_name = "%s/%s" % (
                container_name_array[0],
                container_name_array[1],
            )
        self.apiroot = "https://hub.docker.com/v2/repositories"

    def _query_tag_api(self, tag=None):
        tag_responses = []
        if tag is None:
            url = "%s/%s/tags?page_size=%s" % (self.apiroot, self.container_name, 100)
        else:
            url = "%s/%s/tags/%s" % (self.apiroot, self.container_name, tag)

        while True:
            response = self.get_request(url)
            tag_responses.extend(response.json()["results"])
            url = response.json().get("next")
            if url is None:
                break

        return {
            tag["name"]: tag.get(
                "digest", tag.get("images", [{}])[0].get("digest", "unknown")
            )
            for tag in tag_responses
            if tag.get("name") is not None
        }

    def manifest(self, tag):
        raise NotImplementedError(
            "Manifest retrieval for DockerHubImage has not been implemented."
        )

    def config(self):
        raise NotImplementedError(
            "Config retrieval for DockerHubImage has not been implemented."
        )


class NGCImage(DockerImage):

    """
    A thin client for getting metadata about an image on NGC.
    """

    def __init__(self, container_name):
        super().__init__(container_name)
        self.apiroot = None
        self.container_name = container_name.replace("nvcr.io/", "", 1)

        from ngcsdk import Client

        self.client = Client()
        self.client.configure(
            os.environ.get("SHPC_NGC_API_KEY"),
        )

    def _query_tag_api(self):
        image_list = self.client.registry.image.list(self.container_name)
        return {image.tag: image.digest for image in image_list}

    def manifest(self, tag):
        raise NotImplementedError(
            "Manifest retrieval for NGCImage has not been implemented."
        )

    def config(self):
        raise NotImplementedError(
            "Config retrieval for NGCImage has not been implemented."
        )
