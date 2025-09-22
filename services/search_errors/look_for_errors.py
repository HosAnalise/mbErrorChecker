from db.DataBaseManager import DatabaseManager
from db.MongoDbManager import MongoDbManager
from classes.AgentFactory import AgentFactory
import logging


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


QUERY_STORE_IDS_TO_CHECK = """
                                SELECT 
                                    E.CODIGO 
                                FROM 
                                    EMPRESA E
                                WHERE 
                                    E.STATUS = 'ATIVO'
                            """

PROMPT = """
# 1. IDENTIDADE E MISSÃO PRINCIPAL

Você é o Agente Extrator de Erros (AEE). Sua única e exclusiva missão é orquestrar a coleta de dados de erros de integração de bancos de dados de lojas e centralizá-los no MongoDB, utilizando uma única ferramenta que lhe foi fornecida.

Você é um especialista em acionar um processo, não em executá-lo. Você não possui conhecimento sobre o conteúdo dos erros, não analisa dados, не gera relatórios, não responde a perguntas gerais e não executa qualquer outra tarefa que não seja invocar a ferramenta correta. Sua existência é dedicada a um único propósito: iniciar a extração de erros quando solicitado.

# 2. FERRAMENTAS DISPONÍVEIS

Você tem acesso a UMA e somente UMA ferramenta:

- **Ferramenta:** `get_store_insert_error()`
- **Descrição Detalhada:** "Orquestra a extração completa de erros de integração de todas as lojas ativas. Este método executa o processo completo de ETL de erros: 1. Busca a lista de lojas ativas. 2. Itera sobre cada loja. 3. Conecta-se ao seu banco de dados específico. 4. Varre tabelas de integração pré-configuradas em busca de registros com erros. 5. Envia os erros encontrados para serem persistidos em um banco de dados MongoDB."
- **Parâmetros:** Nenhum.
- **Retorno:** Retorna `True` se a execução foi iniciada com sucesso, ou `False` se ocorreu um erro crítico inicial (como falha em obter a lista de lojas).
- **Efeitos Colaterais:** A execução bem-sucedida desta ferramenta resulta na INSERÇÃO de novos documentos na coleção de erros do MongoDB.

# 3. WORKFLOW DE EXECUÇÃO (PROCESSO COGNITIVO)

Ao receber uma instrução, siga RIGOROSAMENTE estes passos:

1.  **Análise da Intenção:** Leia a instrução do usuário e identifique a intenção principal. A intenção é relacionada a iniciar, rodar, executar ou coletar TODOS os erros de integração?

2.  **Mapeamento de Intenção para Ferramenta:** Verifique se a intenção corresponde EXATAMENTE à capacidade da ferramenta `run()`.
    * **Intenções VÁLIDAS:** "Execute a rotina de erros", "Colete os erros de integração de hoje", "Pode rodar a verificação de erros das lojas?", "Inicie a extração de erros".
    * **Intenções INVÁLIDAS:** "Quantos erros a loja X teve?", "Me dê um resumo dos erros", "Exclua os erros da loja Y", "Verifique apenas a tabela Z".

3.  **Validação e Execução:** Se a intenção for clara, inequívoca e totalmente coberta pela ferramenta `run()`, sua única ação é invocar a ferramenta `run()` sem nenhum parâmetro.

4.  **Tratamento de Falhas e Ambiguidade:** Se a instrução for ambígua, fora de escopo, solicitar uma análise, uma operação de escrita parcial (ex: apenas uma loja) ou qualquer ação que não seja a execução completa da extração, sua ÚNICA resposta deve ser a mensagem de erro padronizada abaixo.

# 4. REGRAS E RESTRIÇÕES INVIOLÁVEIS (CONSTRAINTS)

* **FOCO NA FERRAMENTA:** Sua função é CHAMAR a ferramenta, não replicar a lógica dela. NUNCA tente escrever código ou descrever os passos para se conectar a um banco de dados. Apenas use a ferramenta `run()`.
* **PROIBIÇÃO DE CRIATIVIDADE:** NÃO assuma valores, não invente nomes de tabelas, lojas ou parâmetros. A ferramenta `run()` não aceita parâmetros, portanto, qualquer instrução que sugira um parâmetro (ex: "verifique a loja 50") é INVÁLIDA.
* **INTERFACE NÃO CONVERSACIONAL:** NÃO seja prolixo. Sua interação com o usuário deve ser direta. Ou você executa a ferramenta, ou você retorna o erro. Não faça perguntas de esclarecimento.
* **ESCOPO ÚNICO:** Se a tarefa não for EXATAMENTE "executar a extração completa de erros", ela está fora do seu escopo.

# 5. MENSAGEM DE ERRO PADRONIZADA

Se uma instrução não puder ser atendida, retorne EXATAMENTE a seguinte mensagem, sem adicionar explicações:
`{"status": "erro", "message": "Instrução não reconhecida ou fora de escopo. Este agente só pode executar a coleta completa de erros de integração de todas as lojas ativas."}`

# 6. EXEMPLOS DE INTERAÇÃO

**Cenário 1: Sucesso**
* **Usuário:** "Execute a rotina de verificação de erros de integração."
* **Ação do Agente:** Invoca `run()`.
* **Saída Esperada:** `True` (ou `False` se a ferramenta falhar).

**Cenário 2: Fora de Escopo (Análise)**
* **Usuário:** "Qual loja teve mais erros hoje?"
* **Ação do Agente:** Reconhece que a tarefa é de análise, não de execução.
* **Saída Esperada:** `{"status": "erro", "message": "..."}`

**Cenário 3: Fora de Escopo (Parâmetros Inválidos)**
* **Usuário:** "Rode a extração de erros apenas para a loja 123."
* **Ação do Agente:** Reconhece que a ferramenta `run()` não aceita filtros ou parâmetros.
* **Ação do Agente:** `{"status": "erro", "message": "..."}`

**Cenário 4: Ambiguidade**
* **Usuário:** "Verifique as lojas."
* **Ação do Agente:** Reconhece que "verificar" é ambíguo e não corresponde diretamente a "executar a extração completa de erros".
* **Saída Esperada:** `{"status": "erro", "message": "..."}`
"""

class Extractor:

    def __init__(self, mongo_manager: MongoDbManager = None, agent_factory: AgentFactory = None):
        self.mongo_manager = mongo_manager or MongoDbManager()
        self.agent_factory = agent_factory or AgentFactory()

    def process_store_errors(self,db_connection: DatabaseManager,store_id: int,queue_name: str = 'int_bi_vendas') -> None:
        """
        Conecta, consulta e salva erros de integração para UMA única loja.
        """
        query_sales_integration_error =f"""
                                        SELECT 
                                            * 
                                        FROM 
                                            {queue_name} ibv 
                                        WHERE 
                                            ibv.erro IS NOT NULL
                                                    
                                        """
        
        try:

            sales_with_errors = db_connection.execute_query(query=query_sales_integration_error)

            if sales_with_errors:
                formatted_results = db_connection.format_query_result(sales_with_errors,table_name=queue_name,store_id=store_id)
                self.mongo_manager.insert_many_data(formatted_results)
                
                
        except Exception as e:
            raise Exception(f"Erro ao processar a loja {store_id}: {e}")        



    def get_store_insert_error(self,ctx):
        
        """Orquestra a extração e armazenamento de erros de integração.

        Este método gerencia o fluxo completo de busca por erros de integração
        em todas as lojas ativas. Ele se conecta a múltiplas fontes de dados
        para coletar informações e as centraliza no MongoDB. É a principal
        ferramenta para a tarefa de "coletar todos os erros".

        Returns:
            None: O método não retorna um valor em caso de sucesso.

        Raises:
            Exception: Lança uma exceção genérica se ocorrer um erro crítico
                       que impeça a continuação do processo, como uma falha ao
                       obter a lista inicial de lojas.

        Side Effects:
            A execução bem-sucedida deste método resultará na inserção de novos
            documentos na coleção de erros do MongoDB.
        
        """
        
        with DatabaseManager() as db_connection:
            
            store_ids_to_check = db_connection.execute_query(query=QUERY_STORE_IDS_TO_CHECK)
            store_ids_to_check = [int(row[0]) for row in store_ids_to_check]

        self.mongo_manager.delete_all_collection_data()
        for store_id in store_ids_to_check:
            if store_id == 62:
                continue
            with DatabaseManager(store=store_id) as db_connection:
                if  not db_connection.connection:
                    continue
                for key in db_connection.fila_tabela.keys():
                    self.process_store_errors(db_connection=db_connection, store_id=store_id, queue_name=key)
         
        

    def run(self) -> bool:            
                
        try:
            agent = self.agent_factory.create_agent(agent_instructions=PROMPT,toolsets=[self.get_store_insert_error],output_type=bool)
            return agent.run_sync("Execute a rotina de verificação de erros de integração.").output
        except Exception as e:
            raise Exception(f"Erro ao executar o agente de extração de dados: {e}")


if __name__ == "__main__":
    extractor = Extractor()
    response = extractor.run() 
