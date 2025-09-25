from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import logging
from os import getenv
from models.DbModel.QueryReturnModel import QueryReturnModel
from dotenv import load_dotenv
from pymongo.results import InsertOneResult, InsertManyResult
from pymongo.server_api import ServerApi
import hashlib
from settings.settings import get_mongo_settings




load_dotenv()

logger = logging.getLogger(__name__)


class MongoDbManager:
    """
    MongoDB connection handler.
    """

    def __init__(self,settings=None):
        self.settings = settings or get_mongo_settings()
        self.uri = self.settings.MONGODB_URI
        self.db_name = self.settings.MONGO_DB_NAME
        self.collection_name = self.settings.MONGO_COLLECTION_NAME
        self.client = MongoClient(self.uri,server_api=ServerApi('1'))
        self.db = self.client[self.db_name]

    # def __enter__(self):
    #     try:
    #         self.client = MongoClient(self.uri) if not self.client else self.client
    #         self.db = self.client[self.db_name] if not self.db else self.db

    #     except ConnectionFailure as e:
    #         logger.error(f"Error connecting to MongoDB: {e}")
    #     return self.db

    # def __exit__(self, exc_type, exc_value, traceback):
    #     if self.client:
    #         self.client.close()

    def insert_data(self, data: QueryReturnModel) -> InsertOneResult | None:
        
        """Insere um único documento e retorna o resultado da operação."""

        self.delete_all_collection_data()
        if self.db is not None:
            collection = self.db[self.collection_name]
            # Retorna o resultado que contém o inserted_id
            return collection.insert_one(data.model_dump())
        return None

    def insert_many_data(self, data: list[QueryReturnModel]) -> InsertManyResult | None:
        """Insere múltiplos documentos e retorna o resultado da operação."""


        if self.db is not None:
            collection = self.db[self.collection_name]
            documents = [item.model_dump() for item in data]
            if not documents:
                return None
            
            return collection.insert_many(documents)
        return None

    def get_data(self,collection_name:str = 'mb_error_check')->list[QueryReturnModel]:
        if self.db is not None:
            if collection_name:
                self.collection_name = collection_name

            collection = self.db[self.collection_name]

            return [QueryReturnModel(**item) for item in collection.find()] 
        


    def get_emails(self):
        if self.db is not None:
            collection = self.db['emails']
            return collection.find()    
        
    def get_data_by_store_id(self, id: int):
        if self.db:
            collection = self.db[self.collection]
            return collection.find({"store": id})
        
    def delete_all_collection_data(self,collection_name:str = 'mb_error_check'):
        if self.db is not None:
            if collection_name:
                self.collection_name = collection_name

            collection = self.db[self.collection_name]
            return collection.delete_many({})
