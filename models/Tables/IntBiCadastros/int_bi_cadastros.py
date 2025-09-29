import datetime
from typing import Optional

from sqlalchemy import VARCHAR, TIMESTAMP, FLOAT, INTEGER,DATE,TIME
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class IntBiCadastros(Base):
    """
    Modelo para a tabela que armazena dados de cadastros para o BI.
    """
    __tablename__ = "int_bi_cadastros"

    codigo: Mapped[float] = mapped_column(FLOAT, primary_key = True)
    
    tipo: Mapped[int] = mapped_column(INTEGER, primary_key = True)
    
    tentativas: Mapped[int] = mapped_column(INTEGER)
    
    guid_web: Mapped[str] = mapped_column(VARCHAR(255))
    
    data_hora_tentativa: Mapped[datetime.datetime] = mapped_column(TIMESTAMP)
    
    data_hora_inclusao: Mapped[datetime.datetime] = mapped_column(TIMESTAMP)
    
    erro: Mapped[Optional[str]] = mapped_column(VARCHAR, nullable=True)

class Clientes(Base):
    """
    Modelo para a tabela que armazena dados de clientes.
    """
    __tablename__ = "clientes"

    codigo: Mapped[float] = mapped_column(FLOAT, primary_key=True)
    
    nome: Mapped[str] = mapped_column(VARCHAR(255))
    
    endereco: Mapped[str] = mapped_column(VARCHAR(255))
    
    bairro: Mapped[str] = mapped_column(VARCHAR(255))
    
    cidade: Mapped[str] = mapped_column(VARCHAR(255))
    
    uf: Mapped[str] = mapped_column(VARCHAR(2))
    
    cep: Mapped[str] = mapped_column(VARCHAR(10))
    
    ddd: Mapped[str] = mapped_column(VARCHAR(5))
    
    telefone: Mapped[str] = mapped_column(VARCHAR(20))
    
    rg: Mapped[str] = mapped_column(VARCHAR(20))
    
    cpf: Mapped[str] = mapped_column(VARCHAR(14))
    
    data_nasc: Mapped[datetime.date] = mapped_column(DATE)
    
    profissao: Mapped[str] = mapped_column(VARCHAR(100))
    
    grupo: Mapped[str] = mapped_column(VARCHAR(100))
    
    conjuge: Mapped[str] = mapped_column(VARCHAR(100))
    
    banco: Mapped[str] = mapped_column(VARCHAR(100))
    
    comercio: Mapped[str] = mapped_column(VARCHAR(100))
    
    autoriza: Mapped[str] = mapped_column(VARCHAR(10))
    
    convenio: Mapped[float] = mapped_column(FLOAT)
    
    matricula: Mapped[float] = mapped_column(FLOAT)
    
    admissao: Mapped[datetime.date] = mapped_column(DATE)
    
    credito: Mapped[str] = mapped_column(VARCHAR(10))
    
    limite: Mapped[float] = mapped_column(FLOAT)
    
    debito: Mapped[float] = mapped_column(FLOAT)
    
    vencimento: Mapped[float] = mapped_column(FLOAT)
    
    prazo: Mapped[float] = mapped_column(FLOAT)
    
    desconto: Mapped[float] = mapped_column(FLOAT)
    
    cadastro: Mapped[datetime.date] = mapped_column(DATE)
    
    desc_venda: Mapped[str] = mapped_column(VARCHAR(255))
    
    obs: Mapped[str] = mapped_column(VARCHAR(255))
    
    convenio_2: Mapped[int] = mapped_column(INTEGER)
    
    convenio_3: Mapped[int] = mapped_column(INTEGER)
    
    matricula_2: Mapped[int] = mapped_column(INTEGER)
    
    matricula_3: Mapped[int] = mapped_column(INTEGER)
    
    nometitular: Mapped[str] = mapped_column(VARCHAR(255))
    
    nometitular_2: Mapped[str] = mapped_column(VARCHAR(255))
    
    nometitular_3: Mapped[str] = mapped_column(VARCHAR(255))
    
    dtnascconjuge: Mapped[datetime.date] = mapped_column(DATE)
    
    itensreconhece: Mapped[str] = mapped_column(VARCHAR(255))
    
    email: Mapped[str] = mapped_column(VARCHAR(255))
    
    filiacao: Mapped[str] = mapped_column(VARCHAR(255))
    
    celular: Mapped[str] = mapped_column(VARCHAR(20))
    
    observacoes: Mapped[str] = mapped_column(VARCHAR(255))
    
    filial: Mapped[str] = mapped_column(VARCHAR(100))
    
    excluido: Mapped[str] = mapped_column(VARCHAR(10))
    
    empresa: Mapped[float] = mapped_column(FLOAT)
    
    fechamento: Mapped[int] = mapped_column(INTEGER)
    
    tolerancia: Mapped[int] = mapped_column(INTEGER)
    
    senhaconv: Mapped[str] = mapped_column(VARCHAR(50))
    
    cliente_a_prazo: Mapped[str] = mapped_column(VARCHAR(10))
    
    dia_semana_vencimento: Mapped[str] = mapped_column(VARCHAR(20))
    
    naturalidade: Mapped[str] = mapped_column(VARCHAR(100))
    
    diafechamento: Mapped[float] = mapped_column(FLOAT)
    
    statusconvenio: Mapped[str] = mapped_column(VARCHAR(50))
    
    enderecocom: Mapped[str] = mapped_column(VARCHAR(255))
    
    bairrocom: Mapped[str] = mapped_column(VARCHAR(255))
    
    cidadecom: Mapped[str] = mapped_column(VARCHAR(255))
    
    ufcom: Mapped[str] = mapped_column(VARCHAR(2))
    
    cepcom: Mapped[str] = mapped_column(VARCHAR(10))
    
    telefonecom1: Mapped[str] = mapped_column(VARCHAR(20))
    
    telefonecom2: Mapped[str] = mapped_column(VARCHAR(20))
    
    grupos_produtos: Mapped[str] = mapped_column(VARCHAR(255))
    
    referencia1: Mapped[str] = mapped_column(VARCHAR(255))
    
    referencia2: Mapped[str] = mapped_column(VARCHAR(255))
    
    nr_cartao: Mapped[str] = mapped_column(VARCHAR(50))
    
    callcenter: Mapped[str] = mapped_column(VARCHAR(50))
    
    pbm: Mapped[str] = mapped_column(VARCHAR(50))
    
    limite_convenio: Mapped[float] = mapped_column(FLOAT)
    
    debito_convenio: Mapped[float] = mapped_column(FLOAT)
    
    sexo: Mapped[str] = mapped_column(VARCHAR(10))
    
    gerar_cartao: Mapped[str] = mapped_column(VARCHAR(10))
    
    via_cartao: Mapped[float] = mapped_column(FLOAT)
    
    bairroref1: Mapped[str] = mapped_column(VARCHAR(255))
    
    bairroref2: Mapped[str] = mapped_column(VARCHAR(255))
    
    cepref1: Mapped[str] = mapped_column(VARCHAR(10))
    
    cepref2: Mapped[str] = mapped_column(VARCHAR(10))
    
    ufref1: Mapped[str] = mapped_column(VARCHAR(2))
    
    ufref2: Mapped[str] = mapped_column(VARCHAR(2))
    
    cidaderef1: Mapped[str] = mapped_column(VARCHAR(255))
    
    cidaderef2: Mapped[str] = mapped_column(VARCHAR(255))
    
    statusprazo: Mapped[str] = mapped_column(VARCHAR(50))
    
    forma_compra: Mapped[str] = mapped_column(VARCHAR(50))
    
    nomevendedor: Mapped[str] = mapped_column(VARCHAR(255))
    
    vendedor: Mapped[str] = mapped_column(VARCHAR(255))
    
    dia_fechamento: Mapped[float] = mapped_column(FLOAT)
    
    forma_cobranca: Mapped[str] = mapped_column(VARCHAR(50))
    
    agencia: Mapped[str] = mapped_column(VARCHAR(50))
    
    conta_corrente: Mapped[str] = mapped_column(VARCHAR(50))
    
    apelido: Mapped[str] = mapped_column(VARCHAR(50))
    
    dependente: Mapped[str] = mapped_column(VARCHAR(255))
    
    dependente_2: Mapped[str] = mapped_column(VARCHAR(255))
    
    dependente_3: Mapped[str] = mapped_column(VARCHAR(255))
    
    ref_bancaria: Mapped[str] = mapped_column(VARCHAR(255))
    
    status: Mapped[str] = mapped_column(VARCHAR(50))
    
    tipo_pessoa: Mapped[str] = mapped_column(VARCHAR(50))
    
    classifi_produtos: Mapped[str] = mapped_column(VARCHAR(255))
    
    situacao: Mapped[str] = mapped_column(VARCHAR(50))
    
    senhas: Mapped[str] = mapped_column(VARCHAR(255))
    
    motivo_liberacao_campos: Mapped[str] = mapped_column(VARCHAR(255))
    
    funcionario_cad: Mapped[float] = mapped_column(FLOAT)
    
    classificacao: Mapped[str] = mapped_column(VARCHAR(50))
    
    cliente_chequepre: Mapped[str] = mapped_column(VARCHAR(10))
    
    tolerancia_inadimp: Mapped[float] = mapped_column(FLOAT)
    
    maximo_parcelas: Mapped[float] = mapped_column(FLOAT)
    
    vlr_min_parcela: Mapped[float] = mapped_column(FLOAT)
    
    endentrega: Mapped[str] = mapped_column(VARCHAR(255))
    
    importacao_matricula: Mapped[str] = mapped_column(VARCHAR(255))
    
    telefoneref1: Mapped[str] = mapped_column(VARCHAR(20))
    
    telefoneref2: Mapped[str] = mapped_column(VARCHAR(20))
    
    situacao_cliente: Mapped[str] = mapped_column(VARCHAR(50))
    
    status_2: Mapped[str] = mapped_column(VARCHAR(50))
    
    nome_empresa: Mapped[str] = mapped_column(VARCHAR(255))
    
    renda_mensal: Mapped[float] = mapped_column(FLOAT)
    
    sexo_conjuge: Mapped[str] = mapped_column(VARCHAR(10))
    
    orgao_expedidor: Mapped[str] = mapped_column(VARCHAR(50))
    
    uf_orgao: Mapped[str] = mapped_column(VARCHAR(2))
    
    cod_plano: Mapped[float] = mapped_column(FLOAT)
    
    merchcard_codigo: Mapped[float] = mapped_column(FLOAT)
    
    merchcard_descricao: Mapped[str] = mapped_column(VARCHAR(255))
    
    logradouro_id: Mapped[float] = mapped_column(FLOAT)
    
    datacadastro: Mapped[datetime.date] = mapped_column(DATE)
    
    merchcard_versao: Mapped[int] = mapped_column(INTEGER)
    
    compl_logradouro: Mapped[str] = mapped_column(VARCHAR(255))
    
    cod_medico: Mapped[float] = mapped_column(FLOAT)
    
    nr_cartao_fidelize: Mapped[float] = mapped_column(FLOAT)
    
    etiqueta_impressa: Mapped[str] = mapped_column(VARCHAR(50))
    
    obs_inadimplencia: Mapped[str] = mapped_column(VARCHAR(255))
    
    obs_caixa: Mapped[str] = mapped_column(VARCHAR(255))
    
    cod_contabil_conv: Mapped[float] = mapped_column(FLOAT)
    
    emitir_num_pedido: Mapped[str] = mapped_column(VARCHAR(50))
    
    antes_alterar: Mapped[str] = mapped_column(VARCHAR(255))
    
    ult_alteracao: Mapped[datetime.datetime] = mapped_column(TIMESTAMP)
    
    num_end: Mapped[str] = mapped_column(VARCHAR(20))
    
    cond_pagamento: Mapped[float] = mapped_column(FLOAT)
    
    tabela_desconto: Mapped[float] = mapped_column(FLOAT)
    
    diretorio_foto: Mapped[str] = mapped_column(VARCHAR(255))
    
    whatsapp: Mapped[int] = mapped_column(INTEGER)
    
    flag_ecommerce: Mapped[int] = mapped_column(INTEGER)
    
    nr_cartao_aprazo: Mapped[str] = mapped_column(VARCHAR(50))
    
    wpp_msgs_automaticas: Mapped[str] = mapped_column(VARCHAR(10))
    
    desc_individual_aprazo: Mapped[str] = mapped_column(VARCHAR(255))
    
    fc_v8: Mapped[int] = mapped_column(INTEGER)
    
    id_ifood: Mapped[int] = mapped_column(INTEGER)
    
    retencao_iss: Mapped[str] = mapped_column(VARCHAR(10))
    
    retencao_nfe_irrf: Mapped[int] = mapped_column(INTEGER)
    
    retencao_nfe_csll: Mapped[int] = mapped_column(INTEGER)
    
    id_unico_contato: Mapped[int] = mapped_column(INTEGER)
    
    cod_conceito: Mapped[int] = mapped_column(INTEGER)
    
    observacoesnfe: Mapped[str] = mapped_column(VARCHAR(255))
    
    nome_conceito: Mapped[str] = mapped_column(VARCHAR(255))
    
    data_expiracao_conceito: Mapped[datetime.date] = mapped_column(DATE)
    
    valor_entrada_minima_crediario: Mapped[float] = mapped_column(FLOAT)
    
    limite_temporario: Mapped[float] = mapped_column(FLOAT)
    
    limite_temporario_validade: Mapped[datetime.date] = mapped_column(DATE)
    
    dt_alt: Mapped[datetime.datetime] = mapped_column(TIMESTAMP)
    
    nome_sem_acento: Mapped[str] = mapped_column(VARCHAR(255))

class Produtos(Base):
    """
    Modelo para a tabela que armazena dados de produtos.
    """
    __tablename__ = "produtos"

    codigo: Mapped[float] = mapped_column(FLOAT, primary_key=True)
    
    cod_barra: Mapped[float] = mapped_column(FLOAT)
    
    descricao: Mapped[str] = mapped_column(VARCHAR(255))
    
    est_atual: Mapped[float] = mapped_column(FLOAT)
    
    prc_venda: Mapped[float] = mapped_column(FLOAT)
    
    caracteristica: Mapped[str] = mapped_column(VARCHAR(255))
    
    apresentacao: Mapped[str] = mapped_column(VARCHAR(255))
    
    classificacao: Mapped[str] = mapped_column(VARCHAR(255))
    
    fabricante: Mapped[str] = mapped_column(VARCHAR(255))
    
    princativo: Mapped[str] = mapped_column(VARCHAR(255))
    
    functerapeutica: Mapped[str] = mapped_column(VARCHAR(255))
    
    acaoterapeutica: Mapped[str] = mapped_column(VARCHAR(255))
    
    unidade: Mapped[str] = mapped_column(VARCHAR(50))
    
    tipo: Mapped[str] = mapped_column(VARCHAR(50))
    
    margem: Mapped[str] = mapped_column(VARCHAR(50))
    
    etiqueta: Mapped[str] = mapped_column(VARCHAR(50))
    
    label: Mapped[str] = mapped_column(VARCHAR(50))
    
    desconto: Mapped[float] = mapped_column(FLOAT)
    
    custo: Mapped[float] = mapped_column(FLOAT)
    
    fracao: Mapped[float] = mapped_column(FLOAT)
    
    lucro: Mapped[float] = mapped_column(FLOAT)
    
    dsc_max: Mapped[float] = mapped_column(FLOAT)
    
    prc_promo: Mapped[float] = mapped_column(FLOAT)
    
    aliquota: Mapped[str] = mapped_column(VARCHAR(50))
    
    piscofins: Mapped[str] = mapped_column(VARCHAR(50))
    
    preco_novo: Mapped[float] = mapped_column(FLOAT)
    
    vigencia: Mapped[datetime.date] = mapped_column(DATE)
    
    est_minimo: Mapped[float] = mapped_column(FLOAT)
    
    est_maximo: Mapped[float] = mapped_column(FLOAT)
    
    est_ideal: Mapped[float] = mapped_column(FLOAT)
    
    est_autom: Mapped[float] = mapped_column(FLOAT)
    
    comissao: Mapped[float] = mapped_column(FLOAT)
    
    controlado: Mapped[str] = mapped_column(VARCHAR(50))
    
    dcb: Mapped[str] = mapped_column(VARCHAR(50))
    
    validade_promo: Mapped[datetime.date] = mapped_column(DATE)
    
    princativo2: Mapped[str] = mapped_column(VARCHAR(255))
    
    ult_entrada: Mapped[datetime.date] = mapped_column(DATE)
    
    ult_saida: Mapped[datetime.date] = mapped_column(DATE)
    
    datacadastro: Mapped[datetime.date] = mapped_column(DATE)
    
    customedio: Mapped[float] = mapped_column(FLOAT)
    
    desc_individual: Mapped[float] = mapped_column(FLOAT)
    
    grupo: Mapped[str] = mapped_column(VARCHAR(255))
    
    status: Mapped[str] = mapped_column(VARCHAR(50))
    
    pbm: Mapped[str] = mapped_column(VARCHAR(50))
    
    desc_pbm: Mapped[str] = mapped_column(VARCHAR(255))
    
    status_compra: Mapped[str] = mapped_column(VARCHAR(50))
    
    lote_interno: Mapped[str] = mapped_column(VARCHAR(50))
    
    manipulavel: Mapped[str] = mapped_column(VARCHAR(50))
    
    manipulado: Mapped[str] = mapped_column(VARCHAR(50))
    
    inicio_promo: Mapped[datetime.date] = mapped_column(DATE)
    
    curva: Mapped[str] = mapped_column(VARCHAR(50))
    
    desc_especial: Mapped[float] = mapped_column(FLOAT)
    
    validade_desc_especial: Mapped[datetime.date] = mapped_column(DATE)
    
    inicio_desc_especial: Mapped[datetime.date] = mapped_column(DATE)
    
    produto_pai: Mapped[float] = mapped_column(FLOAT)
    
    mf_ficha: Mapped[float] = mapped_column(FLOAT)
    
    continuo: Mapped[str] = mapped_column(VARCHAR(50))
    
    dias_ideal: Mapped[float] = mapped_column(FLOAT)
    
    prc_liq_ult_entrada: Mapped[float] = mapped_column(FLOAT)
    
    prc_bruto_ult_entrada: Mapped[float] = mapped_column(FLOAT)
    
    ult_preco: Mapped[float] = mapped_column(FLOAT)
    
    ult_reajuste: Mapped[datetime.date] = mapped_column(DATE)
    
    venmax: Mapped[float] = mapped_column(FLOAT)
    
    nr_reg_ms: Mapped[str] = mapped_column(VARCHAR(50))
    
    markup: Mapped[float] = mapped_column(FLOAT)
    
    valor_markup: Mapped[float] = mapped_column(FLOAT)
    
    tipi: Mapped[str] = mapped_column(VARCHAR(50))
    
    cfg_estideal: Mapped[str] = mapped_column(VARCHAR(50))
    
    atualizado_merchcompras: Mapped[str] = mapped_column(VARCHAR(50))
    
    pmc: Mapped[float] = mapped_column(FLOAT)
    
    custo_contabil: Mapped[float] = mapped_column(FLOAT)
    
    captacaoobrigatoria: Mapped[str] = mapped_column(VARCHAR(50))
    
    forma_compra: Mapped[str] = mapped_column(VARCHAR(50))
    
    inativacao_motivo: Mapped[str] = mapped_column(VARCHAR(255))
    
    cod_piscofins: Mapped[float] = mapped_column(FLOAT)
    
    inconsistente: Mapped[str] = mapped_column(VARCHAR(50))
    
    data_consistencia: Mapped[datetime.date] = mapped_column(DATE)
    
    categoria: Mapped[float] = mapped_column(FLOAT)
    
    localizacao: Mapped[str] = mapped_column(VARCHAR(255))
    
    forma_venda: Mapped[str] = mapped_column(VARCHAR(50))
    
    informa_qtd: Mapped[str] = mapped_column(VARCHAR(50))
    
    cod_nbm: Mapped[float] = mapped_column(FLOAT)
    
    dsc_max_gerente: Mapped[float] = mapped_column(FLOAT)
    
    seq_classificacao: Mapped[float] = mapped_column(FLOAT)
    
    cst: Mapped[float] = mapped_column(FLOAT)
    
    origem_st: Mapped[float] = mapped_column(FLOAT)
    
    nivel_participacao: Mapped[str] = mapped_column(VARCHAR(50))
    
    reducao_base: Mapped[float] = mapped_column(FLOAT)
    
    prc_farmacia_popular: Mapped[float] = mapped_column(FLOAT)
    
    cod_conta_credito: Mapped[float] = mapped_column(FLOAT)
    
    cod_conta_debito: Mapped[float] = mapped_column(FLOAT)
    
    cod_conta_estoque: Mapped[float] = mapped_column(FLOAT)
    
    flag: Mapped[float] = mapped_column(FLOAT)
    
    hash_origem: Mapped[int] = mapped_column(INTEGER)
    
    hash_atual: Mapped[int] = mapped_column(INTEGER)
    
    prolongado: Mapped[str] = mapped_column(VARCHAR(50))
    
    unidade_p344: Mapped[str] = mapped_column(VARCHAR(50))
    
    dt_inicio_promo: Mapped[datetime.date] = mapped_column(DATE)
    
    cod_ajuste_credito_sn: Mapped[str] = mapped_column(VARCHAR(50))
    
    codigo_servico: Mapped[float] = mapped_column(FLOAT)
    
    observacoes: Mapped[str] = mapped_column(VARCHAR(255))
    
    cod_empresa_prod: Mapped[float] = mapped_column(FLOAT)
    
    ult_alteracao: Mapped[datetime.datetime] = mapped_column(TIMESTAMP)
    
    nz_homologado: Mapped[str] = mapped_column(VARCHAR(50))
    
    codigo_cest: Mapped[float] = mapped_column(FLOAT)
    
    nz_conferido: Mapped[int] = mapped_column(INTEGER)
    
    produto_tele_entrega: Mapped[str] = mapped_column(VARCHAR(50))
    
    codigo_tiss: Mapped[str] = mapped_column(VARCHAR(50))
    
    classificacao_nbm: Mapped[float] = mapped_column(FLOAT)
    
    descricao_ecommerce: Mapped[str] = mapped_column(VARCHAR(255))
    
    grupo_ecommerce: Mapped[str] = mapped_column(VARCHAR(255))
    
    classificacao_ecommerce: Mapped[str] = mapped_column(VARCHAR(255))
    
    ecommerce: Mapped[str] = mapped_column(VARCHAR(50))
    
    origem_cst: Mapped[int] = mapped_column(INTEGER)
    
    obs_fiscal: Mapped[str] = mapped_column(VARCHAR(255))
    
    codigo_tiss_criado: Mapped[int] = mapped_column(INTEGER)
    
    preco_fabrica: Mapped[float] = mapped_column(FLOAT)
    
    flag_ecommerce: Mapped[int] = mapped_column(INTEGER)
    
    ult_desconto_febrafar: Mapped[float] = mapped_column(FLOAT)
    
    ult_desconto_objectpro: Mapped[float] = mapped_column(FLOAT)
    
    ult_desconto_linkedfarma: Mapped[float] = mapped_column(FLOAT)
    
    qtd_apresentacao: Mapped[float] = mapped_column(FLOAT)
    
    ult_desconto_epharma: Mapped[float] = mapped_column(FLOAT)
    
    ult_desconto_vidalink: Mapped[float] = mapped_column(FLOAT)
    
    ult_desconto_orizon: Mapped[float] = mapped_column(FLOAT)
    
    ult_desconto_portal_drogaria: Mapped[float] = mapped_column(FLOAT)
    
    ult_desconto_funcional_card: Mapped[float] = mapped_column(FLOAT)
    
    ult_desconto_global_saude: Mapped[float] = mapped_column(FLOAT)
    
    fc_v8: Mapped[int] = mapped_column(INTEGER)
    
    peso: Mapped[float] = mapped_column(FLOAT)
    
    largura: Mapped[float] = mapped_column(FLOAT)
    
    altura: Mapped[float] = mapped_column(FLOAT)
    
    profundidade: Mapped[float] = mapped_column(FLOAT)
    
    id_ficha: Mapped[str] = mapped_column(VARCHAR(50))
    
    codigo_integracoes: Mapped[str] = mapped_column(VARCHAR(50))
    
    pmpf: Mapped[float] = mapped_column(FLOAT)
    
    pmpf_percentual_aprazo: Mapped[float] = mapped_column(FLOAT)
    
    princativo_hos: Mapped[str] = mapped_column(VARCHAR(255))
    
    prc_farmacia_popular_bf: Mapped[float] = mapped_column(FLOAT)
    
    etqprod_id: Mapped[str] = mapped_column(VARCHAR(50))
    
    codigo_integracoes_kits: Mapped[str] = mapped_column(VARCHAR(50))
    
    cod_classificacao_preco: Mapped[int] = mapped_column(INTEGER)
    
    custo_contabil_rede: Mapped[float] = mapped_column(FLOAT)
    
    estoque_dia_anterior_rede: Mapped[float] = mapped_column(FLOAT)
    
    curva_rede: Mapped[str] = mapped_column(VARCHAR(50))
    
    peso_bruto: Mapped[float] = mapped_column(FLOAT)
    
    descricao_curta_bling: Mapped[str] = mapped_column(VARCHAR(255))
    
    img_bling_local: Mapped[int] = mapped_column(INTEGER)
    
    ult_desconto_ellomais: Mapped[float] = mapped_column(FLOAT)
    
    segmento: Mapped[int] = mapped_column(INTEGER)
    
    dt_alt: Mapped[datetime.datetime] = mapped_column(TIMESTAMP)
    
    piscofins_old: Mapped[str] = mapped_column(VARCHAR(50))
    
    preco_unificado: Mapped[int] = mapped_column(INTEGER)
    
    preco_ecommerce: Mapped[float] = mapped_column(FLOAT)
    
    custo_contabil_rede_anterior: Mapped[float] = mapped_column(FLOAT)

class Convenio(Base): 
    """
    Modelo para a tabela que armazena dados de convenios.
    """
    __tablename__ = "convenio"

    codigo: Mapped[float] = mapped_column(FLOAT, primary_key=True)
    
    nome: Mapped[str] = mapped_column(VARCHAR(255))
    
    endereco: Mapped[str] = mapped_column(VARCHAR(255))
    
    bairro: Mapped[str] = mapped_column(VARCHAR(255))
    
    cidade: Mapped[str] = mapped_column(VARCHAR(255))
    
    uf: Mapped[str] = mapped_column(VARCHAR(2))
    
    cep: Mapped[str] = mapped_column(VARCHAR(10))
    
    ddd: Mapped[str] = mapped_column(VARCHAR(5))
    
    telefone: Mapped[str] = mapped_column(VARCHAR(20))
    
    dddfax: Mapped[str] = mapped_column(VARCHAR(5))
    
    fax: Mapped[str] = mapped_column(VARCHAR(20))
    
    ramal: Mapped[float] = mapped_column(FLOAT)
    
    cgc: Mapped[str] = mapped_column(VARCHAR(20))
    
    insc: Mapped[str] = mapped_column(VARCHAR(20))
    
    contato: Mapped[str] = mapped_column(VARCHAR(100))
    
    vencimento: Mapped[float] = mapped_column(FLOAT)
    
    prazo: Mapped[float] = mapped_column(FLOAT)
    
    condicao: Mapped[str] = mapped_column(VARCHAR(50))
    
    obs: Mapped[str] = mapped_column(VARCHAR(255))
    
    maximo: Mapped[float] = mapped_column(FLOAT)
    
    em_nome: Mapped[str] = mapped_column(VARCHAR(255))
    
    desconto: Mapped[float] = mapped_column(FLOAT)
    
    block: Mapped[str] = mapped_column(VARCHAR(10))
    
    desc_venda: Mapped[str] = mapped_column(VARCHAR(255))
    
    contribuicao: Mapped[float] = mapped_column(FLOAT)
    
    textoreconhece: Mapped[str] = mapped_column(VARCHAR(255))
    
    receita: Mapped[str] = mapped_column(VARCHAR(255))
    
    filial: Mapped[float] = mapped_column(FLOAT)
    
    itensreconhece: Mapped[str] = mapped_column(VARCHAR(255))
    
    plano: Mapped[float] = mapped_column(FLOAT)
    
    empresa: Mapped[float] = mapped_column(FLOAT)
    
    fechamento: Mapped[float] = mapped_column(FLOAT)
    
    venc_a_cada: Mapped[float] = mapped_column(FLOAT)
    
    obriga_cad_func: Mapped[str] = mapped_column(VARCHAR(10))
    
    senhas: Mapped[str] = mapped_column(VARCHAR(255))
    
    dividirlimite: Mapped[str] = mapped_column(VARCHAR(10))
    
    limiteporcliente: Mapped[str] = mapped_column(VARCHAR(10))
    
    dia_fechamento: Mapped[int] = mapped_column(INTEGER)
    
    status: Mapped[str] = mapped_column(VARCHAR(50))
    
    grupo: Mapped[str] = mapped_column(VARCHAR(100))
    
    grupos_produtos: Mapped[str] = mapped_column(VARCHAR(255))
    
    modalidade: Mapped[str] = mapped_column(VARCHAR(50))
    
    fantasia: Mapped[str] = mapped_column(VARCHAR(255))
    
    insc_municipal: Mapped[str] = mapped_column(VARCHAR(50))
    
    caixa_postal: Mapped[str] = mapped_column(VARCHAR(50))
    
    dt_cadastro: Mapped[datetime.date] = mapped_column(DATE)
    
    forma_compra: Mapped[str] = mapped_column(VARCHAR(50))
    
    entrega_fatura: Mapped[str] = mapped_column(VARCHAR(50))
    
    consultor: Mapped[float] = mapped_column(FLOAT)
    
    cobranca: Mapped[str] = mapped_column(VARCHAR(50))
    
    desconto_manip: Mapped[float] = mapped_column(FLOAT)
    
    debito_convenio: Mapped[float] = mapped_column(FLOAT)
    
    relatorio_tipo: Mapped[str] = mapped_column(VARCHAR(50))
    
    relatorio_ordem: Mapped[str] = mapped_column(VARCHAR(50))
    
    relatorio_itens: Mapped[str] = mapped_column(VARCHAR(255))
    
    senha: Mapped[str] = mapped_column(VARCHAR(50))
    
    desconto_fatura: Mapped[float] = mapped_column(FLOAT)
    
    icms: Mapped[str] = mapped_column(VARCHAR(50))
    
    end_corresp: Mapped[str] = mapped_column(VARCHAR(255))
    
    bairro_corresp: Mapped[str] = mapped_column(VARCHAR(255))
    
    cidade_corresp: Mapped[str] = mapped_column(VARCHAR(255))
    
    cep_corresp: Mapped[str] = mapped_column(VARCHAR(10))
    
    uf_corresp: Mapped[str] = mapped_column(VARCHAR(2))
    
    telefone_corresp: Mapped[str] = mapped_column(VARCHAR(20))
    
    fax_corresp: Mapped[str] = mapped_column(VARCHAR(20))
    
    email: Mapped[str] = mapped_column(VARCHAR(255))
    
    classifi_produtos: Mapped[str] = mapped_column(VARCHAR(255))
    
    maximo_parcelas: Mapped[float] = mapped_column(FLOAT)
    
    vlr_min_parcela: Mapped[float] = mapped_column(FLOAT)
    
    vlr_min_parcelas: Mapped[float] = mapped_column(FLOAT)
    
    recarga_celular: Mapped[str] = mapped_column(VARCHAR(50))
    
    desconto_fecha_fatura: Mapped[float] = mapped_column(FLOAT)
    
    obrigar_autorizacao: Mapped[str] = mapped_column(VARCHAR(10))
    
    fin_class_contabil: Mapped[str] = mapped_column(VARCHAR(50))
    
    desconto_em_folha: Mapped[str] = mapped_column(VARCHAR(10))
    
    desc_progres: Mapped[str] = mapped_column(VARCHAR(255))
    
    n_faturas: Mapped[float] = mapped_column(FLOAT)
    
    desc_especial: Mapped[str] = mapped_column(VARCHAR(255))
    
    desconto_avista: Mapped[float] = mapped_column(FLOAT)
    
    conta_contabil: Mapped[str] = mapped_column(VARCHAR(50))
    
    merchcard_codigo: Mapped[float] = mapped_column(FLOAT)
    
    merchcard_descricao: Mapped[str] = mapped_column(VARCHAR(255))
    
    logradouro_id: Mapped[float] = mapped_column(FLOAT)
    
    compl_logradouro: Mapped[str] = mapped_column(VARCHAR(255))
    
    merchcard_convenio_auxiliar: Mapped[str] = mapped_column(VARCHAR(255))
    
    carencia_fechamento: Mapped[float] = mapped_column(FLOAT)
    
    ult_alteracao: Mapped[datetime.datetime] = mapped_column(TIMESTAMP)
    
    alerta: Mapped[str] = mapped_column(VARCHAR(255))
    
    num_end: Mapped[str] = mapped_column(VARCHAR(20))
    
    integracao_webservice: Mapped[str] = mapped_column(VARCHAR(255))
    
    multi_fechamento: Mapped[str] = mapped_column(VARCHAR(10))
    
    contribuicao_dependente: Mapped[float] = mapped_column(FLOAT)
    
    tabela_desconto: Mapped[float] = mapped_column(FLOAT)
    
    desc_progress: Mapped[str] = mapped_column(VARCHAR(255))
    
    flag_ecommerce: Mapped[int] = mapped_column(INTEGER)
    
    fecha_convenio: Mapped[str] = mapped_column(VARCHAR(10))
    
    dt_alt: Mapped[datetime.datetime] = mapped_column(TIMESTAMP)
    
    webservice_chave_api: Mapped[str] = mapped_column(VARCHAR(255))
    
    webservice_senha: Mapped[str] = mapped_column(VARCHAR(255))
    
    webservice_url: Mapped[str] = mapped_column(VARCHAR(255))
    
    webservice_usuario: Mapped[str] = mapped_column(VARCHAR(255))

class Empresa(Base): 
    """
    Modelo para a tabela que armazena dados de empresas.
    """
    __tablename__ = "empresa"

    codigo: Mapped[float] = mapped_column(FLOAT, primary_key=True)
    
    nome: Mapped[str] = mapped_column(VARCHAR(255))
    
    endereco: Mapped[str] = mapped_column(VARCHAR(255))
    
    bairro: Mapped[str] = mapped_column(VARCHAR(255))
    
    cidade: Mapped[str] = mapped_column(VARCHAR(255))
    
    uf: Mapped[str] = mapped_column(VARCHAR(2))
    
    cep: Mapped[str] = mapped_column(VARCHAR(10))
    
    ddd: Mapped[str] = mapped_column(VARCHAR(5))
    
    telefone: Mapped[str] = mapped_column(VARCHAR(20))
    
    cgc: Mapped[str] = mapped_column(VARCHAR(20))
    
    insc: Mapped[str] = mapped_column(VARCHAR(20))
    
    fantasia: Mapped[str] = mapped_column(VARCHAR(255))
    
    minimo: Mapped[float] = mapped_column(FLOAT)
    
    desconto: Mapped[float] = mapped_column(FLOAT)
    
    mensagem: Mapped[str] = mapped_column(VARCHAR(255))
    
    tipo: Mapped[str] = mapped_column(VARCHAR(50))
    
    licenca: Mapped[str] = mapped_column(VARCHAR(50))
    
    farmaceutico: Mapped[str] = mapped_column(VARCHAR(255))
    
    crf: Mapped[str] = mapped_column(VARCHAR(50))
    
    licencafederal: Mapped[float] = mapped_column(FLOAT)
    
    regiao: Mapped[str] = mapped_column(VARCHAR(50))
    
    ims: Mapped[str] = mapped_column(VARCHAR(50))
    
    site: Mapped[str] = mapped_column(VARCHAR(255))
    
    email: Mapped[str] = mapped_column(VARCHAR(255))
    
    compl_logradouro: Mapped[str] = mapped_column(VARCHAR(255))
    
    nr_logradouro: Mapped[str] = mapped_column(VARCHAR(20))
    
    logradouro: Mapped[str] = mapped_column(VARCHAR(255))
    
    tp_logradouro: Mapped[str] = mapped_column(VARCHAR(50))
    
    fax: Mapped[str] = mapped_column(VARCHAR(20))
    
    estab_viacard: Mapped[str] = mapped_column(VARCHAR(50))
    
    usuario_viacard: Mapped[str] = mapped_column(VARCHAR(50))
    
    senha_viacard: Mapped[str] = mapped_column(VARCHAR(50))
    
    ip_server: Mapped[str] = mapped_column(VARCHAR(50))
    
    source: Mapped[str] = mapped_column(VARCHAR(50))
    
    blocodecodigo: Mapped[str] = mapped_column(VARCHAR(50))
    
    licenca_controlado: Mapped[str] = mapped_column(VARCHAR(50))
    
    cpf_farmaceutico: Mapped[str] = mapped_column(VARCHAR(14))
    
    enquadramentoestadual: Mapped[str] = mapped_column(VARCHAR(50))
    
    enquadramentofederal: Mapped[str] = mapped_column(VARCHAR(50))
    
    despesafixa: Mapped[float] = mapped_column(FLOAT)
    
    despesavariavel: Mapped[float] = mapped_column(FLOAT)
    
    status: Mapped[str] = mapped_column(VARCHAR(50))
    
    numero: Mapped[float] = mapped_column(FLOAT)
    
    complemento: Mapped[str] = mapped_column(VARCHAR(255))
    
    cnae_fiscal: Mapped[str] = mapped_column(VARCHAR(50))
    
    ie_subst_trib: Mapped[str] = mapped_column(VARCHAR(50))
    
    insc_m: Mapped[str] = mapped_column(VARCHAR(50))
    
    insc_suframa: Mapped[str] = mapped_column(VARCHAR(50))
    
    nome_cont: Mapped[str] = mapped_column(VARCHAR(255))
    
    cpf_cont: Mapped[str] = mapped_column(VARCHAR(14))
    
    crc_cont: Mapped[str] = mapped_column(VARCHAR(50))
    
    cnpj_cont: Mapped[str] = mapped_column(VARCHAR(20))
    
    cep_cont: Mapped[str] = mapped_column(VARCHAR(10))
    
    uf_cont: Mapped[str] = mapped_column(VARCHAR(2))
    
    mun_cont: Mapped[str] = mapped_column(VARCHAR(50))
    
    end_cont: Mapped[str] = mapped_column(VARCHAR(255))
    
    nr_cont: Mapped[str] = mapped_column(VARCHAR(20))
    
    compl_cont: Mapped[str] = mapped_column(VARCHAR(255))
    
    bairro_cont: Mapped[str] = mapped_column(VARCHAR(255))
    
    ddd_cont: Mapped[str] = mapped_column(VARCHAR(5))
    
    fone_cont: Mapped[str] = mapped_column(VARCHAR(20))
    
    fax_cont: Mapped[str] = mapped_column(VARCHAR(20))
    
    email_cont: Mapped[str] = mapped_column(VARCHAR(255))
    
    cpfcontador: Mapped[str] = mapped_column(VARCHAR(14))
    
    cpfresp: Mapped[str] = mapped_column(VARCHAR(14))
    
    crccontador: Mapped[str] = mapped_column(VARCHAR(50))
    
    datajunta: Mapped[str] = mapped_column(VARCHAR(50))
    
    funcaoresp: Mapped[str] = mapped_column(VARCHAR(50))
    
    inscmunicipal: Mapped[str] = mapped_column(VARCHAR(50))
    
    nomecontador: Mapped[str] = mapped_column(VARCHAR(255))
    
    nomeresp: Mapped[str] = mapped_column(VARCHAR(255))
    
    regjunta: Mapped[str] = mapped_column(VARCHAR(50))
    
    irpj: Mapped[float] = mapped_column(FLOAT)
    
    cssl: Mapped[float] = mapped_column(FLOAT)
    
    codigo_radar: Mapped[float] = mapped_column(FLOAT)
    
    logradouro_id: Mapped[float] = mapped_column(FLOAT)
    
    apuracao_credito: Mapped[str] = mapped_column(VARCHAR(50))
    
    regime_apuracao: Mapped[str] = mapped_column(VARCHAR(50))
    
    closeup_rede: Mapped[float] = mapped_column(FLOAT)
    
    closeup_filial: Mapped[float] = mapped_column(FLOAT)
    
    dia_vencimento_obrigacao: Mapped[int] = mapped_column(INTEGER)
    
    cod_rec_obrigacao: Mapped[str] = mapped_column(VARCHAR(50))
    
    cert_negativa_debitos: Mapped[float] = mapped_column(FLOAT)
    
    cod_rec_previdencia: Mapped[str] = mapped_column(VARCHAR(50))
    
    sublimite_sn: Mapped[int] = mapped_column(INTEGER)
    
    cod_rec_pis: Mapped[str] = mapped_column(VARCHAR(50))
    
    cod_rec_cofins: Mapped[str] = mapped_column(VARCHAR(50))
    
    diferenca_maxima: Mapped[float] = mapped_column(FLOAT)
    
    sat_assinatura: Mapped[str] = mapped_column(VARCHAR(255))
    
    ip_capturareceita: Mapped[str] = mapped_column(VARCHAR(50))
    
    aliquota_sn: Mapped[float] = mapped_column(FLOAT)
    
    senha_vendas_cscl: Mapped[str] = mapped_column(VARCHAR(50))
    
    codigo_tiss: Mapped[str] = mapped_column(VARCHAR(50))
    
    cnes: Mapped[str] = mapped_column(VARCHAR(50))
    
    hash_origem: Mapped[int] = mapped_column(INTEGER)
    
    hash_atual: Mapped[int] = mapped_column(INTEGER)
    
    empresa_vinculada: Mapped[float] = mapped_column(FLOAT)
    
    flag_ecommerce: Mapped[int] = mapped_column(INTEGER)
    
    chave_pix: Mapped[str] = mapped_column(VARCHAR(255))
    
    cidade_pix: Mapped[str] = mapped_column(VARCHAR(255))
    
    lgpd_token: Mapped[str] = mapped_column(VARCHAR(255))
    
    id_ifood: Mapped[str] = mapped_column(VARCHAR(255))
    
    rg_farmaceutico: Mapped[str] = mapped_column(VARCHAR(20))
    
    licenca_civil: Mapped[str] = mapped_column(VARCHAR(50))
    
    ult_alteracao: Mapped[datetime.datetime] = mapped_column(TIMESTAMP)
    
    lat: Mapped[float] = mapped_column(FLOAT)
    
    lng: Mapped[float] = mapped_column(FLOAT)
    
    crm: Mapped[int] = mapped_column(INTEGER)
    
    crf_formula: Mapped[str] = mapped_column(VARCHAR(50))
    
    cpf_farmaceutico_formula: Mapped[str] = mapped_column(VARCHAR(14))
    
    farmaceutico_formula: Mapped[str] = mapped_column(VARCHAR(255))
    
    rg_farmaceutico_formula: Mapped[str] = mapped_column(VARCHAR(20))
    
    tema_sistema: Mapped[int] = mapped_column(INTEGER)
    
    cadastra_produto: Mapped[str] = mapped_column(VARCHAR(50))
    
    cadastra_fornecedor: Mapped[str] = mapped_column(VARCHAR(50))
    
    api_key_financeiro: Mapped[str] = mapped_column(VARCHAR(255))
    
    ip_servidor_mb: Mapped[str] = mapped_column(VARCHAR(50))
    
    cod_farmaceutico: Mapped[int] = mapped_column(INTEGER)
    
    cod_farmaceutico_subst: Mapped[int] = mapped_column(INTEGER)
    
    cod_farmaceutico_formula: Mapped[int] = mapped_column(INTEGER)
    
    cod_farmaceutico_formula_subst: Mapped[int] = mapped_column(INTEGER)
    
    licenca_mapa: Mapped[str] = mapped_column(VARCHAR(50))
    
    unico_contato_msg_auto: Mapped[int] = mapped_column(INTEGER)
    
    data_abertura: Mapped[datetime.date] = mapped_column(DATE)
    
    hora_abertura: Mapped[datetime.time] = mapped_column(TIME)
    
    hora_fechamento: Mapped[datetime.time] = mapped_column(TIME)
    
    max_parcela_crediario: Mapped[int] = mapped_column(INTEGER)
    
    max_parcela_convenio: Mapped[int] = mapped_column(INTEGER)
    
    cod_cdl_associado: Mapped[int] = mapped_column(INTEGER)
    
    entrada_automatica_nfe: Mapped[str] = mapped_column(VARCHAR(50))

class Fornece(Base):
    """
    Modelo para a tabela que armazena dados de fornecedores.
    """
    __tablename__ = "fornece"

    codigo: Mapped[float] = mapped_column(FLOAT, primary_key=True)
    
    nome: Mapped[str] = mapped_column(VARCHAR(255))
    
    endereco: Mapped[str] = mapped_column(VARCHAR(255))
    
    bairro: Mapped[str] = mapped_column(VARCHAR(255))
    
    cidade: Mapped[str] = mapped_column(VARCHAR(255))
    
    uf: Mapped[str] = mapped_column(VARCHAR(2))
    
    cep: Mapped[str] = mapped_column(VARCHAR(10))
    
    ddd: Mapped[str] = mapped_column(VARCHAR(5))
    
    telefone: Mapped[str] = mapped_column(VARCHAR(20))
    
    cgc: Mapped[str] = mapped_column(VARCHAR(20))
    
    insc: Mapped[str] = mapped_column(VARCHAR(20))
    
    fantasia: Mapped[str] = mapped_column(VARCHAR(255))
    
    minimo: Mapped[float] = mapped_column(FLOAT)
    
    desconto: Mapped[float] = mapped_column(FLOAT)
    
    mensagem: Mapped[str] = mapped_column(VARCHAR(255))
    
    tipo: Mapped[str] = mapped_column(VARCHAR(50))
    
    licenca: Mapped[str] = mapped_column(VARCHAR(50))
    
    farmaceutico: Mapped[str] = mapped_column(VARCHAR(255))
    
    crf: Mapped[str] = mapped_column(VARCHAR(50))
    
    licencafederal: Mapped[float] = mapped_column(FLOAT)
    
    regiao: Mapped[str] = mapped_column(VARCHAR(50))
    
    ims: Mapped[str] = mapped_column(VARCHAR(50))
    
    site: Mapped[str] = mapped_column(VARCHAR(255))
    
    email: Mapped[str] = mapped_column(VARCHAR(255))
    
    compl_logradouro: Mapped[str] = mapped_column(VARCHAR(255))
    
    nr_logradouro: Mapped[str] = mapped_column(VARCHAR(20))
    
    logradouro: Mapped[str] = mapped_column(VARCHAR(255))
    
    tp_logradouro: Mapped[str] = mapped_column(VARCHAR(50))
    
    fax: Mapped[str] = mapped_column(VARCHAR(20))
    
    estab_viacard: Mapped[str] = mapped_column(VARCHAR(50))
    
    usuario_viacard: Mapped[str] = mapped_column(VARCHAR(50))
    
    senha_viacard: Mapped[str] = mapped_column(VARCHAR(50))
    
    ip_server: Mapped[str] = mapped_column(VARCHAR(50))
    
    source: Mapped[str] = mapped_column(VARCHAR(50))
    
    blocodecodigo: Mapped[str] = mapped_column(VARCHAR(50))
    
    licenca_controlado: Mapped[str] = mapped_column(VARCHAR(50))
    
    cpf_farmaceutico: Mapped[str] = mapped_column(VARCHAR(14))
    
    enquadramentoestadual: Mapped[str] = mapped_column(VARCHAR(50))
    
    enquadramentofederal: Mapped[str] = mapped_column(VARCHAR(50))
    
    despesafixa: Mapped[float] = mapped_column(FLOAT)
    
    despesavariavel: Mapped[float] = mapped_column(FLOAT)
    
    status: Mapped[str] = mapped_column(VARCHAR(50))
    
    numero: Mapped[float] = mapped_column(FLOAT)
    
    complemento: Mapped[str] = mapped_column(VARCHAR(255))
    
    cnae_fiscal: Mapped[str] = mapped_column(VARCHAR(50))
    
    ie_subst_trib: Mapped[str] = mapped_column(VARCHAR(50))
    
    insc_m: Mapped[str] = mapped_column(VARCHAR(50))
    
    insc_suframa: Mapped[str] = mapped_column(VARCHAR(50))
    
    nome_cont: Mapped[str] = mapped_column(VARCHAR(255))
    
    cpf_cont: Mapped[str] = mapped_column(VARCHAR(14))
    
    crc_cont: Mapped[str] = mapped_column(VARCHAR(50))
    
    cnpj_cont: Mapped[str] = mapped_column(VARCHAR(20))
    
    cep_cont: Mapped[str] = mapped_column(VARCHAR(10))
    
    uf_cont: Mapped[str] = mapped_column(VARCHAR(2))
    
    mun_cont: Mapped[str] = mapped_column(VARCHAR(50))
    
    end_cont: Mapped[str] = mapped_column(VARCHAR(255))
    
    nr_cont: Mapped[str] = mapped_column(VARCHAR(20))
    
    compl_cont: Mapped[str] = mapped_column(VARCHAR(255))
    
    bairro_cont: Mapped[str] = mapped_column(VARCHAR(255))
    
    ddd_cont: Mapped[str] = mapped_column(VARCHAR(5))
    
    fone_cont: Mapped[str] = mapped_column(VARCHAR(20))
    
    fax_cont: Mapped[str] = mapped_column(VARCHAR(20))
    
    email_cont: Mapped[str] = mapped_column(VARCHAR(255))
    
    cpfcontador: Mapped[str] = mapped_column(VARCHAR(14))
    
    cpfresp: Mapped[str] = mapped_column(VARCHAR(14))
    
    crccontador: Mapped[str] = mapped_column(VARCHAR(50))
    
    datajunta: Mapped[str] = mapped_column(VARCHAR(50))
    
    funcaoresp: Mapped[str] = mapped_column(VARCHAR(50))
    
    inscmunicipal: Mapped[str] = mapped_column(VARCHAR(50))
    
    nomecontador: Mapped[str] = mapped_column(VARCHAR(255))
    
    nomeresp: Mapped[str] = mapped_column(VARCHAR(255))
    
    regjunta: Mapped[str] = mapped_column(VARCHAR(50))
    
    irpj: Mapped[float] = mapped_column(FLOAT)
    
    cssl: Mapped[float] = mapped_column(FLOAT)
    
    codigo_radar: Mapped[float] = mapped_column(FLOAT)
    
    logradouro_id: Mapped[float] = mapped_column(FLOAT)
    
    apuracao_credito: Mapped[str] = mapped_column(VARCHAR(50))
    
    regime_apuracao: Mapped[str] = mapped_column(VARCHAR(50))
    
    closeup_rede: Mapped[float] = mapped_column(FLOAT)
    
    closeup_filial: Mapped[float] = mapped_column(FLOAT)
    
    dia_vencimento_obrigacao: Mapped[int] = mapped_column(INTEGER)
    
    cod_rec_obrigacao: Mapped[str] = mapped_column(VARCHAR(50))
    
    cert_negativa_debitos: Mapped[float] = mapped_column(FLOAT)
    
    cod_rec_previdencia: Mapped[str] = mapped_column(VARCHAR(50))
    
    sublimite_sn: Mapped[int] = mapped_column(INTEGER)
    
    cod_rec_pis: Mapped[str] = mapped_column(VARCHAR(50))
    
    cod_rec_cofins: Mapped[str] = mapped_column(VARCHAR(50))
    
    diferenca_maxima: Mapped[float] = mapped_column(FLOAT)
    
    sat_assinatura: Mapped[str] = mapped_column(VARCHAR(255))
    
    ip_capturareceita: Mapped[str] = mapped_column(VARCHAR(50))
    
    aliquota_sn: Mapped[float] = mapped_column(FLOAT)
    
    senha_vendas_cscl: Mapped[str] = mapped_column(VARCHAR(50))
    
    codigo_tiss: Mapped[str] = mapped_column(VARCHAR(50))
    
    cnes: Mapped[str] = mapped_column(VARCHAR(50))
    
    hash_origem: Mapped[int] = mapped_column(INTEGER)
    
    hash_atual: Mapped[int] = mapped_column(INTEGER)
    
    empresa_vinculada: Mapped[float] = mapped_column(FLOAT)
    
    flag_ecommerce: Mapped[int] = mapped_column(INTEGER)
    
    chave_pix: Mapped[str] = mapped_column(VARCHAR(255))
    
    cidade_pix: Mapped[str] = mapped_column(VARCHAR(255))
    
    lgpd_token: Mapped[str] = mapped_column(VARCHAR(255))
    
    id_ifood: Mapped[str] = mapped_column(VARCHAR(255))
    
    rg_farmaceutico: Mapped[str] = mapped_column(VARCHAR(20))
    
    licenca_civil: Mapped[str] = mapped_column(VARCHAR(50))
    
    ult_alteracao: Mapped[datetime.datetime] = mapped_column(TIMESTAMP)
    
    lat: Mapped[float] = mapped_column(FLOAT)
    
    lng: Mapped[float] = mapped_column(FLOAT)
    
    crm: Mapped[int] = mapped_column(INTEGER)
    
    crf_formula: Mapped[str] = mapped_column(VARCHAR(50))
    
    cpf_farmaceutico_formula: Mapped[str] = mapped_column(VARCHAR(14))
    
    farmaceutico_formula: Mapped[str] = mapped_column(VARCHAR(255))
    
    rg_farmaceutico_formula: Mapped[str] = mapped_column(VARCHAR(20))
    
    tema_sistema: Mapped[int] = mapped_column(INTEGER)
    
    cadastra_produto: Mapped[str] = mapped_column(VARCHAR(50))
    
    cadastra_fornecedor: Mapped[str] = mapped_column(VARCHAR(50))
    
    api_key_financeiro: Mapped[str] = mapped_column(VARCHAR(255))
    
    ip_servidor_mb: Mapped[str] = mapped_column(VARCHAR(50))
    
    cod_farmaceutico: Mapped[int] = mapped_column(INTEGER)
    
    cod_farmaceutico_subst: Mapped[int] = mapped_column(INTEGER)
    
    cod_farmaceutico_formula: Mapped[int] = mapped_column(INTEGER)
    
    cod_farmaceutico_formula_subst: Mapped[int] = mapped_column(INTEGER)
    
    licenca_mapa: Mapped[str] = mapped_column(VARCHAR(50))
    
    unico_contato_msg_auto: Mapped[int] = mapped_column(INTEGER)
    
    data_abertura: Mapped[datetime.date] = mapped_column(DATE)
    
    hora_abertura: Mapped[datetime.time] = mapped_column(TIME)
    
    hora_fechamento: Mapped[datetime.time] = mapped_column(TIME)
    
    max_parcela_crediario: Mapped[int] = mapped_column(INTEGER)
    
    max_parcela_convenio: Mapped[int] = mapped_column(INTEGER)
    
    cod_cdl_associado: Mapped[int] = mapped_column(INTEGER)
    
    entrada_automatica_nfe: Mapped[str] = mapped_column(VARCHAR(255))

class Funciona(Base):
    """
    Modelo para a tabela que armazena dados de funcionários.
    """
    __tablename__ = "funciona"

    codigo: Mapped[float] = mapped_column(FLOAT, primary_key=True)
    
    nome: Mapped[str] = mapped_column(VARCHAR(255))
    
    cpf: Mapped[str] = mapped_column(VARCHAR(14))
    
    data_nasc: Mapped[datetime.date] = mapped_column(DATE)
    
    paterna: Mapped[str] = mapped_column(VARCHAR(255))
    
    materna: Mapped[str] = mapped_column(VARCHAR(255))
    
    endereco: Mapped[str] = mapped_column(VARCHAR(255))
    
    bairro: Mapped[str] = mapped_column(VARCHAR(255))
    
    cidade: Mapped[str] = mapped_column(VARCHAR(255))
    
    uf: Mapped[str] = mapped_column(VARCHAR(2))
    
    cep: Mapped[str] = mapped_column(VARCHAR(10))
    
    ddd: Mapped[str] = mapped_column(VARCHAR(5))
    
    telefone: Mapped[str] = mapped_column(VARCHAR(20))
    
    admissao: Mapped[datetime.date] = mapped_column(DATE)
    
    carteira: Mapped[float] = mapped_column(FLOAT)
    
    serie: Mapped[str] = mapped_column(VARCHAR(50))
    
    escolar: Mapped[str] = mapped_column(VARCHAR(100))
    
    salario: Mapped[float] = mapped_column(FLOAT)
    
    comissao: Mapped[float] = mapped_column(FLOAT)
    
    senha: Mapped[str] = mapped_column(VARCHAR(50))
    
    nivel: Mapped[str] = mapped_column(VARCHAR(50))
    
    obs: Mapped[str] = mapped_column(VARCHAR(255))
    
    funcao: Mapped[str] = mapped_column(VARCHAR(100))
    
    pagamento: Mapped[str] = mapped_column(VARCHAR(50))
    
    entrada: Mapped[datetime.date] = mapped_column(DATE)
    
    saida: Mapped[datetime.date] = mapped_column(DATE)
    
    interinicio: Mapped[datetime.date] = mapped_column(DATE)
    
    interfim: Mapped[datetime.date] = mapped_column(DATE)
    
    tolerancia: Mapped[int] = mapped_column(INTEGER)
    
    status: Mapped[str] = mapped_column(VARCHAR(50))
    
    e_mail: Mapped[str] = mapped_column(VARCHAR(255))
    
    fax: Mapped[str] = mapped_column(VARCHAR(20))
    
    apelido: Mapped[str] = mapped_column(VARCHAR(50))
    
    usuario_fp: Mapped[str] = mapped_column(VARCHAR(50))
    
    senha_fp: Mapped[str] = mapped_column(VARCHAR(50))
    
    ult_alteracao: Mapped[datetime.datetime] = mapped_column(TIMESTAMP)
    
    data_senha_alterada: Mapped[datetime.date] = mapped_column(DATE)
    
    entregador: Mapped[str] = mapped_column(VARCHAR(50))
    
    rg: Mapped[str] = mapped_column(VARCHAR(20))
    
    gestor: Mapped[str] = mapped_column(VARCHAR(50))
    
    cod_gestor: Mapped[float] = mapped_column(FLOAT)
    
    cod_substituto: Mapped[float] = mapped_column(FLOAT)
    
    ativa_substituto: Mapped[str] = mapped_column(VARCHAR(10))
    
    cod_funcao: Mapped[float] = mapped_column(FLOAT)
    
    celular: Mapped[str] = mapped_column(VARCHAR(20))
    
    crf: Mapped[str] = mapped_column(VARCHAR(50))
    
    id_unico_contato: Mapped[int] = mapped_column(INTEGER)
    
    farmaceutico: Mapped[str] = mapped_column(VARCHAR(255))
    
    farmaceutico_assinatura: Mapped[bytes] = mapped_column()
    
    farmaceutico_rubrica: Mapped[bytes] = mapped_column()
    
    limite_adicional_crediario: Mapped[float] = mapped_column(FLOAT)
    
    limite_adicional_convenio: Mapped[float] = mapped_column(FLOAT)
    
    apikeyentregador: Mapped[str] = mapped_column(VARCHAR(255))

class Medico(Base):
    """
    Modelo para a tabela que armazena dados de médicos.
    """
    __tablename__ = "medico"

    codigo: Mapped[float] = mapped_column(FLOAT, primary_key=True)
    
    crm: Mapped[float] = mapped_column(FLOAT)
    
    nome: Mapped[str] = mapped_column(VARCHAR(255))
    
    endereco: Mapped[str] = mapped_column(VARCHAR(255))
    
    bairro: Mapped[str] = mapped_column(VARCHAR(255))
    
    cidade: Mapped[str] = mapped_column(VARCHAR(255))
    
    uf: Mapped[str] = mapped_column(VARCHAR(2))
    
    especial: Mapped[str] = mapped_column(VARCHAR(100))
    
    convenio: Mapped[str] = mapped_column(VARCHAR(100))
    
    cadastro: Mapped[datetime.date] = mapped_column(DATE)
    
    ddd: Mapped[str] = mapped_column(VARCHAR(5))
    
    telefone: Mapped[str] = mapped_column(VARCHAR(20))
    
    cep: Mapped[str] = mapped_column(VARCHAR(10))
    
    cpf: Mapped[str] = mapped_column(VARCHAR(14))
    
    celular: Mapped[str] = mapped_column(VARCHAR(20))
    
    obs: Mapped[str] = mapped_column(VARCHAR(255))
    
    data_nasc: Mapped[datetime.date] = mapped_column(DATE)
    
    especialidade: Mapped[str] = mapped_column(VARCHAR(100))
    
    status: Mapped[str] = mapped_column(VARCHAR(50))
    
    motivo_inativacao: Mapped[str] = mapped_column(VARCHAR(255))
    
    tipo: Mapped[str] = mapped_column(VARCHAR(50))
    
    uf_conselho: Mapped[str] = mapped_column(VARCHAR(2))
    
    consultor: Mapped[float] = mapped_column(FLOAT)
    
    logradouro_id: Mapped[float] = mapped_column(FLOAT)
    
    datacadastro: Mapped[datetime.date] = mapped_column(DATE)
    
    ult_alteracao: Mapped[datetime.datetime] = mapped_column(TIMESTAMP)
    
    medicina_chinesa: Mapped[str] = mapped_column(VARCHAR(255))
    
    rg: Mapped[str] = mapped_column(VARCHAR(20))
    
    endereco_comercial: Mapped[str] = mapped_column(VARCHAR(255))
    
    bairro_comercial: Mapped[str] = mapped_column(VARCHAR(255))
    
    cidade_comercial: Mapped[str] = mapped_column(VARCHAR(255))
    
    uf_comercial: Mapped[str] = mapped_column(VARCHAR(2))
    
    cep_comercial: Mapped[str] = mapped_column(VARCHAR(10))
    
    telefone_comercial: Mapped[str] = mapped_column(VARCHAR(20))
    
    celular_comercial: Mapped[str] = mapped_column(VARCHAR(20))
    
    idnextel_comercial: Mapped[str] = mapped_column(VARCHAR(50))
    
    email_comercial: Mapped[str] = mapped_column(VARCHAR(255))
    
    logradouro_id_comercial: Mapped[float] = mapped_column(FLOAT)
    
    desconto_om: Mapped[float] = mapped_column(FLOAT)
    
    cbos: Mapped[str] = mapped_column(VARCHAR(50))
    
    uni_crm: Mapped[float] = mapped_column(FLOAT)
    
    uni_nome: Mapped[str] = mapped_column(VARCHAR(255))
    
    clinica: Mapped[str] = mapped_column(VARCHAR(255))
    
    fc_v8: Mapped[int] = mapped_column(INTEGER)
    
    comissao_om: Mapped[float] = mapped_column(FLOAT)
    
    sipeagro: Mapped[str] = mapped_column(VARCHAR(255))

class Notificacoes(Base):
    """
    Modelo para a tabela que armazena dados de notificações.
    """
    __tablename__ = "notificacoes"

    id: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    
    mensagem: Mapped[str] = mapped_column(VARCHAR(255))
    
    operador: Mapped[int] = mapped_column(INTEGER)
    
    data_inclusao: Mapped[datetime.datetime] = mapped_column(TIMESTAMP)
    
    emissor: Mapped[int] = mapped_column(INTEGER)
    
    titulo: Mapped[str] = mapped_column(VARCHAR(255))
    
    data_inicio: Mapped[datetime.datetime] = mapped_column(TIMESTAMP)
    
    tipo: Mapped[int] = mapped_column(INTEGER)

class Representantes(Base):
    """
    Modelo para a tabela que armazena dados de representantes.
    """
    __tablename__ = "representantes"

    codigo: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    
    nome: Mapped[str] = mapped_column(VARCHAR(255))
    
    email: Mapped[str] = mapped_column(VARCHAR(255))
    
    telefone: Mapped[str] = mapped_column(VARCHAR(20))
    
    celular: Mapped[str] = mapped_column(VARCHAR(20))
    
    status: Mapped[str] = mapped_column(VARCHAR(50))

class Transportadora(Base):
    """
    Modelo para a tabela que armazena dados de transportadora.
    """
    __tablename__ = "transportadora"

    codigo: Mapped[float] = mapped_column(FLOAT, primary_key=True)
    
    nome: Mapped[str] = mapped_column(VARCHAR(255))
    
    endereco: Mapped[str] = mapped_column(VARCHAR(255))
    
    bairro: Mapped[str] = mapped_column(VARCHAR(255))
    
    cidade: Mapped[str] = mapped_column(VARCHAR(255))
    
    uf: Mapped[str] = mapped_column(VARCHAR(2))
    
    cnpj: Mapped[str] = mapped_column(VARCHAR(20))
    
    cep: Mapped[str] = mapped_column(VARCHAR(10))
    
    ddd: Mapped[float] = mapped_column(FLOAT)
    
    telefone: Mapped[str] = mapped_column(VARCHAR(20))
    
    insc_estadual: Mapped[str] = mapped_column(VARCHAR(50))
    
    status: Mapped[str] = mapped_column(VARCHAR(50))
    
    logradouro_id: Mapped[float] = mapped_column(FLOAT)
    
    datacadastro: Mapped[datetime.date] = mapped_column(DATE)
    
    ult_alteracao: Mapped[datetime.datetime] = mapped_column(TIMESTAMP)
    
    email: Mapped[str] = mapped_column(VARCHAR(255))