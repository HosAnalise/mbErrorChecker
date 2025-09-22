from classes.Email import EmailModel, EmailComposer, EmailSender,EmailRecipientModel,EmailListModel
from os import getenv
from models.ErrorModel.ErrorModel import ErrorSummaryModel
from db.MongoDbManager import MongoDbManager
import textwrap
import logging

logger = logging.getLogger(__name__)    
logging.basicConfig(level=logging.INFO)



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
    try:
        email_list = mongo_manager.get_data(collection_name="emails")
        email_list_model = EmailListModel(emails=[EmailRecipientModel(**email) for email in email_list])

        return [email.email for email in email_list_model.emails if email.is_active == '1']
    except Exception as e:
        logger.error(f"Erro ao recuperar destinatários: {e}")
        return []   

def create_email_model(body: str, email: list[str]) -> EmailModel:
    """Cria o modelo de e-mail com base nos dados de erro."""

    return EmailModel(
                destinatario=email,
                assunto=f"Erros encontrados nos robôs da filial MB",
                corpo=body
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
  



def _build_email_body(grouped_fails: list[ErrorSummaryModel]) -> str:
    """Constrói o corpo de texto consolidado para o e-mail de erros."""
    
    report_parts = []
    
    for summary in grouped_fails:
        header = textwrap.dedent(f"""
                                    Email enviado através do sistema de monitoramento de erros dos robôs. Arquitetado e desenvolvido por Gabriel Siqueira em colaboração com Fabiano Urquiza.
                                 
                                    A loja MB filial {summary.store} apresentou {len(summary.errors)} erros.
                                    Erros:
                                """
                                )

        error_details_list = []
        for error in summary.errors:
            error_formatted = textwrap.dedent(f"""
                Segue o resumo do erro: {error.details}
                Ocorrências: {error.occurrences}
                Tabela: {error.table_name}
                Análise: {error.analysis_response.analysis}
                Causa: {error.analysis_response.cause}
                Classificação: {error.analysis_response.error_classification}
                Passos para resolução: {error.analysis_response.resolution_steps}
                Criticidade: {error.analysis_response.criticality}
            """)
            error_details_list.append(error_formatted)
        
        full_store_report = header + "\n-----------------\n".join(error_details_list)
        report_parts.append(full_store_report)

    return "\n\n========================================\n\n".join(report_parts)



def send_email(grouped_fails: list[ErrorSummaryModel]) -> None:
    """Envia um único e-mail de notificação consolidado para uma lista de destinatários."""

    EMAIL, PASSWORD = get_credentials()
    if not EMAIL or not PASSWORD:
        logger.error("Credenciais de e-mail não encontradas. O e-mail não será enviado.")
        return

    recipients = get_recipients()
    if not recipients:
        logger.warning("Nenhum destinatário encontrado. O e-mail não será enviado.")
        return 
    
    final_body = _build_email_body(grouped_fails)
    
    email_data = create_email_model(body=final_body, email=recipients) 

    message = build_message(EMAIL, email_data)
    
    gmail_server = build_server_config(EMAIL, PASSWORD)
    sender = EmailSender(**gmail_server)

    try:  

        logger.info(f"Enviando e-mail consolidado para: {', '.join(recipients)}")
        sender.send(message)
        logger.info("E-mail enviado com sucesso!")

    except Exception as e:
        logger.error(f"Erro ao enviar e-mail: {e}")
