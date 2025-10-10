# 🤖 Projeto de Análise e Notificação de Erros

## 📝 Descrição

Este projeto é um sistema automatizado para monitoramento e análise de logs de integração de dados (BI). Ele utiliza a biblioteca **Drain3** para fazer o parsing de logs, identificar padrões de erro, classificar novas ocorrências e, em seguida, notificar os responsáveis por e-mail. A aplicação é orquestrada para garantir que os erros sejam detectados, processados e comunicados de forma eficiente.

O fluxo principal consiste em:
1.  **Buscar** por logs de erro em fontes de dados.
2.  **Analisar** os erros usando um serviço de análise para identificar a causa raiz.
3.  **Agrupar** erros semelhantes usando a técnica de fingerprinting do Drain3.
4.  **Armazenar** os resultados da análise em um banco de dados (MongoDB e/ou relacional).
5.  **Notificar** as equipes responsáveis por e-mail com os detalhes do erro.

---

## 📂 Estrutura do Projeto

O projeto está organizado nos seguintes diretórios para garantir uma clara separação de responsabilidades:

.
├── 📁classes/              # Classes principais e fábricas (factories)
├── 📁db/                   # Módulos de gerenciamento de banco de dados
├── 📁models/               # Modelos de dados (Pydantic, SQLAlchemy, etc.)
├── 📁services/             # Lógica de negócio e orquestração
├── 📁tools/                # Ferramentas e scripts auxiliares
├── .env                    # Arquivo de variáveis de ambiente (NÃO versionar)
├── .gitignore              # Arquivo para ignorar arquivos no Git
├── app.py                  # (Opcional) Ponto de entrada para um servidor web (Ex: FastAPI)
├── main.py                 # Ponto de entrada principal da aplicação
├── drain3.ini              # Arquivo de configuração do Drain3
├── drain3_state.json       # Estado salvo do Drain3 (templates de log)
├── README.md               # Documentação do projeto
└── requirements.txt        # Dependências do projeto


### Detalhamento dos Diretórios

* **`📁classes`**: Contém as classes principais do sistema.
    * `AgentFactory.py`: Fábrica para criar agentes ou serviços.
    * `Drain3.py`: Wrapper ou implementação customizada do log parser Drain3.
    * `Email.py`: Classe para construção e formatação de e-mails.
    * `TextFormatter.py`: Utilitários para formatação de texto.

* **`📁db`**: Módulos responsáveis pela comunicação com os bancos de dados.
    * `AlchemyManager.py`: Gerenciador de conexão para bancos de dados relacionais usando SQLAlchemy.
    * `MongoDbManager.py`: Gerenciador de conexão para o banco de dados NoSQL MongoDB.

* **`📁models`**: Define a estrutura dos dados utilizados na aplicação.
    * `DbModel/`: Modelos para retornos de queries.
    * `ErrorModel/`: Modelo que representa um erro analisado.
    * `FingerPrintModel/`: Modelo para os padrões (fingerprints) de log.
    * `Tables/`: Mapeamento das tabelas do banco de dados relacional (ex: `int_bi_vendas`).

* **`📁services`**: Onde reside a lógica de negócio da aplicação.
    * `bussines_logic/`: Contém os serviços que executam as regras de negócio.
        * `error_analysis_service.py`: Serviço principal que analisa os erros.
        * `orchestrator.py`: Orquestra o fluxo de execução dos outros serviços.
    * `presentation/`: Camada de apresentação, como notificações.
        * `email_notifier.py`: Serviço que envia os e-mails.
    * `search_errors/`: Serviço para buscar e coletar os logs de erro.
    * `update_registers/`: Serviço para atualizar registros no banco de dados.

* **`📁tools`**: Ferramentas auxiliares para tarefas específicas, como scripts de manipulação de dados.

---

## 🚀 Começando

Siga os passos abaixo para configurar e executar o projeto em seu ambiente local.

### Pré-requisitos

* **Python 3.10+**
* **Pip** (gerenciador de pacotes do Python)
* Acesso a um banco de dados **PostgreSQL** (ou outro relacional)
* Acesso a um banco de dados **MongoDB**

### Instalação

1.  **Clone o repositório:**
    ```sh
    git clone <URL_DO_SEU_REPOSITORIO>
    cd <NOME_DO_PROJETO>
    ```

2.  **Crie e ative um ambiente virtual:**
    ```sh
    # Windows
    python -m venv venv
    .\venv\Scripts\activate

    # Linux / macOS
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```sh
    pip install -r requirements.txt
    ```

4.  **Configure as variáveis de ambiente:**
    * Renomeie o arquivo `.env.example` para `.env` (se houver um example) ou crie um novo.
    * Preencha o arquivo `.env` com as credenciais necessárias:

    ```ini
    # Banco de Dados Relacional (PostgreSQL)
    DB_USER=seu_usuario
    DB_PASSWORD=sua_senha
    DB_HOST=localhost
    DB_PORT=5432
    DB_NAME=seu_banco

    # MongoDB
    MONGO_URI=mongodb://localhost:27017/
    MONGO_DB_NAME=seu_banco_mongo

    # Configurações de E-mail (SMTP)
    EMAIL_HOST=smtp.example.com
    EMAIL_PORT=587
    EMAIL_USER=seu_email@example.com
    EMAIL_PASSWORD=sua_senha
    ```

---

## ▶️ Uso

Para executar a aplicação, rode o script principal a partir da raiz do projeto:
sh
python main.py


## </> instruções de desenvolvimento

O sistema foi projetado para operar como um executável autônomo (.exe), iniciado por um serviço integrador. Sua função principal é monitorar filas de processamento de dados, identificar erros e executar de forma automatizada as ferramentas de correção adequadas para cada cenário.

Fluxo Operacional-------------------------------------------------------

O processo de automação segue as seguintes etapas:

Monitoramento Contínuo: O sistema observa ativamente as filas em busca de mensagens que indiquem erros operacionais.

Classificação de Ferramentas:

Ferramentas Padrão: Um conjunto de ferramentas base é executado em todas as instâncias para diagnósticos e manutenções gerais.

Ferramentas Personalizadas: Ferramentas específicas são acionadas dinamicamente com base no tipo de erro detectado.

Gerenciamento de Soluções com Banco Vetorial:

Para associar um erro à sua solução, o sistema utilizará um banco de dados vetorial.

Cada "template de erro" (descrição textual do problema) será convertido em um embedding (representação vetorial) e armazenado.

Associado a cada embedding, um metadado contendo um hash de erro será salvo. Este hash serve como um identificador que aponta para o conjunto de ferramentas personalizadas necessárias para solucionar aquele erro específico.

Processo de Identificação e Resolução:
a. Ao detectar um novo erro na fila, o sistema realiza uma busca por similaridade semântica no banco de dados vetorial para encontrar o template de erro mais correspondente.
b. Um processo de re-ranking é aplicado aos resultados da busca para refinar e garantir a seleção do template mais preciso.
c. Com o template correto identificado, o sistema recupera o hash de erro associado.
d. As informações e as ferramentas vinculadas ao hash são então enviadas a um agente autônomo, que as utilizará para executar os procedimentos de correção do problema.


Tipos de Erro e Estratégias de Correção------------------------------------

O sistema foi arquitetado para tratar duas categorias distintas de erros, cada uma com um fluxo de resolução e manutenção específico.

3.1. Erros Explícitos (Baseados em Logs)

Esta categoria refere-se a falhas técnicas concretas, que geram saídas de log rastreáveis.

Definição: Erros que produzem uma evidência física, como um stack trace de aplicação, uma exceção de banco de dados (SQL error) ou logs detalhados de falha de processamento.

Ciclo de Evolução: O tratamento para estes erros é um processo reativo e contínuo:

Detecção: Um novo erro explícito, ainda não catalogado, é identificado.

Desenvolvimento: Uma solução é desenvolvida para corrigir a causa raiz do problema.

Catalogação: Após a validação da solução, duas ações são executadas:

Criação de Ferramentas: As novas rotinas de correção são encapsuladas como "Ferramentas Personalizadas" para o agente autônomo.

Criação de Template: O stack trace ou log do erro é utilizado para criar um novo "template de erro", que é adicionado ao banco de dados vetorial junto ao hash que aponta para as novas ferramentas.

3.2. Erros de Validação (Regras de Negócio)

Esta categoria abrange inconsistências lógicas ou falhas de integridade de dados que não necessariamente geram um erro de sistema.

Definição: Desvios de padrões esperados, como dados em formato incorreto, violações de regras de negócio ou inconsistências entre registros.

Tratamento: Estes erros são identificados proativamente pelas "Ferramentas Padrão", que executam rotinas de validação contínuas. As lógicas de verificação e correção para este tipo de erro são implementadas diretamente nessas ferramentas, que compõem a base de validação padrão do sistema.




