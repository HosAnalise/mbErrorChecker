import datetime
from typing import Optional

from sqlalchemy import VARCHAR, TIMESTAMP, FLOAT, INTEGER,DATE,TIME
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class IntBiEntregas(Base):
    """
    Modelo para a tabela que armazena dados de entregas para o BI.
    """
    __tablename__ = "int_bi_entregas"

    nr_entrega: Mapped[float] = mapped_column(FLOAT, primary_key=True)
    
    empresa: Mapped[float] = mapped_column(FLOAT, primary_key=True)
    
    tentativas: Mapped[int] = mapped_column(INTEGER)
    
    guid_web: Mapped[str] = mapped_column(VARCHAR(255))
    
    data_hora_tentativa: Mapped[datetime.datetime] = mapped_column(TIMESTAMP)
    
    data_hora_inclusao: Mapped[datetime.datetime] = mapped_column(TIMESTAMP)
    
    erro: Mapped[Optional[str]] = mapped_column(VARCHAR(1000))

class Entregas(Base):
    """
    Modelo para a tabela que armazena dados de entregas.
    """
    __tablename__ = "entregas"

    data: Mapped[datetime.date] = mapped_column(DATE)
    
    hora_pedido: Mapped[datetime.time] = mapped_column(TIME)
    
    atendente: Mapped[float] = mapped_column(FLOAT)
    
    hora_saida: Mapped[datetime.time] = mapped_column(TIME)
    
    valor: Mapped[float] = mapped_column(FLOAT)
    
    lancamen: Mapped[str] = mapped_column(VARCHAR(255))
    
    hora_retorno: Mapped[datetime.time] = mapped_column(TIME)
    
    entregador: Mapped[float] = mapped_column(FLOAT)
    
    empresa: Mapped[float] = mapped_column(FLOAT, primary_key=True)
    
    nr_entrega: Mapped[float] = mapped_column(FLOAT, primary_key=True)
    
    venda: Mapped[float] = mapped_column(FLOAT)
    
    troco: Mapped[float] = mapped_column(FLOAT)
    
    cliente: Mapped[float] = mapped_column(FLOAT)
    
    convenio: Mapped[float] = mapped_column(FLOAT)
    
    obs1: Mapped[Optional[str]] = mapped_column(VARCHAR(255))
    
    obs2: Mapped[Optional[str]] = mapped_column(VARCHAR(255))
    
    obs3: Mapped[Optional[str]] = mapped_column(VARCHAR(255))
    
    obs4: Mapped[Optional[str]] = mapped_column(VARCHAR(255))
    
    nrcaixa: Mapped[float] = mapped_column(FLOAT)
    
    taxa: Mapped[float] = mapped_column(FLOAT)
    
    data_retorno: Mapped[datetime.date] = mapped_column(DATE)
    
    tipo_endereco: Mapped[Optional[str]] = mapped_column(VARCHAR(255))
    
    motivo: Mapped[Optional[str]] = mapped_column(VARCHAR(255))
    
    data_entrega: Mapped[datetime.date] = mapped_column(DATE)
    
    hora_entrega: Mapped[datetime.time] = mapped_column(TIME)
    
    turno_entrega: Mapped[float] = mapped_column(FLOAT)
    
    nr_pedido: Mapped[float] = mapped_column(FLOAT)
    
    venda_retorno: Mapped[float] = mapped_column(FLOAT)
    
    empresa_retorno: Mapped[float] = mapped_column(FLOAT)
    
    valor_dev: Mapped[float] = mapped_column(FLOAT)
    
    end_cod_logradouro: Mapped[float] = mapped_column(FLOAT)
    
    end_complemento: Mapped[Optional[str]] = mapped_column(VARCHAR(255))
    
    end_numero: Mapped[Optional[str]] = mapped_column(VARCHAR(255))
    
    end_referencia: Mapped[Optional[str]] = mapped_column(VARCHAR(255))
    
    separador: Mapped[float] = mapped_column(FLOAT)
    
    expedidor: Mapped[float] = mapped_column(FLOAT)
    
    observacoes: Mapped[Optional[str]] = mapped_column(VARCHAR(255))
    
    romaneio: Mapped[float] = mapped_column(FLOAT)
    
    email_enviado: Mapped[float] = mapped_column(FLOAT)
    
    data_hora_estorno: Mapped[Optional[datetime.datetime]] = mapped_column(TIMESTAMP)
    
    operador_estorno: Mapped[float] = mapped_column(FLOAT)
    
    seq_agrupador: Mapped[float] = mapped_column(FLOAT)
    
    entrega_original: Mapped[float] = mapped_column(FLOAT)
    
    entrega_original_empresa: Mapped[float] = mapped_column(FLOAT)
    
    empresa_romaneio: Mapped[float] = mapped_column(FLOAT)
    
    reentrega: Mapped[int] = mapped_column(INTEGER)
    
    codigo_endereco: Mapped[float] = mapped_column(FLOAT)
    
    nrcaixa_retorno: Mapped[float] = mapped_column(FLOAT)
    
    id_entregas_app: Mapped[float] = mapped_column(FLOAT)
    
    sended_to_hos_entregas: Mapped[int] = mapped_column(INTEGER)
    
    id_financasweb: Mapped[float] = mapped_column(FLOAT)
    
    frete: Mapped[float] = mapped_column(FLOAT)
    
    status_pgto: Mapped[int] = mapped_column(INTEGER)
    
    pago_loja: Mapped[int] = mapped_column(INTEGER)
    
    id_agrupamento: Mapped[int] = mapped_column(INTEGER)
    
    empresa_frete: Mapped[int] = mapped_column(INTEGER)
    
    romaneio_ordem: Mapped[int] = mapped_column(INTEGER)