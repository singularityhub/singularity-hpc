"""

Copyright (C) 2021 Vanessa Sochat.

This Source Code Form is subject to the terms of the
Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed
with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""

from shpc.logger import bot
import shpc.utils as utils
import os


def add(
    self,
    image_path=None,
    image_uri=None,
    image_name=None,
    url=None,
    metadata=None,
    save=True,
    copy=False,
):

    """dummy add simple returns an object that mimics a database entry, so the
    calling function (in push or pull) can interact with it equally. Most
    variables (other than image_path) are not used."""

    print("DUMMY ADD")
    import IPython

    IPython.embed()

    # We can only save if the image is provided
    if image_path is not None:
        if not os.path.exists(image_path):
            bot.exit("Cannot find %s" % image_path)

    if image_uri is None:
        bot.exit("You must provide an image uri <collection>/<namespace>")

    names = parse_image_name(remove_uri(image_uri))
    bot.debug("Added %s to filesystem" % names["uri"])

    # Create a dummy container on the fly
    class DummyContainer:
        def __init__(self, image_path, client_name, url, names):
            self.image = image_path
            self.client = client_name
            self.url = url
            self.name = names["image"]
            self.tag = names["tag"]
            self.uri = names["uri"]

    container = DummyContainer(image_path, self.client_name, url, names)

    bot.info("[container][add] %s" % names["uri"])
    return container


def init_db(self, db_path=None):
    """initialize the database, meaning we just set the name to be dummy"""

    # Database Setup, use default if uri not provided
    self.database = "dummy"
