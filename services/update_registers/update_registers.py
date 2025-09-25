from db.DataBaseManager import DatabaseManager
from db.MongoDbManager import MongoDbManager
from services.bussines_logic.error_analysis_service import ErrorAnalysis
import logging
import time 

logging.basicConfig(level=logging.INFO)



def build_query(table_name: str, column_name: str, column_code: int):

    query = f"""UPDATE {table_name} 
                SET DATA = DATA
                WHERE {column_name} = {column_code}"""
    return query

def update_registers(erro_analyze: ErrorAnalysis = ErrorAnalysis(), mongo_db_manager: MongoDbManager = MongoDbManager()):
    try:
        
        logging.info("Iniciando atualização de registros...")

        errors_list = mongo_db_manager.get_data()
        if not errors_list:
            logging.info("Nenhum erro encontrado.")
            return
        
        grouped_store = erro_analyze.group_errors_by_store(errors_list)
        if not grouped_store.errors:
            logging.info("Nenhum grupo de erro foi formado.")
            return

        for error_group in grouped_store.errors:
            id_store = error_group.store
            logging.info(f"\n--- Processando Loja: {id_store} ---")
                
            with DatabaseManager(store=id_store) as db_manager:

                for single_error in error_group.error:
                    table_error = single_error.table_name.lower()
                    query_foi_montada = False

                    for table_name_queue, column_name in db_manager.fila_tabela.items():
                        if table_error == table_name_queue.lower():
                            for table_error, nome_coluna_chave in column_name.items():
                                            
                                query = build_query(table_name=table_error, column_name=nome_coluna_chave, column_code=single_error.code)

                                logging.info(f"[Loja {id_store}] Ação encontrada para o código {single_error.code}.")

                                db_manager.execute_query(query)
                                query_foi_montada = True

                        if not query_foi_montada:
                            logging.info(f"[Loja {id_store}] AVISO: A tabela '{single_error.table_name}' não tem uma ação de UPDATE mapeada.")
                
        return True

    except Exception as e:
        logging.error(f"Ocorreu um erro inesperado ao processar a loja {id_store}: {e} query foi: {query}", exc_info=True)
        return False        

if __name__ == "__main__":
    update_registers()