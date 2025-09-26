import datetime
from typing import Optional

from sqlalchemy import VARCHAR, TIMESTAMP, FLOAT, INTEGER,DATE,TIME
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class IntBiNotas(Base):
    """
    Modelo para a tabela que armazena dados de notas para o BI.
    """
    __tablename__ = "int_bi_notas"

    codigo: Mapped[float] = mapped_column(FLOAT, primary_key = True)
    
    empresa: Mapped[float] = mapped_column(FLOAT, primary_key = True)
    
    tentativas: Mapped[int] = mapped_column(INTEGER)
    
    guid_web: Mapped[str] = mapped_column(VARCHAR(255))
    
    data_hora_tentativa: Mapped[datetime.datetime] = mapped_column(TIMESTAMP)
    
    data_hora_inclusao: Mapped[datetime.datetime] = mapped_column(TIMESTAMP)
    
    erro: Mapped[Optional[str]] = mapped_column(VARCHAR(1000))

class CabNf(Base):
    """
    Modelo para a tabela que armazena dados de notas.
    """
    __tablename__ = "cab_nf"

    codigo: Mapped[float] = mapped_column(FLOAT, primary_key=True)
    
    nr_nota: Mapped[float] = mapped_column(FLOAT)
    
    tipo: Mapped[str] = mapped_column(VARCHAR(50))
    
    natureza: Mapped[str] = mapped_column(VARCHAR(50))
    
    cfop: Mapped[str] = mapped_column(VARCHAR(10))
    
    ie_subst_trib: Mapped[str] = mapped_column(VARCHAR(20))
    
    dest_nome: Mapped[str] = mapped_column(VARCHAR(255))
    
    dest_cnpj: Mapped[str] = mapped_column(VARCHAR(20))
    
    dest_endereco: Mapped[str] = mapped_column(VARCHAR(255))
    
    dest_bairro: Mapped[str] = mapped_column(VARCHAR(100))
    
    dest_cep: Mapped[str] = mapped_column(VARCHAR(20))
    
    dest_cidade: Mapped[str] = mapped_column(VARCHAR(100))
    
    dest_fone: Mapped[str] = mapped_column(VARCHAR(20))
    
    dest_uf: Mapped[str] = mapped_column(VARCHAR(2))
    
    dest_ie: Mapped[str] = mapped_column(VARCHAR(20))
    
    data_emissao: Mapped[datetime.date] = mapped_column(DATE)
    
    data_saida_entrada: Mapped[datetime.date] = mapped_column(DATE)
    
    hora_saida_entrada: Mapped[datetime.time] = mapped_column(TIME)
    
    base_subst: Mapped[float] = mapped_column(FLOAT)
    
    valor_subst: Mapped[float] = mapped_column(FLOAT)
    
    valor_produtos: Mapped[float] = mapped_column(FLOAT)
    
    valor_frete: Mapped[float] = mapped_column(FLOAT)
    
    valor_seguro: Mapped[float] = mapped_column(FLOAT)
    
    despesas_acessorias: Mapped[float] = mapped_column(FLOAT)
    
    valor_ipi: Mapped[float] = mapped_column(FLOAT)
    
    valor_nota: Mapped[float] = mapped_column(FLOAT)
    
    desconto_nota: Mapped[float] = mapped_column(FLOAT)
    
    pdesconto_nota: Mapped[float] = mapped_column(FLOAT)
    
    operador: Mapped[float] = mapped_column(FLOAT)
    
    nome_operador: Mapped[str] = mapped_column(VARCHAR(100))
    
    cupom: Mapped[float] = mapped_column(FLOAT)
    
    venda: Mapped[float] = mapped_column(FLOAT)
    
    empresa: Mapped[float] = mapped_column(FLOAT, primary_key=True)
    
    dest_codigo: Mapped[float] = mapped_column(FLOAT)
    
    cancelado: Mapped[str] = mapped_column(VARCHAR(10))
    
    cif_fob: Mapped[str] = mapped_column(VARCHAR(10))
    
    transportadora: Mapped[str] = mapped_column(VARCHAR(100))
    
    fiscal: Mapped[str] = mapped_column(VARCHAR(10))
    
    data_impressao: Mapped[datetime.date] = mapped_column(DATE)
    
    status_duplicata: Mapped[int] = mapped_column(INTEGER)
    
    fis_nat_opera: Mapped[str] = mapped_column(VARCHAR(50))
    
    campox: Mapped[str] = mapped_column(VARCHAR(50))
    
    base_icms_dev: Mapped[float] = mapped_column(FLOAT)
    
    valor_icms_dev: Mapped[float] = mapped_column(FLOAT)
    
    tot_itens: Mapped[float] = mapped_column(FLOAT)
    
    observacao1: Mapped[str] = mapped_column(VARCHAR(255))
    
    estacao: Mapped[float] = mapped_column(FLOAT)
    
    cod_transportador: Mapped[float] = mapped_column(FLOAT)
    
    nota_origem: Mapped[float] = mapped_column(FLOAT)
    
    observacao: Mapped[str] = mapped_column(VARCHAR(255))
    
    modelo: Mapped[str] = mapped_column(VARCHAR(10))
    
    serie: Mapped[str] = mapped_column(VARCHAR(10))
    
    peso_bruto: Mapped[float] = mapped_column(FLOAT)
    
    peso_liq: Mapped[float] = mapped_column(FLOAT)
    
    volumes: Mapped[int] = mapped_column(INTEGER)
    
    data_vencimento: Mapped[datetime.date] = mapped_column(DATE)
    
    agrupada: Mapped[str] = mapped_column(VARCHAR(10))
    
    data_vencimento2: Mapped[datetime.date] = mapped_column(DATE)
    
    data_vencimento3: Mapped[datetime.date] = mapped_column(DATE)
    
    data_vencimento4: Mapped[datetime.date] = mapped_column(DATE)
    
    data_vencimento5: Mapped[datetime.date] = mapped_column(DATE)
    
    data_vencimento6: Mapped[datetime.date] = mapped_column(DATE)
    
    valor_vencimento: Mapped[float] = mapped_column(FLOAT)
    
    valor_vencimento2: Mapped[float] = mapped_column(FLOAT)
    
    valor_vencimento3: Mapped[float] = mapped_column(FLOAT)
    
    valor_vencimento4: Mapped[float] = mapped_column(FLOAT)
    
    valor_vencimento5: Mapped[float] = mapped_column(FLOAT)
    
    valor_vencimento6: Mapped[float] = mapped_column(FLOAT)
    
    valor_gnre: Mapped[float] = mapped_column(FLOAT)
    
    codigo_transportadora: Mapped[float] = mapped_column(FLOAT)
    
    tp_nf: Mapped[str] = mapped_column(VARCHAR(10))
    
    cod_barras_nfe: Mapped[str] = mapped_column(VARCHAR(50))
    
    valor_pis: Mapped[float] = mapped_column(FLOAT)
    
    valor_cofins: Mapped[float] = mapped_column(FLOAT)
    
    valor_pis_st: Mapped[float] = mapped_column(FLOAT)
    
    valor_cofins_st: Mapped[float] = mapped_column(FLOAT)
    
    dataenvio_nfe: Mapped[str] = mapped_column(VARCHAR(50))
    
    digestvalue_nfe: Mapped[str] = mapped_column(VARCHAR(255))
    
    lote_nfe: Mapped[float] = mapped_column(FLOAT)
    
    motivo_nfe: Mapped[str] = mapped_column(VARCHAR(255))
    
    nrorecebimento_nfe: Mapped[str] = mapped_column(VARCHAR(50))
    
    protocolo_nfe: Mapped[str] = mapped_column(VARCHAR(50))
    
    status_nfe: Mapped[int] = mapped_column(INTEGER)
    
    tipo_ambiente_nfe: Mapped[int] = mapped_column(INTEGER)
    
    versao_aplicativo_nfe: Mapped[str] = mapped_column(VARCHAR(50))
    
    versao_nfe: Mapped[str] = mapped_column(VARCHAR(20))
    
    dest_email: Mapped[str] = mapped_column(VARCHAR(100))
    
    dest_numero: Mapped[str] = mapped_column(VARCHAR(20))
    
    cod_barras_nfe_ref: Mapped[str] = mapped_column(VARCHAR(50))
    
    nfe_finalidade: Mapped[int] = mapped_column(INTEGER)
    
    ordem_compra: Mapped[float] = mapped_column(FLOAT)
    
    observacao_id: Mapped[float] = mapped_column(FLOAT)
    
    inf_compl_id: Mapped[float] = mapped_column(FLOAT)
    
    base_subst_retido: Mapped[float] = mapped_column(FLOAT)
    
    valor_subst_retido: Mapped[float] = mapped_column(FLOAT)
    
    cond_pagamento: Mapped[int] = mapped_column(INTEGER)
    
    placa: Mapped[str] = mapped_column(VARCHAR(10))
    
    uf_placa: Mapped[str] = mapped_column(VARCHAR(2))
    
    codigo_antt: Mapped[str] = mapped_column(VARCHAR(20))
    
    dest_complemento: Mapped[str] = mapped_column(VARCHAR(100))
    
    nr_conta_convenio: Mapped[float] = mapped_column(FLOAT)
    
    numero_pedido_nfe: Mapped[str] = mapped_column(VARCHAR(50))
    
    numero_autorizacao: Mapped[float] = mapped_column(FLOAT)
    
    dest_ddd: Mapped[str] = mapped_column(VARCHAR(5))
    
    dest_fax: Mapped[str] = mapped_column(VARCHAR(20))
    
    hora_emissao: Mapped[datetime.time] = mapped_column(TIME)
    
    valor_outros: Mapped[float] = mapped_column(FLOAT)
    
    valor_icms: Mapped[float] = mapped_column(FLOAT)
    
    base_icms: Mapped[float] = mapped_column(FLOAT)
    
    valor_fcp: Mapped[float] = mapped_column(FLOAT)
    
    numero_fatura: Mapped[str] = mapped_column(VARCHAR(50))
    
    hash_origem: Mapped[int] = mapped_column(INTEGER)
    
    hash_atual: Mapped[int] = mapped_column(INTEGER)
    
    valor_fcp_st_ret: Mapped[float] = mapped_column(FLOAT)
    
    valor_fcp_st: Mapped[float] = mapped_column(FLOAT)
    
    valor_icms_desonerado: Mapped[float] = mapped_column(FLOAT)
    
    ipi_devolvido: Mapped[float] = mapped_column(FLOAT)
    
    partilha_icms_uf_destino: Mapped[float] = mapped_column(FLOAT)
    
    partilha_icms_uf_emitente: Mapped[float] = mapped_column(FLOAT)
    
    partilha_valor_fcp: Mapped[float] = mapped_column(FLOAT)
    
    valor_fcp_st_info: Mapped[float] = mapped_column(FLOAT)
    
    dest_pais: Mapped[int] = mapped_column(INTEGER)
    
    menssagem_sefaz: Mapped[str] = mapped_column(VARCHAR(255))
    
    consumidor_final: Mapped[str] = mapped_column(VARCHAR(10))
    
    carta_correcao: Mapped[str] = mapped_column(VARCHAR(255))
    
    intermediador: Mapped[int] = mapped_column(INTEGER)
    
    intermediador_cnpj: Mapped[str] = mapped_column(VARCHAR(20))
    
    intermediador_usuario: Mapped[str] = mapped_column(VARCHAR(50))
    
    tipo_difal: Mapped[int] = mapped_column(INTEGER)
    
    percentual_irrf: Mapped[float] = mapped_column(FLOAT)
    
    valor_irrf: Mapped[float] = mapped_column(FLOAT)
    
    percentual_csll: Mapped[float] = mapped_column(FLOAT)
    
    valor_csll: Mapped[float] = mapped_column(FLOAT)
    
    dest_contribuinte_icms: Mapped[int] = mapped_column(INTEGER)
    
    descontar_icms_desonerado: Mapped[str] = mapped_column(VARCHAR(10))
    
    cod_nota_agrupamento: Mapped[int] = mapped_column(INTEGER)