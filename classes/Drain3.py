from drain3 import TemplateMiner
from drain3.template_miner_config import TemplateMinerConfig
import logging
import sys
from os.path import dirname, abspath, join
from models.FingerPrintModel.FingerPrintModel import FingerPrintModel
from models.DbModel.QueryReturnModel import QueryReturnModel
from drain3.persistence_handler import FilePersistence
from classes.TextFormatter import TextFormatter



logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='%(message)s')


class Drain3Miner:

    def __init__(self,text_formatter: TextFormatter = None):
        self.drain_config_template = TemplateMinerConfig()
        self.project_root = dirname(dirname(abspath(__file__)))
        self.drain_config_template.load(join(self.project_root, "drain3.ini"))
        self.drain_config_template.profiling_enabled = True
        self.persistence_handler = FilePersistence(file_path=join(self.project_root, "drain3_state.json"))
        self.template_miner = TemplateMiner(config=self.drain_config_template,persistence_handler=self.persistence_handler)
        self.text_formatter = text_formatter or TextFormatter()



    def make_fingerprint(self, data: list[QueryReturnModel]) -> tuple[list[FingerPrintModel], str]:
        """
        Normaliza e agrupa logs de erro para criar fingerprints únicos.

        Processa uma lista de registros de erro, sanitiza o conteúdo e usa o
        TemplateMiner para agrupar logs semelhantes. Garante que cada cluster
        (fingerprint) seja adicionado apenas uma vez.

        Args:
            data: Lista de registros retornados do banco contendo, por exemplo, a tabela e a mensagem de erro.

        Returns:
            Uma tupla contendo:
            - lista de FingerPrintModel com os clusters únicos
        """
        try:
            fingerprints: dict[str, FingerPrintModel] = {}

            for entry in data:

                search_result = self.text_formatter.regex_sanitize_search(entry.erro)
                sanitized_content = self.text_formatter.sanitize_log(entry.erro if search_result is None else search_result)
                replaced_content = self.text_formatter.clean_content(sanitized_content) 
                regexed_content = self.text_formatter.regex_sanitize_pro(replaced_content)

                


                response = self.template_miner.add_log_message(regexed_content)
                   

                cluster_id = response.get('cluster_id')

                if not cluster_id:
                    continue               
            
                if cluster_id in fingerprints.keys():

                    if entry.store not in fingerprints[cluster_id].store:
                        fingerprints[cluster_id].store.append(entry.store)
                        fingerprints[cluster_id].table_name = entry.table_name
                        fingerprints[cluster_id].template_mined = response.get('template_mined', fingerprints[cluster_id].template_mined)

                else:
                    fingerprints[cluster_id] = FingerPrintModel(
                        **response, 
                        store=[entry.store],
                        table_name=entry.table_name
                    )




            


            return list(fingerprints.values())

        except Exception as exc:  
            logger.error("Erro ao criar fingerprint: %s", exc)
            return []