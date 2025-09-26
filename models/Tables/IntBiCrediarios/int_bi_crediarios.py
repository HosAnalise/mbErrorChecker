import datetime
from typing import Optional

from sqlalchemy import VARCHAR, TIMESTAMP, FLOAT, INTEGER,DATE,TIME
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class IntBiCrediarios(Base):
    """
    Modelo para a tabela que armazena dados de crediarios para o BI.
    """
    __tablename__ = "int_bi_crediarios"

    venda: Mapped[float] = mapped_column(FLOAT, primary_key=True)
    
    empresa: Mapped[float] = mapped_column(FLOAT, primary_key=True)
    
    parcela: Mapped[float] = mapped_column(FLOAT, primary_key=True)
    
    tentativas: Mapped[int] = mapped_column(INTEGER)
    
    guid_web: Mapped[str] = mapped_column(VARCHAR(255))
    
    data_hora_tentativa: Mapped[datetime.datetime] = mapped_column(TIMESTAMP)
    
    data_hora_inclusao: Mapped[datetime.datetime] = mapped_column(TIMESTAMP)
    
    erro: Mapped[Optional[str]] = mapped_column(VARCHAR, nullable=True)

class Crediarios(Base):
    """
    Modelo para a tabela que armazena dados de crediarios.
    """
    __tablename__ = "crediarios"

    venda_origem: Mapped[float] = mapped_column(FLOAT)
    
    empresa_origem: Mapped[float] = mapped_column(FLOAT)
    
    parcela: Mapped[float] = mapped_column(FLOAT)
    
    venda: Mapped[float] = mapped_column(FLOAT)
    
    empresa: Mapped[float] = mapped_column(FLOAT)
    
    cliente: Mapped[float] = mapped_column(FLOAT)
    
    debito: Mapped[float] = mapped_column(FLOAT)
    
    credito: Mapped[float] = mapped_column(FLOAT)
    
    motivo: Mapped[str] = mapped_column(VARCHAR(255))
    
    conferido: Mapped[int] = mapped_column(INTEGER)
    
    data_hora: Mapped[datetime.datetime] = mapped_column(TIMESTAMP)
    
    vencimento: Mapped[datetime.date] = mapped_column(DATE)
    
    fechamento: Mapped[datetime.date] = mapped_column(DATE)
    
    comprador: Mapped[int] = mapped_column(INTEGER)
    
    operador: Mapped[float] = mapped_column(FLOAT)
    
    cupom: Mapped[float] = mapped_column(FLOAT)
    
    ecf: Mapped[float] = mapped_column(FLOAT)
    
    venda_estorno: Mapped[float] = mapped_column(FLOAT)
    
    taxa_renegociacao: Mapped[float] = mapped_column(FLOAT)
    
    desconto_renegociacao: Mapped[float] = mapped_column(FLOAT)
    
    contrato_renegociacao: Mapped[float] = mapped_column(FLOAT)
    
    empresa_renegociacao: Mapped[float] = mapped_column(FLOAT)
    
    cond_pagamento: Mapped[int] = mapped_column(INTEGER)
    
    fin_id_movimentacao: Mapped[str] = mapped_column(VARCHAR(255))
    
    id_boleto: Mapped[str] = mapped_column(VARCHAR(255))
    
    id: Mapped[str] = mapped_column(VARCHAR(255), primary_key=True)
    
    pre_pagamento: Mapped[str] = mapped_column(VARCHAR(255))
    
    id_web: Mapped[int] = mapped_column(INTEGER)
    
    id_merito: Mapped[str] = mapped_column(VARCHAR(255))
    
    id_finfat_merito: Mapped[str] = mapped_column(VARCHAR(255))
    
    id_grupo: Mapped[int] = mapped_column(INTEGER)
    
    data_alteracao: Mapped[datetime.datetime] = mapped_column(TIMESTAMP)
    
    dt_alt: Mapped[datetime.datetime] = mapped_column(TIMESTAMP)
    
    dt_cancel: Mapped[datetime.date] = mapped_column(DATE)
    
    deletar: Mapped[int] = mapped_column(INTEGER)
    
    judicial: Mapped[int] = mapped_column(INTEGER)