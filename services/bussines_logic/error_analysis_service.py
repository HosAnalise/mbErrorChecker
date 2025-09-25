from classes.AgentFactory import AgentFactory
from db.MongoDbManager import MongoDbManager
import backoff
from pydantic_ai import Agent
from models.ErrorModel.ErrorModel import ErrorModel, ErrorListModel,ErrorSummaryModel,AnalysisResponseModel,QueryReturnModel,ErrorDetailModel
from classes.Drain3 import Drain3Miner
import logging
from collections import defaultdict

logging.basicConfig(level=logging.INFO) 




class ErrorAnalysis:
    """Classe para análise de erros usando um agente."""

    def __init__(self,mongo_manager: MongoDbManager = None, agent: Agent = None, drain3_miner: Drain3Miner = None):
        self.mongo_manager = mongo_manager or MongoDbManager()
        self.analyse_agent = agent or AgentFactory().create_error_analysis_agent()
        self.drain3_miner = drain3_miner or Drain3Miner()




    def group_errors_by_store(self, list_errors: list[QueryReturnModel]) -> ErrorListModel:
        """
        Group errors by store code.

        Args:
            errors (list[QueryReturnModel]): List of query return models.

        Returns:
            ErrorListModel: Object with store code as key and list of errors as value.
        """

        try:
            grouped_errors = defaultdict(list)



            for error in list_errors:

                grouped_errors[error.store].append(error)

    
            return ErrorListModel(
                errors=[
                    ErrorModel(
                        error=value,
                        store=key,
                        count=len(value)
                    ) for key,value in grouped_errors.items()
                ]
            )    
        except Exception as e:
            logging.error("Erro ao agrupar erros por loja: %s", e, exc_info=True)
            return ErrorListModel(errors=[])
        
 


    @backoff.on_exception(backoff.expo, Exception,max_tries=20)
    def execute_agent(self, agent: Agent, data: dict) -> AnalysisResponseModel:
        """Executa o agente de análise de erros."""
        try:
            return agent.run_sync(data).output
        except Exception as e:
            logging.error("Erro ao executar o agente: %s", e, exc_info=True)
            raise e
        




    def run(self) -> ErrorSummaryModel:
        """Executa o processo de análise de erros de forma Pythônica."""
        try:
            data = self.mongo_manager.get_data()
            
            if not data:
                logging.warning("Nenhum dado encontrado para análise.")
                return ErrorSummaryModel(errors=[])               

            fingerprint_list = self.drain3_miner.make_fingerprint(data)
           

            error_summaries = [
                ErrorDetailModel(
                    details=fp.template_mined,
                    store_occurrences=fp.store,
                    table_name=fp.table_name,
                    analysis_response=self.execute_agent(
                        self.analyse_agent, {"template": fp.template_mined}
                    )
                )
                for fp in fingerprint_list
            ]
            
            return ErrorSummaryModel(errors=error_summaries)

        except Exception as e:
            logging.error("Erro ao executar o processo de análise: %s", e, exc_info=True)
            return ErrorSummaryModel(errors=[])
    


if __name__ == "__main__":

    error_agent = ErrorAnalysis()


    error_agent.run()




  

    

