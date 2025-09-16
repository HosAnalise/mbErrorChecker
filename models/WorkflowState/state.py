from pydantic import BaseModel
from models.DbModel.QueryReturnModel import QueryReturnModel
from models.ErrorModel.ErrorModel import ErrorModel 



class workflowState(BaseModel):
    raw_messages: str
    analyzed_errors: list[QueryReturnModel]
    grouped_errors: ErrorModel
