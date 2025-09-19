from db.DataBaseManager import DatabaseManager
from db.MongoDbManager import MongoDbManager
from classes.ErrorAnalysisService  import ErrorAnalysisService


erro_analyze = ErrorAnalysisService

mongo_db_manager = MongoDbManager()

def update_registers():
        print("Iniciando atualização de registros...")

        errors_list = mongo_db_manager.get_data()
        if not errors_list:
            print("Nenhum erro encontrado.")
            return
        
        grouped_store = erro_analyze.group_errors_by_store(errors_list)
        seen = set()
        for error_model in grouped_store.errors:
            id_store = error_model.store
            erros = error_model.error
            
            with DatabaseManager(store=id_store) as data_base_manager:
                for err in erros:
                    err_table_name = err.table_name
                    if err_table_name:
                        for db_table_name,queue in data_base_manager.fila_tabela.items():
                            for column_name,column_value in queue.items():
                                for err_ref in erros:
                                    if err_ref.table_name.lower() == db_table_name.lower() and err_ref.store == id_store:
                                        query = f"""UPDATE {column_name}
                                                    SET DATA = DATA
                                                    WHERE {column_value} = {err_ref.code} 
                                                """
                                        if query:
                                            print(f"Loja: {id_store}")
                                            print(query)
                                        else:
                                            print(f"LOJA:{id_store} Nenhum erro encontrado!")
                                                                                                                        
                                # if query:
                                # data_base_manager.execute_query(query)
if __name__ == "__main__":
    update_registers()