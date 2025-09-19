from classes.AgentFactory import AgentFactory
from db.MongoDbManager import MongoDbManager
from classes.ErrorAnalysisService import ErrorAnalysisService
import backoff
from pydantic_ai import Agent
from models.ErrorModel.ErrorModel import ErrorModel,ErrorDetailModel
from drain3 import TemplateMiner
from drain3.template_miner_config import TemplateMinerConfig
import re
import unicodedata

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

    def __init__(self):
        self.mongo_manager = MongoDbManager()
        self.agent_factory = AgentFactory()
        self.error_analysis_service = ErrorAnalysisService()
        self.drain_config_template = TemplateMinerConfig()
        
        self.drain_config_template.drain_depth = 4
        self.drain_config_template.drain_sim_th = 0.4
        self.drain_config_template.drain_max_children = 100

        self.template_miner = TemplateMiner(config = self.drain_config_template)    

    def sanitize_log(self, log: str) -> str:
        """Sanitiza o log removendo caracteres especiais e espaços extras."""
        sanitized_content = unicodedata.normalize('NFKC', log)

        sanitized_content = re.sub(r'\s+', ' ', sanitized_content).strip()

        return sanitized_content  
    

    


    @backoff.on_exception(backoff.expo, Exception,max_tries=20)
    def execute_agent(self, agent: Agent, data: ErrorModel) -> ErrorDetailModel:
        """Executa o agente de análise de erros."""
        
        return agent.run_sync(data.model_dump()).output
    





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
            # Em um sistema real, aqui você logaria o erro.
            print(f"Erro na expressão regular: {e}")
            return text # Retorna o texto original em caso de erro

        return sanitized_text

    def make_fingerprint(self, data: ErrorModel) -> str:
        """
        Normaliza uma string de erro para criar um fingerprint.
        
        """




  
        try:
            lot_response = []
            if data.store == 9:
                for entry in data.error:

                

                        sanitezed_content = self.sanitize_log(entry.erro)
                        regexed_content = self.regex_sanitize_pro(sanitezed_content)
                        replaced_content = regexed_content.replace('\r\n', '\n').replace('\\', '').replace('rn', ' ')
                        response = self.template_miner.add_log_message(replaced_content)
                        print('\n\n\n')
                        print(response)
                        lot_response.append(response) if response['cluster_count'] not in lot_response else None

                print(f"tamanho lot_response criado com sucesso: {len(lot_response)}")
        except Exception as e:
            print(f"Erro ao criar fingerprint: {e}")
            return None


    def run(self):
        """Executa o processo de análise de erros."""

        try:
            print("Iniciando o processo de análise de erros...")
            
            # agent = self.agent_factory.create_error_analysis_agent()
            # print("Agente criado com sucesso.")

            data = self.mongo_manager.get_data()
            
            if not data:
                print("Nenhum dado encontrado.")
                return None

            grouped_errors = self.error_analysis_service.group_errors_by_store(data)
            print("Erros agrupados por loja com sucesso.")

            lot_response = []

            for error in grouped_errors.errors:
                self.make_fingerprint(error)
                # response = self.execute_agent(agent=agent, data=error)
                # lot_response.append(response)
                # print(response.model_dump())

            return lot_response
        except Exception as e:
            print(f"Erro ao executar o agente: {e}")
            return None

if __name__ == "__main__":

    error_agent = ErrorAnalysis()


    error_agent.run()




  

    

