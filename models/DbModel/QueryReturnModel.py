from pydantic import BaseModel,Field
import datetime



class QueryReturnModel(BaseModel):
    code: int = Field(..., description="ID da tabela")
    empresa: int = Field(..., description="ID da empresa")
    tentativas: int = Field(..., description="Número de tentativas")
    guid_web: str = Field(..., description="GUID da web")
    data_hora_tentativa: datetime = Field(..., description="Data e hora da tentativa")
    data_hora_inclusao: datetime = Field(..., description="Data e hora de inclusão")
    erro: str = Field(..., description="Descrição do erro")
    store:int = Field(..., description="Codigo da loja que o erro pertence")
    table_name:str = Field(..., description="Nome da tabela onde o erro ocorreu")