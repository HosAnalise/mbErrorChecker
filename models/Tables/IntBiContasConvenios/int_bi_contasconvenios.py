import datetime
from typing import Optional

from sqlalchemy import VARCHAR, TIMESTAMP, FLOAT, INTEGER,DATE,TIME
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class IntBiContasConvenios(Base):
    """
    Modelo para a tabela que armazena dados de contas convenios para o BI.
    """
    __tablename__ = "int_bi_contasconvenios"

    nr_conta: Mapped[float] = mapped_column(FLOAT, primary_key=True)
    
    empresa: Mapped[float] = mapped_column(FLOAT, primary_key=True)
    
    convenio: Mapped[float] = mapped_column(FLOAT, primary_key=True)
    
    excluir: Mapped[int] = mapped_column(INTEGER)
    
    tentativas: Mapped[int] = mapped_column(INTEGER)
    
    guid_web: Mapped[str] = mapped_column(VARCHAR(255))
    
    data_hora_tentativa: Mapped[datetime.datetime] = mapped_column(TIMESTAMP)
    
    data_hora_inclusao: Mapped[datetime.datetime] = mapped_column(TIMESTAMP)
    
    erro: Mapped[Optional[str]] = mapped_column(VARCHAR(1000))

class ContasConvenios(Base):
    """
    Modelo para a tabela que armazena dados de contas convenios.
    """
    __tablename__ = "contasconvenios"

    convenio: Mapped[float] = mapped_column(FLOAT, primary_key=True)
    
    nr_conta: Mapped[float] = mapped_column(FLOAT, primary_key=True)
    
    vencimento: Mapped[datetime.date] = mapped_column(DATE)
    
    valor: Mapped[float] = mapped_column(FLOAT)
    
    juros: Mapped[float] = mapped_column(FLOAT)
    
    desconto: Mapped[float] = mapped_column(FLOAT)
    
    saldo: Mapped[float] = mapped_column(FLOAT)
    
    ultpagamento: Mapped[Optional[datetime.date]] = mapped_column(DATE)
    
    valorpago: Mapped[float] = mapped_column(FLOAT)
    
    hora: Mapped[Optional[datetime.time]] = mapped_column(TIME)
    
    empresa: Mapped[float] = mapped_column(FLOAT, primary_key=True)
    
    fin_codigo: Mapped[float] = mapped_column(FLOAT)
    
    fin_cod_empresa: Mapped[int] = mapped_column(INTEGER)
    
    nr_fatura: Mapped[Optional[str]] = mapped_column(VARCHAR(255))
    
    dt_inicial: Mapped[Optional[datetime.date]] = mapped_column(DATE)
    
    dt_final: Mapped[Optional[datetime.date]] = mapped_column(DATE)
    
    data_fechamento: Mapped[Optional[datetime.datetime]] = mapped_column(TIMESTAMP)
    
    id_finanacasweb: Mapped[int] = mapped_column(INTEGER)
    
    id_financasweb: Mapped[int] = mapped_column(INTEGER)
    
    desconto_fatura: Mapped[float] = mapped_column(FLOAT)