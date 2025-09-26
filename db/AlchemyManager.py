from sqlalchemy import create_engine
from settings.settings import get_db_settings, get_firebird_settings
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker





class AlchemyManager:

    def __init__(self, database='postgres'):
        self.database ="postgresql+psycopg2" if database == 'postgres' else "firebird+fdb"
        self.settings =  get_db_settings() if database == 'postgres' else get_firebird_settings()
        self.url_postgres = f"{self.database}://{self.settings.DB_USER}:{self.settings.DB_PASSWORD}@{self.settings.DB_HOST_TEMPLATE}:{self.settings.DB_PORT}/{self.settings.DB_NAME}" 
        self.url_firebird = f"{self.database}://{self.settings.DB_USER}:{self.settings.DB_PASSWORD}@{self.settings.DB_HOST_TEMPLATE}:{self.settings.DB_PORT}/{self.settings.DB_PATH}"
        self.engine = None
        self.session = None

    def __enter__(self):
        self.engine = self.db_create_engine()
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        if self.engine:
            self.engine.dispose()
            self.engine = None

    def db_create_engine(self):
        try:
            connection_string = self.url_postgres if self.database == 'postgres' else self.url_firebird

            engine = create_engine(url=connection_string, echo=False, pool_pre_ping=True)
            return engine
        except SQLAlchemyError as e:
            print(f"Error creating the database engine: {e}")
            return None
        
    def create_session(self):
        if not self.engine:
            self.engine = self.db_create_engine()
        Session = sessionmaker(bind=self.engine)
        return Session()
    