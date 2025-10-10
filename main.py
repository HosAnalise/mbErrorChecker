from services.bussines_logic.orchestrator import Orchestrator
import logging
from services.search_errors.look_for_errors import Extractor 
from services.bussines_logic.error_analysis_service import ErrorAnalysis
from services.update_registers.update_registers import update_registers as updater
from services.presentation.email_notifier import send_email as notifier
from db.MongoDbManager import MongoDbManager
from classes.AgentFactory import AgentFactory
from classes.Drain3 import Drain3Miner
from classes.TextFormatter import TextFormatter
from db.AlchemyManager import AlchemyManager



logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

logger.info("Iniciando o aplicativo.")

if __name__ == "__main__":
    data_base = AlchemyManager()
    mongo_manager = MongoDbManager()
    extractor = Extractor(db_connection=data_base,mongo_manager=mongo_manager)
    agent_factory = AgentFactory()
    text_formatter = TextFormatter()
    drain3_miner = Drain3Miner(text_formatter=text_formatter)
    error_analysis = ErrorAnalysis(mongo_manager=mongo_manager, agent=agent_factory.google_agent, drain3_miner=drain3_miner)

    orchestrator = Orchestrator(extractor=extractor, updater=updater(error_analysis=error_analysis), error_analysis=error_analysis, notifier=notifier(mongo_manager=mongo_manager))

    app = orchestrator.make_workflow()

    final_state = app.invoke({})    
    if final_state.get("final_result"):
        logger.info(f"Resultado final: {final_state['final_result']}")
    else:
        logger.info("Todos os registros foram processados com sucesso. Nenhum e-mail foi enviado.")
        logger.info("All records have been processed successfully. No email was sent.")





