from classes.AgentFactory import AgentFactory
from classes.ErrorAnalysisService import ErrorAnalysisService




def create_error_analysis_agent(toolsets:list=[]):
    """Create an error analysis agent using the AgentFactory."""
 
    with agent_factory := AgentFactory():
        agent_factory.google_agent.run_sync(toolsets=toolsets)



if __name__ == "__main__":
    create_error_analysis_agent(toolsets=[ErrorAnalysisService.group_errors_by_store])         