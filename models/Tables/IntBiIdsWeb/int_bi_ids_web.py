import datetime
from typing import Optional

from sqlalchemy import VARCHAR, TIMESTAMP, FLOAT, INTEGER,DATE,TIME
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class IntBiIdsWeb(Base):
    """
    Modelo para a tabela que armazena dados de ids web para o BI.
    """
    __tablename__ = "int_bi_ids_web"

    tipo: Mapped[str] = mapped_column(VARCHAR, primary_key=True)
    
    codigo: Mapped[float] = mapped_column(FLOAT, primary_key=True)
    
    id_web: Mapped[int] = mapped_column(INTEGER)