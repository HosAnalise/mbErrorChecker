#criar classe de conexao com mongoDB usando como base a classe DataBaseManager

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

class MongoDbManager:
    """
    MongoDB connection handler.
    """

    def __init__(self, uri, db_name):
        self.uri = uri
        self.db_name = db_name
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
