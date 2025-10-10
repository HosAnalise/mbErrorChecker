import abc
from sqlalchemy import create_engine,select,Select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from settings.settings import get_db_settings, get_firebird_settings, get_oracle_settings
from typing import TypeVar, Type, Tuple

T = TypeVar('T')




class DatabaseConnector(abc.ABC):
    """
    Interface (Produto Abstrato) que define o contrato para todos os conectores de banco de dados.
    """
    def __init__(self, settings):
        self.settings = settings

    @abc.abstractmethod
    def get_connection_url(self) -> str:
        """Método abstrato que deve ser implementado por cada conector concreto."""
        pass



class PostgresConnector(DatabaseConnector):
    """Implementação concreta para PostgreSQL."""
    def get_connection_url(self) -> str:
        prefix = 'postgresql+psycopg2'
        return (f"{prefix}://{self.settings.DB_USER_POSTGRES}:{self.settings.DB_PASSWORD_POSTGRES}@"
                f"{self.settings.DB_HOST_TEMPLATE_POSTGRES}:{self.settings.DB_PORT_POSTGRES}/{self.settings.DB_NAME_POSTGRES}")

class FirebirdConnector(DatabaseConnector):
    """Implementação concreta para Firebird."""
    def get_connection_url(self) -> str:
        prefix = 'firebird+fdb'
        return (f"{prefix}://{self.settings.DB_USER_FIREBIRD}:{self.settings.DB_PASSWORD_FIREBIRD}@"
                f"{self.settings.DB_HOST_TEMPLATE_FIREBIRD}:{self.settings.DB_PORT_FIREBIRD}/{self.settings.DB_PATH_FIREBIRD}")

class OracleConnector(DatabaseConnector):
    """Implementação concreta para Oracle."""
    def get_connection_url(self) -> str:
        prefix = 'oracle+cx_oracle'
        return (f"{prefix}://{self.settings.DB_USER_ORACLE}:{self.settings.DB_PASSWORD_ORACLE}@"
                f"{self.settings.DB_HOST_TEMPLATE_ORACLE}:{self.settings.DB_PORT_ORACLE}/?service_name={self.settings.DB_NAME_ORACLE}")


class DatabaseConnectorFactory:
    """Fábrica responsável por instanciar o conector de banco de dados correto."""
    
    _connectors = {
        'postgres': PostgresConnector,
        'firebird': FirebirdConnector,
        'oracle': OracleConnector,
    }
    
    _settings_map = {
        'postgres': get_db_settings(),
        'firebird': get_firebird_settings(),
        'oracle': get_oracle_settings(),
    }

    @staticmethod
    def create_connector(db_type: str) -> DatabaseConnector:
        """
        Cria e retorna uma instância do conector apropriado.
        """
        db_type = db_type.lower()
        connector_class = DatabaseConnectorFactory._connectors.get(db_type)
        settings = DatabaseConnectorFactory._settings_map.get(db_type)

        if not connector_class or not settings:
            raise ValueError(f"Tipo de banco de dados desconhecido ou não suportado: '{db_type}'")
            
        return connector_class(settings())



class AlchemyManager:
    def __init__(self, database: str = 'postgres'):
        self.connector = DatabaseConnectorFactory.create_connector(db_type=database)
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
            connection_string = self.connector.get_connection_url()
            engine = create_engine(url=connection_string, echo=False, pool_pre_ping=True)
            return engine
        except SQLAlchemyError as e:
            print(f"Erro ao criar a engine do banco de dados: {e}")
            return None
            
    def create_session(self):
        if not self.engine:
            self.engine = self.db_create_engine()
        Session = sessionmaker(bind=self.engine)
        return Session()
    
    def build_query_for_errors(model_class: Type[T]) -> Select[Tuple[T]]:
        """
        Builds a SQLAlchemy Select object to fetch records from a specific model
        where the 'error' column is not null.

        Args:
            model_class: The ORM model class for which the query will be built.

        Returns:
            A Select object that can be executed later in a Session.
        """
      
        if not hasattr(model_class, 'error'):
            raise AttributeError(f"The model '{model_class.__name__}' does not have an 'error' attribute for filtering.")
            
        return select(model_class).where(model_class.error.is_not(None))
       
        