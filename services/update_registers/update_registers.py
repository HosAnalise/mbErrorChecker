from db.DataBaseManager import DatabaseManager
from db.MongoDbManager import MongoDbManager

mongo_db_manager = MongoDbManager()
data_base_manager = DatabaseManager() 

def update_registers():
    print("Iniciando atualização de dados...")
    
    errors_list = mongo_db_manager.get_data()
    if not errors_list:
        print("Nenhum erro encontrado.")
        return

    for error in errors_list:
        table_name = error.get("table_name")
        if table_name:
            for table_name,queue in mongo_db_manager.fila_tabela.items():
                for key,value in queue.items():
                    for error in errors_list:
                        
                        

                        query = f"""UPDATE 
                                        {key}
                                    SET 
                                        DATA = DATA
                                    WHERE 
                                        {value} = {error.get("code")}                             
                                

                        """ if error.get("table_name").lower() == table_name.lower() else ""

                        print(query)

                       # data_base_manager.execute_query(query)

update_registers()