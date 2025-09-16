from pydantic import BaseModel,Field
from models.DbModel.QueryReturnModel import QueryReturnModel




class ErrorModel(BaseModel):    
    error: QueryReturnModel = Field(..., description="Lista de erros do banco de dados")
    count: int = Field(..., description="Quantidade de erros")
    type: str = Field(..., description="Tipo do erro")


class ErrorListModel(BaseModel):
    errors: list[ErrorModel] = Field(..., description="Lista de erros agrupados por loja e tipo")    
    code:int = Field(..., description="Codigo da loja que o erro pertence")


