#criar classe de conexao com mongoDB usando como base a classe DataBaseManager
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import logging
from os import getenv

logger = logging.getLogger(__name__)


class MongoDbManager:
    """
    MongoDB connection handler.
    """

    def __init__(self,):
        self.uri = getenv("MONGO_URI")
        self.db_name = getenv("MONGO_DB_NAME")
        self.collection_name = getenv("MONGO_COLLECTION_NAME")
        self.client = None
        self.db = None

    def __enter__(self):
        try:
            self.client = MongoClient(self.uri)
            self.db = self.client[self.db_name]

        except ConnectionFailure as e:
            logger.error(f"Error connecting to MongoDB: {e}")
        return self.db

    def __exit__(self, exc_type, exc_value, traceback):
        if self.client:
            self.client.close()
