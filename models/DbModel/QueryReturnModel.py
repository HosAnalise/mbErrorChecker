from pydantic import BaseModel
import datetime




class QueryReturnModel(BaseModel):
    venda: int
    empresa: int
    tentativas: int
    guid_web: str
    data_hora_tentativa: datetime
    data_hora_inclusao: datetime
    erro: str