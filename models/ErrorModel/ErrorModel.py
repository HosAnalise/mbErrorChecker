from pydantic import BaseModel,Field
from models.DbModel.QueryReturnModel import QueryReturnModel




class ErrorModel(BaseModel):    
    error: list[QueryReturnModel] = Field(..., description="Lista com todo erros encontrados por loja do banco de dados")
    store: int = Field(..., description="Loja que o erro pertence")
    count: int = Field(..., description="Quantidade de erros encontrados por loja")


class ErrorListModel(BaseModel):
    errors: list[ErrorModel] = Field(..., description="Lista de erros agrupados por loja e tipo")    


class ErrorSummaryModel(BaseModel):
    summary: str = Field(..., description="Resumo dos erros encontrados")
    total_errors: int = Field(..., description="Total de erros encontrados")
    stores: list[int] = Field(..., description="Lojas com erros")
