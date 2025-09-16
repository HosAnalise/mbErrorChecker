from langgraph.graph import StateGraph, END
from langgraph.graph.state import CompiledStateGraph

from pydantic import BaseModel
from json import loads
from models.agent.agent_pydantic.agent import AgentWork, AgentChat, AgentIntentionOption

import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(message)s'
)

class ChatState(BaseModel):
    agentChat: AgentChat
    intention: str | None = None
    response: str | None = None
    isWorking: bool = False

class AgentGraph:
    def __init__(self, agent_work: AgentWork) -> None:
        self.agent_nvita = agent_work.NVITA
        self.agent_detect_intention = agent_work.DETECT_INTENTION
        self.flow: list[str | None] = []

    def route_by_intention(self, state: ChatState) -> str:
        if state.isWorking == False:
            self.flow.clear()
            state.isWorking = True
            
        self.flow.append('route_by_intention')
        return state.intention

    def detect_intention(self, state: ChatState) -> ChatState:
        self.flow.append('detect_intention')
        resp = self.agent_detect_intention.query(agentChat=state.agentChat).output
        print(resp)
        intention = AgentIntentionOption.model_validate(loads(resp))
        state.intention = 'greet' if intention.cumprimentar else ''
        state.response = "Olá, como você está? Espero que esteja bem. MSG PADRÂO"

        print(state.response)
        return state

    
    def question_agent(self, state: ChatState) -> ChatState:
        self.flow.append('question_agent')
        r = self.agent_nvita.query(agentChat=state.agentChat)
        state.response = r.output

        return state
    
    def final_state(self, state: ChatState) -> ChatState:
        self.flow.append('final_stage')
        logging.info("***")
        logging.info(f"Flow Percorrido: {' -> '.join(self.flow)}")
        logging.info("***")
        

    def compile_graph(self) -> CompiledStateGraph:
        graph = StateGraph(state_schema=ChatState)

        #Nós do Grafo
        graph.add_node(node="agent", action=self.question_agent)
        graph.add_node(node="detect_intention", action=self.detect_intention)
        graph.add_node(node="final_state", action=self.final_state)
        #Flow do Grafo
        graph.set_entry_point(key="detect_intention")
        
        graph.add_conditional_edges(
            source='detect_intention',
            path=self.route_by_intention,
            path_map={
                'greet': 'final_state',
                'default': 'agent'
            }
        )

        graph.add_edge(start_key='agent', end_key='final_state')

        #compilo o grafo
        return graph.compile()