import datetime
from typing import Optional

from sqlalchemy import VARCHAR, TIMESTAMP, FLOAT, INTEGER,DATE,TIME
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class IntBiContasPagar(Base):
    """
    Modelo para a tabela que armazena dados de contas a pagar para o BI.
    """
    __tablename__ = "int_bi_contas_pagar"

    codigo: Mapped[float] = mapped_column(FLOAT, primary_keu = True)
    
    cod_empresa: Mapped[float] = mapped_column(FLOAT, primary_key = True)
    
    parcela: Mapped[float] = mapped_column(FLOAT, primary_key = True)
    
    excluir: Mapped[int] = mapped_column(INTEGER)
    
    tentativas: Mapped[int] = mapped_column(INTEGER)
    
    guid_web: Mapped[str] = mapped_column(VARCHAR(255))
    
    data_hora_tentativa: Mapped[Optional[datetime.datetime]] = mapped_column(TIMESTAMP)
    
    data_hora_inclusao: Mapped[Optional[datetime.datetime]] = mapped_column(TIMESTAMP)
    
    erro: Mapped[Optional[str]] = mapped_column(VARCHAR(1000))

class FinContasPagar(Base):
    """
    Modelo para a tabela que armazena dados de fin contas a pagar.
    """
    __tablename__ = "fin_contas_pagar"

    codigo: Mapped[float] = mapped_column(FLOAT, primary_key=True)
    
    descricao: Mapped[Optional[str]] = mapped_column(VARCHAR(255))
    
    cod_cedente: Mapped[Optional[float]] = mapped_column(FLOAT)
    
    cod_sgp: Mapped[Optional[float]] = mapped_column(FLOAT)
    
    cod_bco_origem: Mapped[Optional[float]] = mapped_column(FLOAT)
    
    cod_frm_pgto: Mapped[Optional[float]] = mapped_column(FLOAT)
    
    cod_empresa: Mapped[Optional[float]] = mapped_column(FLOAT, primary_key=True)
    
    data_emissao: Mapped[Optional[datetime.date]] = mapped_column(DATE)
    
    data_vcto: Mapped[Optional[datetime.date]] = mapped_column(DATE)
    
    parcela: Mapped[Optional[float]] = mapped_column(FLOAT, primary_key=True)
    
    desconto_porcentagem: Mapped[Optional[float]] = mapped_column(FLOAT)
    
    valor: Mapped[Optional[float]] = mapped_column(FLOAT)
    
    total_pago_bruto: Mapped[Optional[float]] = mapped_column(FLOAT)
    
    total_pago_pend_bruto: Mapped[Optional[float]] = mapped_column(FLOAT)
    
    total_pago_liquido: Mapped[Optional[float]] = mapped_column(FLOAT)
    
    conferido: Mapped[Optional[str]] = mapped_column(VARCHAR(50))
    
    obs: Mapped[Optional[str]] = mapped_column(VARCHAR(255))
    
    cod_cc: Mapped[Optional[float]] = mapped_column(FLOAT)
    
    num_documento: Mapped[Optional[str]] = mapped_column(VARCHAR(100))
    
    cod_motivo_cancelado: Mapped[Optional[float]] = mapped_column(FLOAT)
    
    desc_motivo_cancelado: Mapped[Optional[str]] = mapped_column(VARCHAR(255))
    
    data_cancelado: Mapped[Optional[datetime.date]] = mapped_column(DATE)
    
    data_atual_cancelado: Mapped[Optional[datetime.date]] = mapped_column(DATE)
    
    hora_atual_cancelado: Mapped[Optional[datetime.time]] = mapped_column(TIME)
    
    total_pago_pend_liquido: Mapped[Optional[float]] = mapped_column(FLOAT)
    
    data_conferido: Mapped[Optional[datetime.date]] = mapped_column(DATE)
    
    pgto_confirmado: Mapped[Optional[str]] = mapped_column(VARCHAR(50))
    
    data_competencia: Mapped[Optional[datetime.date]] = mapped_column(DATE)
    
    boleto_manual: Mapped[Optional[str]] = mapped_column(VARCHAR(10))
    
    desp_boleto_porcentagem: Mapped[Optional[float]] = mapped_column(FLOAT)
    
    tipo_nota: Mapped[Optional[str]] = mapped_column(VARCHAR(50))
    
    cod_bordero: Mapped[Optional[float]] = mapped_column(FLOAT)
    
    cod_empresa_bordero: Mapped[Optional[int]] = mapped_column(INTEGER)
    
    gnre_mes_ano_ref: Mapped[Optional[str]] = mapped_column(VARCHAR(20))
    
    gnre_numero_convenio: Mapped[Optional[float]] = mapped_column(FLOAT)
    
    gnre_num_nota: Mapped[Optional[float]] = mapped_column(FLOAT)
    
    gnre_data_entrada: Mapped[Optional[datetime.date]] = mapped_column(DATE)
    
    num_parcelas: Mapped[Optional[int]] = mapped_column(INTEGER)
    
    cods_lojas: Mapped[Optional[str]] = mapped_column(VARCHAR(255))
    
    porcentagem_lojas: Mapped[Optional[str]] = mapped_column(VARCHAR(255))
    
    data_hora_registro: Mapped[Optional[datetime.datetime]] = mapped_column(TIMESTAMP)
    
    cod_renegociacao: Mapped[Optional[float]] = mapped_column(FLOAT)
    
    cod_emp_renegociacao: Mapped[Optional[float]] = mapped_column(FLOAT)
    
    data_renegociacao: Mapped[Optional[datetime.date]] = mapped_column(DATE)
    
    acrescimo: Mapped[Optional[float]] = mapped_column(FLOAT)
    
    renegociacao: Mapped[Optional[str]] = mapped_column(VARCHAR(50))
    
    total_previsto: Mapped[Optional[float]] = mapped_column(FLOAT)
    
    parc_nparc: Mapped[Optional[str]] = mapped_column(VARCHAR(50))
    
    desconto_valor: Mapped[Optional[float]] = mapped_column(FLOAT)
    
    desp_boleto_valor: Mapped[Optional[float]] = mapped_column(FLOAT)
    
    total: Mapped[Optional[float]] = mapped_column(FLOAT)
    
    valor_total_aberto: Mapped[Optional[float]] = mapped_column(FLOAT)
    
    status: Mapped[Optional[str]] = mapped_column(VARCHAR(50))
    
    pago: Mapped[Optional[str]] = mapped_column(VARCHAR(50))
    
    id_financasweb: Mapped[Optional[int]] = mapped_column(INTEGER)
    
    cod_barras: Mapped[Optional[str]] = mapped_column(VARCHAR(255))