from db.DataBaseManager import DatabaseManager
from db.MongoDbManager import MongoDbManager
import logging
from db.AlchemyManager import AlchemyManager
from models.Tables import (  IntBiAutorizacoes
                            ,IntBiCadastros
                            ,IntBiCancelamentoDevolve
                            ,IntBiCodCancelamento
                            ,IntBiContasConvenios
                            ,IntBiContasPagar
                            ,IntBiContCaixas
                            ,IntBiCrediarios
                            ,IntBiIdsWeb
                            ,IntBiNotas
                            ,IntBiVendas)





logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class Extractor:
    

    def __init__(self, mongo_manager: MongoDbManager = None, db_connection: DatabaseManager|AlchemyManager = None):
        self.mongo_manager = mongo_manager 
        self.db_connection = db_connection 

        self._tables = [
            IntBiAutorizacoes.IntBiAutorizacoes,
            IntBiCadastros.IntBiCadastros,
            IntBiCancelamentoDevolve.IntBiCancelamentoDevolve,
            IntBiCodCancelamento.IntBiCodCancelamento,
            IntBiContasConvenios.IntBiContasConvenios,
            IntBiContasPagar.IntBiContasPagar,
            IntBiContCaixas.IntBiContCaixas,
            IntBiCrediarios.IntBiCrediarios,
            IntBiIdsWeb.IntBiIdsWeb,
            IntBiNotas.IntBiNotas,
            IntBiVendas.IntBiVendas
        ]

    
        

    def process_all_table_errors(self)-> list:
        """Processes errors from all predefined tables.
        
        Returns:
            list: A consolidated list of records containing errors from all tables.
        """
        all_errors = []
        
        try:
            for  table_class in self._tables:
                all_errors.extend(self.db_connection.dinamyc_select(table_class=table_class))

        except Exception as e:
            logger.error(f"Error to process a tables {e}")

        return all_errors   
        

    def run(self) -> bool:            
                
        try:
          self.get_store_insert_error()
          
        except Exception as e:
            raise Exception(f"Error to extract data: {e}")


if __name__ == "__main__":
    extractor = Extractor()
    response = extractor.run() 
