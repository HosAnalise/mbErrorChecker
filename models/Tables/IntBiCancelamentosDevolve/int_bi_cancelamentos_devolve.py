import datetime
from typing import Optional
import int_bi_vendas_relations

from sqlalchemy import VARCHAR, TIMESTAMP, FLOAT, INTEGER,DATE,TIME
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class IntBiCancelamentosDevolve(Base):
    """
    Modelo para a tabela que armazena dados de cancelamentos devolve para o BI.
    """
    __tablename__ = "int_bi_cancelamentos_devolve"

    venda: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    
    empresa: Mapped[int] = mapped_column(INTEGER, primary_key = True)
    
    id_financasweb: Mapped[int] = mapped_column(INTEGER)
    
    data_hora_inclusao: Mapped[datetime.datetime] = mapped_column(TIMESTAMP)
    
    data_hora_tentativa: Mapped[Optional[datetime.datetime]] = mapped_column(TIMESTAMP, nullable=True)
    
    guid_web: Mapped[str] = mapped_column(VARCHAR(255))
    
    erro: Mapped[Optional[str]] = mapped_column(VARCHAR(1024), nullable=True)