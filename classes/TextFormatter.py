import unicodedata
import re
import logging
from typing import Optional




logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(message)s')



PATTERNS_SPECIFIC = [
    (re.compile(r'\b[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\b'), '{GUID}'),
    (re.compile(r'\b\d{4}-\d{2}-\d{2}[ T]\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+-]\d{2}:\d{2})?\b'), '{TIMESTAMP}'),
    (re.compile(r'("forma_recebimento":\s*")([A-Z]+)(")', re.IGNORECASE), r'\1{PAYMENT_METHOD}\3'),
]

PATTERNS_MULTILINE = [
    (r'RequestBody:.*?(?=\s*(?:GUID:|StackTrace:|\Z))', '{REQUEST_BODY}'),
    (r'StackTrace:.*?--- End of inner exception stack trace ---', '{STACK_TRACE}'), 
    (r'Extrato do Json da Venda: \{.*?\} \}', '{SALE_DATA}'),
    (r'("parcelas":\s*)\[.*?\]', r'\1[]'),
    (r'("tributacoes":\s*)\{.*?\}', r'\1{}'),
    (r'("produto":\s*)\[.*?\]', r'\1[]'),
]

PATTERNS_SENTENCES = [
    (re.compile(r'Erro ao enviar a venda.*?,/'), 'Erro ao enviar a venda {ID},/'),
    (re.compile(r', empresa.*?\./', re.DOTALL), ', empresa {ID}./'),
]

PATTERNS_GENERIC = [
    (re.compile(r'\b\d{5,}\b'), '{ID}'),  
    (re.compile(r'\b\d{1,4}(\.\d+)?\b'), '{VALUE}'), 
]

PATTERNS_SEARCH = [
    r'"message":\s*(.*?)(?=\s*RequestBody:)', 
    r'"erro":\s*(.*?)(?=\s*} ] } })',
    r'"erro":\s*(.*?)(?=\s*"codigo hos":)',
    r'ResponseBody:\s*(.*?)(?=\s*--- End of inner exception stack trace ---)',
]






class TextFormatter:


    def sanitize_log(self, log: str) -> str:

        """Sanitiza o log removendo caracteres especiais e espaços extras."""
        try:
            sanitized_content = unicodedata.normalize('NFKC', log)

            sanitized_content = re.sub(r'\s+', ' ', sanitized_content).strip()

            return sanitized_content
        except Exception as e:
            logging.error("Erro ao sanitizar log: %s", e, exc_info=True)
            return log


    def regex_sanitize_pro(self,text: str) -> str:
        """
        Sanitiza o texto usando uma abordagem ordenada e eficiente de expressões regulares.
        Aplica as regras da mais específica para a mais genérica para evitar conflitos.
        """
        sanitized_text = text
        try:
            
            for pattern, placeholder in PATTERNS_SENTENCES:
                sanitized_text = pattern.sub(placeholder, sanitized_text)

            for pattern, placeholder in PATTERNS_MULTILINE:
                sanitized_text = re.sub(pattern, placeholder, sanitized_text, flags=re.DOTALL)

            for pattern, placeholder in PATTERNS_SPECIFIC:
                sanitized_text = pattern.sub(placeholder, sanitized_text)

            for pattern, placeholder in PATTERNS_GENERIC:
                sanitized_text = pattern.sub(placeholder, sanitized_text)           
                
        except re.error as e:
            logging.error(f"Erro na expressão regular: {e}")
            return text 

        return sanitized_text    




    def regex_sanitize_search(self, text: str) -> Optional[str]:
        """
        Sanitiza o texto usando uma abordagem ordenada e eficiente de expressões regulares.
        Aplica as regras da mais específica para a mais genérica para evitar conflitos.
        """
        try:
            for re_pattern in PATTERNS_SEARCH:
                search = re.search(pattern=re_pattern, string=text, flags=re.DOTALL)

                if search:
                    return search.group(1)                    

        except re.error as e:
            logging.error(f"Erro na expressão regular: {e}")
            return None       
          
        return None

    def clean_content(self, content: str) -> str:
                # content = content.replace('\r\n', '\n')
                content = content.replace(r'\rn', ' ')
                content = content.replace('\\', '')
                content = content.replace('[rn', '[')
                content = content.replace('{rn', '{')
                content = content.replace(']rn', ']')
                content = content.replace('}rn', '}')
                content = content.replace(',rn', ',')
                content = content.replace('"rn', '"')
                return content.strip()       