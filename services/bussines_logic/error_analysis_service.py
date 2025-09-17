from classes.AgentFactory import AgentFactory
from models.DbModel.QueryReturnModel import QueryReturnModel
from db.MongoDbManager import MongoDbManager


class ErrorAnalysisAgent:
    """Classe para análise de erros usando um agente."""

    def __init__(self):
        self.mongo_manager = MongoDbManager()
        self.agent_factory = AgentFactory()

    
 
    def run(self, data: list[QueryReturnModel]) -> list[QueryReturnModel]:
        """Executa o agente de análise de erros."""
        return self.agent_factory.google_agent.run_sync(data).output




    

