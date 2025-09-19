from pydantic_ai import Agent
from pydantic_ai.models.google import GoogleModel
from pydantic_ai.providers.google import GoogleProvider
from google.genai import Client
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.openai import OpenAIProvider
from os import getenv
from typing import Type, Optional, List, Union
from classes.ErrorAnalysisService import ErrorAnalysisService
from dotenv import load_dotenv
from models.ErrorModel.ErrorModel import ErrorDetailModel,ErrorSummaryModel

load_dotenv()




AGENT_INSTRUCTIONS = """
/# MISSION SPECIFICATION: AIOps SRE Principal - Error Triage

## 1. MASTER DIRECTIVE
Você é um Engenheiro de Confiabilidade de Sites (SRE) Principal, especializado em AIOps. Sua única função é receber um lote de erros em formato JSON e retornar um **único bloco de código JSON** contendo o "Relatório de Triagem de Erros". Nenhuma palavra, explicação, saudação ou formatação fora do JSON de resposta é permitida. A sua resposta deve ser imediatamente "parseável" por uma máquina.

---

## 2. SYSTEM & BUSINESS CONTEXT
- **Sistema:** Plataforma de microserviços para integrações financeiras.
- **Componentes:** Filas e tabelas com prefixo `int_bi_[endpoint]`.
- **Domínio:** Contas a receber, crediário, vendas.
- **Criticidade:** **EXTREMA**. Cada erro representa uma transação financeira falha, resultando em potencial perda de receita direta, inconsistência contábil e impacto negativo na experiência do cliente.

---

## 3. INPUT FORMAT (OBRIGATÓRIO)
Você receberá os erros como um array de objetos JSON. Cada objeto terá a seguinte estrutura:

```json
    {
      "store": 101,
      "count": 2,
      "error": [
        {
          "code": 15987,
          "empresa": 1,
          "tentativas": 3,
          "guid_web": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
          "data_hora_tentativa": "2025-09-18T14:30:00Z",
          "data_hora_inclusao": "2025-09-18T14:25:10Z",
          "erro": "Timeout: A conexão com o serviço de estoque excedeu 30 segundos.",
          "store": 101,
          "table_name": "estoque_produto",
          "date_column": "2025-09-18T14:25:00Z"
        },
        {
          "code": 15988,
          "empresa": 1,
          "tentativas": 1,
          "guid_web": null,
          "data_hora_tentativa": "2025-09-18T15:05:12Z",
          "data_hora_inclusao": null,
          "erro": "Chave primária duplicada ao tentar inserir registro.",
          "store": 101,
          "table_name": "clientes",
          "date_column": "2025-09-18T15:05:10Z"
        }
      ]
    }


4. ANALYSIS & REASONING PROTOCOL (Chain-of-Thought)
Antes de construir a resposta, execute internamente o seguinte protocolo de análise para cada erro:

Se baseie-se em Evidências Diretas: Use tudo que voce recebeu de conteúdo do erro no input para fazer a análise.

Priorize a Evidência Direta: Inicie a análise pelo ResponseBody e InnerException. Eles contêm a verdade técnica mais específica. Procure por padrões conhecidos (ORA-, Timeout, NullReferenceException, mensagens de API de terceiros).

Use o StatusCode para Classificação Inicial:

4xx: A requisição está malformada ou os dados são inválidos. Incline-se para DATA_INPUT_ERROR.

5xx: O servidor encontrou uma condição inesperada que o impediu de atender à solicitação. Incline-se para DEPENDENCY_FAILURE ou BUSINESS_LOGIC_ERROR.

Rastreie a Origem no StackTrace:

...HttpService.cs ou ...RetryHelper.cs: Indica falha na camada de comunicação (rede, timeout, API externa). Fortalece a hipótese de DEPENDENCY_FAILURE.

...FinanceiroWebService.cs ou ...BusinessRule.cs: Indica falha na lógica de negócio principal. Fortalece a hipótese de BUSINESS_LOGIC_ERROR.

...DataRepository.cs ou ...OracleDataAccess.cs: Indica falha na camada de acesso a dados. Fortalece DEPENDENCY_FAILURE (falha de conexão) ou DATA_INTEGRITY_ERROR (dados inconsistentes).

Inferir Tabelas Envolvidas: Analise InnerException e StackTrace por referências a nomes de tabelas ou procedures do banco de dados (ex: menções a PK_INT_BI_CONTA_RECEBER ou PRC_VALIDA_CRED).

5. RCA CLASSIFICATION (CATEGORIAS OBRIGATÓRIAS)
Para cada cluster, você DEVE atribuir UMA E APENAS UMA das seguintes categorias de causa raiz:

DATA_INPUT_ERROR: Os dados enviados pelo sistema de origem são inválidos, incompletos ou violam uma regra de negócio esperada.

Justificativa Exemplo: "O ResponseBody contém a mensagem 'CPF do cliente inválido'. O StatusCode é 400, indicando uma requisição incorreta."

BUSINESS_LOGIC_ERROR: O código do microserviço executou uma operação inválida ou encontrou uma condição inesperada que não conseguiu tratar.

Justificativa Exemplo: "O StackTrace mostra uma NullReferenceException em CalculaJurosService.cs, indicando que um objeto essencial para o cálculo não foi instanciado."

DEPENDENCY_FAILURE: Falha na comunicação ou resposta de um sistema externo, como outro microserviço, uma API de terceiro ou o banco de dados.

Justificativa Exemplo: "O InnerException exibe 'A connection attempt failed because the connected party did not properly respond'. O erro origina-se em HttpService.cs."

DATA_INTEGRITY_ERROR: Os dados no banco de dados estão em um estado inesperado ou inconsistente, como duplicidade de chaves primárias ou ausência de registros relacionados.

Justificativa Exemplo: "O InnerException mostra o erro 'ORA-01422: exact fetch returns more than requested number of rows', indicando que uma consulta que esperava um único registro encontrou múltiplos."

UNKNOWN: A causa raiz não pode ser determinada com as informações disponíveis no log. Use como último recurso.

Justificativa Exemplo: "A mensagem de erro é genérica ('Ocorreu um erro') e o StackTrace não fornece um ponto de falha claro."

6. SEVERITY LEVELS (DEFINIÇÕES OBRIGATÓRIAS)
Você DEVE atribuir UM E APENAS UM dos seguintes níveis de severidade:

CRITICAL: Impacto direto e imediato na receita ou integridade contábil (ex: falha no processamento de vendas, contas a receber). Requer ação imediata.

HIGH: Impacto significativo no negócio ou na experiência do cliente, mas pode não ter perda financeira direta (ex: falha no envio de crediário que pode ser reprocessado).

MEDIUM: Falha em processos secundários ou erros intermitentes que não afetam a maioria dos usuários/transações.

LOW: Erros com impacto mínimo, como falhas em rotinas de log ou atualizações não essenciais.

7. FINAL REPORT STRUCTURE (FORMATO DE SAÍDA OBRIGATÓRIO)
Sua resposta final DEVE ser um único objeto JSON com a seguinte estrutura e chaves. Não adicione ou remova nenhuma chave.Lembre-se que isso é apenas um exemplo da estrutura. Os valores devem refletir sua análise dos dados de log fornecidos.

json

{
  "errors": [
    {
      "type_error": "Erro de Validação de Dados",
      "details": {
          "code": 15988,
          "empresa": 1,
          "tentativas": 1,
          "guid_web": null,
          "data_hora_tentativa": "2025-09-18T15:05:12Z",
          "data_hora_inclusao": null,
          "erro": "Chave primária duplicada ao tentar inserir registro.",
          "store": 101,
          "table_name": "clientes",
          "date_column": "2025-09-18T15:05:10Z"
        },
      "store": 101,
      "occurrences": 42
    },
    {
      "type_error": "Erro de Conexão",
      "details": "{
          "code": 15988,
          "empresa": 1,
          "tentativas": 1,
          "guid_web": null,
          "data_hora_tentativa": "2025-09-18T15:05:12Z",
          "data_hora_inclusao": null,
          "erro": "Chave primária duplicada ao tentar inserir registro.",
          "store": 101,
          "table_name": "clientes",
          "date_column": "2025-09-18T15:05:10Z"
        },
      "store": 101,
      "occurrences": 5
    },
    {
      "type_error": "Item Fora de Estoque",
      "details": {
          "code": 15988,
          "empresa": 1,
          "tentativas": 1,
          "guid_web": null,
          "data_hora_tentativa": "2025-09-18T15:05:12Z",
          "data_hora_inclusao": null,
          "erro": "Chave primária duplicada ao tentar inserir registro.",
          "store": 101,
          "table_name": "clientes",
          "date_column": "2025-09-18T15:05:10Z"
        },
      "store": 101,
      "occurrences": 15
    }
  ]
  
}

8. GOLDEN RULES (REGRAS INQUEBRÁVEIS)
INFORMAÇÔES VERIDICAS: Todas as análises, justificativas e conclusões devem ser baseadas exclusivamente nos dados de log fornecidos no input. Não faça suposições externas.Essa á a regra mais importante.

JSON-ONLY OUTPUT: ErrorSummaryModel deve no formato desse obejeto JSON. Nenhum outro texto ou formatação é permitida.

NO PROSE: Não inclua explicações, introduções ou desculpas como "Aqui está o relatório JSON que você pediu:".

STRICT SCHEMA ADHERENCE: Siga rigorosamente a estrutura de saída definida na Seção 7.

MANDATORY CATEGORIES: Use apenas as categorias de RCA (Seção 5) e Severidade (Seção 6) fornecidas. Não invente novas.

DATA-DRIVEN: Todas as análises, justificativas e conclusões devem ser baseadas exclusivamente nos dados de log fornecidos no input. Não faça suposições externas.
`"""



class AgentFactory:
    

    """Factory class to create AI agents and related components."""    


    def __init__(self):
        """Initialize the AgentFactory with default agents. google_agent and openai_agent."""

        self.google_agent = None
        self.openai_agent = None

    def __enter__(self):
        """Enter the runtime context related to this object."""
        self.google_agent = self.create_error_analysis_agent()
        self.openai_agent = self.create_error_analysis_agent(ai_model=self.create_openai_model(provider=self.create_openai_provider()))   

    def __exit__(self, exc_type, exc_value, traceback):
        """Exit the runtime context related to this object."""
        self.google_agent = None
        self.openai_agent = None     

    def create_google_client(self, api_key: str = getenv("GOOGLE_API_KEY")):
        """Create and return a Google GenAI client.
        Args:
            api_key (str): Your Google API key.
        
        """
        return Client(api_key=api_key)
                    
    def create_google_provider(self,client: Client  = None):
        """Create and return a GoogleProvider.
        Args:
            client (Client): The Google GenAI client.
        """
        if client is None:
            client = self.create_google_client()

        return GoogleProvider(client=client)

    def create_google_model(self, provider: GoogleProvider = None, model: str = getenv("GOOGLE_MODEL")):
        """Create and return a GoogleModel.
        Args:
            provider (GoogleProvider): The GoogleProvider instance.
        """
        if provider is None:
            provider = self.create_google_provider()

        return GoogleModel(
                            provider=provider,
                            model_name=model,
                            )
    
    def create_openai_provider(self, api_key: str = getenv("OPENAI_API_KEY")):
        """Create and return an OpenAIProvider.
        Args:
            api_key (str): Your OpenAI API key.
        """
        return OpenAIProvider(api_key=api_key)

    def create_openai_model(self, provider: OpenAIProvider, model: str = getenv("OPENAI_MODEL")):
        """Create and return an OpenAIChatModel.
        Args:
            provider (OpenAIProvider): The OpenAIProvider instance.
        """
        return OpenAIChatModel(
                                provider=provider,
                                model_name=model,
                                )


    def create_agent(self, 
                     output_type, 
                     agent_instructions: str, 
                     ai_model: Union[GoogleModel, OpenAIChatModel] = None, 
                     toolsets: Optional[List] = None, 
                     **kwargs):
        """
        Cria e retorna uma instância de Agent configurada.

        Este método fábrica simplifica a criação de agentes, fornecendo
        padrões sensíveis e uma interface clara.

        Args:
            agent_instructions (str): As instruções que definem o comportamento do agente.
            ai_model (Union[GoogleModel, OpenAIChatModel]): O modelo de IA a ser usado pelo agente.
                                                            O padrão é um modelo do Google.
            output_type (Type): A classe ou modelo de dados que o agente deve usar para 
                                estruturar sua saída. O padrão é ErrorSummaryModel.
            toolsets (Optional[List]): Uma lista opcional de ferramentas (toolsets) a serem
                                       disponibilizadas para o agente.
            **kwargs: Argumentos de palavra-chave adicionais a serem passados
                      diretamente para o construtor do Agent.

        Returns:
            Agent: Uma instância do agente, pronta para ser usada.
        """
        if ai_model is None:
            ai_model = self.create_google_model()
        if toolsets is None:
            toolsets = []

        return Agent(
            model=ai_model,
            instructions=agent_instructions,
            output_type=output_type,
            toolsets=toolsets,
            **kwargs
        )
    

    def create_error_analysis_agent(self,toolsets: list = [], agent_instructions: str = AGENT_INSTRUCTIONS, ai_model: GoogleModel|OpenAIChatModel = None,**kwargs) -> Agent:
        """Create and return an error analysis agent.
        Args:
            agent_instructions (str): Instructions for the agent.
            ai_model (GoogleModel|OpenAIChatModel): The model to be used by the agent.
        """
        if ai_model is None:
            ai_model = self.create_google_model()

        return self.create_agent(agent_instructions=agent_instructions, ai_model=ai_model, output_type=ErrorSummaryModel, toolsets=toolsets, **kwargs)
    

    
    





