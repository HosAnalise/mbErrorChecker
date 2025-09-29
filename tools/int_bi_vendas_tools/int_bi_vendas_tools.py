from models.Tables.IntBiVendas.int_bi_vendas_relations import IntBiVendas,Caixa
from models.Tables.IntBiVendas.web_tables_vendas import Venda,VendaRecebimento
from sqlalchemy import update,delete,select
import logging
from sqlalchemy.orm import Session


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class IntBiVendasTools:

    def __init__(self, session_local:Session=None, session_cloud:Session=None):
        self.session_local = session_local
        self.session_cloud = session_cloud

    def update_caixa(self, venda: float) -> None:
        """Atualiza Caixa por ID da venda, acionando a trigger do BI.

        Transação com rollback em caso de erro.
        Hash: INTBI-CAIXA-UPDATE-001

        Args:
            venda (float): ID da venda para atualização.
        """
        stmt = (
                update(Caixa).
                where(Caixa.venda == venda).
                values(data= Caixa.data)
                )

        self.session_local.execute(stmt)
    

    def update_int_bi_vendas(self, venda: float) -> None:
        """Atualiza IntBiVendas por ID da venda, acionando a trigger do BI.

        Transação com rollback em caso de erro.
        Hash: INTBI-INTBIVENDAS-UPDATE-001

        Args:
            venda (float): ID da venda para atualização.
        """
        stmt = (
                update(IntBiVendas).
                where(IntBiVendas.venda == venda).
                values(venda= IntBiVendas.venda)
                )

        response = self.session_local.execute(stmt)
        return response.rowcount

    def delete_int_bi_vendas(self, venda: float) -> None:
        """Deleta registro de IntBiVendas por ID da venda.

        Transação com rollback em caso de erro.

        Hash: INTBI-INTBIVENDAS-DELETE-001

        Args:
            venda (float): ID da venda para deleção.
        """
        stmt = (
                delete(IntBiVendas).
                where(IntBiVendas.venda == venda)
                )
        result = self.session_local.execute(stmt)
        return result.rowcount
       


    def delete_int_bi_vendas(self, venda_id: float) -> int:
        """Deleta registros de IntBiVendas pelo ID da venda.

        Esta operação é executada dentro de uma transação existente
        e não realiza commit ou rollback.

        Hash: INTBI-INTBIVENDAS-DELETE-001

        Args:
            venda_id (float): ID da venda para deleção.

        Returns:
            int: O número de registros deletados.
        """
        stmt = (
                delete(IntBiVendas).
                where(IntBiVendas.venda == venda_id)
                )
        
        result = self.session_local.execute(stmt)
        return result.rowcount      

   

    def check_for_sales(self) -> list[tuple[int,int]]:
        """Verifica se o registro de IntBiVendas foi recebido no banco de dados cloud.

        HASH: INTBI-SALES-001

        Returns:
            bool: True se o registro foi recebido, False caso contrário.
        """
        stmt_local = (
                            select(Caixa.id_financasweb,Caixa.venda).
                            where(
                                Caixa.id_financasweb is not None,
                                Caixa.lancamen != 'TV'
                                ) 
                    )
        
        return self.session_local.execute(stmt_local).all()
    

    def check_for_sale(self,venda:int) -> list[tuple[int,int]]:
        """Verifica se o registro de IntBiVendas foi recebido no banco de dados cloud.

        HASH: INTBI-SALES-001

        Returns:
            list[tuple[int,int]]: Se o registro foi recebido, None
              caso contrário.
        """
        stmt_local = (
                        select(Caixa.id_financasweb,Caixa.venda).
                        where(
                            Caixa.id_financasweb is not None , 
                            Caixa.lancamen != 'TV' , 
                            Caixa.venda == venda
                            )
                    )
        
        return self.session_local.execute(stmt_local).first()
     

    def check_for_sales_exist_in_cloud(self, id_financasweb: int) -> int|None:
        """Verifica se o registro de IntBiVendas foi recebido no banco de dados cloud.

        HASH: INTBI-SALES-001

        Args:
            id_financasweb (float): ID da venda para verificação.

        Returns:
            int|None: retorna o VENDA_ID se o registro foi recebido, None caso contrário.
        """

        float_to_int = int(id_financasweb)
        stmt_cloud = (
                        select(Venda.VENDA_ID).
                        where(Venda.VENDA_HOS_ID == float_to_int)
                    )
        
        result = self.session_cloud.execute(stmt_cloud).first()

        return result 
    

    def check_for_sales_receipt_in_cloud(self, venda_id: int) -> int|None:

        """Verifica se o registro de VendaRecebimento foi recebido no banco de dados cloud.

        HASH: INTBI-SALES-001

        Args:
            venda_id (int): ID da venda para verificação.

        Returns:
            int|None: O ID da venda se o registro foi recebido, None caso contrário.
        """

        stmt_cloud = (
                    select(VendaRecebimento.VENDA_ID).
                    where(VendaRecebimento.VENDA_ID == venda_id)
                    )
        
        result = self.session_cloud.execute(stmt_cloud).first()
        return result 

    






            





