from classes.AgentFactory import AgentFactory
from db.MongoDbManager import MongoDbManager
import backoff
from pydantic_ai import Agent
from models.ErrorModel.ErrorModel import ErrorModel,ErrorDetailModel, ErrorListModel,ErrorSummaryModel,AnalysisResponseModel
from drain3 import TemplateMiner
from drain3.template_miner_config import TemplateMinerConfig
import re
import unicodedata
import logging
from collections import defaultdict
from pydantic_ai.agent import RunContext

logging.basicConfig(level=logging.INFO) 



PATTERNS_SPECIFIC = [
    (re.compile(r'\b[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\b'), '{GUID}'),
    (re.compile(r'\b\d{4}-\d{2}-\d{2}[ T]\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+-]\d{2}:\d{2})?\b'), '{TIMESTAMP}'),
    (re.compile(r'("forma_recebimento":\s*")([A-Z]+)(")', re.IGNORECASE), r'\1{PAYMENT_METHOD}\3'),
]

PATTERNS_MULTILINE = [
    (r'RequestBody:.*?(?=\s*(?:GUID:|StackTrace:|\Z))', '{REQUEST_BODY}'),
    (r'StackTrace:.*?--- End of inner exception stack trace ---', '{STACK_TRACE}'), 
    (r'Extrato do Json da Venda: \{.*?\} \}', '{SALE_DATA}'),
    (r'("parcelas":\s*)\[.*?\]', r'\1[]'),
    (r'("tributacoes":\s*)\{.*?\}', r'\1{}'),
    (r'("produto":\s*)\[.*?\]', r'\1[]'),
]

PATTERNS_SENTENCES = [
    (re.compile(r'Erro ao enviar a venda.*?,/'), 'Erro ao enviar a venda {ID},/'),
    (re.compile(r', empresa.*?\./'), ', empresa {ID}./'),
]

PATTERNS_GENERIC = [
    (re.compile(r'\b\d{5,}\b'), '{ID}'),  
    (re.compile(r'\d+(\.\d+)?'), '{VALUE}'), 
]




class ErrorAnalysis:
    """Classe para análise de erros usando um agente."""

    def __init__(self,mongo_manager: MongoDbManager = None, agent: Agent = None):
        self.mongo_manager = mongo_manager or MongoDbManager()
        self.analyse_agent = agent or AgentFactory().create_error_analysis_agent()
        self.drain_config_template = TemplateMinerConfig()
        
        self.drain_config_template.drain_depth = 4
        self.drain_config_template.drain_sim_th = 0.4
        self.drain_config_template.drain_max_children = 100

        self.template_miner = TemplateMiner(config = self.drain_config_template)    




    def group_errors_by_store(self, ctx: RunContext) -> ErrorListModel:
        """
        Group errors by store code.

        Args:
            errors (list[QueryReturnModel]): List of query return models.

        Returns:
            ErrorListModel: Object with store code as key and list of errors as value.
        """

        try:
            grouped_errors = defaultdict(list)
            list_errors = ctx



            for error in list_errors:

                grouped_errors[error.store].append(error)

    
            return ErrorListModel(
                errors=[
                    ErrorModel(
                        error=value,
                        store=key,
                        count=len(value)
                    ) for key,value in grouped_errors.items()
                ]
            )    
        except Exception as e:
            logging.error("Erro ao agrupar erros por loja: %s", e, exc_info=True)
            return ErrorListModel(errors=[])
        
    def sanitize_log(self, log: str) -> str:

        """Sanitiza o log removendo caracteres especiais e espaços extras."""
        try:
            sanitized_content = unicodedata.normalize('NFKC', log)

            sanitized_content = re.sub(r'\s+', ' ', sanitized_content).strip()

            return sanitized_content
        except Exception as e:
            logging.error("Erro ao sanitizar log: %s", e, exc_info=True)
            return log


    @backoff.on_exception(backoff.expo, Exception,max_tries=20)
    def execute_agent(self, agent: Agent, data: dict) -> AnalysisResponseModel:
        """Executa o agente de análise de erros."""
        try:
            return agent.run_sync(data).output
        except Exception as e:
            logging.error("Erro ao executar o agente: %s", e, exc_info=True)
            raise e
        
    def regex_sanitize_pro(self,text: str) -> str:
        """
        Sanitiza o texto usando uma abordagem ordenada e eficiente de expressões regulares.
        Aplica as regras da mais específica para a mais genérica para evitar conflitos.
        """
        sanitized_text = text
        try:
            
            for pattern, placeholder in PATTERNS_SPECIFIC:
                sanitized_text = pattern.sub(placeholder, sanitized_text)

            for pattern, placeholder in PATTERNS_SENTENCES:
                sanitized_text = pattern.sub(placeholder, sanitized_text)

            for pattern, placeholder in PATTERNS_MULTILINE:
                sanitized_text = re.sub(pattern, placeholder, sanitized_text, flags=re.DOTALL)

            for pattern, placeholder in PATTERNS_GENERIC:
                sanitized_text = pattern.sub(placeholder, sanitized_text)
                
        except re.error as e:
            logging.error(f"Erro na expressão regular: {e}")
            return text 

        return sanitized_text

    def make_fingerprint(self, data: ErrorModel) -> list[dict]:
        """
        Normaliza e agrupa logs de erro para criar fingerprints únicos.

        Esta função processa uma lista de erros, sanitiza cada entrada e usa o 
        TemplateMiner para agrupar logs semelhantes. Ela garante que cada cluster 
        de log (fingerprint) seja adicionado à lista de resultados apenas uma vez.

        Args:
            data: Um objeto ErrorModel contendo os dados do erro, incluindo a loja e as mensagens.

        Returns:
            Uma lista de dicionários, onde cada dicionário representa um cluster de log único.
            Retorna uma lista vazia se não houver erros para processar ou se a loja não for a alvo.
            Retorna None em caso de uma exceção inesperada.
        """  
        try:
            unique_responses = {}
            for entry in data.error:               

                    sanitezed_content = self.sanitize_log(entry.erro)

                    regexed_content = self.regex_sanitize_pro(sanitezed_content)

                    replaced_content = regexed_content.replace('\r\n', '\n').replace('\\', '').replace('rn', ' ')

                    response = self.template_miner.add_log_message(replaced_content)

                    unique_responses[response.get('cluster_id')] = response 

                    table_name = entry.table_name if hasattr(entry, 'table_name') else 'N/A'
                    

            return list(unique_responses.values()), table_name if unique_responses else []

        except Exception as e:
            logging.error("Erro ao criar fingerprint: %s", e)
            return None


    def run(self)->list[ErrorSummaryModel]:
        """Executa o processo de análise de erros."""

        try:
            

            data = self.mongo_manager.get_data()
            
            if not data:
                logging.warning("Nenhum dado encontrado.")
                return []

            grouped_errors_by_store = self.group_errors_by_store(data)

            if not grouped_errors_by_store.errors:
                logging.warning("Nenhum erro agrupado encontrado.")
                return []

            error_summaries: list[ErrorSummaryModel] = []

            for store_errors in grouped_errors_by_store.errors:

                fingerprint_list, table_name = self.make_fingerprint(store_errors)
                

                if not fingerprint_list:
                    logging.info(f"Nenhum fingerprint gerado para a loja {store_errors.store}.")
                    continue

                
                error_details = [
                    ErrorDetailModel(
                        details=fingerprint.get('template_mined'),
                        occurrences=fingerprint.get('cluster_size', 1),
                        table_name=table_name or 'N/A', 
                        analysis_response=self.execute_agent(
                            agent=self.analyse_agent,
                            data=fingerprint.get('template_mined')
                        )
                    ) for fingerprint in fingerprint_list
                ]

                error_summaries.append(ErrorSummaryModel(
                    store=store_errors.store,
                    errors=error_details
                ))            

            return error_summaries
        
        except Exception as e:
            logging.error("Erro ao executar o agente: %s", e, exc_info=True)
            return []

if __name__ == "__main__":

    error_agent = ErrorAnalysis()


    error_agent.run()




  

    

