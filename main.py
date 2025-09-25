from services.bussines_logic.orchestrator import make_workflow
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

logger.info("Iniciando o aplicativo.")

if __name__ == "__main__":
    app = make_workflow()

    final_state = app.invoke({})


     
    if final_state.get("resultado_final"):
        logger.info(f"Resultado final: {final_state['resultado_final']}")
    else:
        logger.info("Todos os registros foram processados com sucesso. Nenhum e-mail foi enviado.")





