from pydantic import BaseModel,Field
from models.DbModel.QueryReturnModel import QueryReturnModel
from models.ErrorModel.ErrorModel import ErrorModel 
from pydantic_ai import Agent




class workflowState(BaseModel):
    raw_messages: str = Field(..., description="Mensagens brutas recebidas para análise")
    analyzed_errors: list[QueryReturnModel] = Field(..., description="Lista de erros analisados")
    grouped_errors: ErrorModel = Field(..., description="Erros agrupados por código de loja")
    agent: Agent = Field(..., description="Agente responsável pela análise")
