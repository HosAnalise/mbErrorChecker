import datetime
from typing import Optional

from sqlalchemy import  ForeignKey,  VARCHAR, TIMESTAMP, FLOAT,INTEGER
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, sessionmaker

class Base(DeclarativeBase):
    pass

class IntBiVendas(Base):
    """
    Modelo para a tabela que armazena dados de vendas para o BI.
    """
    __tablename__ = "int_bi_vendas"
    
    venda: Mapped[int] = mapped_column(primary_key=True)
    
    empresa_id: Mapped[int] = mapped_column(ForeignKey("empresas.id"))

    tentativas: Mapped[Optional[int]]

    guid_web: Mapped[Optional[str]] = mapped_column(VARCHAR(100))
    
    
    data_hora_tentativa: Mapped[Optional[datetime.datetime]] = mapped_column(TIMESTAMP)
    data_hora_inclusao: Mapped[Optional[datetime.datetime]] = mapped_column(TIMESTAMP)
    
    erro: Mapped[Optional[str]]  

   
    def __repr__(self) -> str:
        return f"<IntBiVendas( venda={self.venda}, empresa_id={self.empresa_id}, erro={self.erro})>"