__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2020-2021, Vanessa Sochat"
__license__ = "MPL 2.0"

from sqlalchemy import (
    create_engine,
    Column,
    DateTime,
    Integer,
    String,
    Text,
    ForeignKey,
    func,
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import UniqueConstraint
from sqlalchemy.orm import backref, relationship, scoped_session, sessionmaker

from shpc.logger import logger
from uuid import uuid4
import os

Base = declarative_base()

# NOTE: These modules are not in use, and likely to be removed.


class Collection(Base):

    # TODO need to redo these for modules, etc.
    __tablename__ = "collection"
    id = Column(Integer, primary_key=True)
    name = Column(String(150), unique=True)
    token = Column(String(50))
    created_at = Column(DateTime, default=func.now())
    containers = relationship(
        "Container",
        lazy="select",
        cascade="delete,all",
        backref=backref("collection", lazy="joined"),
    )

    def __init__(self, name=None, token=None):
        self.name = name
        if token is None:
            token = str(uuid4())
        self.token = token

    def __repr__(self):
        return "<Collection %r>" % (self.name)

    def __str__(self):
        return "<Collection %r>" % (self.name)

    def url(self):
        """return the collection url"""
        return "file://"


class Container(Base):
    """a container belongs to a collection

    Parameters
    ==========
    created_at: the creation date of the image / container
    metrics: typically the inspection of the image. If not possible, then the
             basic name (uri) derived from the user is used.
    tag: the image tag
    image: the path to the image on the filesystem (can be Null)
    url: the url where the imate was ultimately retrieved, call be Null
    client: the client backend associated with the image, the type(client)
    version: a version string associated with the image
    :collection_id: the id of the colletion to which the image belongs.

    We index / filter containers based on the full uri, which is assembled
               from the <collection>/<namespace>:<tag>@<version>, then stored
               as a variable, and maintained separately for easier query.
    """

    __tablename__ = "container"
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=func.now())
    metrics = Column(Text, nullable=False)
    name = Column(String(250), nullable=False)
    tag = Column(String(250), nullable=False)
    image = Column(String(250), nullable=True)
    url = Column(String(500), nullable=True)
    uri = Column(String(500), nullable=True)
    client = Column(String(50), nullable=False)
    version = Column(String(250), nullable=True)
    collection_id = Column(Integer, ForeignKey("collection.id"), nullable=False)

    __table_args__ = (
        UniqueConstraint(
            "collection_id", "name", "tag", "client", "version", name="_container_uc"
        ),
    )

    def __repr__(self):
        if self.uri is None:
            return "<Container %r>" % (self.name)
        return "<Container %r>" % (self.uri)

    def __str__(self):
        if self.uri is None:
            return "<Container %r>" % (self.name)
        return "<Container %r>" % (self.uri)

    def get_uri(self):
        """generate a uri on the fly from database parameters if one is not
        saved with the initial model (it should be, but might not be possible)
        """
        uri = "%s/%s:%s" % (self.collection.name, self.name, self.tag)
        if self.version not in [None, ""]:
            uri = "%s@%s" % (uri, self.version)
        return uri


def init_db(self, db_path):
    """initialize the database, with the default database path or custom of

    the format sqlite:////<install_root>/shpc.db
    """

    # Database Setup, use default if uri not provided
    self.database = "sqlite:///%s" % db_path

    # If the path isn't defined, cut out early
    if not db_path:
        return

    # Ensure that the parent_folder exists)
    parent_folder = os.path.dirname(db_path)

    # Case 1: Does not exist
    if not os.path.exists(parent_folder):
        logger.exit("Database location {} does not exist.".format(parent_folder))

    # Case 2: Insufficient permission for write
    if not os.access(parent_folder, os.W_OK):
        logger.exit("Insufficient permission to write to {}".format(parent_folder))

    logger.debug("Database located at %s" % self.database)
    self.engine = create_engine(self.database, convert_unicode=True)
    self.session = scoped_session(
        sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
    )

    Base.query = self.session.query_property()

    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    Base.metadata.create_all(bind=self.engine)
    self.Base = Base
