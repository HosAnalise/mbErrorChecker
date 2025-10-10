import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from dotenv import load_dotenv
from pydantic import BaseModel, EmailStr, FilePath, field_validator
from typing import Optional
import os

load_dotenv()

class EmailRecipientModel(BaseModel):
    """ Pydantic model to validate an email recipient."""
    email: EmailStr 
    destinatario: str
    is_active: str  

    @field_validator('is_active', mode='before')
    def validate_is_active(cls, v):
        """Validate if is_active is '0' or '1'."""
        if v not in ('0', '1'):
            raise ValueError("The field 'is_active' must be '0' or '1' in EmailRecipientModel.")
        return v

class EmailListModel(BaseModel):
    """ Pydantic model to validate a list of email recipients."""
    emails: list[EmailRecipientModel]
    
    @field_validator('emails')
    def validate_emails(cls, v):
        """Valida se a lista de e-mails não está vazia."""
        if not v and isinstance(v, list):
            raise ValueError("The email list cannot be empty in EmailListModel.")
        return v



class EmailModel(BaseModel):
    """ Pydantic model to validate the data of an email."""
    destinatario: list[EmailStr] | EmailStr
    assunto: str
    corpo: str
    caminho_imagem: Optional[FilePath] = None
    nome_arquivo_anexo: Optional[str] = None


    @field_validator('caminho_imagem', 'nome_arquivo_anexo', mode='before')
    def validate_image_fields(cls, v, info):
        """Valida se ambos os campos de imagem são fornecidos juntos."""
        caminho_imagem = info.data.get('caminho_imagem')
        nome_arquivo_anexo = info.data.get('nome_arquivo_anexo')
        if (caminho_imagem and not nome_arquivo_anexo) or (nome_arquivo_anexo and not caminho_imagem):
            raise ValueError("Ambos 'caminho_imagem' e 'nome_arquivo_anexo' devem ser fornecidos juntos.")
        return v

class EmailComposer:
    """
    Constrói um objeto MIMEMultipart a partir de um modelo de dados.
    Sua única responsabilidade é montar a mensagem.
    """
    def __init__(self, remetente: str, data: EmailModel):
        self.remetente = remetente
        self.data = data
        self.msg = MIMEMultipart()

    def _build_headers(self):
        """Constrói os cabeçalhos do e-mail."""
        self.msg['From'] = self.remetente
        self.msg['To'] = self.data.destinatario
        self.msg['Subject'] = self.data.assunto

    def _attach_body(self):
        """Anexa o corpo de texto ao e-mail."""
        self.msg.attach(MIMEText(self.data.corpo, 'plain', 'utf-8'))

    def _attach_image(self):
        """Anexa a imagem, se um caminho for fornecido."""
        if self.data.caminho_imagem and self.data.nome_arquivo_anexo:
            with open(self.data.caminho_imagem, 'rb') as fp:
                imagem = MIMEImage(fp.read(), name=self.data.nome_arquivo_anexo)
                imagem.add_header(
                    'Content-Disposition',
                    f'attachment; filename="{self.data.nome_arquivo_anexo}"'
                )
                self.msg.attach(imagem)

    def build_message(self) -> MIMEMultipart:
        """
        Orquestra a construção do e-mail e retorna o objeto MIME completo.
        """
        self._build_headers()
        self._attach_body()
        self._attach_image()
        return self.msg


class EmailSender:
    """
    Envia um objeto MIMEMultipart usando um servidor SMTP.
    Sua única responsabilidade é a comunicação com o servidor.
    """
    def __init__(self, host: str, port: int, email: str, senha: str):
        self.host = host
        self.port = port
        self.email = email
        self.senha = senha

    def send(self, message: MIMEMultipart):
        """Conecta-se ao servidor e envia a mensagem."""
        try:
            with smtplib.SMTP(self.host, self.port) as server:
                server.starttls()
                server.login(self.email, self.senha)
                server.send_message(message)
            print("E-mail enviado com sucesso!")
            return True
        except smtplib.SMTPAuthenticationError:
            print("Erro de autenticação. Verifique e-mail/senha ou use uma Senha de App.")
            return False
        except Exception as e:
            print(f"Ocorreu um erro ao enviar o e-mail: {e}")
            return False


if __name__ == "__main__":
    EMAIL_REMETENTE = os.getenv('EMAIL')
    SENHA_REMETENTE = os.getenv('SENHA')

    if not EMAIL_REMETENTE or not SENHA_REMETENTE:
        raise ValueError("As variáveis de ambiente EMAIL e SENHA não foram definidas.")

    try:
        dados_email = EmailModel(
            destinatario="destinatario.feliz@exemplo.com",
            assunto="Código Refatorado e Modular!",
            corpo="Olá!\n\nEste e-mail foi enviado com uma arquitetura de classes muito mais limpa e modular em Python.\n\nAtenciosamente,\nSeu Código.",
            caminho_imagem="./caminho/para/sua/imagem.jpg", 
            nome_arquivo_anexo="python-logo.jpg"
        )
    except Exception as e:
        print(f"Erro na validação dos dados do e-mail: {e}")
        exit()

    print("Montando a mensagem...")
    compositor = EmailComposer(remetente=EMAIL_REMETENTE, data=dados_email)
    mensagem_pronta = compositor.build_message()

    servidor_gmail = {
        "host": "smtp.gmail.com",
        "port": 587,
        "email": EMAIL_REMETENTE,
        "senha": SENHA_REMETENTE
    }
    enviador = EmailSender(**servidor_gmail)

    print("Enviando o e-mail...")
    enviador.send(mensagem_pronta)