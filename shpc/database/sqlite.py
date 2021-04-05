__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2020-2021, Vanessa Sochat"
__license__ = "MPL 2.0"


# NOTE: this structure is not developed yet, and is likely to be removed.


def get_or_create_collection(self, name):
    """get a collection if it exists. If it doesn't exist, create it first.

    Parameters
    ==========
    name: the collection name parsed from parse_image_names()['collection']
    """
    from shpc.database.models import Collection

    collection = self.get_collection(name)

    # If it doesn't exist, create it
    if collection is None:
        collection = Collection(name=name)
        self.session.add(collection)
        self.session.commit()

    return collection


def get_collection(self, name):
    """get a collection, if it exists, otherwise return None."""
    from shpc.database.models import Collection

    return Collection.query.filter(Collection.name == name).first()


def get_container(self, name, collection_id, tag="latest", version=None):

    """get a container, otherwise return None."""
    from shpc.database.models import Container

    if not version:
        container = Container.query.filter_by(
            collection_id=collection_id, name=name, tag=tag
        ).first()
    else:
        container = Container.query.filter_by(
            collection_id=collection_id, name=name, tag=tag, version=version
        ).first()
    return container
