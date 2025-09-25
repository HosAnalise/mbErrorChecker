import datetime
from typing import Optional

from sqlalchemy import VARCHAR, TIMESTAMP, FLOAT, INTEGER,DATE,TIME
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class IntBiVendas(Base):
    """
    Modelo para a tabela que armazena dados de vendas para o BI.
    """
    __tablename__ = "int_bi_vendas"
    
    venda: Mapped[float] = mapped_column(FLOAT,primary_key=True)

    empresa: Mapped[float] = mapped_column(FLOAT,primary_key=True)

    tentativas: Mapped[Optional[int]] = mapped_column(INTEGER)

    guid_web: Mapped[Optional[str]] = mapped_column(VARCHAR(100))
    
    data_hora_tentativa: Mapped[Optional[datetime.datetime]] = mapped_column(TIMESTAMP)
    
    data_hora_inclusao: Mapped[Optional[datetime.datetime]] = mapped_column(TIMESTAMP)
    
    erro: Mapped[Optional[str]]  

   
    def __repr__(self) -> str:
        return f"<IntBiVendas( venda={self.venda}, empresa_id={self.empresa}, erro={self.erro})>"
    


class Caixa(Base):
    """
    Modelo para a tabela que armazena dados de caixa.
    """
    __tablename__ = "caixa"

    data: Mapped[Optional[datetime.datetime]] = mapped_column(DATE)
    
    cupom: Mapped[Optional[float]] = mapped_column(FLOAT)

    lancamen: Mapped[Optional[str]] = mapped_column(VARCHAR(2))

    forma_pg: Mapped[Optional[str]] = mapped_column(VARCHAR(30))

    ecf: Mapped[Optional[float]] = mapped_column(FLOAT)

    valor: Mapped[Optional[float]] = mapped_column(FLOAT)

    hora: Mapped[Optional[datetime.time]] = mapped_column(TIME)

    venda: Mapped[float] = mapped_column(FLOAT,primary_key=True)

    estacao: Mapped[Optional[float]] = mapped_column(FLOAT)

    op_caixa: Mapped[Optional[float]] = mapped_column(FLOAT)

    empresa: Mapped[float] = mapped_column(FLOAT,primary_key=True)

    teleentrega: Mapped[Optional[str]] = mapped_column(VARCHAR(3))

    dinheiro: Mapped[Optional[float]] = mapped_column(FLOAT)

    cheque: Mapped[Optional[float]] = mapped_column(FLOAT)

    cartao: Mapped[Optional[float]] = mapped_column(FLOAT)

    aprazo: Mapped[Optional[float]] = mapped_column(FLOAT)

    convenio: Mapped[Optional[float]] = mapped_column(FLOAT)

    outros: Mapped[Optional[float]] = mapped_column(FLOAT)

    tipovenda: Mapped[Optional[str]] = mapped_column(VARCHAR(5))

    nrcaixa: Mapped[Optional[float]] = mapped_column(FLOAT)

    valor_dev: Mapped[Optional[float]] = mapped_column(FLOAT)

    motivo_dev: Mapped[Optional[str]] = mapped_column(VARCHAR(500))

    desconto: Mapped[Optional[float]] = mapped_column(FLOAT)

    nssu: Mapped[Optional[float]] = mapped_column(FLOAT)

    operador: Mapped[Optional[float]] = mapped_column(FLOAT)

    cheque_pre: Mapped[Optional[float]] = mapped_column(FLOAT)

    cheque_retirado: Mapped[Optional[str]] = mapped_column(VARCHAR(3))

    pgto_credito: Mapped[Optional[float]] = mapped_column(FLOAT)

    fin_cod_motivo: Mapped[Optional[int]] = mapped_column(INTEGER)

    fin_sangria_validada: Mapped[Optional[str]] = mapped_column(VARCHAR(3))

    fin_sangria_descricao: Mapped[Optional[str]] = mapped_column(VARCHAR(500))

    fin_sangria_documento: Mapped[Optional[str]] = mapped_column(VARCHAR(30))

    flag_fin: Mapped[Optional[str]] = mapped_column(VARCHAR(3))

    ccf: Mapped[Optional[float]] = mapped_column(FLOAT)

    gnf: Mapped[Optional[float]] = mapped_column(FLOAT)

    grg: Mapped[Optional[float]] = mapped_column(FLOAT)

    cdc: Mapped[Optional[float]] = mapped_column(FLOAT)

    cancelado: Mapped[Optional[str]] = mapped_column(VARCHAR(7))

    pgto_fidelidade: Mapped[Optional[float]] = mapped_column(FLOAT,nullable=False)

    fin_id_movimentacao_sangria: Mapped[Optional[str]] = mapped_column(VARCHAR(40))

    fin_id_movimentacao: Mapped[Optional[str]] = mapped_column(VARCHAR(40))

    pbm: Mapped[Optional[str]] = mapped_column(VARCHAR(30))

    fin_venda_cancelada: Mapped[Optional[str]] = mapped_column(VARCHAR(3))

    flag: Mapped[Optional[float]] = mapped_column(FLOAT)

    merchcard_nsu: Mapped[Optional[float]] = mapped_column(FLOAT)

    hash_origem: Mapped[Optional[int]] = mapped_column(INTEGER)

    hash_atual: Mapped[Optional[int]] = mapped_column(INTEGER)

    ambiente_nfce: Mapped[Optional[int]] = mapped_column(INTEGER)

    chave_nfce: Mapped[Optional[int]] = mapped_column(INTEGER)

    seq_movimento_nfce: Mapped[Optional[float]] = mapped_column(FLOAT)

    serie_nfce: Mapped[Optional[int]] = mapped_column(INTEGER)

    nsu_giftcard: Mapped[Optional[float]] = mapped_column(FLOAT)

    nr_nota: Mapped[Optional[float]] = mapped_column(FLOAT)

    serie_nota: Mapped[Optional[str]] = mapped_column(VARCHAR(3))

    nome_comprador: Mapped[Optional[str]] = mapped_column(VARCHAR(50))

    cpf_comprador: Mapped[Optional[str]] = mapped_column(VARCHAR(20))

    soma_fidelidade: Mapped[Optional[float]] = mapped_column(FLOAT)

    id_clube_compras: Mapped[Optional[str]] = mapped_column(VARCHAR(50))

    id: Mapped[Optional[str]] = mapped_column(VARCHAR(40))

    troco_solidario: Mapped[Optional[float]] = mapped_column(FLOAT)

    venda_retorno: Mapped[Optional[str]] = mapped_column(VARCHAR(3))

    valor_pbm: Mapped[Optional[float]] = mapped_column(FLOAT)

    valor_deposito: Mapped[Optional[float]] = mapped_column(FLOAT)

    valor_boleto: Mapped[Optional[float]] = mapped_column(FLOAT)

    valor_transferencia: Mapped[Optional[float]] = mapped_column(FLOAT)

    valor_pecfebrafar: Mapped[Optional[float]] = mapped_column(FLOAT)

    modo_captacao: Mapped[Optional[str]] = mapped_column(VARCHAR(20))

    id_hosdigitalize: Mapped[Optional[str]] = mapped_column(VARCHAR(40))

    valor_boleto_parcelado: Mapped[Optional[float]] = mapped_column(FLOAT)

    cod_modo_captacao: Mapped[Optional[int]] = mapped_column(INTEGER)

    id_marka: Mapped[Optional[str]] = mapped_column(VARCHAR(40))

    enviado_iqva: Mapped[Optional[int]] = mapped_column(INTEGER)

    id_financasweb: Mapped[Optional[float]] = mapped_column(FLOAT)

    codigo_bling: Mapped[Optional[float]] = mapped_column(FLOAT)

    merito_pdvnfs_cod: Mapped[Optional[int]] = mapped_column(INTEGER)

    id_pdvnfs_merito: Mapped[Optional[str]] = mapped_column(VARCHAR(40))

    id_finoper_merito: Mapped[Optional[str]] = mapped_column(VARCHAR(40))

    id_fincc_merito: Mapped[Optional[str]] = mapped_column(VARCHAR(40))

    id_finfat_merito: Mapped[Optional[str]] = mapped_column(VARCHAR(40))

    tipo_tef_merito: Mapped[Optional[str]] = mapped_column(VARCHAR(3))

    diferenca_troco: Mapped[Optional[float]] = mapped_column(FLOAT)

    fin_sangria_fornecedor: Mapped[Optional[float]] = mapped_column(FLOAT)

    fin_sangria_vencimento: Mapped[Optional[datetime.date]] = mapped_column(DATE)

    fin_sangria_conta: Mapped[Optional[float]] = mapped_column(FLOAT)

    fin_sangria_tipo_deposito: Mapped[Optional[str]] = mapped_column(VARCHAR(20))

    flag_integracao_merito: Mapped[Optional[int]] = mapped_column(INTEGER)

    id_fidelizasim: Mapped[Optional[str]] = mapped_column(VARCHAR(40))

    id_finfat_finconvenio_merito: Mapped[Optional[str]] = mapped_column(VARCHAR(40))

    id_finfat_crediarios_merito: Mapped[Optional[str]] = mapped_column(VARCHAR(40))

    operador_cancelamento: Mapped[Optional[int]] = mapped_column(INTEGER)

    flag_devolucao_sem_venda: Mapped[Optional[int]] = mapped_column(INTEGER)

    valor_cartao_presente: Mapped[Optional[float]] = mapped_column(FLOAT)
    
    id_bling: Mapped[Optional[int]] = mapped_column(VARCHAR(40))




   

   
    def __repr__(self) -> str:
        return f"<Vendas( venda={self.venda}, empresa_id={self.empresa}, erro={self.erro})>"