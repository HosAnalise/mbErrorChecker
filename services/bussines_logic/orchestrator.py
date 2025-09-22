from langgraph.graph import StateGraph, END
from typing import List, TypedDict, Dict
from services.search_errors.look_for_errors import Extractor 
from services.bussines_logic.error_analysis_service import ErrorAnalysis
from services.presentation.email_notifier import EmailNotifierService
from services.update_registers.update_registers import update_registers as updater
from services.presentation.email_notifier import send_email as notifier
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class GraphState(TypedDict):
    """
    Representa o estado do fluxo de trabalho de verificação de erros.
    """
    process_items: List[Dict]
    updated_itens: List[Dict]
    failures_grouped_by_store: Dict[str, List[Dict]]
    final_result: str
    

def extract_data_node(state: GraphState) -> dict:
    itens = Extractor().run()  
    state['process_items'] = itens
    return state

def update_database_node(state: GraphState) -> dict:

    updater()
    falhados = Extractor().run()  
    state["updated_itens"] = falhados

    return state

def group_failures_node(state: GraphState) -> dict:
    itens_falhados = state["updated_itens"]
    falhas_agrupadas = ErrorAnalysis().run()
    return {"failures_grouped_by_store": falhas_agrupadas}

def send_email_node(state: GraphState) -> dict:
    falhas_agrupadas = state["failures_grouped_by_store"]
    mensagem_final = notifier.run(falhas_agrupadas) 
    return {"final_result": mensagem_final}

def workflow_after_update(state: GraphState) -> str:

    if state["itens_falhados"]:
        return "agrupar_falhas"
    else:
        return "finalizar_sucesso"
    


def make_workflow():
    workflow = StateGraph(GraphState)

    workflow.add_node("process_items", extract_data_node)
    workflow.add_node("update_database", update_database_node)
    workflow.add_node("group_failures", group_failures_node)
    workflow.add_node("send_email", send_email_node)

    workflow.set_entry_point("process_items")

    workflow.add_edge("process_items", "update_database")
    workflow.add_edge("group_failures", "send_email")
    workflow.add_edge("send_email", END)

    workflow.add_conditional_edges(
        "update_database",
        workflow_after_update,
        {
            "group_failures": "group_failures",
            "finalizar_sucesso": END,
        },
    )
    
    return workflow.compile()


if __name__ == "__main__":
    app = make_workflow()
    
    final_state = app.invoke({})
    
    if final_state.get("resultado_final"):
        print(final_state["resultado_final"])
    else:
        print("Todos os registros foram processados com sucesso. Nenhum e-mail foi enviado.")
    
    # Para depuração, você pode imprimir o estado final completo
    # import json
    # print("\n--- Estado Final Detalhado ---")
    # print(json.dumps(final_state, indent=2))