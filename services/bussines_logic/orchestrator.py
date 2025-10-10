from langgraph.graph import StateGraph, END
from typing import  TypedDict,Dict,LiteralString
import logging
from models.ErrorModel.ErrorModel import ErrorSummaryModel


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class GraphState(TypedDict):
    """
    Representa o estado do fluxo de trabalho de verificação de erros.
    """

    process_items: bool
    updated_items: bool
    failures_grouped_by_store: list[ErrorSummaryModel]
    final_result: LiteralString


class Orchestrator:

    def __init__(self, extractor, updater, error_analysis, notifier):
        self.extractor = extractor
        self.updater = updater
        self.error_analysis = error_analysis
        self.notifier = notifier

    def extract_data_node(self, state: GraphState) -> Dict:
        itens = self.extractor.run()  
        return {"process_items": itens}

    def update_database_node(self, state: GraphState) -> Dict:
        self.updater()
        failed = self.extractor.run()  
        return {"updated_items": failed}


    def group_failures_node(self, state: GraphState) -> Dict:
        grouped_fails = self.error_analysis.run()
        return {"failures_grouped_by_store": grouped_fails}

    def send_email_node(self,state: GraphState) -> Dict:
        grouped_fails = state["failures_grouped_by_store"]
        mensagem_final = self.notifier(grouped_fails) 
        return {"final_result": mensagem_final}

    def workflow_after_update(self,state: GraphState) -> LiteralString:

        if state["updated_items"]:
            return "group_failures"
        else:
            return "final_result"
        


    def make_workflow(self) -> StateGraph:
        workflow = StateGraph(GraphState)

        workflow.add_node("extract_data", self.extract_data_node)
        workflow.add_node("update_database", self.update_database_node)
        workflow.add_node("group_failures", self.group_failures_node)
        workflow.add_node("send_email", self.send_email_node)

        workflow.set_entry_point("extract_data")

        workflow.add_edge("extract_data", "update_database")
        workflow.add_edge("group_failures", "send_email")
        workflow.add_edge("send_email", END)

        workflow.add_conditional_edges(
            "update_database",
            self.workflow_after_update,
            {
                "group_failures": "group_failures",
                "final_result": END,
            },
        )
        
        return workflow.compile()


if __name__ == "__main__":

    orchestrator = Orchestrator()
        
    app = orchestrator.make_workflow()
    
    final_state = app.invoke({})

    if final_state.get("final_result"):
        logger.info(final_state["final_result"])
    else:
        logger.info("Todos os registros foram processados com sucesso. Nenhum e-mail foi enviado.")

