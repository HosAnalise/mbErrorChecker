from datetime import datetime
import psycopg
import logging
from models.DbModel.QueryReturnModel import QueryReturnModel
import hashlib
from settings.settings import get_db_settings



logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logging.basicConfig(level=logging.INFO)

c_handler = logging.StreamHandler()
c_handler.setLevel(logging.INFO) 

logger.addHandler(c_handler)



class DatabaseManager:
    """
    Database connection handler.

    Args:
        store (int): Store number used to build the database host IP. Default is 99.
    """

    def __init__(self, store=99, settings=None):
        self.settings = settings or get_db_settings()
        self.store = store
        self.host = self.settings.DB_HOST_TEMPLATE.format(store=self.store, domain="250" if store != 99 else "230")
        
        self.connection = None
        self.cursor = None
        self.fila_tabela = {
            # "int_bi_autorizacoes":{"caixa_autorizacoes": "cupom"},
            # # "int_bi_cadastros":{""},
            # # "int_bi_cancelamentos_devolve":{""}, -- coluna da tabela fila guid_web fora de ordem.
            # # "int_bi_cod_cancelamentos":{"caixa": "venda"}, -- colunas a mais (cliente, convenio e nr_pedido)
            # # "int_bi_contas_pagar":{"fin_contas_pagar": "codigo"}, -- colunas a mais (parcela e excluir)
            # # "int_bi_contasconvenios":{"contasconvenios": "convenio"}, -- colunas a mais (convenio e excluir)
            # "int_bi_contcaixas":{"controledecaixa": "ncaixa"},
            # # "int_bi_crediarios":{"crediarios": "codigo"}, -- colunas a mais (parcela)
            # "int_bi_entregas":{"entregas": "nr_entrega"},
            # # "int_bi_ids_web":{""},
            # "int_bi_notas":{"cab_nf": "nr_nota"},
            "int_bi_vendas": {"caixa": "venda"}
            }



    def __enter__(self):
        self.connection = self.db_connection()
        if self.connection:
            self.cursor = self.connection.cursor()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.connection:
            self.connection.close()
            self.cursor = None

   
    def db_connection(self):
        try:
            connection = psycopg.connect(
                dbname=self.settings.DB_NAME,
                user=self.settings.DB_USER,
                password=self.settings.DB_PASSWORD,
                host=self.host,
                port=self.settings.DB_PORT,
                connect_timeout=10
            )
            return connection
        except Exception as e:
            logger.error(f"Error connecting to the database {self.host}: {e}")

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
        if not self.cursor or not self.connection:
            logger.error("No database cursor or connection available.")
            return []
       
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
            if self.connection is not None:
                self.connection.rollback()

            raise e

    def format_query_result(self, resultados: list, table_name: str, store_id: int) -> list[QueryReturnModel]:
        return [
            QueryReturnModel(
                code=row[0],
                empresa=row[1],
                tentativas=row[2],
                guid_web=row[3],
                data_hora_tentativa=row[4],
                data_hora_inclusao=row[5],
                erro=row[6],
                table_name=table_name,
                store=store_id,
                date_column=datetime.now(),
                hash=hashlib.md5(str(row[6]).encode()).hexdigest()
            )
            for row in resultados
        ]
                    

   