import psycopg
import logging
from os import getenv
from models.DbModel.QueryReturnModel import QueryReturnModel


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logging.basicConfig(level=logging.INFO)

c_handler = logging.StreamHandler()
c_handler.setLevel(logging.INFO) 

logger.addHandler(c_handler)


fila_tabela = {
    "vendas": "caixa"
}

class DatabaseManager:
    """
    Database connection handler.

    Args:
        store (int): Store number used to build the database host IP. Default is 99.
    """

    def __init__(self, store=99):

        self.store = store
        self.connection = None
        self.cursor = None
       



    def __enter__(self):
        self.connection = self.db_connection()
        if self.connection:
            self.cursor = self.connection.cursor()
        return self.connection

    def __exit__(self, exc_type, exc_value, traceback):
        if self.connection:
            self.connection.close()
            self.cursor = None

   
    def db_connection(self):
        try:
            connection = psycopg.connect(
                dbname=getenv("DB_NAME"),
                user=getenv("DB_USER"),
                password=getenv("DB_PASSWORD"),
                host=f"192.168.{self.store}.250" if self.store != 99 else "192.168.99.230",
                port=getenv("DB_PORT"),
                connect_timeout=5
            )
            return connection
        except Exception as e:
            logger.error(f"Error connecting to the database 192.168.{self.store:02}.250: {e}")
            return None

    def execute_query(self, query, params=None):
        """
        Execute a SQL query.

        Args:
            query (str): SQL query string.
            params (tuple, optional): Parameters for the query.

        Returns:
            list or None: Query result for SELECT, None otherwise.
        """
        if not self.cursor:
            logger.error("No database cursor available.")
            return None
        try:
            self.cursor.execute(query, params)
            if query.strip().lower().startswith("select"):
                result = self.cursor.fetchall()
            else:
                self.connection.commit()
                result = None
            return result
        except Exception as e:
            logger.error(f"Error executing query: {e}")
            return None
        

    def format_query_result(self, resultados: list) -> list[QueryReturnModel]:


            return [
                ## Exemplo de Model Pydantic
                QueryReturnModel(
                    venda=row[0],
                    empresa=row[1],
                    tentativas=row[2],
                    guid_web=row[3],
                    data_hora_tentativa=row[4],
                    data_hora_inclusao=row[5],
                    erro=row[6]
                )
                for row in resultados
            ]
                    

   