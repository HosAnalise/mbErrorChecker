from pydantic import BaseModel,Field
from models.DbModel.QueryReturnModel import QueryReturnModel
from typing import List



class ErrorModel(BaseModel):    
    error: list[QueryReturnModel] = Field(..., description="Lista com todo erros encontrados por loja do banco de dados")
    store: int = Field(..., description="Loja que o erro pertence")
    count: int = Field(..., description="Quantidade de erros encontrados por loja")

class ErrorModelByTable(BaseModel):    
    error: list[QueryReturnModel] = Field(..., description="Lista com todo erros encontrados por tabela do banco de dados")
    table_name: str = Field(..., description="Nome da tabela que o erro pertence")
    count: int = Field(..., description="Quantidade de erros encontrados por tabela")

class ErrorListModel(BaseModel):
    errors: list[ErrorModel]|list[ErrorModelByTable] = Field(..., description="Lista de erros agrupados por loja e tipo")  

class AnalysisResponseModel(BaseModel):
    analysis: str = Field(..., description="Lista de análises detalhadas de erros")
    cause: str = Field(..., description="Causa provável do erro")
    error_classification: str = Field(..., description="Classificação do erro")
    resolution_steps: str = Field(..., description="Passos sugeridos para resolução do erro")
    criticality: str = Field(..., description="Criticidade do erro")

class ErrorDetailModel(BaseModel):
    details: str = Field(..., description="Detalhes do erro")
    store_occurrences: list[int] = Field(..., description="Lojas onde o erro ocorreu")
    table_name: str = Field(..., description="Nome da tabela onde o erro ocorreu")
    analysis_response: AnalysisResponseModel = Field(..., description="Resposta detalhada da análise do erro")

class ErrorSummaryModel(BaseModel):
    errors: List[ErrorDetailModel] = Field(..., description="Lista detalhada de erros")






