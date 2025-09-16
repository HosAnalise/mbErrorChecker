from pydantic_ai import Agent
from pydantic_ai.models.google import GoogleModel
from pydantic_ai.providers.google import GoogleProvider
from google.genai import Client
from models.ErrorModel.ErrorModel import ErrorModel
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.openai import OpenAIProvider
from os import getenv

AGENT_INSTRUCTIONS = """
1. DIRETIVA DE PERSONA E OBJETIVO CORE

Você é um Engenheiro SRE (Site Reliability Engineer) Principal, especialista em AIOps (IA para Operações de TI). Sua missão não é apenas agrupar logs, mas sim realizar uma triagem inteligente de erros em um sistema de microserviços. Você deve identificar a causa raiz provável, avaliar o impacto no negócio e fornecer recomendações acionáveis para a equipe de engenharia. Seu objetivo final é gerar um "Relatório de Triagem de Erros" conciso e de alto valor.

// 2. CONTEXTO DO SISTEMA

O sistema monitorado processa filas de integração em tabelas com prefixo `int_bi_[endpoint]`. Cada registro na lista de entrada representa uma falha de processamento capturada. A tarefa é analisar um lote desses erros para entender o que está acontecendo no ambiente de produção, priorizar os problemas e direcionar a resolução.

// 3. DADOS DE ENTRADA (PAYLOAD DE ERROS)

A seguir, a lista de objetos de erro brutos que você deve analisar. A estrutura e os dados podem variar, mas sua análise deve ser muito mais profunda.

System.Exception: Erro ao enviar recebimento 990046324, empresa 99! Empresa 99. Endpoint: v2/recebimentoIndividualVenda.
 ---> Erro Web no envio do crediário 880140, empresa 99! Empresa 99. Endpoint: contaReceberSemVenda.
StackTrace:    at HOS.Integracoes.Application.Services.FinanceiroWebService.EnviarContaReceber(Int64 vendaOrigem, Int32 empresaOrigem, CancellationToken cancellationToken) in C:\Fontes\.NET\HOS.Integracoes\HOS.Integracoes.Application\Services\FinanceiroWebService.cs:line 10882
   at HOS.Integracoes.Application.Services.FinanceiroWebService.EnviarContasAnteriores(Crediario crediario, CancellationToken cancellationToken) in C:\Fontes\.NET\HOS.Integracoes\HOS.Integracoes.Application\Services\FinanceiroWebService.cs:line 10234
   at HOS.Integracoes.Application.Services.FinanceiroWebService.ObterRecebimentoCrediario(Caixa caixa, CancellationToken cancellationToken) in C:\Fontes\.NET\HOS.Integracoes\HOS.Integracoes.Application\Services\FinanceiroWebService.cs:line 10139
   at HOS.Integracoes.Application.Services.FinanceiroWebService.ObterRecebimento(Int64 venda, Int32 empresa, CancellationToken cancellationToken) in C:\Fontes\.NET\HOS.Integracoes\HOS.Integracoes.Application\Services\FinanceiroWebService.cs:line 10086
   at HOS.Integracoes.Application.Services.FinanceiroWebService.EnviarRecebimento(Int64 venda, Int32 empresa, IntBiVenda intBiVenda, CancellationToken cancellationToken) in C:\Fontes\.NET\HOS.Integracoes\HOS.Integracoes.Application\Services\FinanceiroWebService.cs:line 9948
InnerException: Erro de client ao enviar post. (Status Code: 400 BadRequest)
ResponseBody: [{"message":"Não foi possível inserir a Conta a receber","erro":"ORA-01422: exact fetch returns more than requested number of rows\n","stack":"ORA-06512: at \"ERP.BD_CONTA_RECEBER\", line 2426\n"}]GUID: 04A81F8429480F07AA0353F72503F6A4F84844E75FCB30EE4C2474B04FA0E4E5
RequestBody: [
  [
    {
      "crm": 4595,
      "codigo_farma": 880140,
      "n_parcela": 1,
      "n_parcela_total": 5,
      "pessoa_cliente_id": 3557064,
      "data_vencimento": "2023-04-10T00:00:00",
      "data_prevista_pagamento": "2023-04-10T00:00:00",
      "valor_parcela": 100.0,
      "data_emissao": "2023-04-10T10:50:18",
      "data_registro": "2023-04-10T10:50:18",
      "numero_documento": 880140,
      "numero_pedido": 880140,
      "codigo_barras": 0
    }
  ]
]
StackTrace:    at HOS.Integracoes.Application.Services.FinanceiroWebService.ResponsePolicy(HttpResponseMessage response, String content, String result, CancellationToken cancellationToken) in C:\Fontes\.NET\HOS.Integracoes\HOS.Integracoes.Application\Services\FinanceiroWebService.cs:line 247
   at HOS.Infrastructure.Services.HttpService.RunResponsePolicy(HttpResponseMessage response, String content, String result, CancellationToken cancellationToken) in C:\Fontes\.NET\HOS.Infrastructure\Services\HttpService.cs:line 395
   at HOS.Infrastructure.Services.HttpService.SendRequest[T](String url, HttpMethod method, Object payload, IEnumerable`1 headers, IEnumerable`1 parameters, CancellationToken cancellationToken) in C:\Fontes\.NET\HOS.Infrastructure\Services\HttpService.cs:line 204
   at HOS.Infrastructure.Services.RetryHelper.RetryAsync[T](Func`1 func, Int32 maxAttempts, Int32 delayMilliseconds, Predicate`1 shouldRetry, CancellationToken cancellationToken)
   at HOS.Infrastructure.Services.RetryHelper.RetryAsync[T](Func`1 func, Int32 maxAttempts, Int32 delayMilliseconds, Predicate`1 shouldRetry, CancellationToken cancellationToken) in C:\Fontes\.NET\HOS.Infrastructure\Services\RetryHelper.cs:line 120
   at HOS.Infrastructure.Services.HttpService.SendAsync[T](String url, HttpMethod method, Object payload, IEnumerable`1 headers, IEnumerable`1 parameters, CancellationToken cancellationToken) in C:\Fontes\.NET\HOS.Infrastructure\Services\HttpService.cs:line 147
   at HOS.Infrastructure.Services.HttpService.PostAsync[T](String url, Object payload, IEnumerable`1 headers, IEnumerable`1 parameters, CancellationToken cancellationToken) in C:\Fontes\.NET\HOS.Infrastructure\Services\HttpService.cs:line 111
   at HOS.Infrastructure.Services.HttpService.PostAsync(String url, Object payload, IEnumerable`1 headers, IEnumerable`1 parameters, CancellationToken cancellationToken) in C:\Fontes\.NET\HOS.Infrastructure\Services\HttpService.cs:line 107
   at HOS.Integracoes.Common.Infraestructure.Workers.GuardianProxy`1.AwaitGeneric[TResult](Task task, GuardianProxy`1 self) in C:\Fontes\.NET\HOS.Integracoes\HOS.Integracoes.Common\Infraestructure\Workers\GuardianProxy.cs:line 118
   at HOS.Integracoes.Application.Services.FinanceiroWebService.EnviarContaReceber(Int64 vendaOrigem, Int32 empresaOrigem, CancellationToken cancellationToken) in C:\Fontes\.NET\HOS.Integracoes\HOS.Integracoes.Application\Services\FinanceiroWebService.cs:line 10835
   --- End of inner exception stack trace ---System.Exception: Erro ao enviar recebimento 990046324, empresa 99! Empresa 99. Endpoint: v2/recebimentoIndividualVenda.
 ---> Erro Web no envio do crediário 880140, empresa 99! Empresa 99. Endpoint: contaReceberSemVenda.
StackTrace:    at HOS.Integracoes.Application.Services.FinanceiroWebService.EnviarContaReceber(Int64 vendaOrigem, Int32 empresaOrigem, CancellationToken cancellationToken) in C:\Fontes\.NET\HOS.Integracoes\HOS.Integracoes.Application\Services\FinanceiroWebService.cs:line 10882
   at HOS.Integracoes.Application.Services.FinanceiroWebService.EnviarContasAnteriores(Crediario crediario, CancellationToken cancellationToken) in C:\Fontes\.NET\HOS.Integracoes\HOS.Integracoes.Application\Services\FinanceiroWebService.cs:line 10234
   at HOS.Integracoes.Application.Services.FinanceiroWebService.ObterRecebimentoCrediario(Caixa caixa, CancellationToken cancellationToken) in C:\Fontes\.NET\HOS.Integracoes\HOS.Integracoes.Application\Services\FinanceiroWebService.cs:line 10139
   at HOS.Integracoes.Application.Services.FinanceiroWebService.ObterRecebimento(Int64 venda, Int32 empresa, CancellationToken cancellationToken) in C:\Fontes\.NET\HOS.Integracoes\HOS.Integracoes.Application\Services\FinanceiroWebService.cs:line 10086
   at HOS.Integracoes.Application.Services.FinanceiroWebService.EnviarRecebimento(Int64 venda, Int32 empresa, IntBiVenda intBiVenda, CancellationToken cancellationToken) in C:\Fontes\.NET\HOS.Integracoes\HOS.Integracoes.Application\Services\FinanceiroWebService.cs:line 9948
InnerException: Erro de client ao enviar post. (Status Code: 400 BadRequest)
ResponseBody: [{"message":"Não foi possível inserir a Conta a receber","erro":"ORA-01422: exact fetch returns more than requested number of rows\n","stack":"ORA-06512: at \"ERP.BD_CONTA_RECEBER\", line 2426\n"}]GUID: 04A81F8429480F07AA0353F72503F6A4F84844E75FCB30EE4C2474B04FA0E4E5
RequestBody: [
  [
    {
      "crm": 4595,
      "codigo_farma": 880140,
      "n_parcela": 1,
      "n_parcela_total": 5,
      "pessoa_cliente_id": 3557064,
      "data_vencimento": "2023-04-10T00:00:00",
      "data_prevista_pagamento": "2023-04-10T00:00:00",
      "valor_parcela": 100.0,
      "data_emissao": "2023-04-10T10:50:18",
      "data_registro": "2023-04-10T10:50:18",
      "numero_documento": 880140,
      "numero_pedido": 880140,
      "codigo_barras": 0
    }
  ]
]
StackTrace:    at HOS.Integracoes.Application.Services.FinanceiroWebService.ResponsePolicy(HttpResponseMessage response, String content, String result, CancellationToken cancellationToken) in C:\Fontes\.NET\HOS.Integracoes\HOS.Integracoes.Application\Services\FinanceiroWebService.cs:line 247
   at HOS.Infrastructure.Services.HttpService.RunResponsePolicy(HttpResponseMessage response, String content, String result, CancellationToken cancellationToken) in C:\Fontes\.NET\HOS.Infrastructure\Services\HttpService.cs:line 395
   at HOS.Infrastructure.Services.HttpService.SendRequest[T](String url, HttpMethod method, Object payload, IEnumerable`1 headers, IEnumerable`1 parameters, CancellationToken cancellationToken) in C:\Fontes\.NET\HOS.Infrastructure\Services\HttpService.cs:line 204
   at HOS.Infrastructure.Services.RetryHelper.RetryAsync[T](Func`1 func, Int32 maxAttempts, Int32 delayMilliseconds, Predicate`1 shouldRetry, CancellationToken cancellationToken)
   at HOS.Infrastructure.Services.RetryHelper.RetryAsync[T](Func`1 func, Int32 maxAttempts, Int32 delayMilliseconds, Predicate`1 shouldRetry, CancellationToken cancellationToken) in C:\Fontes\.NET\HOS.Infrastructure\Services\RetryHelper.cs:line 120
   at HOS.Infrastructure.Services.HttpService.SendAsync[T](String url, HttpMethod method, Object payload, IEnumerable`1 headers, IEnumerable`1 parameters, CancellationToken cancellationToken) in C:\Fontes\.NET\HOS.Infrastructure\Services\HttpService.cs:line 147
   at HOS.Infrastructure.Services.HttpService.PostAsync[T](String url, Object payload, IEnumerable`1 headers, IEnumerable`1 parameters, CancellationToken cancellationToken) in C:\Fontes\.NET\HOS.Infrastructure\Services\HttpService.cs:line 111
   at HOS.Infrastructure.Services.HttpService.PostAsync(String url, Object payload, IEnumerable`1 headers, IEnumerable`1 parameters, CancellationToken cancellationToken) in C:\Fontes\.NET\HOS.Infrastructure\Services\HttpService.cs:line 107
   at HOS.Integracoes.Common.Infraestructure.Workers.GuardianProxy`1.AwaitGeneric[TResult](Task task, GuardianProxy`1 self) in C:\Fontes\.NET\HOS.Integracoes\HOS.Integracoes.Common\Infraestructure\Workers\GuardianProxy.cs:line 118
   at HOS.Integracoes.Application.Services.FinanceiroWebService.EnviarContaReceber(Int64 vendaOrigem, Int32 empresaOrigem, CancellationToken cancellationToken) in C:\Fontes\.NET\HOS.Integracoes\HOS.Integracoes.Application\Services\FinanceiroWebService.cs:line 10835
   --- End of inner exception stack trace ---

`"""

class ErrorAnalysisService:
    def __init__(self, agent: Agent):
        self.agent = agent

    def analyze_errors(self, raw_messages: str) -> ErrorModel:
        """
        Analyze raw error messages and return structured error data.

        Args:
            raw_messages (str): Raw error messages to be analyzed.

        """
        # Call the agent's method to analyze the errors
        return self.agent.run(raw_messages)


class AgentFactory:

    """Factory class to create AI agents and related components."""    

    def create_google_client(self, api_key: str = getenv("GOOGLE_API_KEY")):
        """Create and return a Google GenAI client.
        Args:
            api_key (str): Your Google API key.
        
        """
        return Client(api_key=api_key)
                    
    def create_google_provider(self,client: Client = create_google_client()):
        """Create and return a GoogleProvider.
        Args:
            client (Client): The Google GenAI client.
        """
        return GoogleProvider(client=client)

    def create_google_model(self, provider: GoogleProvider = create_google_provider()):
        """Create and return a GoogleModel.
        Args:
            provider (GoogleProvider): The GoogleProvider instance.
        """
        return GoogleModel(
                            provider=provider,
                            model_name="gemini-pro",
                            )
    
    def create_openai_provider(self, api_key: str):
        """Create and return an OpenAIProvider.
        Args:
            api_key (str): Your OpenAI API key.
        """
        return OpenAIProvider(api_key=api_key)
    
    def create_openai_model(self, provider: OpenAIProvider):
        """Create and return an OpenAIChatModel.
        Args:
            provider (OpenAIProvider): The OpenAIProvider instance.
        """
        return OpenAIChatModel(
                                provider=provider,
                                model_name="gpt-4-turbo",
                                temperature=0.7,
                                max_retries=3
                                )
    
    
    def create_agent(self,agent_instructions:str, ai_model: GoogleModel|OpenAIChatModel = create_google_model(),output=ErrorModel,toolsets:list=[]):
        """
        Create and return an Agent.
        Args:
            agent_instructions (str): Instructions for the agent.
            ai_model (GoogleModel|OpenAIChatModel): The model to be used by the agent.
            output: The output model for the agent.
        """
        return Agent(
                    model=ai_model,
                    output_type=output,
                    instructions=agent_instructions,
                    toolsets=[tool for tool in toolsets],  
                    )
    

    def create_error_analysis_agent(self,toolsets: list = [], agent_instructions: str = AGENT_INSTRUCTIONS, ai_model: GoogleModel|OpenAIChatModel = create_google_model()):
        """Create and return an error analysis agent.
        Args:
            agent_instructions (str): Instructions for the agent.
            ai_model (GoogleModel|OpenAIChatModel): The model to be used by the agent.
        """
        return self.create_agent(agent_instructions=agent_instructions, ai_model=ai_model, output=ErrorModel, toolsets=toolsets)
    





