from sqlalchemy import CHAR, VARCHAR, TIMESTAMP, FLOAT, INTEGER,DATE
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
import datetime
from typing import Optional


class Base(DeclarativeBase):
    pass


class Venda(Base):
    __tablename__ = "venda"

    
    VENDA_ID: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    
    GRUPO_LOJA_ID: Mapped[Optional[int]] = mapped_column(INTEGER)
    
    LOJA_ID: Mapped[Optional[int]] = mapped_column(INTEGER)
    
    CAIXA_CONTROLE_ID: Mapped[Optional[int]] = mapped_column(INTEGER)
    
    OPERADOR_ID: Mapped[Optional[int]] = mapped_column(INTEGER)
    
    PESSOA_CLIENTE_ID: Mapped[Optional[int]] = mapped_column(INTEGER)
    
    DATA_HORA: Mapped[Optional[datetime.datetime]] = mapped_column(TIMESTAMP)
    
    CUPOM: Mapped[Optional[int]] = mapped_column(INTEGER)
    
    VENDA_ORIGEM_ID: Mapped[Optional[int]] = mapped_column(INTEGER)
    
    OBSERVACAO_VENDA: Mapped[Optional[str]] = mapped_column(VARCHAR(250))
    
    GNF_NUMERO: Mapped[Optional[int]] = mapped_column(INTEGER)
    
    GRG_NUMERO: Mapped[Optional[int]] = mapped_column(INTEGER)
    
    CLIENTE_NOME: Mapped[Optional[str]] = mapped_column(VARCHAR(500))
    
    CLIENTE_CPF_CNPJ: Mapped[Optional[str]] = mapped_column(VARCHAR(18))
    
    PESSOA_DEPENDENTE_ID: Mapped[Optional[int]] = mapped_column(INTEGER)
    
    VENDA_HOS_ID: Mapped[Optional[int]] = mapped_column(INTEGER)
    
    VENDA_ORIGEM_PAGAMENTO_ID: Mapped[Optional[int]] = mapped_column(INTEGER)
    
    NUMERO_PEDIDO: Mapped[Optional[str]] = mapped_column(VARCHAR(250))
    
    SINCRONIZACAO: Mapped[Optional[int]] = mapped_column(INTEGER)
    
    CONFERIDO: Mapped[Optional[str]] = mapped_column(CHAR(1))
    
    DELETADA_API: Mapped[Optional[int]] = mapped_column(INTEGER)
    
    E_CORTESIA: Mapped[Optional[str]] = mapped_column(CHAR(1))
    
    VENDA_FORMA_CAPTACAO_ID: Mapped[Optional[int]] = mapped_column(INTEGER)
    
    EDITADO_LEGADO: Mapped[Optional[str]] = mapped_column(CHAR(1))
    
    E_TELE_ENTREGA_AVULSA: Mapped[Optional[str]] = mapped_column(CHAR(1))


class VendaRecebimento(Base):
    __tablename__ = "venda_recebimento"

    
    VENDA_RECEBIMENTO_ID: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    
    SEQUENCIA_PAGAMENTO: Mapped[Optional[int]] = mapped_column(INTEGER)
    
    VALOR_RECEBIDO: Mapped[Optional[float]] = mapped_column(FLOAT)
    
    VENDA_ID: Mapped[Optional[int]] = mapped_column(INTEGER)
    
    FORMA_RECEBIMENTO_ID: Mapped[Optional[int]] = mapped_column(INTEGER)
    
    CAIXA_CONTROLE_RECEBIMENTO_ID: Mapped[Optional[int]] = mapped_column(INTEGER)
    
    JUROS: Mapped[Optional[float]] = mapped_column(FLOAT)
    
    DESCONTO: Mapped[Optional[float]] = mapped_column(FLOAT)
    
    MULTA: Mapped[Optional[float]] = mapped_column(FLOAT)
    
    DATA_RECEBIMENTO: Mapped[Optional[datetime.date]] = mapped_column(DATE)
    
    VENDA_PARCELA_ID: Mapped[Optional[int]] = mapped_column(INTEGER)
    
    PESSOA_OPERADOR_ID: Mapped[Optional[int]] = mapped_column(INTEGER)
    
    CODIGO_HOS: Mapped[Optional[int]] = mapped_column(INTEGER)
    
    CONTA_ID: Mapped[Optional[int]] = mapped_column(INTEGER)
    
    CONFERIDO: Mapped[Optional[str]] = mapped_column(CHAR(1))
    
    ACRESCIMOS: Mapped[Optional[float]] = mapped_column(FLOAT)
    
    TAXAS: Mapped[Optional[float]] = mapped_column(FLOAT)


