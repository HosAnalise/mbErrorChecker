from sqlalchemy import create_engine
from settings.settings import get_db_settings, get_firebird_settings
from sqlalchemy.exc import SQLAlchemyError





class AlchemyManager:
    def __init__(self, database='postgres'):
        self.database ="postgresql+psycopg2" if database == 'postgres' else "firebird+fdb"
        self.settings =  get_db_settings() if database == 'postgres' else get_firebird_settings()
        self.url_postgres = f"{self.database}://{self.settings.DB_USER}:{self.settings.DB_PASSWORD}@{self.settings.DB_HOST_TEMPLATE}:{self.settings.DB_PORT}/{self.settings.DB_NAME}" 
        self.url_firebird = f"{self.database}://{self.settings.DB_USER}:{self.settings.DB_PASSWORD}@{self.settings.DB_HOST_TEMPLATE}:{self.settings.DB_PORT}/{self.settings.DB_PATH}"



    def db_create_engine(self):
        try:
            connection_string = self.url_postgres if self.database == 'postgres' else self.url_firebird

            engine = create_engine(url=connection_string, echo=False, pool_pre_ping=True)
            return engine
        except SQLAlchemyError as e:
            print(f"Error creating the database engine: {e}")
            return None
    