import datetime
from typing import Optional

from sqlalchemy import VARCHAR, TIMESTAMP, FLOAT, INTEGER,DATE,TIME
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class IntBiContCaixas(Base):
    """
    Modelo para a tabela que armazena dados de contas caixas para o BI.
    """
    __tablename__ = "int_bi_contcaixas"

    ncaixa: Mapped[float] = mapped_column(FLOAT, primary_key=True)
    
    empresa: Mapped[float] = mapped_column(FLOAT, primary_key = True)
    
    tentativas: Mapped[int] = mapped_column(INTEGER)
    
    guid_web: Mapped[str] = mapped_column(VARCHAR(255))
    
    data_hora_tentativa: Mapped[datetime.datetime] = mapped_column(TIMESTAMP)
    
    data_hora_inclusao: Mapped[datetime.datetime] = mapped_column(TIMESTAMP)
    
    erro: Mapped[Optional[str]] = mapped_column(VARCHAR, nullable=True)

class ControledeCaixa(Base):
    """
    Modelo para a tabela que armazena dados de controle de caixa.
    """
    __tablename__ = "controledecaixa"

    ncaixa: Mapped[float] = mapped_column(FLOAT, primary_key=True)
    
    horaini: Mapped[datetime.time] = mapped_column(TIME)
    
    dataini: Mapped[datetime.date] = mapped_column(DATE)
    
    operadorini: Mapped[float] = mapped_column(FLOAT)
    
    valorini: Mapped[float] = mapped_column(FLOAT)
    
    horafin: Mapped[datetime.time] = mapped_column(TIME)
    
    datafin: Mapped[datetime.date] = mapped_column(DATE)
    
    operadorfin: Mapped[float] = mapped_column(FLOAT)
    
    troco: Mapped[float] = mapped_column(FLOAT)
    
    valorfin: Mapped[float] = mapped_column(FLOAT)
    
    valreal: Mapped[float] = mapped_column(FLOAT)
    
    terminal: Mapped[float] = mapped_column(FLOAT)
    
    status: Mapped[float] = mapped_column(FLOAT)
    
    operadoratual: Mapped[float] = mapped_column(FLOAT)
    
    pedidos: Mapped[float] = mapped_column(FLOAT)
    
    empresa: Mapped[float] = mapped_column(FLOAT, primary_key = True)
    
    caixapendente: Mapped[Optional[str]] = mapped_column(VARCHAR(255), nullable=True)
    
    fin_flag: Mapped[Optional[str]] = mapped_column(VARCHAR(255), nullable=True)
    
    bloqueado: Mapped[Optional[str]] = mapped_column(VARCHAR(255), nullable=True)
    
    obs: Mapped[Optional[str]] = mapped_column(VARCHAR(255), nullable=True)
    
    observacao: Mapped[Optional[str]] = mapped_column(VARCHAR(255), nullable=True)
    
    id_movimentacao_abertura: Mapped[Optional[str]] = mapped_column(VARCHAR(255), nullable=True)
    
    id_movimentacao_fechamento: Mapped[Optional[str]] = mapped_column(VARCHAR(255), nullable=True)
    
    id: Mapped[Optional[str]] = mapped_column(VARCHAR(255), nullable=True)
    
    id_financasweb: Mapped[float] = mapped_column(FLOAT)
    
    fincaixa_sessao_id: Mapped[Optional[str]] = mapped_column(VARCHAR(255), nullable=True)
    
    fincaixa_sessaousu_id: Mapped[Optional[str]] = mapped_column(VARCHAR(255), nullable=True)
    
    fincaixa_id: Mapped[Optional[str]] = mapped_column(VARCHAR(255), nullable=True)
    
    dinheiro: Mapped[float] = mapped_column(FLOAT)