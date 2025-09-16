from pydantic import BaseModel,Field
from models.DbModel.QueryReturnModel import QueryReturnModel




class ErrorModel(BaseModel):
    error: list[QueryReturnModel] = Field(..., description="Lista de erros do banco de dados")
    code: int = Field(..., description="Codigo da loja que o erro pertence")

