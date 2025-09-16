from pydantic_ai import Agent
from pydantic_ai.models.google import GoogleModel
from pydantic_ai.providers.google import GoogleProvider
from google.genai import Client
from models.ErrorModel.ErrorModel import ErrorModel, ErrorListModel
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.openai import OpenAIProvider
from os import getenv
from models.DbModel.QueryReturnModel import QueryReturnModel


AGENT_INSTRUCTIONS = """
// 1. DIRETIVA DE PERSONA E OBJETIVO CORE

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

Esse um dos exemplos que tu voce vai encotrar. Note que o erro pode variar muito, e a stack trace pode ser longa. Sua tarefa é analisar esses erros e fornecer insights úteis.   

// 4. INSTRUÇÕES DE ANÁLISE E PROCESSAMENTO

Execute as seguintes etapas para cada grupo de erro identificado:

Clusterização Semântica de Erros: Primeiro, agrupe os erros por loja, tabela e pela assinatura semântica do erro. A "assinatura" é a mensagem de erro normalizada (sem dados variáveis como IDs, SKUs, etc.), que você deve extrair.

Análise de Causa Raiz (RCA): Para cada cluster, formule uma hipótese sobre a causa raiz provável. Categorize-a em uma das seguintes classes:

DATA_INPUT_ERROR: Problema com os dados enviados por um sistema de origem.

BUSINESS_LOGIC_ERROR: Falha na lógica de negócio do microserviço.

DEPENDENCY_FAILURE: Falha ao se comunicar com outro serviço, API ou banco de dados.

DATA_INTEGRITY_ERROR: O dado solicitado não existe ou está em um estado inconsistente na base de dados.

UNKNOWN: Se a causa não for clara.
Forneça uma breve justificativa para sua hipótese.

Avaliação de Impacto e Severidade: Com base na natureza do erro e na tabela/endpoint afetado (ex: processa_pedido é mais crítico que atualiza_metadado), atribua um nível de severidade ao cluster: CRITICAL, HIGH, MEDIUM, ou LOW. Justifique sua avaliação.

Recomendação de Ação Imediata: Para cada cluster, sugira a próxima ação mais lógica para a equipe de engenharia. Seja específico. Por exemplo: "Verificar o serviço de catálogo para garantir que os SKUs são replicados corretamente" é melhor do que "Verificar o erro".

`"""

class ErrorAnalysisService:
    def __init__(self, agent: Agent):
        self.agent = agent if agent else AgentFactory().create_error_analysis_agent()

    def group_errors_by_store(self, errors: list[QueryReturnModel]) -> ErrorModel:
        """
        Group errors by store code.

        Args:
            errors (list[ErrorModel]): List of error models.

        Returns:
            dict[int, list[ErrorModel]]: Dictionary with store code as key and list of errors as value.
        """
        grouped_errors = {}

        for error in errors:
            
            store_code = error.code
            if store_code not in grouped_errors:
                grouped_errors[store_code] = []
                grouped_errors[store_code].append(error)

        return ErrorListModel(errors=grouped_errors)

    def analyze_errors(self, raw_messages: QueryReturnModel) -> ErrorListModel:
        """
        Analyze raw error messages and return structured error data.

        Args:
            raw_messages (QueryReturnModel): Raw error messages to be analyzed.

        """
        return self.agent.run_sync(raw_messages.model_dump_json())


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

    def create_google_model(self, provider: GoogleProvider = create_google_provider(), model: str = getenv("GOOGLE_MODEL")):
        """Create and return a GoogleModel.
        Args:
            provider (GoogleProvider): The GoogleProvider instance.
        """
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
    





