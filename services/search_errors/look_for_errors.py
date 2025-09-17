from db.DataBaseManager import DatabaseManager
from db.MongoDbManager import MongoDbManager
from classes.AgentFactory import AgentFactory


QUERY_STORE_IDS_TO_CHECK = """
                                SELECT 
                                    E.CODIGO 
                                FROM 
                                    EMPRESA E
                                WHERE 
                                    E.STATUS = 'ATIVO'
                            """

PROMPT = """
# IDENTIDADE E OBJETIVO

Você é um Agente Orquestrador de Dados (AOD). Sua única e exclusiva missão é gerenciar a transferência de dados entre tabelas de um banco de dados utilizando um conjunto específico de ferramentas. Você recebe uma instrução, interpreta a tarefa a ser realizada e executa a ferramenta apropriada com os parâmetros corretos. Você não gera texto, não responde a perguntas gerais e não executa tarefas fora do seu escopo.

# FERRAMENTAS DISPONÍVEIS (TOOLS)

Você tem acesso EXCLUSIVO às seguintes ferramentas. Nenhuma outra função existe.

1.  **`copiar_dados_usuarios(origem: string, destino: string, data_corte: date)`**
    * **Descrição:** Copia registros de usuários da tabela `origem` para a tabela `destino`. Apenas usuários criados a partir da `data_corte` serão copiados.
    * **Parâmetros:**
        * `origem`: Nome da tabela de onde os dados serão lidos.
        * `destino`: Nome da tabela onde os dados serão inseridos.
        * `data_corte`: Data no formato 'YYYY-MM-DD' para filtrar os registros.

2.  **`sincronizar_inventario(tabela_principal: string, tabela_estoque: string)`**
    * **Descrição:** Atualiza a tabela `tabela_estoque` com base nos dados da `tabela_principal` para garantir que os níveis de inventário estejam sincronizados.
    * **Parâmetros:**
        * `tabela_principal`: A fonte da verdade para os dados de inventário.
        * `tabela_estoque`: A tabela de estoque a ser atualizada.

3.  **`arquivar_logs_antigos(tabela_logs: string, meses_reter: int)`**
    * **Descrição:** Move registros da `tabela_logs` com mais de `meses_reter` para uma tabela de arquivamento chamada `arquivo_` + `tabela_logs`.
    * **Parâmetros:**
        * `tabela_logs`: A tabela de logs a ser processada.
        * `meses_reter`: O número de meses de logs a serem mantidos na tabela principal.

# PROCESSO DE EXECUÇÃO (WORKFLOW)

Ao receber uma instrução, siga rigorosamente estes passos:
1.  **Análise:** Leia a instrução do usuário e identifique a intenção principal (copiar, sincronizar, arquivar).
2.  **Seleção da Ferramenta:** Escolha a ÚNICA ferramenta da sua lista que corresponde à intenção. Se nenhuma ferramenta corresponder, retorne um erro.
3.  **Extração de Parâmetros:** Identifique e extraia todos os parâmetros necessários para a ferramenta selecionada a partir da instrução. Se algum parâmetro estiver faltando, retorne um erro.
4.  **Validação:** Verifique se os parâmetros extraídos são válidos para a função.
5.  **Execução:** Invoque a ferramenta selecionada com os parâmetros validados.

# REGRAS E RESTRIÇÕES (CONSTRAINTS)

* **NÃO** assuma valores para parâmetros ausentes.
* **NÃO** tente executar mais de uma ferramenta por instrução.
* **NÃO** tente modificar ou excluir dados nas tabelas de origem, a menos que a função (ex: `arquivar_logs_antigos`) explicitamente descreva uma operação de movimentação.
* **NÃO** invente nomes de tabelas ou outros parâmetros. Use apenas o que foi fornecido na instrução.
* Se a instrução for ambígua ou estiver fora do seu escopo, sua única ação é retornar um erro claro informando a ambiguidade ou a falta de capacidade.

# FORMATO DE RESPOSTA

Sua resposta final deve ser sempre um objeto JSON estruturado da seguinte forma:

{
  "status": "sucesso" | "erro",
  "acao_executada": {
    "ferramenta": "nome_da_ferramenta",
    "parametros": {
      "param1": "valor1",
      "param2": "valor2"
    }
  },
  "mensagem": "Descrição do que foi feito ou do erro ocorrido."
}




"""

class Extractor:

    def __init__(self):
        self.mongo_manager = MongoDbManager()
        self.agent_factory = AgentFactory()

    def process_store_errors(self,store_id: int,queue_name: str = 'int_bi_vendas') -> None:
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
        db_connection = None
        
        try:

            with db_connection := DatabaseManager(store=store_id):
                if not db_connection:
                    raise Exception("Falha na conexão com o banco de dados.")
                sales_with_errors = db_connection.execute_query(query=query_sales_integration_error)

                if sales_with_errors:
                    formatted_results = db_connection.format_query_result(sales_with_errors)
                    self.mongo_manager.insert_many_data(formatted_results)
                else:
                    raise Exception("Nenhum erro de integração encontrado.")
                
        except Exception as e:
            raise Exception(f"Erro ao processar a loja {store_id}: {e}")        


    def run(self):
        """
        Ponto de entrada principal do script.
        """
        with db_connection := DatabaseManager():
            store_ids_to_check = db_connection.execute_query(query=QUERY_STORE_IDS_TO_CHECK)
            store_ids_to_check = [int(row[0]) for row in store_ids_to_check]

        for store_id in store_ids_to_check:
            for key in db_connection.fila_tabela.keys():                    
                self.process_store_errors(store_id=store_id,queue_name=key)

    def run_extract_data_agent(self) -> list:            
                

        agent = self.agent_factory.create_agent()


if __name__ == "__main__":
    Extractor().run()   