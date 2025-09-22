from db.DataBaseManager import DatabaseManager
from db.MongoDbManager import MongoDbManager
from classes.ErrorAnalysisService  import ErrorAnalysisService

erro_analyze = ErrorAnalysisService()
mongo_db_manager = MongoDbManager()

def update_registers():
        print("Iniciando atualização de registros...")


        errors_list = mongo_db_manager.get_data()
        if not errors_list:
            print("Nenhum erro encontrado.")
            return
        
        grouped_store = erro_analyze.group_errors_by_store(errors_list)
        if not grouped_store.errors:
            print("Nenhum grupo de erro foi formado.")
            return

        for error_group in grouped_store.errors:
            id_store = error_group.store
            print(f"\n--- Processando Loja: {id_store} ---")
                
            try:
                with DatabaseManager(store=id_store) as db_manager:
                    if not db_manager.connection:
                        print(f"Falha ao conectar na base de dados da loja {id_store}.")
                        continue

                    for single_error in error_group.error:
                        tabela_do_erro = single_error.table_name.lower()
                        query_foi_montada = False

                        for nome_tabela_fila, mapa_destino in db_manager.fila_tabela.items():
                            if tabela_do_erro == nome_tabela_fila.lower():
                                for nome_tabela_alvo, nome_coluna_chave in mapa_destino.items():
                                                
                                    query = f"""UPDATE {nome_tabela_alvo}
                                            SET DATA = DATA
                                            WHERE {nome_coluna_chave} = {single_error.code}"""

                                    print(f"[Loja {id_store}] Ação encontrada para o código {single_error.code}.")

                                    db_manager.execute_query(query)
                                    query_foi_montada = True
                                    print(query)
                                    break

                            if not query_foi_montada:
                                print(f"[Loja {id_store}] AVISO: A tabela '{single_error.table_name}' não tem uma ação de UPDATE mapeada.")

            except Exception as e:
                print(f"Ocorreu um erro inesperado ao processar a loja {id_store}: {e}")

        print("\nProcesso finalizado.")

if __name__ == "__main__":
    update_registers()