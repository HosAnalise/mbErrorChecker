from classes.AgentFactory import AgentFactory
from models.DbModel.QueryReturnModel import QueryReturnModel
from db.MongoDbManager import MongoDbManager
from classes.ErrorAnalysisService import ErrorAnalysisService






class ErrorAnalysisAgent:
    """Classe para análise de erros usando um agente."""

    def __init__(self):
        self.mongo_manager = MongoDbManager()
        self.agent_factory = AgentFactory()
        self.error_analysis_service = ErrorAnalysisService()

    
 
    def run(self, data: list[QueryReturnModel]) -> list[QueryReturnModel]:
        """Executa o agente de análise de erros."""

        agent = self.agent_factory.create_error_analysis_agent()
        # agent = self.agent_factory.create_agent(output_type=str)

        grouped_errors = self.error_analysis_service.group_errors_by_store(data)

        response = agent.run_sync(grouped_errors.model_dump())
        
        return response.output

if __name__ == "__main__":  
    error_agent = ErrorAnalysisAgent()
    mongo_manager = MongoDbManager()

    data = mongo_manager.get_data()


    analyzed_data = error_agent.run(data)

    print(analyzed_data)


  

    

