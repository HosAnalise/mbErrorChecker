from db.DataBaseManager import DatabaseManager
from db.MongoDbManager import MongoDbManager

mongo_db_manager = MongoDbManager()
data_base_manager = DatabaseManager() 

def update_registers(): 
    errors_list = mongo_db_manager.get_data()   

    for table_name,value in mongo_db_manager.fila_tabela.items():
        for key,value in value.items():
            for error in errors_list:

                query = f"""UPDATE 
                                {key}
                            SET 
                                DATA = DATA
                            WHERE 
                                {value} = {error.get("code")}                             
                        

                """ if error.get("table_name").lower() == table_name.lower() else ""
                data_base_manager.execute_query(query)

update_registers()