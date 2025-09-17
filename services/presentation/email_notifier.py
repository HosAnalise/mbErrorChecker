from classes.Email import EmailModel, EmailComposer, EmailSender,EmailRecipientModel,EmailListModel
from os import getenv
from models.ErrorModel.ErrorModel import ErrorSummaryModel
from db.MongoDbManager import MongoDbManager


mongo_manager = MongoDbManager()

def get_credentials():
    """Obtém as credenciais de e-mail (usuário e senha) de variáveis de ambiente."""
    EMAIL = getenv('EMAIL')
    PASSWORD = getenv('PASSWORD')

    if not EMAIL or not PASSWORD:
        raise ValueError("As variáveis de ambiente EMAIL e PASSWORD não foram definidas.")
    
    return EMAIL, PASSWORD

def get_recipients():
    """Recupera a lista de destinatários do banco de dados."""
    email_list = mongo_manager.get_data(collection_name="emails")
    email_list_model = EmailListModel(emails=[EmailRecipientModel(**email) for email in email_list])

    return [email.email for email in email_list_model.emails if email.is_active == '1']

def create_email_model(summary: ErrorSummaryModel, email: str) -> EmailModel:
    """Cria o modelo de e-mail com base nos dados de erro."""

    return EmailModel(
                destinatario=email,
                assunto="Erros encontrados em lojas da MB",
                corpo=f"""Esse email foi gerado automaticamente para informar que foram encontrados erros em algumas lojas da MB.

                Erros encontrados na loja {summary.stores}: Quantidade {summary.total_errors} erros.

                Erros: {summary.summary}

                \n\nAtenciosamente,\nSistema de Monitoramento de Erros.""",
            )

def build_message(remetente: str, data: EmailModel) -> EmailModel:
    """Constrói a mensagem de e-mail."""
    compositor = EmailComposer(remetente=remetente, data=data)
    mensagem_pronta = compositor.build_message()
    return mensagem_pronta

def build_server_config(email: str, password: str) -> dict:
    """Configura o servidor SMTP do Gmail."""
    return {
            "host": "smtp.gmail.com",
            "port": 587,
            "email": email,
            "senha": password
        }
  



def send_email():
    """
    Envia e-mails de notificação para uma lista de destinatários utilizando as credenciais configuradas.
    Este método executa as seguintes etapas:
    1. Obtém as credenciais de e-mail (usuário e senha) de variáveis de ambiente.
    2. Valida se as credenciais estão presentes, lançando um erro caso contrário.
    3. Recupera a lista de destinatários.
    4. Para cada destinatário:
        - Cria o modelo de e-mail com base nos dados de erro.
        - Constrói a mensagem de e-mail.
        - Configura o servidor SMTP do Gmail.
        - Inicializa o remetente e envia a mensagem.
    Exceções:
        ValueError: Se as variáveis de ambiente EMAIL ou PASSWORD não estiverem definidas.
    Observação:
        Esta função é adequada para ser utilizada por agentes automatizados ou sistemas de monitoramento que necessitam notificar usuários sobre eventos ou erros detectados.
    """


    EMAIL, PASSWORD = get_credentials()
   

    if not EMAIL or not PASSWORD:
        raise ValueError("As variáveis de ambiente EMAIL e PASSWORD não foram definidas.")
    
    email_data = create_email_model(summary="fd", email=email)

    message = build_message(EMAIL, email_data)

    gmail_server = build_server_config(EMAIL, PASSWORD)

    for email in get_recipients():

        sender = EmailSender(**gmail_server)

        sender.send(message)
