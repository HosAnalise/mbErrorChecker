import datetime
from typing import Optional

from sqlalchemy import VARCHAR, TIMESTAMP, FLOAT, INTEGER,DATE,TIME
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass

class IntBiCodCancelamento(Base):
    """
    Modelo para a tabela que armazena dados de cod_cancelamento para o BI.
    """
    __tablename__ = "int_bi_cod_cancelamento"

    venda: Mapped[float] = mapped_column(FLOAT, primary_key=True)
    
    empresa: Mapped[float] = mapped_column(FLOAT, primary_key=True)
    
    cliente: Mapped[float] = mapped_column(FLOAT)
    
    convenio: Mapped[float] = mapped_column(FLOAT)
    
    nr_pedido: Mapped[float] = mapped_column(FLOAT)
    
    data_hora: Mapped[datetime.datetime] = mapped_column(TIMESTAMP)
    
    tentativas: Mapped[int] = mapped_column(INTEGER)
    
    guid_web: Mapped[str] = mapped_column(VARCHAR(255))
    
    data_hora_tentativa: Mapped[datetime.datetime] = mapped_column(TIMESTAMP)
    
    data_hora_inclusao: Mapped[datetime.datetime] = mapped_column(TIMESTAMP)
    
    erro: Mapped[Optional[str]] = mapped_column(VARCHAR, nullable=True)

class Caixa(Base):
    """
    Modelo para a tabela que armazena dados de caixa.
    """
    __tablename__ = "caixa"

    data: Mapped[datetime.date] = mapped_column(DATE)
    
    cupom: Mapped[float] = mapped_column(FLOAT)
    
    lancamen: Mapped[str] = mapped_column(VARCHAR(255))
    
    forma_pg: Mapped[str] = mapped_column(VARCHAR(255))
    
    ecf: Mapped[float] = mapped_column(FLOAT)
    
    valor: Mapped[float] = mapped_column(FLOAT)
    
    hora: Mapped[datetime.time] = mapped_column(TIME)
    
    venda: Mapped[float] = mapped_column(FLOAT, primary_key=True)
    
    estacao: Mapped[float] = mapped_column(FLOAT)
    
    op_caixa: Mapped[float] = mapped_column(FLOAT)
    
    empresa: Mapped[float] = mapped_column(FLOAT, primary_key=True)
    
    teleentrega: Mapped[str] = mapped_column(VARCHAR(255))
    
    dinheiro: Mapped[float] = mapped_column(FLOAT)
    
    cheque: Mapped[float] = mapped_column(FLOAT)
    
    cartao: Mapped[float] = mapped_column(FLOAT)
    
    aprazo: Mapped[float] = mapped_column(FLOAT)
    
    convenio: Mapped[float] = mapped_column(FLOAT)
    
    outros: Mapped[float] = mapped_column(FLOAT)
    
    tipovenda: Mapped[str] = mapped_column(VARCHAR(255))
    
    nrcaixa: Mapped[float] = mapped_column(FLOAT)
    
    valor_dev: Mapped[float] = mapped_column(FLOAT)
    
    motivo: Mapped[str] = mapped_column(VARCHAR(255))
    
    desconto: Mapped[float] = mapped_column(FLOAT)
    
    nss: Mapped[float] = mapped_column(FLOAT)
    
    operador: Mapped[float] = mapped_column(FLOAT)
    
    cheque_pre: Mapped[float] = mapped_column(FLOAT)
    
    cheque_retirado: Mapped[str] = mapped_column(VARCHAR(255))
    
    pgto_credito: Mapped[float] = mapped_column(FLOAT)
    
    fin_cod_motivo: Mapped[int] = mapped_column(INTEGER)
    
    fin_sangria_validada: Mapped[str] = mapped_column(VARCHAR(255))
    
    fin_sangria_descricao: Mapped[str] = mapped_column(VARCHAR(255))
    
    fin_sangria_documento: Mapped[str] = mapped_column(VARCHAR(255))
    
    flag_fin: Mapped[str] = mapped_column(VARCHAR(255))
    
    ccf: Mapped[float] = mapped_column(FLOAT)
    
    gnf: Mapped[float] = mapped_column(FLOAT)
    
    grg: Mapped[float] = mapped_column(FLOAT)
    
    cdc: Mapped[float] = mapped_column(FLOAT)
    
    cancelado: Mapped[str] = mapped_column(VARCHAR(255))
    
    pgto_fidelidade: Mapped[float] = mapped_column(FLOAT)
    
    fin_id_movimentacao_sangria: Mapped[str] = mapped_column(VARCHAR(255))
    
    fin_id_movimentacao: Mapped[str] = mapped_column(VARCHAR(255))
    
    pbm: Mapped[str] = mapped_column(VARCHAR(255))
    
    fin_venda_cancelada: Mapped[str] = mapped_column(VARCHAR(255))
    
    flag: Mapped[float] = mapped_column(FLOAT)
    
    merchcard_nsu: Mapped[float] = mapped_column(FLOAT)
    
    hash_origem: Mapped[int] = mapped_column(INTEGER)
    
    hash_atual: Mapped[int] = mapped_column(INTEGER)
    
    ambiente_nfce: Mapped[int] = mapped_column(INTEGER)
    
    chave_nfce: Mapped[str] = mapped_column(VARCHAR(255))
    
    seq_movimento_nfce: Mapped[float] = mapped_column(FLOAT)
    
    serie_nfce: Mapped[int] = mapped_column(INTEGER)
    
    nsu_giftcard: Mapped[float] = mapped_column(FLOAT)
    
    nr_nota: Mapped[float] = mapped_column(FLOAT)
    
    serie_nota: Mapped[str] = mapped_column(VARCHAR(255))
    
    nome_comprador: Mapped[str] = mapped_column(VARCHAR(255))
    
    cpf_comprador: Mapped[str] = mapped_column(VARCHAR(255))
    
    soma_fidelidade: Mapped[float] = mapped_column(FLOAT)
    
    id_clube_compras: Mapped[str] = mapped_column(VARCHAR(255))
    
    id: Mapped[str] = mapped_column(VARCHAR(255), primary_key=True)
    
    troco_solidario: Mapped[float] = mapped_column(FLOAT)
    
    venda_retorno: Mapped[float] = mapped_column(FLOAT)
    
    valor_pbm: Mapped[float] = mapped_column(FLOAT)
    
    valor_deposito: Mapped[float] = mapped_column(FLOAT)
    
    valor_boleto: Mapped[float] = mapped_column(FLOAT)
    
    valor_transferencia: Mapped[float] = mapped_column(FLOAT)
    
    valor_pecfebrafar: Mapped[float] = mapped_column(FLOAT)
    
    modo_captacao: Mapped[str] = mapped_column(VARCHAR(255))
    
    id_hosdigitalize: Mapped[str] = mapped_column(VARCHAR(255))
    
    valor_boleto_parcelado: Mapped[float] = mapped_column(FLOAT)
    
    cod_modo_captacao: Mapped[int] = mapped_column(INTEGER)
    
    id_marka: Mapped[str] = mapped_column(VARCHAR(255))
    
    enviado_iqvia: Mapped[int] = mapped_column(INTEGER)
    
    id_financasweb: Mapped[float] = mapped_column(FLOAT)
    
    codigo_bling: Mapped[float] = mapped_column(FLOAT)
    
    merito_pdvnfs_cod: Mapped[int] = mapped_column(INTEGER)
    
    id_pdvnfs_merito: Mapped[str] = mapped_column(VARCHAR(255))
    
    id_finoper_merito: Mapped[str] = mapped_column(VARCHAR(255))
    
    id_fincc_merito: Mapped[str] = mapped_column(VARCHAR(255))
    
    id_finfat_merito: Mapped[str] = mapped_column(VARCHAR(255))
    
    tipo_tef_merito: Mapped[str] = mapped_column(VARCHAR(255))
    
    diferenca_troco: Mapped[float] = mapped_column(FLOAT)
    
    fin_sangria_fornecedor: Mapped[float] = mapped_column(FLOAT)
    
    fin_sangria_vencimento: Mapped[datetime.date] = mapped_column(DATE)
    
    fin_sangria_conta: Mapped[float] = mapped_column(FLOAT)
    
    fin_sangria_tipo_deposito: Mapped[str] = mapped_column(VARCHAR(255))
    
    id_fidelizasim: Mapped[str] = mapped_column(VARCHAR(255))
    
    operador_cancelamento: Mapped[int] = mapped_column(INTEGER)
    
    id_finfat_finconvenio_merito: Mapped[str] = mapped_column(VARCHAR(255))
    
    id_finfat_crediarios_merito: Mapped[str] = mapped_column(VARCHAR(255))
    
    flag_devolucao_sem_venda: Mapped[int] = mapped_column(INTEGER)
    
    data_alteracao: Mapped[datetime.datetime] = mapped_column(TIMESTAMP)
    
    valor_cartao_presente: Mapped[float] = mapped_column(FLOAT)
    
    id_bling: Mapped[int] = mapped_column(INTEGER)