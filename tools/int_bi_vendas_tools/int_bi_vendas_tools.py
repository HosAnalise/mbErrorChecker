from models.Tables.IntBiVendas.int_bi_vendas_relations import IntBiVendas,Caixa
from sqlalchemy import update



class IntBiVendasTools:

    def __init__(self, session_local, session_cloud=None):
        self.session_local = session_local
        self.session_cloud = session_cloud

    def update_caixa(self, venda: float) -> None:
        """Atualiza Caixa por ID da venda, acionando a trigger do BI.

        Transação com rollback em caso de erro.
        Hash: INTBI-CAIXA-UPDATE-001

        Args:
            venda (float): ID da venda para atualização.
        """
        try:
            stmt = (
                    update(Caixa).
                    where(Caixa.venda == venda).
                    values(data= Caixa.data)
                    )

            self.session.execute(stmt)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            print(f"Erro ao atualizar Caixa: {e}")



            





