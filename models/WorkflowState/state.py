from pydantic import BaseModel,Field
from models.DbModel.QueryReturnModel import QueryReturnModel
from models.ErrorModel.ErrorModel import ErrorModel 
from pydantic_ai import Agent




class workflowState(BaseModel):
    analyzed_errors: list[QueryReturnModel] = Field(..., description="Lista de erros analisados")
    updated_errors: list[QueryReturnModel] = Field(..., description="Lista de erros atualizados")
    grouped_errors: ErrorModel = Field(..., description="Erros agrupados por código de loja")
    agent: Agent = Field(..., description="Agente responsável pela análise")
