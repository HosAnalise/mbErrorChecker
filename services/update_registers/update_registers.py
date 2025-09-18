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
        
        for id_store,error in grouped_store.items():         
            with DatabaseManager(store=id_store) as data_base_manager:
                for error in error:
                    table_name = error.table_name
                    if table_name:
                        for table_name,queue in data_base_manager.fila_tabela.items():
                            for key,value in queue.items():
                                for error in errors_list:

                                    query = f"""UPDATE 
                                                    {key}
                                                SET 
                                                    DATA = DATA
                                                WHERE 
                                                    {value} = {error.code}                                                                                 

                                    """ if error.table_name.lower() == table_name.lower() else False

                                    print(query)
                                # if query:
                                # data_base_manager.execute_query(query)
if __name__ == "__main__":
    update_registers()