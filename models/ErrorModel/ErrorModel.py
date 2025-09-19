from pydantic import BaseModel,Field
from models.DbModel.QueryReturnModel import QueryReturnModel
from typing import List



class ErrorModel(BaseModel):    
    error: list[QueryReturnModel] = Field(..., description="Lista com todo erros encontrados por loja do banco de dados")
    store: int = Field(..., description="Loja que o erro pertence")
    count: int = Field(..., description="Quantidade de erros encontrados por loja")


class ErrorListModel(BaseModel):
    errors: list[ErrorModel] = Field(..., description="Lista de erros agrupados por loja e tipo")    


class ErrorDetailModel(BaseModel):
    type_error: str = Field(..., description="Tipo do erro")
    details: ErrorModel = Field(..., description="Detalhes do erro")
    store: int = Field(..., description="Loja que o erro pertence")
    occurrences: int = Field(..., description="Quantidade de ocorrências do erro")
    table_name: str = Field(..., description="Nome da tabela onde o erro ocorreu")


class ErrorSummaryModel(BaseModel):
    errors: List[ErrorDetailModel] = Field(..., description="Lista detalhada de erros")






