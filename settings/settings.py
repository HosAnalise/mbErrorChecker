from pydantic_settings import BaseSettings
from functools import lru_cache

class PostgreSQLSettings(BaseSettings):
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST_TEMPLATE: str
    DB_PORT: int

    class Config:
        env_file = ".env"
        env_prefix = "POSTGRES_" 


class FirebirdSettings(BaseSettings):
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST_TEMPLATE: str
    DB_PORT: int
    DB_PATH: str = None

    class Config:
        env_file = ".env"
        env_prefix = "FIREBIRD_"

class MongoSettings(BaseSettings):
    MONGODB_URI: str
    MONGO_DB_NAME: str
    MONGO_COLLECTION_NAME: str

    class Config:
        env_file = ".env"



class OracleSettings(BaseSettings):
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST_TEMPLATE: str
    DB_PORT: int

    class Config:
        env_file = ".env"
        env_prefix = "ORACLE_"        


class GoogleSettings(BaseSettings):
    GOOGLE_API_KEY: str
    GOOGLE_MODEL: str

    class Config:
        env_file = ".env"
        env_prefix = "GOOGLE_"      

class EmailSettings(BaseSettings):
    EMAIL_HOST: str
    EMAIL_PORT: int
    EMAIL_HOST_USER: str
    EMAIL_HOST_PASSWORD: str
    EMAIL_USE_TLS: bool
    EMAIL_USE_SSL: bool
    EMAIL_FROM: str
    EMAIL_TO: str

    class Config:
        env_file = ".env"
        env_prefix = "EMAIL_"          

@lru_cache()
def get_oracle_settings() -> OracleSettings:
    return OracleSettings()

@lru_cache()
def get_firebird_settings() -> FirebirdSettings:
    return FirebirdSettings()        


@lru_cache()
def get_google_settings() -> GoogleSettings:
    return GoogleSettings()

@lru_cache()
def get_db_settings() -> PostgreSQLSettings:
    return PostgreSQLSettings()

@lru_cache()
def get_mongo_settings() -> MongoSettings:
    return MongoSettings()

@lru_cache()
def get_email_settings() -> EmailSettings:
    return EmailSettings()


@lru_cache()
def get_all_settings():
    return {
        "db": get_db_settings(),
        "mongo": get_mongo_settings(),
        "google": get_google_settings(),
        "email": get_email_settings()
    }

