from langgraph.graph import StateGraph, END
from typing import List, TypedDict, Dict
from services.search_errors.look_for_errors import Extractor 
from services.update_registers.update_registers import UpdateService
from services.bussines_logic.error_analysis_service import ErrorAnalysisAgent
from services.presentation.email_notifier import EmailNotifierService

class GraphState(TypedDict):
    """
    Representa o estado do fluxo de trabalho de verificação de erros.
    """
    process_items: List[Dict]
    sucessfully_items: List[Dict]
    failed_items: List[Dict]
    failures_grouped_by_store: Dict[str, List[Dict]]
    final_result: str
    

def extract_data_node(state: GraphState) -> dict:
    itens = Extractor().run()  
    state['process_items'] = [item.dict() for item in itens]
    return state

def update_database_node(state: GraphState) -> dict:
    process_items = state["process_items"]

    falhados = updater.run(process_items)
    return {
        "itens_falhados": [f.dict() for f in falhados],
    }

def group_failures_node(state: GraphState) -> dict:
    itens_falhados = state["itens_falhados"]
    falhas_agrupadas = ErrorAnalysisAgent().run(itens_falhados)
    return {"failures_grouped_by_store": falhas_agrupadas}

def send_email_node(state: GraphState) -> dict:
    falhas_agrupadas = state["failures_grouped_by_store"]
    mensagem_final = notifier.run(falhas_agrupadas) 
    return {"final_result": mensagem_final}

def decidir_fluxo_apos_update(state: GraphState) -> str:

    if state["itens_falhados"]:
        return "agrupar_falhas"
    else:
        return "finalizar_sucesso"
    


def construir_grafo():
    workflow = StateGraph(GraphState)

    workflow.add_node("extrair_dados", extract_data_node)
    workflow.add_node("atualizar_banco", update_database_node)
    workflow.add_node("agrupar_falhas", group_failures_node)
    workflow.add_node("enviar_email", send_email_node)

    workflow.set_entry_point("extrair_dados")

    workflow.add_edge("extrair_dados", "atualizar_banco")
    workflow.add_edge("agrupar_falhas", "enviar_email")
    workflow.add_edge("enviar_email", END)

    workflow.add_conditional_edges(
        "atualizar_banco",
        decidir_fluxo_apos_update,
        {
            "agrupar_falhas": "agrupar_falhas",
            "finalizar_sucesso": END,
        },
    )
    
    return workflow.compile()


if __name__ == "__main__":
    app = construir_grafo()
    
    final_state = app.invoke({})
    
    if final_state.get("resultado_final"):
        print(final_state["resultado_final"])
    else:
        print("Todos os registros foram processados com sucesso. Nenhum e-mail foi enviado.")
    
    # Para depuração, você pode imprimir o estado final completo
    # import json
    # print("\n--- Estado Final Detalhado ---")
    # print(json.dumps(final_state, indent=2))