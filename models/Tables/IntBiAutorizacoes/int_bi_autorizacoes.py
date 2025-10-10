import datetime
from typing import Optional

from sqlalchemy import VARCHAR, TIMESTAMP, FLOAT, INTEGER
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass

class IntBiAutorizacoes(Base):
    """
    Modelo para a tabela que armazena dados de autorizacoes para o BI.
    """
    __tablename__ = "int_bi_autorizacoes"

    venda: Mapped[float] = mapped_column(FLOAT, primary_key=True) 

    empresa: Mapped[float] = mapped_column(FLOAT, primary_key=True)
    
    tentativas: Mapped[int] = mapped_column(INTEGER)
    
    guid_web: Mapped[str] = mapped_column(VARCHAR(255))
    
    data_hora_tentativa: Mapped[datetime.datetime] = mapped_column(TIMESTAMP)
    
    data_hora_inclusao: Mapped[datetime.datetime] = mapped_column(TIMESTAMP)
    
    erro: Mapped[Optional[str]] = mapped_column(VARCHAR, nullable=True)

class CaixaAutorizacoes(Base):
    """
    Modelo para a tabela que armazena dados de caixa_autorizacoes.
    """
    __tablename__ = "caixa_autorizacoes"

    venda_origem: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    
    empresa_origem: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    
    status: Mapped[int] = mapped_column(INTEGER)
    
    cupom: Mapped[int] = mapped_column(INTEGER)
    
    documento: Mapped[str] = mapped_column(VARCHAR(255))
    
    data_hora: Mapped[datetime.datetime] = mapped_column(TIMESTAMP)
    
    tipo: Mapped[int] = mapped_column(INTEGER)
    
    valor: Mapped[float] = mapped_column(FLOAT)
    
    valor_liberado: Mapped[float] = mapped_column(FLOAT)
    
    operador: Mapped[int] = mapped_column(INTEGER)
    
    fin_cod_motivo: Mapped[int] = mapped_column(INTEGER)
    
    descricao: Mapped[str] = mapped_column(VARCHAR(255))
    
    id_caixa_origem: Mapped[str] = mapped_column(VARCHAR(255))
    
    nr_caixa_origem: Mapped[int] = mapped_column(INTEGER)
    
    id_caixa_destino: Mapped[str] = mapped_column(VARCHAR(255))
    
    nr_caixa_destino: Mapped[int] = mapped_column(INTEGER)
    
    venda_destino: Mapped[int] = mapped_column(INTEGER)
    
    empresa_destino: Mapped[int] = mapped_column(INTEGER)
    
    estacao: Mapped[int] = mapped_column(INTEGER)
    
    autorizacao: Mapped[int] = mapped_column(INTEGER)
    
    observacao: Mapped[str] = mapped_column(VARCHAR(255))
    
    pessoa: Mapped[int] = mapped_column(INTEGER)
    
    data_vencimento: Mapped[datetime.datetime] = mapped_column(TIMESTAMP)
    
    id_financasweb: Mapped[float] = mapped_column(FLOAT)
    
    valor_em: Mapped[str] = mapped_column(VARCHAR(255))