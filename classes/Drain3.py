from drain3 import TemplateMiner
from drain3.template_miner_config import TemplateMinerConfig
import logging
from models.FingerPrintModel.FingerPrintModel import FingerPrintModel
from models.DbModel.QueryReturnModel import QueryReturnModel   

import json
import logging
import os
import subprocess
import sys
import time
from os.path import dirname

logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='%(message)s')

class Drain3Miner:


    def __init__(self):
        self.drain_config_template = TemplateMinerConfig()
        
        self.drain_config_template.load(f"{dirname(__file__)}/drain3.ini")
        self.drain_config_template.profiling_enabled = True
        
        self.template_miner = TemplateMiner(config = self.drain_config_template)    




        def make_fingerprint(self, data: QueryReturnModel) -> list[dict]:
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
                for entry in data:               

                        sanitezed_content = self.sanitize_log(entry.erro)

                        regexed_content = self.regex_sanitize_pro(sanitezed_content)

                        replaced_content = regexed_content.replace('\r\n', '\n').replace('\\', '').replace('rn', ' ')

                        response = self.template_miner.add_log_message(replaced_content)

                        unique_responses[response.get('cluster_id')] = FingerPrintModel(**response)

                        table_name = entry.table_name if hasattr(entry, 'table_name') else 'N/A'
                        

                return list(unique_responses.values()), table_name if unique_responses else []

            except Exception as e:
                logging.error("Erro ao criar fingerprint: %s", e)
                return None