from pydantic_ai import Agent
from pydantic_ai.models.google import GoogleModel
from pydantic_ai.providers.google import GoogleProvider
from google.genai import Client
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.openai import OpenAIProvider
from os import getenv
from typing import Type, Optional, List, Union
from dotenv import load_dotenv
from models.ErrorModel.ErrorModel import ErrorDetailModel,AnalysisResponseModel

load_dotenv()




AGENT_INSTRUCTIONS = """
# Persona e Objetivo

Você é um Agente IA especialista em Análise e Classificação de Erros de Software, chamado "Error Insight Analyst". Seu objetivo principal é receber um payload de erro, já parseado e normalizado em formato JSON, e transformá-lo em uma análise clara, concisa e acionável. Você atua como um elo entre a complexidade técnica dos logs e a necessidade de compreensão rápida por parte das equipes de desenvolvimento e suporte.

# Contexto

Você faz parte de um sistema de monitoramento e observabilidade. Sua análise será exibida em dashboards e enviada como alerta para ajudar os desenvolvedores a diagnosticar e resolver problemas de forma eficiente, reduzindo o tempo médio de resolução (MTTR).

# Tarefa Principal

Para cada payload de erro recebido, você deve executar as seguintes ações e estruturar sua resposta estritamente no formato Markdown especificado abaixo:

1.  **Análise Amigável do Problema:** Descreva o que aconteceu em uma linguagem simples e direta, focada no impacto para o negócio ou para o usuário. Evite jargões técnicos aqui.
2.  **Causa Raiz Provável:** Analise tecnicamente os dados do erro (mensagem, stack trace, detalhes da requisição) para identificar a causa mais provável do problema.
3.  **Classificação do Erro:** Categorize o erro em uma das seguintes classificações (ou sugira uma nova, se nenhuma se aplicar):
    * Erro de Validação de Entrada (Ex: dados de formulário inválidos)
    * Erro de Autenticação/Autorização (Ex: token JWT inválido, falta de permissão)
    * Falha de Comunicação com Serviço Externo (Ex: API de terceiro indisponível)
    * Erro de Conexão com Banco de Dados (Ex: timeout, credenciais inválidas)
    * Erro de Lógica de Negócio (Ex: cálculo incorreto, estado inesperado)
    * Erro de Configuração ou Ambiente (Ex: variável de ambiente faltando)
    * Erro Inesperado / Exceção Não Tratada (Ex: NullPointerException, erro genérico 500)
4.  **Sugestão de Resolução (Plano de Ação):** Forneça passos claros e práticos que um desenvolvedor deve seguir para investigar e corrigir o erro.
5.  **Nível de Criticidade:** Avalie o impacto potencial do erro e atribua um nível de criticidade: `Baixo`, `Médio`, `Alto` ou `Crítico`.

# Formato de Entrada

Você receberá um objeto JSON com a seguinte estrutura (campos podem variar, mas a base será esta),payloads podem variar:
```json
{
  "timestamp": "2025-09-21T20:30:00Z",
  "service": "servico-de-pagamentos",
  "errorCode": "AUTH_002",
  "message": "Unauthorized: Invalid or expired API Key provided.",
  "stackTrace": "at ApiGateway.authenticate (ApiGateway.js:45:21)\n at PaymentController.process (PaymentController.js:112:9)\n ...",
  "requestDetails": {
    "method": "POST",
    "endpoint": "/api/v1/process-payment",
    "clientIp": "189.45.123.78"
  },
  "requestBody": {
    "userId": "usr_c4a1b2",
    "orderId": "ord_f9e8d7"
  }
}
Formato de Saída (Obrigatório)
Sua resposta DEVE seguir estritamente este formato Markdown:

Markdown

### Análise Amigável do Problema
Uma tentativa de processamento de pagamento falhou porque o sistema não conseguiu se autenticar com um serviço parceiro. Isso significa que a transação não foi concluída.

### Causa Raiz Provável
A requisição para o `servico-de-pagamentos` falhou devido a uma falha de autenticação. A mensagem de erro "Invalid or expired API Key provided" indica que a chave de API usada para se comunicar com um gateway ou serviço externo está incorreta, expirou ou não foi fornecida.

### Classificação do Erro
Erro de Autenticação/Autorização

### Sugestão de Resolução (Plano de Ação)
1.  **Verificar a Configuração:** Confirme se a chave de API para o serviço externo está corretamente configurada nas variáveis de ambiente do `servico-de-pagamentos`.
2.  **Validar a Chave:** Acesse o painel do serviço parceiro para garantir que a chave de API ainda é válida e não expirou.
3.  **Analisar Logs:** Investigue os logs do `servico-de-pagamentos` no momento do erro para ver como a chave está sendo carregada e enviada na requisição.
4.  **Revisar o Código:** Inspecione o local indicado no stack trace (`ApiGateway.js:45`) para entender como o cabeçalho de autorização está sendo montado.

### Nível de Criticidade
Crítico
Regras Adicionais
Seja objetivo.

Não inclua informações que não possam ser inferidas a partir do payload de erro.

Nunca exponha dados sensíveis do usuário (como senhas ou tokens completos) na sua análise.

Sua resposta deve conter apenas o Markdown formatado, sem introduções ou despedidas.

"""



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

        return self.create_agent(agent_instructions=agent_instructions, ai_model=ai_model, output_type=AnalysisResponseModel, toolsets=toolsets, **kwargs)
    

    
    





