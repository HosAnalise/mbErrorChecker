from datetime import datetime
import psycopg
import logging
from os import getenv
from models.DbModel.QueryReturnModel import QueryReturnModel
from dotenv import load_dotenv

load_dotenv()


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

    def __init__(self, store=99):

        self.store = store
        self.connection = None
        self.cursor = None
        self.fila_tabela = {
<<<<<<< HEAD
            "int_bi_autorizacoes":{"caixa_autorizacoes": "cupom"},
            # "int_bi_cadastros":{""},
            # "int_bi_cancelamentos_devolve":{""}, -- coluna da tabela fila guid_web fora de ordem.
            # "int_bi_cod_cancelamentos":{"caixa": "venda"}, -- colunas a mais (cliente, convenio e nr_pedido)
            # "int_bi_contas_pagar":{"fin_contas_pagar": "codigo"}, -- colunas a mais (parcela e excluir)
            # "int_bi_contasconvenios":{"contasconvenios": "convenio"}, -- colunas a mais (convenio e excluir)
            "int_bi_contcaixas":{"controledecaixa": "ncaixa"},
            # "int_bi_crediarios":{"crediarios": "codigo"}, -- colunas a mais (parcela)
            "int_bi_entregas":{"entregas": "nr_entrega"},
            # "int_bi_ids_web":{""},
            "int_bi_notas":{"cab_nf": "nr_nota"},
=======
            # "int_bi_autorizacoes":{"caixa_autorizacoes": "cupom"},
            # # "int_bi_cadastros":{""},
            # # "int_bi_cancelamentos_devolve":{""},
            # "int_bi_cod_cancelamentos":{"caixa": "venda"},
            # "int_bi_contas_pagar":{"fin_contas_pagar": "codigo"},
            # "int_bi_contasconvenios":{"contasconvenios": "convenio"},
            # "int_bi_contcaixas":{"controledecaixa": "ncaixa"},
            # "int_bi_crediarios":{"crediarios": "codigo"},
            # "int_bi_entregas":{"entregas": "nr_entrega"},
            # # "int_bi_ids_web":{""},
            # "int_bi_notas":{"cab_nf": "nr_nota"},
>>>>>>> c8da9ae0d1f8f7e7883e9bfbf9c935cf509b704b
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
                dbname=getenv("DB_NAME"),
                user=getenv("DB_USER"),
                password=getenv("DB_PASSWORD"),
                host=f"192.168.{self.store}.250" if self.store != 99 else "192.168.99.230",
                port=getenv("DB_PORT"),
                connect_timeout=10
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
            return None
        

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
                date_column=datetime.now()
            )
            for row in resultados
        ]
                    

   