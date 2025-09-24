from classes.Email import EmailModel, EmailComposer, EmailSender,EmailRecipientModel,EmailListModel
from os import getenv
from models.ErrorModel.ErrorModel import ErrorSummaryModel
from db.MongoDbManager import MongoDbManager
import textwrap
import logging

from services.bussines_logic.error_analysis_service import ErrorAnalysis

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
        email_list = mongo_manager.get_emails()
        email_list_model = EmailListModel(emails=[EmailRecipientModel(**email) for email in email_list])

        return [email.email for email in email_list_model.emails if email.is_active == '1']
    except Exception as e:
        logger.error(f"Erro ao recuperar destinatários: {e}")
        return []   

def create_email_model(body: str, email: list[str]) -> EmailModel:
    """Cria o modelo de e-mail com base nos dados de erro."""

    receipients = ', '.join(email) if isinstance(email, list) else email

    return EmailModel(
                destinatario=receipients,
                assunto=f"Erros encontrados em filiais da MB",
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



def _clean_text(text: any) -> str:
    """
    Converte o texto para string, substitui caracteres de espaço não padrão
    e remove o espaçamento extra no início e no fim.
    """
    text_str = str(text)
    
    cleaned_text = text_str.replace('\xa0', ' ').replace('\n', ' ').replace('\r', ' ')
    

    return cleaned_text.strip()




def _build_email_body(grouped_fails: ErrorSummaryModel) -> str:
    """Constrói o corpo de texto consolidado para o e-mail de erros."""
    
    header = "Prezado(a),\n\nForam identificados os seguintes erros nas filiais da MB:"
    footer = "Email enviado através do sistema de Monitoramento MbErrorCheck. Arquitetado e desenvolvido por Gabriel Siqueira em colaboração com Fabiano Urquiza."
    
    error_details_list = [
        textwrap.dedent(f"""\
            IDs das lojas afetadas:
                {_clean_text(', '.join(map(str, summary.store_occurrences)))}

            Segue o resumo do erro:
                {_clean_text(summary.details)}

            Tabela:
                {_clean_text(summary.table_name)}

            Análise:
                {_clean_text(summary.analysis_response.analysis)}

            Causa:
                {_clean_text(summary.analysis_response.cause)}

            Classificação:
                {_clean_text(summary.analysis_response.error_classification)}
            
            Passos para resolução:
                {_clean_text(summary.analysis_response.resolution_steps)}

            Criticidade:
                {_clean_text(summary.analysis_response.criticality)}
        """) for summary in grouped_fails.errors
    ]
    
    all_errors_string = "\n\n----------------------------------------\n\n".join(error_details_list)
    
    return f"{header}\n\n{all_errors_string}\n\n{footer}"



def send_email(grouped_fails: ErrorSummaryModel) -> None:
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



if __name__ == "__main__":
    
    error_agent = ErrorAnalysis()


    errors = error_agent.run()


    send_email(errors)


