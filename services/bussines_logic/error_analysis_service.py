from classes.AgentFactory import AgentFactory
from models.DbModel.QueryReturnModel import QueryReturnModel



def run_error_analysis_agent(data: list[QueryReturnModel]):
    """Create an error analysis agent using the AgentFactory."""
 
    with agent_factory := AgentFactory():
        return agent_factory.google_agent.run_sync(data).output
       


if __name__ == "__main__":

    

    run_error_analysis_agent(data=[])
