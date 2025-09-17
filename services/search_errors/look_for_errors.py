import os
from logging import getLogger
from db.DataBaseManager import DatabaseManager

LOG_DIRECTORY = 'logs'



QUERY_SALES_INTEGRATION_ERRORS ="""
                                    SELECT 
                                        
                                  FROM 
                                      int_bi{queue_name} ibv 
                                  WHERE 
                                      ibv.erro IS NOT NULL
                              """

QUERY_STORE_IDS_TO_CHECK = """
                                SELECT 
                                    E.CODIGO 
                                FROM 
                                    EMPRESA E
                                WHERE 
                                    E.STATUS = 'ATIVO'
                            """

logger = getLogger(__name__)


def _save_results_to_file(store_id: int, results: list, directory: str):
    """
    Salva uma lista de resultados em um arquivo de log para uma loja específica.
    """
    if not results:
        return

    os.makedirs(directory, exist_ok=True)
    file_path = os.path.join(directory, f"erros_loja_{store_id}.log")
    
    logger.info(f"Salvando {len(results)} resultado(s) da loja {store_id} em {file_path}")
    
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(f"{row}\n" for row in results)
    except IOError as e:
        logger.error(f"Falha ao escrever no arquivo {file_path}: {e}")


def process_store_errors(store_id: int):
    """
    Conecta, consulta e salva erros de integração para UMA única loja.
    """
    logger.info(f"Verificando erros de integração para a loja: {store_id}")
    db_connection = None
    try:


        with DatabaseManager(store=store_id) as db_connection:
            if not db_connection:
                logger.error(f"Não foi possível conectar à loja {store_id}. Pulando...")
                return
            sales_with_errors = db_connection.execute_query(query=QUERY_SALES_INTEGRATION_ERRORS)

            if sales_with_errors:
                formatted_results = db_connection.format_query_result(sales_with_errors)
                _save_results_to_file(store_id=store_id, results=formatted_results, directory=LOG_DIRECTORY)
            else:
                logger.info(f"Nenhum erro encontrado para a loja {store_id}.")
            
    except Exception as e:
        logger.error(f"Erro ao processar a loja {store_id}: {e}")
  


def main():
    """
    Ponto de entrada principal do script.
    """
    with DatabaseManager() as db_connection:
        store_ids_to_check = db_connection.execute_query(query=QUERY_STORE_IDS_TO_CHECK)
        store_ids_to_check = [int(row[0]) for row in store_ids_to_check]

    for store_id in store_ids_to_check:
        process_store_errors(store_id=store_id)
    logger.info("Verificação de todas as lojas concluída.")


if __name__ == "__main__":
    main()