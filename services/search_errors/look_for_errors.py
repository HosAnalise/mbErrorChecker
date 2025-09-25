from db.DataBaseManager import DatabaseManager
from db.MongoDbManager import MongoDbManager
from classes.AgentFactory import AgentFactory
import logging


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


QUERY_STORE_IDS_TO_CHECK = """
                                SELECT 
                                    E.CODIGO 
                                FROM 
                                    EMPRESA E
                                WHERE 
                                    E.STATUS = 'ATIVO'
                            """



class Extractor:

    def __init__(self, mongo_manager: MongoDbManager = None):
        self.mongo_manager = mongo_manager or MongoDbManager()

    def process_store_errors(self,db_connection: DatabaseManager,store_id: int,queue_name: str = 'int_bi_vendas') -> None:
        """
        Conecta, consulta e salva erros de integração para UMA única loja.
        """
        query_sales_integration_error =f"""
                                        SELECT 
                                            * 
                                        FROM 
                                            {queue_name} ibv 
                                        WHERE 
                                            ibv.erro IS NOT NULL
                                                    
                                        """
        
        try:

            sales_with_errors = db_connection.execute_query(query=query_sales_integration_error)

            if sales_with_errors:
                formatted_results = db_connection.format_query_result(sales_with_errors,table_name=queue_name,store_id=store_id)
                self.mongo_manager.insert_many_data(formatted_results)
                
                
        except Exception as e:
            raise Exception(f"Erro ao processar a loja {store_id}: {e}")        



    def get_store_insert_error(self):
        
        """Orquestra a extração e armazenamento de erros de integração.

        Este método gerencia o fluxo completo de busca por erros de integração
        em todas as lojas ativas. Ele se conecta a múltiplas fontes de dados
        para coletar informações e as centraliza no MongoDB. É a principal
        ferramenta para a tarefa de "coletar todos os erros".

        Returns:
            None: O método não retorna um valor em caso de sucesso.

        Raises:
            Exception: Lança uma exceção genérica se ocorrer um erro crítico
                       que impeça a continuação do processo, como uma falha ao
                       obter a lista inicial de lojas.

        Side Effects:
            A execução bem-sucedida deste método resultará na inserção de novos
            documentos na coleção de erros do MongoDB.
        
        """
        
        with DatabaseManager() as db_connection:
            
            store_ids_to_check = db_connection.execute_query(query=QUERY_STORE_IDS_TO_CHECK)
            store_ids_to_check = [int(row[0]) for row in store_ids_to_check]

        self.mongo_manager.delete_all_collection_data()
        for store_id in store_ids_to_check:
            if store_id == 62:
                continue
            with DatabaseManager(store=store_id) as db_connection:
                if  not db_connection.connection:
                    continue
                for key in db_connection.fila_tabela.keys():
                    self.process_store_errors(db_connection=db_connection, store_id=store_id, queue_name=key)
         
        

    def run(self) -> bool:            
                
        try:
          
          self.get_store_insert_error()
        except Exception as e:
            raise Exception(f"Erro ao executar o agente de extração de dados: {e}")


if __name__ == "__main__":
    extractor = Extractor()
    response = extractor.run() 
